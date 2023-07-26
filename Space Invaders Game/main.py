# shooter game
from turtle import Screen
from player import Player
from enemies import Enemies
from message import Message
import time


screen = Screen()
# Adding Images
screen.register_shape("images/playerspace.gif")
screen.register_shape("images/enemy2.gif")
screen.register_shape("images/bullet.gif")
screen.register_shape("images/space.gif")
screen.bgcolor("black")
screen.bgpic('images/space.gif')
screen.setup(550, 700)
screen.listen()
screen.tracer(0)

player = Player()
enemies = Enemies()
timer = 3
while timer != 0:
    message = Message(f"Game Starts in {timer}")
    message.deleteMessage()
    time.sleep(1)
    timer -= 1

game_is_on = True

screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.shoot, key="space")

while game_is_on:
    # time.sleep(0.005)
    time.sleep(0.01)
    screen.update()
    # Move the bullet
    player.bullet.bullets_move()

    # Create enemies
    enemies.create_enemy()
    enemies.enemy_move()

    # check if bullet hits the enemies
    for each_enemy in enemies.enemies_list:
        for each_bullet in player.bullet.bullet_list:
            if each_enemy.distance(each_bullet) < 20:
                each_enemy.goto(1000, 1000)
                enemies.enemies_list.remove(each_enemy)
                each_bullet.goto(1000, -1000)
                player.bullet.bullet_list.remove(each_bullet)

        # Check if the enemy went over.
        if each_enemy.ycor() < -350:
            game_is_on = False
            message = Message("Game Over")

    # check if no enemies
    if enemies.enemies_finished and enemies.enemies_list == []:
        game_is_on = False
        message = Message("You've  Won")

screen.exitonclick()
