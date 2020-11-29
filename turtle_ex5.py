import turtle

turtle.shape('turtle')

edge_width = 20
shift_length = (edge_width ** 2 * 2) ** 0.5 * 0.5

for i in range(10):
 	
	for j in range(4):
		
		turtle.forward(edge_width)
		
		if j == 3:
			turtle.right(45)
		else:
			turtle.left(90)
	
	turtle.penup()
	edge_width = ((shift_length * (i + 2) * 2) ** 2 / 2) ** 0.5
	turtle.forward(shift_length)
	turtle.pendown()
	turtle.left(135)
	
	
