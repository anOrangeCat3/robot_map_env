from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("地图显示")
        
        # 创建主窗口部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # 创建标签用于显示图片
        image_label = QLabel()
        pixmap = QPixmap("maps/map1.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 将图片标签添加到布局中
        layout.addWidget(image_label)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()