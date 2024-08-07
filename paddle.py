from turtle import Turtle

STARTING_POSITION = [(350, 0), (-350, 0)]

# Move distance of the paddle
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self, position):
        self.paddle = Turtle(shape="square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(position)

    # control paddle movements

    def up(self):
        self.new_y = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def down(self):
        self.new_y = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), self.new_y)