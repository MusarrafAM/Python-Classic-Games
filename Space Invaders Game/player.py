from turtle import Turtle, Screen
from bullet import Bullet

MOVE_SPEED = 30
COLOR = "red"
PLAYER_Y_AXIS = -320

screen = Screen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.bullet = None
        self.speed(0)
        self.player_speed = MOVE_SPEED
        self.shape("images/playerspace.gif")
        self.color(COLOR)
        self.shapesize(stretch_wid=3, stretch_len=2)
        self.penup()
        self.left(90)
        self.goto(0, PLAYER_Y_AXIS)
        self.bullet = Bullet()

    def move_left(self):
        current_x = self.xcor()
        if current_x >= - 265:
            new_x = current_x - self.player_speed
            self.goto(new_x, PLAYER_Y_AXIS)

    def move_right(self):
        current_x = self.xcor()
        if current_x <= 265:
            new_x = current_x + self.player_speed
            self.goto(new_x, PLAYER_Y_AXIS)

    def shoot(self):
        self.bullet.create_bullet(self.xcor())
