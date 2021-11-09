"""This program simulates a turtle racing game. It creates five
turtle icons in different shapes and colors. The icons generate on the left edge
of the turtle window. On each turn, each icon moves 0-2 spaces, randomly generated
by the random module. The race is complete when a turtle crosses the finish line.
"""

import turtle
import random

turtles = list()

def setup():
    """The setup function uses three lists and a for loop to generate the
        turtles used in the program. The global permission allows the use
        of the main turtles list within setup(). The for loop creates a turtle,
        lifts its pen, and moves it to the startline before dropping the pen again.
        Startline is set at the left edge of the turtle window.
    """
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')
    
    turtle_color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    turtle_ycor = [60, 40, 20, 0, -20, -40, -60]
    turtle_shape = ['turtle', 'arrow', 'square', 'circle', 'square', 'arrow', 'turtle']
    
    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape(turtle_shape[i])
        new_turtle.color(turtle_color[i])
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.pendown()
        turtles.append(new_turtle)

def race():
    """Here you go, race fans: the explanation on how this sucker works!
    """
    global turtles
    winner = False
    finishline = 590
    
    while not winner:
        for current_turtle in turtles:
            current_turtle.forward(randint(0,2))




setup()
turtle.mainloop()