import random
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsLineItem, QInputDialog, QMessageBox
from PySide6.QtCore import Qt, QLineF
from PySide6.QtGui import QBrush, QColor, QPen, QFont, QTextCharFormat, QTextCursor
from .tools import load_json

class NodeRectangle(QGraphicsRectItem):
    def __init__(self, x, y, config_path, name="", probability=0, parent=None):
        # Load config from JSON file
        self.config = load_json(config_path)
        
        # Create temporary text to calculate required size
        temp_text = QGraphicsTextItem(f"Tên gọi: {name}\nXác xuất làm việc: {probability}")
        text_rect = temp_text.boundingRect()
        
        # Calculate rectangle size with padding
        self.padding = self.config["rectangle"]["padding"]
        width = max(self.config["rectangle"]["width"], text_rect.width() + self.padding)
        height = max(self.config["rectangle"]["height"], text_rect.height() + self.padding)
        
        # Initialize rectangle with calculated size
        super().__init__(x, y, width, height, parent)
        
        # Setup rectangle style
        self.setBrush(QBrush(QColor(self.config["rectangle"]["fill_color"])))
        pen = QPen(QColor(self.config["id_text"]["outline_color"]))
        pen.setWidth(self.config["rectangle"]["border_width"])
        self.setPen(pen)
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable)
        
        # Track connected arrows and child nodes
        self.connected_arrows = []
        self.child_node = []  # List to store child NodeRectangle objects
        self.success_probability = probability
        self.name_node = name
        
        # Create ID text
        self.rect_id = random.randint(
            self.config["random_id"]["min"],
            self.config["random_id"]["max"]
        )
        self.id_text = QGraphicsTextItem(f"ID: {self.rect_id}", self)
        
        # Format ID text from config
        font = QFont()
        font.setBold(self.config["id_text"]["bold"])
        font.setPointSize(self.config["id_text"]["font_size"])
        
        char_format = QTextCharFormat()
        char_format.setFont(font)
        char_format.setForeground(QColor(self.config["id_text"]["text_color"]))
        char_format.setTextOutline(QPen(
            QColor(self.config["id_text"]["outline_color"]),
            self.config["id_text"]["outline_width"]
        ))
        
        cursor = QTextCursor(self.id_text.document())
        cursor.select(QTextCursor.Document)
        cursor.mergeCharFormat(char_format)
        
        self.id_text.setPos(
            self.config["id_text"]["pos_x"],
            self.config["id_text"]["pos_y"]
        )
        
        # Create centered info text
        self.update_info_text()
        
    def update_info_text(self):
        """Update the info text with current name and probability"""
        # Ensure we have valid config values
        info_config = self.config.get("info_text", {})
        font_size = info_config.get("font_size", 12)
        text_color = info_config.get("text_color", "#FF0000")
        outline_color = info_config.get("outline_color", "#000000")
        bold = info_config.get("bold", False)
        outline_width = info_config.get("outline_width", 1)
        
        self.info_text = QGraphicsTextItem(
            f"Tên gọi: {self.name_node}\nXác xuất làm việc: {self.success_probability:.2f}", 
            self
        )
        
        # Create custom formatting for info text
        info_font = QFont()
        info_font.setBold(bold)
        info_font.setPointSize(font_size)
        
        info_char_format = QTextCharFormat()
        info_char_format.setFont(info_font)
        info_char_format.setForeground(QColor(text_color))
        info_char_format.setTextOutline(QPen(
            QColor(outline_color),
            outline_width
        ))
        
        cursor = QTextCursor(self.info_text.document())
        cursor.select(QTextCursor.Document)
        cursor.mergeCharFormat(info_char_format)
        
        # Calculate center position
        text_width = self.info_text.boundingRect().width()
        text_height = self.info_text.boundingRect().height()
        center_x = (self.rect().width() - text_width) / 2
        center_y = (self.rect().height() - text_height) / 2
        self.info_text.setPos(center_x, center_y)

    def mousePressEvent(self, event):
        """Handle mouse press with proper selection behavior"""
        modifiers = event.modifiers()
        if not (modifiers & Qt.ControlModifier):
            # Only clear selection if clicking without Ctrl on an unselected node
            if not self.isSelected():
                scene = self.scene()
                if scene:
                    scene.clearSelection()
        super().mousePressEvent(event)

    def set_node_info(self, name, probability):
        """Update node information and refresh display"""
        self.name_node = name
        self.success_probability = probability
        
        # Remove old info text if exists
        if hasattr(self, 'info_text'):
            self.scene().removeItem(self.info_text)
            
        # Create new info text with updated values
        self.update_info_text()
        
        # Resize rectangle to fit new text while maintaining minimum size
        text_rect = self.info_text.boundingRect()
        min_width = self.config["rectangle"]["width"]
        min_height = self.config["rectangle"]["height"]
        
        new_width = max(min_width, text_rect.width() + self.padding)
        new_height = max(min_height, text_rect.height() + self.padding)
        
        self.setRect(0, 0, new_width, new_height)
        
        # Also update ID text position if needed
        if hasattr(self, 'id_text'):
            self.id_text.setPos(
                self.config["id_text"]["pos_x"],
                self.config["id_text"]["pos_y"]
            )
        
        # Update text position after resize
        text_width = self.info_text.boundingRect().width()
        text_height = self.info_text.boundingRect().height()
        center_x = (self.rect().width() - text_width) / 2
        center_y = (self.rect().height() - text_height) / 2
        self.info_text.setPos(center_x, center_y)
        
        self.update()  # Trigger repaint

    def calculate_child_probability(self):
        """Calculate probability by multiplying all child node probabilities"""
        if not self.child_node:
            return self.success_probability
        
        product = 1.0
        for child in self.child_node:
            product *= child.calculate_child_probability()
        return product * self.success_probability

    def mouseMoveEvent(self, event):
        """Update connected arrows during movement"""
        super().mouseMoveEvent(event)
        # Update all connected arrows
        for arrow in self.connected_arrows:
            if arrow.scene():
                arrow.update_position()
                arrow.scene().update()

