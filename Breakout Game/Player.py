from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/paddle.gif")
        self.color("black")
        self.shapesize(1, 5)
        self.penup()
        self.goto(0, -330)

    def move_right(self):
        if self.xcor() < 250:
            self.goto(self.xcor() + 20, -330)

    def move_left(self):
        if self.xcor() > -250:
            self.goto(self.xcor() - 20, -330)

    def reset_player(self):
        self.goto(0, -330)