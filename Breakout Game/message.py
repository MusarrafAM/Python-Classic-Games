from turtle import Turtle


class Message:
    def __init__(self, text):
        self.message = Turtle()
        self.message.penup()
        self.message.hideturtle()
        self.message.color("red")
        self.message.write(text, move=False, align="center", font=("Arial", 40, "normal"))

    def deleteMessage(self):
        self.message.clear()
