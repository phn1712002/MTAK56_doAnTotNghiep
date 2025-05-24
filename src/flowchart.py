import random
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtCore import Qt
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

    

    def itemChange(self, change, value):
        """Handle position changes to keep ID text aligned"""
        if change == QGraphicsRectItem.ItemPositionChange:
            config = self._load_config()
            self.id_text.setPos(
                config["id_text"]["pos_x"],
                config["id_text"]["pos_y"]
            )
        return super().itemChange(change, value)

    def mousePressEvent(self, event):
        """Handle mouse press to ensure selection works"""
        self.setSelected(True)
        super().mousePressEvent(event)
