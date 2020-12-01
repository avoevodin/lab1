# Drawing of arc chain
#
# 

import math
import turtle

turtle.shape('turtle')

def arc(r, arc_direction, first_move = 0):
	"""Draw the arc.
	
	Keyword arguments:
	r - radius.
	arc_direction -- direction of turtle moving, 1 - right, 0 - left.
	vert_amount -- amount of polygon vertexes.
	
	At the first bunch of arc turtle should be rotated on half of polygon's angle in 
	the opposite direction of arc-bunches.
	
	"""
    vert_amount = 80
    arc_vert_amount = int(vert_amount / 2);
    edge = 2 * r * math.sin(math.radians(360 / (2 * vert_amount)))
    polygon_angle = (vert_amount - 2) / vert_amount * 180
    angle = 180 - polygon_angle
    
    for i in range(arc_vert_amount):
        if first_move and i == 0: 
            turtle.title(angle)
            rotate_turtle(polygon_angle / 2, not arc_direction)
        else:
            rotate_turtle(angle, arc_direction)
        turtle.forward(edge)
        
def rotate_turtle(angle, arc_direction):
	"""Rotate turtle in needed direction.
	
	Keyword arguments:
	angle -- rotation angle.
	arc_direction -- rotation direction. 1 - right, 0 - left.
	
	"""
    if arc_direction:
        turtle.right(angle)
    else:
        turtle.left(angle)
    
r1 = 24
r2 = r1/4
for i in range(6):
    arc(r1, 1, i == 0)
    arc(r2, 1)
    