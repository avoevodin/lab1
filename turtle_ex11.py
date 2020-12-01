# Drawing butterfly
#
# base_rad - radius of first circles
#
# max_rad - radius of max radius of the circles (not including)
#
# rad_step - step of radius increasing

import math
import turtle

turtle.shape('turtle')

def circle(r):
	"""Drawing of two horizontal symmetric circles with input radius"""
    vert_amount = 80
    edge = 2 * r * math.sin(math.radians(360 / (2 * vert_amount))) 
    angle = 180 - (vert_amount - 2) / vert_amount * 180
    
    for i in range(2):
        for j in range(vert_amount):
            if i:
                turtle.right(angle)
            else:
                turtle.left(angle)
            turtle.forward(edge)

base_rad = 40
max_rad = 120
rad_step = 6

turtle.left(90)

for r in range(base_rad, max_rad, rad_step):
    circle(r)
    r += rad_step