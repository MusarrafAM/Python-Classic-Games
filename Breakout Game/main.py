# Breakout  game
from turtle import Screen
from Player import Player
from obstacles import Obstacles
from ball import Ball
from scoreboard import Scoreboard
from health import Health
from message import Message
import time

screen = Screen()
screen.register_shape("images/paddle.gif")
screen.register_shape("images/fireball.gif")
screen.register_shape("images/space4.gif")

screen.setup(600, 700)
screen.listen()
screen.bgcolor("black")
screen.bgpic('images/space4.gif')

screen.tracer(0)

game_is_on = True

player = Player()
obstacles = Obstacles()
ball = Ball()
scoreboard = Scoreboard()
health = Health()

screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")


obstacles.create_obs()
while game_is_on:
    # time.sleep(0.005)
    time.sleep(0.01)
    ball.ball_move()

    # # Bounce with paddle
    if ball.distance(player) < 35:
        ball.bounce_top_or_paddle()

    # bounce with two side walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_wall()

    # bounce with top wall
    if ball.ycor() > 340:
        ball.bounce_top_or_paddle()

    # collide with obstacles
    for each_obs in obstacles.obstacles_list:
        if ball.distance(each_obs) < 35:
            ball.bounce_top_or_paddle()
            each_obs.goto(500, 500)
            scoreboard.increase_score()

    # Win
    if scoreboard.score == 24:
        game_is_on = False
        Message("You've won!")

    # Game over
    if ball.ycor() < -350:
        if health.health > 1:
            health.decrease_health()
            ball.reset_ball()
            player.reset_player()
        else:
            health.decrease_health()
            game_is_on = False
            Message("Game Over")
    screen.update()

screen.exitonclick()
