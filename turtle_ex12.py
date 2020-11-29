import math
import turtle

turtle.shape('turtle')

def arc(r, arc_direction):
	vert_amount = 80
	arc_vert_amount = int(vert_amount / 2);
	edge = 2 * r * math.sin(math.radians(360 / (2 * vert_amount))) 
	angle = 180 - (vert_amount - 2) / vert_amount * 180
	
	for i in range(arc_vert_amount):
		rotate_turtle(angle, arc_direction)
		turtle.forward(edge)
		
	turtle.title(turtle.pos())

def	rotate_turtle(angle, arc_direction):
	if arc_direction:
		turtle.right(angle)
	else:
		turtle.left(angle)
	
def circle(edge):
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
		turtle.title(turtle.pos())
	
turtle.left(90)

r1 = 24
r2 = r1/4
edge1 = 4
edge2 = 1
for i in range(6):
	arc(r1, 1)
	arc(r2, 1)
	