# Drawing of circle
#
# vert_amount - amount of polygon's vertixes
# angle - polygon's angle
# edge_width - polygon's edge width

import turtle

turtle.shape('turtle')

vert_amount = 200
angle = 180 - (vert_amount - 2) / vert_amount * 180
edge_width = 1

for i in range(vert_amount):
	turtle.left(angle)
	turtle.forward(edge_width)
	