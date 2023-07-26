from turtle import Turtle
from random import randint

ENEMIES_COUNT = 10
COLOR = "blue"


class Enemies:
    def __init__(self):
        self.enemies_list = []
        self.count = 0
        self.enemies_finished = False

    def create_enemy(self):
        if self.count < ENEMIES_COUNT:
            number = randint(1, 60)
            if number == 6:
                self.count += 1
                new_enemy = Turtle("turtle")
                new_enemy.shape("images/enemy2.gif")
                new_enemy.color(COLOR)
                new_enemy.right(90)
                new_enemy.penup()
                new_enemy.goto(randint(-260, 260), 350)
                self.enemies_list.append(new_enemy)
        else:
            self.enemies_finished = True

    def enemy_move(self):
        for enemy in self.enemies_list:
            enemy.forward(1)

    def delete_enemy(self):
        pass
