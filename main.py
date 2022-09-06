# from colorgram import extract  # prepare for extracting color
# get the color list and copy the results for the color_list below
# color_num = 30  # decide how many color do you want
# colors = extract('hirst_spot_painting.jpg', color_num)  # use extract
# rgb_list = []  # create an empty list to save rgb datas
# for colors_item in range(0, color_num-1):  # only catch rgb tuples from what we have extracted
#     rgb = colors[colors_item].rgb
#     rgb_num = (rgb.r, rgb.g, rgb.b)
#     rgb_list.append(rgb_num)
#
# print(rgb_list)
from turtle import *
from random import choice

spot = Turtle()  # create the object
spot.speed('fastest')
spot.hideturtle() # hide the turtle to make the picture purer
colormode(255)  # set the color mode to prevent odd mistikes
color_list = [(246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247), (197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98)]
# move the starting point
spot.penup()  # hide the black line
spot.goto(-200, -200)  # set the starting point

for vetical in range(10):
    for horizon in range(10):
        color = choice(color_list)
        spot.dot(20, color)
        spot.forward(50)
    position = spot.position()  # get the current position of turtle
    spot.goto(position[0]-50*10, position[1]+50)  # move a turtle to start a new line

screen = Screen()
screen.exitonclick()
