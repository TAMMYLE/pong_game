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
screen.tracer(0) # remove animation

""" create paddles """
right_paddle = Paddle(STARTING_POSITION[0])

left_paddle = Paddle(STARTING_POSITION[1])


""" create ball """
main_ball = Ball()

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
    time.sleep(0.09)
    main_ball.move_forward()

    """ detect collisions with top and bottom coors """
    if main_ball.ycor() > 280 or main_ball.ycor() < -280:
        main_ball.bounce_y()
    
    """ detect collisions btw ball and paddles """
    """ check the ball gone far enough to the right(320) and the distance bt paddle and ball is within 50 pixels from the right """
    """ check the ball gone far enough to the left(-320) and the distance bt paddle and ball is within 50 pixels from the left """
    if main_ball.distance(right_paddle.paddle) < 50 and main_ball.xcor() > 320 or main_ball.distance(left_paddle.paddle) < 50 and main_ball.xcor() < -320:
        main_ball.bounce_x()

    """ detect if the ball goes out to the edges of the screen --> yes ---> reset the ball to the center  """
    """                                                        --> no ---> the ball should start moving towards the other player """
    if main_ball.xcor() > 380:
        main_ball.reset_ball()
    
    if main_ball.xcor() < -380:
        main_ball.reset_ball()

screen.exitonclick()