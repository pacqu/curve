from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    #t = 0
    for t in range(0, 360, step):
        x0 = ( r * math.sin(math.radians(t)) ) + cx  
        x1 = ( r * math.sin(math.radians(t + step)) ) + cx  
        y0 = ( r * math.cos(math.radians(t)) ) + cy  
        y1 = ( r * math.cos(math.radians(t + step)) ) + cy  
        add_edge(points, x0, y0, 0, x1, y1, 0)
        
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    x_coefs = []
    y_coefs = []
    if (curve_type == "bezier"):
        x_coefs = generate_curve_coefs(x0, x1, x2, x3, "bezier")
        y_coefs = generate_curve_coefs(y0, y1, y2, y3, "bezier")
    elif (curve_type == "hermite"):
        x_coefs = generate_curve_coefs(x0, x1, x2, x3, "hermite")
        y_coefs = generate_curve_coefs(y0, y1, y2, y3, "hermite")

    xa = x_coefs[0][0]
    xb = x_coefs[0][1]
    xc = x_coefs[0][2]
    xd = x_coefs[0][3]
        
    ya = y_coefs[0][0]
    yb = y_coefs[0][1]
    yc = y_coefs[0][2]
    yd = y_coefs[0][3]    

    t = 0
    while( (t + step) <=1):
        x0 = (xa * (t**3) ) + (xb * (t**2) ) + (xc * t) + xd  
        x1 = (xa * ( (t + step)**3) ) + (xb * ( (t + step)**2) ) + (xc * (t + step)) + xd  
        y0 = (ya * (t**3) ) + (yb * (t**2) ) + (yc * t) + yd  
        y1 = (ya * ( (t + step)**3) ) + (yb * ( (t + step)**2) ) + (yc * (t + step)) + yd  
        add_edge(points, x0, y0, 0, x1, y1, 0)
        t += step


def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

