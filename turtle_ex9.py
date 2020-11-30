# Drawing of nested regular polygons.
#
# r - initial radius of circumscribed circle of the least polygon.
#
# r_step - the step of increasing radius of polygon's circumscribed circle.
#
# edge - the size of polygon's edge, that calculated with radius of circumscribed circle
# and amount of vertexes.
#
# angle - the angle of polygon, that calculated with amount of it's vertexes.
#
# r_angle_first - initial angle of iterative rotating.
# 
# r_angle - angle of iterative rotating, that used for drawing polygon with 
# 'turtle_polygon' function.
# 
# This program code calculates edge and angle of each nested polygon by radius of 
# circumscribed circle and amount of vertexes. Then it move the turtle in the right point
# of crossing the circle and the abscissa. Each polygon is drawing from similar point of 
# each iteration. Abscissa in this cases serves like a bisector. Variable r_angle_init 
# makes turtle direction correct for the turtle_polygon function, and then returns it to 
# the default position. Turtle moves at the next point with the step variable (for the
# first polygon it equal r, then r_step) and iteration repeats.


import math
import turtle

turtle.shape('turtle')

def turtle_polygon(angle, edge, vert_amount):
    """Drawing a regular polygon with size of angle and edge and vertexes amount"""
    for i in range(vert_amount):
        turtle.forward(edge)
        turtle.left(angle)
    
r = 24
r_step = 16

for i in range(3, 21, 1):
    edge = 2 * r * math.sin(math.radians(360 / (2 * i))) 
    angle = (i - 2) / i * 180
    r_angle_init= 180 - angle / 2
    r_angle = 180 - angle
    
    if i == 3:
        step = r
    else:
        step = r_step
        
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()
    turtle.left(r_angle_init)
        
    turtle_polygon(r_angle, edge, i)
    turtle.right(r_angle_init)
    r += r_step
    