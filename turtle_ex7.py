# Drawing of Archimedean spiral
#
# angle_step - step of increasing the angle of moving axe.
#
# shift - shift of the radius of turtle on the moving axe in polar coordinates for 360
# degree turn.
#
# angle - current angle of moving axe.
#
# rad - current radius of turtle in polar coordinates. It depends on the current angle in
# each iteration.
#
# In case we know current target angle and radius of turtle in polar coordinates, we can 
# locate it in cartesian coordinate system, and move turtle there.

import turtle
import math

turtle.shape('turtle')

angle_step = 0.08
shift = 5
angle = angle_step
rad = 0
pi = math.pi

for i in range(1000):
    
    rad = shift * angle / (2 * math.pi)
    x = math.sin(angle) * rad
    y = math.cos(angle) * rad
    
    turtle.goto(x, y)
    angle += angle_step    
    

    

