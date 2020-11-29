# Drawing of square spiral
#
# Just drawing a square spiral. 

import turtle

turtle.shape('turtle')

cur_len = 0
inc_step = 4

for i in range(100):
	
	if i == 0:
		turtle.forward(cur_len)
		cur_len += inc_step	
	
	turtle.left(90)
	turtle.forward(cur_len)
	cur_len += inc_step
	
	