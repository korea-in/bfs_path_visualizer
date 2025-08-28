import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from random import randint

WIDTH_SIZE = 20
HEIGHT_SIZE = 20

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = [[None for _ in range(WIDTH_SIZE)] for _ in range(HEIGHT_SIZE)]
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(0)                 # 버튼 간격 0
        grid.setContentsMargins(0, 0, 0, 0) # 바깥 여백 0
        self.setLayout(grid)

        for h in range(HEIGHT_SIZE):
            for w in range(WIDTH_SIZE):
                btn = QPushButton(self)
                btn.setFixedSize(20, 20)   # 크기 고정
                self.buttons[h][w] = btn
                grid.addWidget(btn, h, w)

        self.setWindowTitle('QGridLayout')
        self.show()

class Dot():
    def __init__(self):
      self.x = randint(0, WIDTH_SIZE-1)
      self.y = randint(0, HEIGHT_SIZE-1)

def changeColor(color: str, qbutton: QPushButton):
    qbutton.setStyleSheet(f"background-color: {color};")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    unit = Dot()
    destination = Dot()
    
    changeColor("#d84141", ex.buttons[unit.y][unit.x])
    changeColor("#4b41d8", ex.buttons[destination.y][destination.x])
    
    sys.exit(app.exec_())
