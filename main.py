from turtle import Turtle, Screen, color
from ball import Ball
from paddle import Paddle
import time


STARTING_POSITION = [(350, 0), (-350, 0)]

screen = Screen()

""" set up the screen """

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

""" create paddles """
screen.tracer(False) # remove animation

right_paddle = Paddle(STARTING_POSITION[0])

left_paddle = Paddle(STARTING_POSITION[1])

screen.tracer(True)

""" create ball """
main_baller = Ball()

""" Listen to key strokes """

screen.listen()

# control left paddle with w, z keys
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="z", fun=left_paddle.down)

# control right paddle with up, down keys
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.01)
    main_baller.move_forward()

    """ detect collisions with top and bottom coors """
    if main_baller.ycor() > 280 or main_baller.ycor() < -280:
        main_baller.bounce_y()
    
    """ detect collisions btw ball and paddles """
    """ check the ball gone far enough to the right(320) and the distance bt paddle and ball is within 50 pixels from the right """
    """ check the ball gone far enough to the left(-320) and the distance bt paddle and ball is within 50 pixels from the left """
    if main_baller.distance(right_paddle.paddle) < 50 and main_baller.xcor() > 320:
        main_baller.bounce_x()
    elif main_baller.distance(left_paddle.paddle) < 50 and main_baller.xcor() < -320:
        main_baller.bounce_x()
screen.exitonclick()