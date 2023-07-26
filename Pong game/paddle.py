from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up_fun(self):
        self.currenty = self.ycor()
        if self.currenty < 250:
            self.goto(self.xcor(), self.currenty + 30)
        

    def down_fun(self):
        self.currenty = self.ycor()
        if self.currenty > -250:
            self.goto(self.xcor(), self.currenty - 30)
        
