from turtle import Turtle
BULLET_SPEED = 10
COLOR = "white"


class Bullet:
    def __init__(self):
        self.bullet_list = []

    def create_bullet(self, x_cor):
        new_bullet = Turtle()
        new_bullet.shape("circle")
        new_bullet.shape("images/bullet.gif")
        new_bullet.speed(0)
        new_bullet.color(COLOR)
        new_bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_bullet.penup()
        new_bullet.goto(x_cor, -300)
        self.bullet_list.append(new_bullet)

    def bullets_move(self):
        for bullet in self.bullet_list:
            new_y = bullet.ycor() + BULLET_SPEED
            bullet.goto(bullet.xcor(), new_y)
            if new_y >= 500:
                self.bullet_list.remove(bullet)









