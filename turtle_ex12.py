import math
import turtle

turtle.shape('turtle')

def arc(r, arc_direction, first_move = 0):
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
        
def    rotate_turtle(angle, arc_direction):
    if arc_direction:
        turtle.right(angle)
    else:
        turtle.left(angle)
    
r1 = 24
r2 = r1/4
edge1 = 4
edge2 = 1
for i in range(6):
    arc(r1, 1, i == 0)
    arc(r2, 1)
    