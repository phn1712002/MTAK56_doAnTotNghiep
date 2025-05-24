import random
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsLineItem
from PySide6.QtCore import Qt, QLineF
from PySide6.QtGui import QBrush, QColor, QPen, QFont, QTextCharFormat, QTextCursor
from .tools import load_json

class NodeRectangle(QGraphicsRectItem):
    def __init__(self, x, y, config_path, parent=None):
        
        # Load config from JSON file
        config = load_json(config_path)
        
        # Initialize rectangle with config values
        super().__init__(x, y, 
                        config["rectangle"]["width"], 
                        config["rectangle"]["height"], 
                        parent)
        
        # Setup rectangle style
        self.setBrush(QBrush(QColor(config["rectangle"]["fill_color"])))
        pen = QPen(QColor(config["id_text"]["outline_color"]))
        pen.setWidth(config["rectangle"]["border_width"])
        self.setPen(pen)
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable)
        
        # Track connected arrows
        self.connected_arrows = []
        
        # Create ID text
        self.rect_id = random.randint(
            config["random_id"]["min"],
            config["random_id"]["max"]
        )
        self.id_text = QGraphicsTextItem(f"ID: {self.rect_id}", self)
        
        # Format ID text from config
        font = QFont()
        font.setBold(config["id_text"]["bold"])
        font.setPointSize(config["id_text"]["font_size"])
        
        char_format = QTextCharFormat()
        char_format.setFont(font)
        char_format.setForeground(QColor(config["id_text"]["text_color"]))
        char_format.setTextOutline(QPen(
            QColor(config["id_text"]["outline_color"]),
            config["id_text"]["outline_width"]
        ))
        
        cursor = QTextCursor(self.id_text.document())
        cursor.select(QTextCursor.Document)
        cursor.mergeCharFormat(char_format)
        
        self.id_text.setPos(
            config["id_text"]["pos_x"],
            config["id_text"]["pos_y"]
        )

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
