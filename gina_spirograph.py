import turtle
from turtle import Turtle, Screen
import random

gina = Turtle()

gina.shape("turtle")
gina.color("lightgreen")
gina.shapesize(2, 2, 2)
gina.turtlesize(2,2,2)
gina.pensize(2)
turtle.speed("fastest")
turtle.speed("fastest")

# Define a function to generate a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Draw 36 circles, each at a different angle and with a random color
for i in range(0, 360, 10):
    gina.color(random_color())  # Set the turtle's color to a random color
    gina.setheading(i)  # Set the turtle's heading to the current angle
    gina.circle(50)  # Draw a circle with radius 50

# Create a screen object and wait for user to close window
screen = Screen()
screen.exitonclick()

# Define a function to generate a random angle
def angle():
    for i in range(0, 360):
        return i



# Define a function to generate a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

for i in range(36):
    gina.color(random_color())
    gina.setheading(10*i)
    gina.circle(50)


screen = Screen()
screen.exitonclick()