class Arrow(QGraphicsLineItem):
    """Custom arrow item to connect nodes in flowchart"""
    def __init__(self, start_node=None, end_node=None):
        super().__init__()
        self.start_node = None
        self.end_node = None
        self.temp_end_pos = None
        self.setPen(QPen(Qt.white, 10))
        
        # Register with nodes
        if start_node:
            self.set_start_node(start_node)
        if end_node:
            self.set_end_node(end_node)
            
        self.update_position()

    def set_start_node(self, node):
        """Set start node and register with it"""
        if self.start_node:
            try:
                self.start_node.connected_arrows.remove(self)
            except ValueError:
                pass
                
        self.start_node = node
        if node and self not in node.connected_arrows:
            node.connected_arrows.append(self)

    def set_end_node(self, node):
        """Set end node and register with it"""
        if self.end_node:
            try:
                self.end_node.connected_arrows.remove(self)
            except ValueError:
                pass
                
        self.end_node = node
        if node and self not in node.connected_arrows:
            node.connected_arrows.append(self)

    def update_position(self, temp_end_pos=None):
        """Update arrow position based on nodes' positions or temporary position"""
        if not self.scene():
            return
            
        if self.start_node:
            # Calculate start position (bottom center of start node)
            start_rect = self.start_node.sceneBoundingRect()
            start_pos = start_rect.center()
            start_pos.setY(start_rect.bottom())
            
            if self.end_node:
                # Calculate end position (top center of end node)
                end_rect = self.end_node.sceneBoundingRect()
                end_pos = end_rect.center()
                end_pos.setY(end_rect.top())
            elif temp_end_pos:
                end_pos = temp_end_pos
            else:
                return
                
            self.setLine(QLineF(start_pos, end_pos))
            self.update()  # Force redraw
            self.scene().update()  # Force scene update
