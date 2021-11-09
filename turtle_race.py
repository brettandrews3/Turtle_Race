"""This program simulates a turtle racing game. It creates five
turtle icons in different shapes and colors. The icons generate on the left edge
of the turtle window. On each turn, each icon moves 0-2 spaces, randomly generated
by the random module. The race is complete when a turtle crosses the finish line.
"""

import turtle
import random

turtles = list()

def setup():
    global turtles
    startline = -480
    
    turtle_color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    turtle_ycor = [60, 40, 20, 0, -20, -40, -60]
    turtle_shape = ['turtle', 'arrow', 'square', 'circle', 'square', 'arrow', 'turtle']
    
    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape(turtle_shape[i])
        new_turtle.color(turtle_color[i])
        new_turtle.setpos(startline, turtle_ycor[i])
        turtles.append(new_turtle)

setup()
turtle.mainloop()