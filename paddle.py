from turtle import Turtle

STARTING_POSITION = [(350, 0), (-350, 0)]

class Paddle:

    def __init__(self):
        self.create_paddles()
        self.control_paddles()

    def create_paddles(self):
        """ create paddle """
        """ 1st paddle -- right side, width = 20, height = 100, x-pos = 350, y-pos = 0 """
        paddle_table = []
        
        for position in STARTING_POSITION:
            paddle = Turtle(shape="square")
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.penup()
            paddle.color("white")
            paddle.goto(position)

            # store paddles into list
            paddle_table.append(paddle)

    def control_paddles(self):
        """ control paddle """
        