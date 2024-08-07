from turtle import Turtle, Screen, color
from paddle import Paddle
import paddle


screen = Screen()

""" set up the screen """

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

""" create paddle """
screen.tracer(False)

paddles = Paddle()

screen.tracer(True)


screen.exitonclick()