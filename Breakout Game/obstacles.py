from turtle import Turtle
import random


coordinates = [
    [-250, 280], [-150, 280], [-50, 280], [50, 280], [150, 280], [250, 280],
    [-250, 230], [-150, 230], [-50, 230], [50, 230], [150, 230], [250, 230],
    [-250, 180], [-150, 180], [-50, 180], [50, 180], [150, 180], [250, 180],
    [-250, 130], [-150, 130], [-50, 130], [50, 130], [150, 130], [250, 130]
]

colour_list = ["red", "blue", "green", "yellow", "orange", "coral",]
class Obstacles():
    def __init__(self):
        self.obstacles_list = []

    def create_obs(self):
        for each in coordinates:
            new_obs = Turtle("square")
            new_obs.penup()
            new_obs.color(random.choice(colour_list))
            new_obs.shapesize(1.5, 4)
            new_obs.goto(each[0], each[1])
            self.obstacles_list.append(new_obs)
