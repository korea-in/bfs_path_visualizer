import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from random import randint
from time import sleep

WIDTH_SIZE = 30
HEIGHT_SIZE = 30
class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

search_coors = []
bf_search_paths = []
af_search_paths = []
search_success = False
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
                    self.boxes[h][w].setStyleSheet("background-color: #eeee00;")
                elif(map_array[h][w] ==  4): #탐색완료
                    self.boxes[h][w].setStyleSheet("background-color: #aaaaaa;")
                elif(map_array[h][w] ==  9): #장애물
                    self.boxes[h][w].setStyleSheet("background-color: #111111;")

class Dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def addPath(bc : Coor, nc : Coor):
    for path in bf_search_paths:
        if(path[len(path) - 1].x == bc.x and path[len(path) - 1].y == bc.y):
            print("경로 추가")
            path.append(nc)
            af_search_paths.append(path)
            return

def searchPath(c : Coor, d : str):
    x = c.x
    y = c.y
    if(d == "U"): y -= 1
    if(d == "D"): y += 1
    if(d == "L"): x -= 1
    if(d == "R"): x += 1
    
    if(x == -1 or x == WIDTH_SIZE or y == -1 or y == HEIGHT_SIZE):
        return
    
    if(map_array[y][x] == 0 or map_array[y][x] == 2):
        next_coor = Coor(x, y)
        search_coors.append(next_coor)
        map_array[y][x] = 3
        addPath(c, next_coor)
    
    return

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
    af_search_paths.append([Coor(0, 0)])

    while(True):
        for paths in af_search_paths:
            for p in paths:
                print("(%d, %d) → " % (p.x, p.y), end='')
            print()
        search_finish = False
        tmp_search_coors = search_coors[:]
        bf_search_paths = af_search_paths[:]
        af_search_paths = []
        search_coors = []
        for coor in tmp_search_coors:
            if(map_array[coor.y][coor.x] != 1):
                map_array[coor.y][coor.x] = 4
            
            searchPath(coor, "R")
            searchPath(coor, "L")
            searchPath(coor, "D")
            searchPath(coor, "U")

        ex.updateMap(map_array)
        QApplication.processEvents()   # UI 강제로 갱신
        
        if(len(search_coors) == 0):
            print("탐색 종료")
            break

    sys.exit(app.exec_())
