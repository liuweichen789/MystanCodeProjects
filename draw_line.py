"""
File: draw_line.py
Name: wei chen
-------------------------
TODO:
odd click add a circle 'start',
window.add(start, x=click.x - SIZE / 2, y=click.y - SIZE / 2)
even click is end of the line,
end_x = click.x
end_y = click.y
draw a line from start to end
line = GLine(start_x, start_y, end_x, end_y)

"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 20
window = GWindow()
DELAY = 700
count = 0
start_x = 0
start_y = 0
start = 0
end = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(two_point)


def two_point(click):
    '''
    滑鼠基數次點擊，點擊時的座標放在start_x， start_y，
    偶數次點擊，點擊時的座標放在end_x, end_y，
    line = GLine(start_x, start_y, end_x, end_y)
    '''
    global count
    global start_x
    global start_y
    global start
    global end
    if count % 2 == 0:
        start = GOval(SIZE, SIZE)
        start.filled = False
        window.add(start, x=click.x - SIZE / 2, y=click.y - SIZE / 2)
        start_x = click.x
        start_y = click.y
        print(start_x, start_y)
        count += 1
    else:                       # 如果這邊用if，上面的if跑完count += 1後，就會符合偶數的條件，繼續跑第2個if，所以這裡要用else
        end_x = click.x
        end_y = click.y
        count += 1
        print(end_x, end_y)
        line = GLine(start_x, start_y, end_x, end_y)
        window.add(line)
        window.remove(start)


if __name__ == "__main__":
    main()
