from turtle import Turtle


class Health(Turtle):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.penup()
        self.hideturtle()
        self.color("red")
        self.update_health()

    def update_health(self):
        self.clear()
        self.goto(-220, 310)
        self.write(f"Chances:{self.health}", align="center", font=("courier", 20, "bold"))

    def decrease_health(self):
        self.health -= 1
        self.update_health()
