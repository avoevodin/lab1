# Drawing square spiral approximately
#
# This program code is like the same code of drawing Archimedean spiral, but with the 
# parametres of key values, which make the spiral approximately looks like a square
# spiral.

import turtle
import math

turtle.shape('turtle')

angle_step = math.radians(45)
shift = 4
angle = 0
rad = 0
pi = math.pi

for i in range(100):
    
    angle = angle + angle_step
    rad = shift * angle / (2 * math.pi)
    x = math.sin(angle) * rad
    y = math.cos(angle) * rad
    
    turtle.goto(x, y)
    angle += angle_step    
    