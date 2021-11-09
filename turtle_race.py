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
    
    turtle_color = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    turtle_ycor = [120, 80, 40, 0, -40, -80, -120]
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
    """race() drives the action of the program. It imports turtles as a global variable
        and sets the win condition, 'winner', to False. The 'while not winner' loop cycles
        through the turtles and moves each one forward 0-2 pixels per pass. After each
        movement, the while loop checks the turtle's current x-coordinate (xcor). If that
        turtle's xcor is >= the finishline value, the win condition is flipped to True
        and the print statement announces the race winner.
    """
    global turtles
    winner = False
    finishline = 590
    
    while not winner:
        for current_turtle in turtles:
            move = random.randint(0,2)
            current_turtle.forward(move)
            
            xcor = current_turtle.xcor()
            if xcor >= finishline:
                winner = True
                winner_color = current_turtle.color()
                print(winner_color[0], 'wins the race!')

setup()
race()
turtle.mainloop()