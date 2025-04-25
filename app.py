from PySide6.QtWidgets import QApplication, QMainWindow
from ui_function import Ui_Funtion
from PySide6.QtGui import QPixmap

app = QApplication([])
qMainWindow = QMainWindow()
ui_main = Ui_Funtion()
ui_main.setupUi(qMainWindow)
ui_main.processSignalAndSlot()
qMainWindow.show()
app.exec()  