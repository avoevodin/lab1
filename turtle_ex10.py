import math
import turtle

turtle.shape('turtle')

def circle(base_angle):
    vert_amount = 80
    angle = 180 - (vert_amount - 2) / vert_amount * 180
    edge_width = 4
    
    turtle.left(base_angle)
    
    for i in range(2):
        for j in range(vert_amount):
            if i:
                turtle.right(angle)
            else:
                turtle.left(angle)
            turtle.forward(edge_width)

axes_count = 4
angle_step = 180 / axes_count
base_angle = 0

for i in range(axes_count):
    circle(base_angle)
    base_angle += angle_step