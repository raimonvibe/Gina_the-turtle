from turtle import Turtle, Screen  # import Turtle and Screen classes from turtle module
import random  # import random module

# create a new Turtle object, set its shape and size
gina = Turtle()
gina.shape("turtle")
gina.shapesize(3, 3, 2)

screen = Screen()  # create a new Screen object
screen.setup(width=900, height=800)  # set screen size

# define a list of colors to use for the painting
colors_painting = [(250, 246, 243), (248, 245, 246), (212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81), (162, 206, 212), (53, 62, 81), (183, 190, 206), (85, 74, 35)]

dot_size = 30  # set dot size
dot_gap = dot_size * 2  # set gap between dots
screen.colormode(255)  # set color mode to RGB (255)

gina.speed(0)  # set turtle speed to maximum
gina.penup()  # pick up the pen
gina.setposition(-350, 350)  # move to the starting position
gina.pendown()  # put down the pen

# loop through rows
for i in range(10):
    # loop through columns
    for j in range(11):
        # calculate index in colors_painting list
        index = i*11 + j
        # choose a random color from the list
        color = random.choice(colors_painting)
        gina.color(color)  # set turtle color
        gina.begin_fill()  # start filling the circle with color
        gina.circle(dot_size/2)  # draw a circle with the chosen color
        gina.end_fill()  # end filling the circle
        # move to next dot position
        gina.penup()
        gina.forward(dot_gap)
        gina.pendown()
    # move to next row
    gina.penup()
    gina.backward(dot_gap*11)
    gina.right(90)
    gina.forward(dot_gap)
    gina.left(90)
    gina.pendown()

screen.exitonclick()  # wait for a user click to exit the screen
