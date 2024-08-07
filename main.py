from turtle import Turtle, Screen, color
from paddle import Paddle
import paddle

STARTING_POSITION = [(350, 0), (-350, 0)]

screen = Screen()

""" set up the screen """

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

""" create paddle """
screen.tracer(False)

right_paddle = Paddle(STARTING_POSITION[0])

left_paddle = Paddle(STARTING_POSITION[1])

screen.tracer(True)

""" Listen to key strokes """

screen.listen()

# control left paddle with w, z keys
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="z", fun=left_paddle.down)

# control right paddle with up, down keys
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

screen.exitonclick()