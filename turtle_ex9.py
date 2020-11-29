import math
import turtle

turtle.shape('turtle')

def turtle_polygon(angle, edge, vert_amount, r_step):
	
	for i in range(vert_amount):
		turtle.forward(edge)
		turtle.left(angle)
	
r = 24
r_step = 16

for i in range(3, 21, 1):
	
	edge = 2 * r * math.sin(math.radians(360 / (2 * i))) 
	angle = (i - 2) / i * 180
	r_angle_first = 180 - angle / 2
	r_angle = 180 - angle
	
	if i == 3:
		step = r
	else:
		step = r_step
		
	turtle.penup()
	turtle.forward(step)
	turtle.pendown()
	turtle.left(r_angle_first)
		
	turtle_polygon(r_angle, edge, i, r_step)
	turtle.right(r_angle_first)
	r += r_step
	