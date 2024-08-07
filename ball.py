import random
from paddle import Paddle
from turtle import Turtle

# Create directions

# set move distance
MOVE_DISTANCE = 200

# ball inherited Turtle class

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(1)
        self.shape("circle")
        self.shapesize(stretch_len=1.2, stretch_wid=1.2)
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move_forward(self):
        """ move the ball forward to new location """
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):
        """ reverse y coordinate when ball hits top or bottom boundaries """
        self.y_move *= -1
       
