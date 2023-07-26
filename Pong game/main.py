from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from message import Message
import time


screen = Screen()

screen.register_shape("images/fireball.gif")
screen.register_shape("images/bg.gif")


screen.tracer(0)

screen.setup(width=800, height=600)
# screen.bgcolor("black")
screen.bgpic('images/bg.gif')
screen.title("Pong")


# Split screen
screen_split = Turtle()
screen_split.hideturtle()
screen_split.pensize(10)
screen_split.color("purple")
screen_split.penup()
screen_split.goto(0, 300)
screen_split.pendown()
screen_split.right(90)

for _ in range(15):
    screen_split.forward(20)
    screen_split.penup()
    screen_split.forward(20)
    screen_split.pendown()


right_paddle = Paddle((380, 0))
right_paddle.color("red")
left_paddle = Paddle((-390, 0))
left_paddle.color("blue")

ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(fun=right_paddle.up_fun, key="Up")
screen.onkey(fun=right_paddle.down_fun, key="Down")

screen.onkey(fun=left_paddle.up_fun, key="w")
screen.onkey(fun=left_paddle.down_fun, key="s")


game_is_on = True


while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with the paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_paddle()

    # right Paddle misses the ball
    if ball.xcor() > 420:
        scoreboard.increase_left()
        ball.reset_ball()

    # left Paddle misses the ball
    if ball.xcor() < -420:
        scoreboard.increase_right()
        ball.reset_ball()

    if scoreboard.right_score >= 10:
        message = Message("Player Red Wins", "red")
        time.sleep(2)
        game_is_on = False

    elif scoreboard.left_score >= 10:
        message = Message("Player Blue Wins", "blue")
        time.sleep(2)
        game_is_on = False


screen.exitonclick()
