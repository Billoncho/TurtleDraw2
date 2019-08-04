# TurtleDraw2.py
# Billy Ridgeway
# Creates a program to draw lines on the screen by using screen clicks.

import turtle                   # Imports the turtle library.
t = turtle.Pen()                # Creates a pen named t.
t.speed(0)                      # Sets the pen's speed to fast.
turtle.bgcolor("blue")          # Set's the background color to blue.
t.pencolor("green")             # Sets the pen's color to green.
t.width(10)                     # Sets the pen's width to 10.
turtle.onscreenclick(t.setpos)  # When the screen is clicked it
                                # will call the function t.setpos
                                # and set the pen to the x y coordinates
                                # where the screen was clicked.
