from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/fireball.gif")
        self.penup()
        self.color("blue")
        self.goto(0, -280)
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.1
        
    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_top_or_paddle(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(0, -280)
        self.bounce_top_or_paddle()
        self.move_speed = 0.1
