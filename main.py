from turtle import Turtle, Screen, colormode
import random
import colorgram
tim = Turtle()
colormode(255)


tim.speed(0)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    rgb_colors.append(color.rgb)


def random_color():
    choice = random.randint(0, 29)
    return rgb_colors[choice].r, rgb_colors[choice].g, rgb_colors[choice].b


tim.ht()
tim.pu()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
start_position = tim.position()
for i in range(10):
    start_position = tim.position()
    tim.pd()
    for j in range(10):
        tim.color(random_color())
        tim.dot(20)
        tim.pu()
        tim.forward(50)
        tim.pd()
    tim.pu()
    tim.setposition(start_position)
    tim.left(90)
    tim.forward(40)
    tim.right(90)


screen = Screen()
screen.exitonclick()
