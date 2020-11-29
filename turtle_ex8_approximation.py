import turtle
import math

turtle.shape('turtle')

angle_step = math.pi / 180 * 45
shift = 8
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
	