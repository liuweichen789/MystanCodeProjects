"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
設定當滑鼠點擊，遊戲就開始。
設定球的四個頂點碰到磚塊，球反彈，磚塊要消失，碰到paddle，球要反彈。
當球掉出視窗下面，NUM_LIVES -= 1，當NUM_LIVES<0，遊戲結束。
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    count = NUM_LIVES
    brick_count = 0  # 計算打到的磚塊
    score_lable = GLabel('Score' + str(brick_count))  # 記分板
    score_lable.font = '-20'

    # Add the animation loop here!
    while True:        # TA: 若沒有第26行的while True，程式一開始就會進到28行，這時開關沒打開，就會到no區，而且只問一次。
        # 點按遊戲開始，球開始動
        if graphics.ball_moving:
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            while True:  # 球除了掉到下面，打到其他牆壁要反彈。
                graphics.ball.move(vx, vy)
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y < 0:
                    vy = -vy
                if graphics.ball.y >= graphics.window.height:
                    count -= 1
                    graphics.ball_moving = False
                    if count > 0:
                        graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2, y=(graphics.window.height - graphics.ball.height) / 2)
                    else:
                        game_over = GLabel('Game over')
                        game_over.font = '-40'
                        graphics.window.add(game_over, x=(graphics.window.width - game_over.width) / 2,
                                            y=(graphics.window.height - game_over.height) / 2)
                    break
                pause(FRAME_RATE)

                # 球撞到板子與磚塊要反彈，但撞到磚塊要將磚塊移除，brick_count += 1
                r = graphics.get_ball_radius()
                x = int(graphics.ball.x)
                y = int(graphics.ball.y)
                maybe_obj_1 = graphics.window.get_object_at(x, y)
                maybe_obj_2 = graphics.window.get_object_at(x + 2 * r, y)
                maybe_obj_3 = graphics.window.get_object_at(x, y + 2 * r)
                maybe_obj_4 = graphics.window.get_object_at(x + 2 * r, y + 2 * r)
                if maybe_obj_1 is not None:
                    if maybe_obj_1 is graphics.paddle:
                        if vy > 0:
                            vy = -vy
                    elif maybe_obj_1 is not score_lable:
                        vy = -vy
                        graphics.window.remove(maybe_obj_1)
                        brick_count += 1
                elif maybe_obj_2 is not None:
                    if maybe_obj_2 is graphics.paddle:
                        if vy > 0:
                            vy = -vy
                    elif maybe_obj_2 is not score_lable:
                        vy = -vy
                        graphics.window.remove(maybe_obj_2)
                        brick_count += 1
                elif maybe_obj_3 is not None:
                    if maybe_obj_3 is graphics.paddle:
                        if vy > 0:
                            vy = -vy
                    elif maybe_obj_3 is not score_lable:
                        vy = -vy
                        graphics.window.remove(maybe_obj_3)
                        brick_count += 1
                elif maybe_obj_4 is not None:
                    if maybe_obj_4 is graphics.paddle:
                        if vy > 0:
                            vy = -vy
                    elif maybe_obj_4 is not score_lable:
                        vy = -vy
                        graphics.window.remove(maybe_obj_4)
                        brick_count += 1
                score_lable.text = 'Score' + str(brick_count)

                # 磚塊已經打完，遊戲結束。
                if brick_count >= graphics.get_brick_cols()*graphics.get_brick_rows():
                    you_win = GLabel('You Win')
                    you_win.font = '-40'
                    graphics.window.add(you_win, x=(graphics.window.width-you_win.width)/2, y=(graphics.window.height-you_win.height)/2)
                    graphics.ball_moving = False
                    break

        pause(FRAME_RATE)

        # 記分板
        graphics.window.add(score_lable, x=0, y=score_lable.height)

        if brick_count >= graphics.get_brick_cols()*graphics.get_brick_rows() or count == 0:
            break  # 遊戲結束，大while True break。


if __name__ == '__main__':
    main()
