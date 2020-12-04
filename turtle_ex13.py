# Drawing a smile
#
# Drawing a smile with functions, that drawing circles and arcs

import math
import turtle

turtle.shape('turtle')

def arc(r, mv_direction):
    """Draw arc with a selected radius and direction of drawing
    
    Keyword arguments:
    r -- the radius of arc-circle (float)
    mv_direction -- the direction of turtle moving. 1 - right
         direction, left direction (int)
    
    """
    
    vert_amount = 80
    arc_vert_amount = int(vert_amount / 2);
    edge = 2 * r * math.sin(math.radians(360 / (2 * vert_amount)))
    polygon_angle = (vert_amount - 2) / vert_amount * 180
    angle = 180 - polygon_angle
    
    for i in range(arc_vert_amount):
        if i == 0: 
            rotate_turtle(polygon_angle / 2, not mv_direction)
        else:
            rotate_turtle(angle, mv_direction)
        turtle.forward(edge)
        
def circle(r, mv_direction):
    """Draw circle with a selected radius and direction of drawing
    
    Keyword arguments:
    r -- the radius of circle (float)
    mv_direction -- the direction of turtle moving. 1 - right
         direction, left direction (int)
    
    """
    vert_amount = 80
    edge = 2 * r * math.sin(math.radians(360 / (2 * vert_amount))) 
    polygon_angle = (vert_amount - 2) / vert_amount * 180
    angle = 180 - polygon_angle
    
    for i in range(vert_amount):
        if i == 0: 
            rotate_turtle(polygon_angle / 2, not mv_direction)
        else:
            rotate_turtle(angle, mv_direction)
        turtle.forward(edge)

def rotate_turtle(angle, mv_direction):
    """Rotate turtle with selected angle and direction of drawing
    
    Keyword arguments:
    angle -- angle of turtle rotation (float)
    mv_direction -- the direction of turtle moving. 1 - right
         direction, left direction (int)
         
    """
    
    if mv_direction == 1:
        turtle.right(angle)
    else:
        turtle.left(angle)
        
face_r = 120    # init parameters
face_r_half = face_r / 2
eye_r = 20
eye_r_shift = eye_r * 1.2
smile_r = face_r / 2
smile_w = 14
nose_l = 24
nose_w = 12

turtle.seth(0)  # draw face
turtle.penup()
turtle.goto(-face_r, 0)
turtle.pendown()
turtle.penup()
turtle.pendown()
turtle.color('black', 'yellow')
turtle.begin_fill()
circle(face_r, 0)
turtle.end_fill()

turtle.color('black', 'blue')

for i in (1, -1):   # draw eyes
    turtle.penup()
    turtle.goto(i * (face_r_half - eye_r_shift), face_r_half - eye_r_shift)
    turtle.pendown()
    turtle.seth(90 * (i-1))
    turtle.begin_fill()
    circle(eye_r, 1)
    turtle.end_fill()
 
turtle.penup()  # draw nose   
turtle.setpos(0, 0)
turtle.pendown()
turtle.width(nose_w)
turtle.seth(90)
turtle.forward(nose_l / 2)
turtle.seth(-90)
turtle.forward(nose_l)

turtle.seth(180)    # draw smile
turtle.penup()
turtle.setpos(face_r / 2, -face_r * 0.2)    
turtle.pendown()  
turtle.color('red')  
arc(smile_r, 1)
