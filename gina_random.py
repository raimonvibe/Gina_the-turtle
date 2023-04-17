from turtle import Turtle, Screen
import random

gina = Turtle()

gina.shape("turtle")
gina.color("lightgreen")
gina.shapesize(2, 2, 2)
gina.turtlesize(2,2,2)
gina.pensize(5)

# Define a function to generate a random angle
def random_angle():
    return random.randint(0, 360)

# Define a function to generate a random distance
def random_distance():
    return random.randint(10, 50)

# Define a function to generate a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Draw a line using a random color
for i in range(100):
    gina.color(random_color())
    angle = random_angle()
    distance = random_distance()
    gina.setheading(angle)
    gina.forward(distance)




screen = Screen()
screen.exitonclick()