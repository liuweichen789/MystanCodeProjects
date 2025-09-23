"""
File: bouncing_ball.py
Name: wei chen
-------------------------
TODO:
ball = GOval(SIZE, SIZE)做一顆球(global variable)
滑鼠點擊後
ball.move(vx, vy)，球開始移動，
if ball.y+SIZE >= window.height， 當球碰到地板vy要變-vy
vy = -vy -  REDUCE，
if ball.x >= window.width，當球彈出視窗外要重新開始。

點擊開關設在def move(mouse)，
global variable : is_clicked = False
點擊後變is_clicked = True，
等球跑出視窗後，再變回is_clicked = False，重新開始

"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
count = 0

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)

is_clicked = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(move)


def move(mouse):
    """
    3次點擊要用if設條件，if count < 3，球才可以啟動。
    預設is_clicked = False，點擊後改為is_clicked = True，等球跑出視窗，再變回is_clicked = False，重新開始

    """
    global count
    global is_clicked
    if count < 3:  # 不可以用while，如果while(狂做)滿足條件，就會是新一次的點擊，不可以讓滑鼠有進來的機會，用if讓上次點擊做完(只問一次)
        if not is_clicked:
            window.add(ball, START_X, START_Y)
            is_clicked = True
            vx = 3
            vy = 0
            while True:
                ball.move(vx, vy)
                if ball.y + SIZE >= window.height:
                    if vy > 0:
                        vy = -vy * REDUCE
                pause(DELAY)
                vy += GRAVITY
                if ball.x > window.width:
                    count += 1
                    is_clicked = False
                    window.add(ball, START_X, START_Y)
                    break
        pause(DELAY)


if __name__ == "__main__":
    main()
