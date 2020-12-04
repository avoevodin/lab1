import turtle

def star(vert_amount, edge_width):

    angle = 180 - 180 / vert_amount 
    turtle.seth(180) # the first edge
    turtle.forward(edge_width)

    for i in range(vert_amount - 1):
        turtle.left(angle)
        turtle.forward(edge_width)
    
edge_width = 100
vert_amount = 5

star(vert_amount, edge_width)

vert_amount = 11
turtle.penup()
turtle.setpos(edge_width + 20, 0)
turtle.pendown()
star(vert_amount, edge_width)