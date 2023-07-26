import turtle
from turtle import Screen
import pandas
from districts_txt import Text

screen = Screen()
screen.title("Name the States")

image = "pic2.gif"
screen.addshape(image)
turtle.shape(image)

score = 0

# Dataframe
data = pandas.read_csv("25_districts.csv")
districts = data["district"].tolist()


screen.tracer(0)

should_continue = True
while should_continue:
    user = turtle.textinput(title=f"{score}/25 districts correct ", prompt="Whats another district name:\n(Enter 'e' to reveal all districts)").title()
    if user == "E":
        should_continue = False
        dataframe = pandas.DataFrame(districts)
        dataframe.to_csv("Learning.txt")
    for district in districts:
        if user == district:
            score += 1
            s = data[data.district == district]
            x = s["x"].item()
            y = s["y"].item()
            name = Text(user, x, y)
            districts.remove(district)
            screen.update()


for d1 in districts:
    s = data[data.district == d1]
    x = s["x"].item()
    y = s["y"].item()
    not_guessed = Text(d1, x, y)
    not_guessed.red()







def get_mouse_click_coor(x, y):
    print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

screen.mainloop()
