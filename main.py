import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from random import randint

WIDTH_SIZE = 30
HEIGHT_SIZE = 30
class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

search_coors = []
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.boxes = [[None for _ in range(WIDTH_SIZE)] for _ in range(HEIGHT_SIZE)]
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(0)                  # 박스 간격 0
        grid.setContentsMargins(0, 0, 0, 0) # 바깥 여백 0
        self.setLayout(grid)

        for h in range(HEIGHT_SIZE):
            for w in range(WIDTH_SIZE):
                label = QLabel(self)
                label.setFixedSize(13, 13)    # 크기 고정
                label.setStyleSheet("background-color: #eeeeee;")
                self.boxes[h][w] = label
                grid.addWidget(label, h, w)

        self.setWindowTitle('QGridLayout')
        self.show()
    
    def updateMap(self, map_array):
        for h in range(HEIGHT_SIZE):
            for w in range(WIDTH_SIZE):
                if(map_array[h][w] == 1): #시작지점
                    self.boxes[h][w].setStyleSheet("background-color: #d84141;")
                elif(map_array[h][w] == 2): #도착지점
                    self.boxes[h][w].setStyleSheet("background-color: #4b41d8;")
                elif(map_array[h][w] ==  3): #탐색중
                    self.boxes[h][w].setStyleSheet("background-color: #aaaaaa;")
                elif(map_array[h][w] ==  4): #탐색완료
                    self.boxes[h][w].setStyleSheet("background-color: #aaaaaa;")
                elif(map_array[h][w] ==  9): #장애물
                    self.boxes[h][w].setStyleSheet("background-color: #111111;")

class Dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def changeColor(color: str, qlabel: QLabel):
    qlabel.setStyleSheet(f"background-color: {color};")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()

    map_array = [[0 for _ in range(WIDTH_SIZE)] for _ in range(HEIGHT_SIZE)]
    
    # 시작지점과 종료지점을 생성
    map_array[0][0] = 1
    map_array[HEIGHT_SIZE-1][WIDTH_SIZE-1] = 2
    
    # 장애물 랜덤으로 생성
    for i in range(20):
        obstacle_width = randint(2, 4)
        obstacle_height = randint(2, 4)
        obstacle_x = randint(0, WIDTH_SIZE-1)
        obstacle_y = randint(0, HEIGHT_SIZE-1)
        for j in range(obstacle_height):
            if(obstacle_y + j >= HEIGHT_SIZE): break
            for k in range(obstacle_width):
                if(obstacle_x + k >= WIDTH_SIZE): break

                if(obstacle_y + j < 3 and obstacle_x + k < 3): continue
                if(obstacle_y + j > HEIGHT_SIZE-3 and obstacle_x + k > WIDTH_SIZE-3): continue
                map_array[obstacle_y + j][obstacle_x + k] = 9

    ex.updateMap(map_array)

    search_coors.append(Coor(0, 0))
    for coor in search_coors:
        # 왼쪽 찾기
        if(coor.x != 0 and map_array[coor.y][coor.x-1] == 0):
            print("왼쪽 찾기 실행")
        # 오른쪽 찾기
        if(coor.x != WIDTH_SIZE-1 and map_array[coor.y][coor.x+1] == 0):
            print("오른쪽 찾기 실행")
        # 위쪽 찾기
        if(coor.y != 0 and map_array[coor.y-1][coor.x] == 0):
            print("위쪽 찾기 실행")
        # 아래쪽 찾기
        if(coor.y != HEIGHT_SIZE-1 and map_array[coor.y+1][coor.x] == 0):
            print("아래쪽 찾기 실행")

    sys.exit(app.exec_())
