from turtle import Turtle


class Message:
    def __init__(self, text, color):
        self.message = Turtle()
        self.message.penup()
        self.message.hideturtle()
        self.message.color(color)
        self.message.write(text, move=False, align="center",
                           font=("Arial", 20, "normal"))

    def deleteMessage(self):
        self.message.clear()
