from turtle import Turtle
BALL_COLOUR = "yellow"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("circle")
        self.shape('images/fireball.gif')
        self.penup()
        self.color(BALL_COLOUR)
        self.move_speed = 2
        self.x_move = self.move_speed
        self.y_move = self.move_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 20

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.move_speed = 2
