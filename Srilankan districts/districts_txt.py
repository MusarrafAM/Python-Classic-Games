from turtle import Turtle


class Text(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.1, stretch_len=0.1)
        self.name1 = name
        self.color("blue")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.write(f"{name}", font=('Times New Roman', 10, 'bold'))



    def red(self):
        self.clear()
        self.color("red")
        self.write(f"{self.name1}", font=('Times New Roman', 10, 'bold'))



