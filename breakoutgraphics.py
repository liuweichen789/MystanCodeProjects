"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
製作遊戲主要物件:brick，ball，paddle。
設定球除了掉到視窗下面以外，打到東西都要反彈。
設定paddle的水平位置由滑鼠控制，但滑鼠超出視窗時，paddle會停在最邊邊。
這定開始遊戲的開關、
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset-self.paddle.height)  # 如果self.window.width改用window_widt是不是一樣?

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(width=brick_width, height=brick_height, x=i * (BRICK_WIDTH + BRICK_SPACING),
                                   y=BRICK_OFFSET+j * (BRICK_HEIGHT + BRICK_SPACING))  # 做出不同位置的brick
                self.brick.filled = True
                if j <= 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 2 <= j <= 3:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'

                elif 4 <= j <= 5:
                    self.brick.fill_color = 'gold'
                    self.brick.color = 'gold'
                elif 6 <= j <= 8:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(
                    self.brick)  # 不可以用self.window.add(self.brick, x=i * (BRICK_WIDTH + BRICK_SPACING), y=j * (BRICK_HEIGHT + BRICK_SPACING))，會同一brick跑過不同位置，停在最後的位

        # Initialize our mouse listeners
        onmousemoved(self.reset_paddle_position)
        # onmousemoved(self.reset_new_paddle_position)  # breakout2 未完成
        onmouseclicked(self.ball_start_moving)
        self.ball_moving = False                      # def 裡面要用到的variable要先在__init__裡面定義，初始化
        self.__dx = 0
        self.__dy = 0

        # new_baddle， breakout2 未完成
        # self.new_baddle = GRect(width=paddle_width*2, height=paddle_height)
        # self.new_baddle.filled = True
        # self.new_baddle.fill_color = 'yellowgreen'
        # self.new_baddle.color = 'yellowgreen'

        # Default initial velocity for the ball
    def get_dx(self):
        """
        dx = random.randrange(1, MAX_X_SPEED)
        每次出發方向不一樣，if random.random() > 0.5:
        self.__dx = - self.__dx
        :return: self.__dx
        """
        self.__dx = random.randrange(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        return self.__dx

    def get_dy(self):
        """
        dy = INITIAL_Y_SPEED
        :return: self.__dy
        """
        self.__dy = INITIAL_Y_SPEED
        return self.__dy

    def ball_start_moving(self, clikc):
        """
        點擊後，self.ball_moving = True
        :param clikc: self.ball_moving = True
        :return: self.ball_moving = True
        """
        self.ball_moving = True

    def reset_paddle_position(self, mouse):
        """
        paddle中點要跟著滑鼠，而且滑鼠跑到視窗外，paddle會到最邊邊，但不會消失
        :param mouse: 滑鼠位置mouse.x
        """
        if mouse.x >= self.window.width-self.paddle.width / 2:
            self.paddle.x = self.window.width-self.paddle.width
        elif mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
        self.paddle.y = self.window.height - PADDLE_OFFSET

    @staticmethod
    def get_ball_radius():
        """
        讓使用者得到球半徑
        :return: BALL_RADIUS
        """
        return BALL_RADIUS

    @staticmethod
    def get_paddle_width():
        """
        讓使用者得到板子寬
        :return: PADDLE_WIDTH
        """
        return PADDLE_WIDTH

    @staticmethod
    def get_brick_rows():         # 試試看用function計算好磚塊數給user用，就可以不用get
        """
        讓使用者得到磚塊行數
        :return: BRICK_ROWS
        """
        return BRICK_ROWS

    @staticmethod
    def get_brick_cols():
        """
        讓使用者得到磚塊列數
        :return: BRICK_COLS
        """
        return BRICK_COLS

    # breakout2 未完成
    # def reset_new_paddle_position(self, mouse):
    #     if mouse.x >= self.window.width-self.new_paddle.width / 2:
    #         self.new_paddle.x = self.window.width-self.nwe_paddle.width
    #     elif mouse.x <= self.new_paddle.width/2:
    #         self.new_paddle.x = 0
    #     else:
    #         self.new_paddle.x = mouse.x - self.new_paddle.width / 2
    #     self.new_paddle.y = self.window.height - PADDLE_OFFSET


