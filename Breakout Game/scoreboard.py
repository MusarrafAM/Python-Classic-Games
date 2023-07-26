from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("green")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(200, 310)
        self.write(f"Score:{self.score}/24", align="center", font=("courier", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()
