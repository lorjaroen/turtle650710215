"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['green', 'purple', 'green', 'purple', 'green', 'purple', 'green', 'purple']:
    t.color(c)
    t.left(45)
    t.forward(75)
    t.left(90)