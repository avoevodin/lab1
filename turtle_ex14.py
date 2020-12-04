# Drawing a stars of 5 and 11 vertexes

import turtle

def star(vert_amount, edge_width):
    """Draw a star with selected vertexes amount and edge-width
    
    Keyword arguments:
    vert_amount -- amount of star's vertexes (int)
    edge_width -- width of star's edge
    
    """
    
    turtle.seth(180) # the first edge
    turtle.forward(edge_width)
    angle = 180 - 180 / vert_amount 
    
    for i in range(vert_amount - 1):
        turtle.left(angle)
        turtle.forward(edge_width)
    
edge_width = 100

vert_amount = 5 # Draw 5-vertexes star
star(vert_amount, edge_width)

vert_amount = 11 # Draw 5-vertexes star
turtle.penup()
turtle.setpos(edge_width + 20, 0)
turtle.pendown()
star(vert_amount, edge_width)