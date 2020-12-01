# Drawing a flower
#
# step_count - count of step of rotation. Each rotation draws two centrally symmetric 
# circles.
#
# angle_step - angle of one-step axis rotation.
#
# base_angle - current angle of rotating axis

import math
import turtle

turtle.shape('turtle')

def circles(base_angle):
	"""Drawing two circles in eight-form around curent axis with curent base angle"""
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

step_count = 4
angle_step = 180 / step_count
base_angle = 0

for i in range(step_count):
    circles(base_angle)
    base_angle += angle_step