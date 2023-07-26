from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.hideturtle()
        self.color("green")
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("courier", 80, "normal"))


    def increase_right(self):
        self.right_score += 1
        self.update_score()


    def increase_left(self):
        self.left_score += 1
        self.update_score()

