"""
File: my_drawing.py
Name: wei chen
----------------------
TODO:
onmousemoved(position):是用來顯示滑鼠位置的座標，用來定位我的圖案要放在哪裡。
用GOval, GRect, GLine, GLabel, GArc, GPolygon，產生各種圖案
用vx，vy，while True，讓花飄走
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GArc, GPolygon
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved
from campy.gui.events.timer import pause

x = 0  # 滑鼠x
y = 0  # 滑鼠y
x_y_lable = GLabel(str(x) + "," + str(y))  # 文字要顯示什麼內容: 滑鼠座標


def main():
    """
    希望成為軟體工程師以後，可以帶著電腦到世界各地去工作。
    """
    global x
    global y
    window = GWindow(600, 800, title='work from anywhere')
    window_frame2 = GRect(550, 50, x=50, y=400)
    window_frame2.filled = True
    window_frame2.fill_color = 'brown'
    window.add(window_frame2)
    sky = GRect(520, 400, x=80, y=0)
    sky.filled = True
    sky.fill_color = 'lightskyblue'
    sky.color = 'lightskyblue'
    window.add(sky)
    mountain = GPolygon()
    mountain.add_vertex((250, 50))
    mountain.add_vertex((80, 200))
    mountain.add_vertex((80, 450))
    mountain.add_vertex((600, 450))
    mountain.add_vertex((600, 200))
    mountain.add_vertex((350, 50))
    mountain.filled = True
    mountain.fill_color = 'lightgray'
    mountain.color = 'lightgray'
    window.add(mountain)
    window_frame2 = GRect(550, 50, x=50, y=400)
    window_frame2.filled = True
    window_frame2.fill_color = 'brown'
    window.add(window_frame2)
    mountain_top = GPolygon()
    mountain_top.add_vertex((250, 50))
    mountain_top.add_vertex((150, 138))
    mountain_top.add_vertex((495, 138))
    mountain_top.add_vertex((350, 50))
    mountain_top.filled = True
    mountain_top.fill_color = 'white'
    mountain_top.color = 'white'
    window.add(mountain_top)
    hill = GArc(550, 470, 0, 180)
    hill.filled = True
    hill.fill_color = 'lightgreen'
    hill.color = 'lightgreen'
    window.add(hill, 60, 282)
    window_frame1 = GRect(30, 450, x=50, y=0)
    window_frame1.filled = True
    window_frame1.fill_color = 'brown'
    window.add(window_frame1)
    cherry_blossoms = GOval(150, 150, x=100, y=170)
    cherry_blossoms.filled = True
    cherry_blossoms.fill_color = 'pink'
    cherry_blossoms.color = 'pink'
    window.add(cherry_blossoms)
    trunk = GRect(5, 75, x=175, y=280)
    trunk.filled = True
    trunk.fill_color = 'black'
    window.add(trunk)
    table = GPolygon()
    table.add_vertex((150, 450))
    table.add_vertex((10, 600))
    table.add_vertex((600, 600))
    table.add_vertex((600, 450))
    table.filled = True
    table.fill_color = 'wheat'
    table.color = 'wheat'
    window.add(table)
    table2 = GRect(590, 30, x=10, y=600)
    table2.filled = True
    table2.fill_color = 'wheat'
    table2.color = 'wheat'
    window.add(table2)
    legs = GRect(50, 170, x=90, y=630)
    legs.filled = True
    legs.fill_color = 'wheat'
    legs.color = 'wheat'
    window.add(legs)
    legs2 = GRect(50, 170, x=580, y=630)
    legs2.filled = True
    legs2.fill_color = 'wheat'
    legs2.color = 'wheat'
    window.add(legs2)
    screen = GRect(150, 70, x=430, y=400)
    screen.filled = True
    screen.fill_color = 'black'
    window.add(screen)
    computer = GPolygon()
    computer.add_vertex((430, 470))
    computer.add_vertex((400, 500))
    computer.add_vertex((560, 500))
    computer.add_vertex((580, 470))
    computer.filled = True
    computer.fill_color = 'black'
    window.add(computer)
    keyboard = GLine(440, 470, 570, 470)
    keyboard.color = 'wheat'
    window.add(keyboard)
    head = GArc(130, 480, 0, 180)
    head.filled = True
    head.fill_color = 'black'
    window.add(head, x=200, y=340)
    neck = GPolygon()
    neck.add_vertex((250, 460))
    neck.add_vertex((240, 490))
    neck.add_vertex((290, 490))
    neck.add_vertex((280, 460))
    neck.filled = True
    neck.fill_color = 'pink'
    neck.color = 'pink'
    window.add(neck)
    body = GArc(160, 200, 0, 180)
    body.filled = True
    body.fill_color = 'yellow'
    body.color = 'yellow'
    window.add(body, x=185, y=470)
    chair = GArc(50, 50, 0, 180)
    chair.filled = True
    chair.fill_color = 'chocolate'
    chair.color = 'chocolate'
    window.add(chair, x=160, y=510)
    chair2 = GArc(50, 50, 0, 180)
    chair2.filled = True
    chair2.fill_color = 'chocolate'
    chair2.color = 'chocolate'
    window.add(chair2, x=210, y=510)
    chair3 = GArc(50, 50, 0, 180)
    chair3.filled = True
    chair3.fill_color = 'chocolate'
    chair3.color = 'chocolate'
    window.add(chair3, x=260, y=510)
    chair4 = GArc(50, 50, 0, 180)
    chair4.filled = True
    chair4.fill_color = 'chocolate'
    chair4.color = 'chocolate'
    window.add(chair4, x=310, y=510)
    chair5 = GRect(200, 280, x=160, y=520)
    chair5.filled = True
    chair5.fill_color = 'chocolate'
    chair5.color = 'chocolate'
    window.add(chair5)
    flower1 = GOval(10, 12, x=400, y=150)
    flower1.filled = True
    flower1.fill_color = 'pink'
    flower1.color = 'pink'
    window.add(flower1)
    flower2 = GOval(10, 12, x=360, y=190)
    flower2.filled = True
    flower2.fill_color = 'pink'
    flower2.color = 'pink'
    window.add(flower2)
    flower3 = GOval(10, 12, x=300, y=190)
    flower3.filled = True
    flower3.fill_color = 'pink'
    flower3.color = 'pink'
    window.add(flower3)
    flower4 = GOval(10, 12, x=330, y=170)
    flower4.filled = True
    flower4.fill_color = 'pink'
    flower4.color = 'pink'
    window.add(flower4)
    flower5 = GOval(10, 12, x=240, y=180)
    flower5.filled = True
    flower5.fill_color = 'pink'
    flower5.color = 'pink'
    window.add(flower5)

    x_y_lable.font = '-25'
    window.add(x_y_lable)  # window.add(x_y_lable, x=x, y=y)
    onmousemoved(position)  # 顯示滑鼠位置的x,y

    vx = 10
    vy = -5
    while True:
        flower1.move(vx, vy)
        flower2.move(vx, vy)
        flower3.move(vx, vy)
        flower4.move(vx, vy)
        flower5.move(vx, vy)
        pause(80)


def position(mouse):
    """
    x_y_lable.x = mouse.x
    x_y_lable.y = mouse.y
    每次滑鼠移動都要更新滑鼠的位置

    """
    global x
    global y
    x_y_lable.x = mouse.x
    x_y_lable.y = mouse.y
    x = x_y_lable.x
    y = x_y_lable.y
    x_y_lable.text = str(x_y_lable.x) + "," + str(x_y_lable.y)


if __name__ == '__main__':
    main()
