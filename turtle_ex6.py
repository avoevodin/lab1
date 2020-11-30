# Drawing a spider consisted of turtles
#
# paw_amount - amount of spider's paws
#
# paw_length - length of spider's paws
#
# angle - angle between the paws

import turtle

turtle.shape('turtle')

paw_amount = 16
paw_length = 80
angle = 360 / paw_amount

for i in range(16):
    turtle.forward(paw_length)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.left(angle)
