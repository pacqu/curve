from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    print transform
    fi =  open(fname, "r")
    lines = []
    for line in fi:
        lines.append(line.strip('\n'))
    print lines
    i = 0
    while( i < len(lines) ):
        cmd = lines[i]
        no_args = ["ident", "apply","quit","display","save",""]    
        if (cmd in no_args ):
            if (cmd == "ident"):
                ident( transform )
            elif (cmd == "apply"):
                matrix_mult(transform, points)
            elif (cmd == "display"):
                clear_screen(screen)
                draw_lines(points, screen, color)
                display(screen)
            elif(cmd == "save"):
                save_ppm(screen, lines[i + 1])
                i += 1
            elif (cmd == "quit"):
                return
            i += 1
        else:
            curr_args = lines[i + 1].split(" ")
            curr_args = [float(j) for j in curr_args]
            print cmd
            print curr_args
            if (cmd == "line"):
                add_edge(points,curr_args[0],curr_args[1],curr_args[2],
                         curr_args[3],curr_args[4],curr_args[5])
            if (cmd == "circle"):
                add_circle( points, curr_args[0],curr_args[1], 0, curr_args[2], 1)
            if (cmd == "hermite"):
                add_curve( points, curr_args[0], curr_args[1], curr_args[2], curr_args[3],
                           curr_args[4], curr_args[5], curr_args[6], curr_args[7], .01, 
                           "hermite")
            if (cmd == "bezier"):
                add_curve( points, curr_args[0], curr_args[1], curr_args[2], curr_args[3],
                           curr_args[4], curr_args[5], curr_args[6], curr_args[7], .01,
                           "bezier")
            if (cmd == "scale"):
                scl = make_scale(curr_args[0],curr_args[1],curr_args[2])
                matrix_mult(scl, transform)
            if (cmd == "xrotate"):
                xr = make_rotX(math.radians(curr_args[0]))
                matrix_mult(xr, transform)
            if (cmd == "yrotate"):
                yr = make_rotY(math.radians(curr_args[0]))
                matrix_mult(yr, transform)
            if (cmd == "zrotate"):
                zr = make_rotZ(math.radians(curr_args[0]))
                matrix_mult(zr, transform)
            if (cmd == "translate"):
                trn = make_translate(curr_args[0], curr_args[1], curr_args[2])
                matrix_mult(trn, transform)
            i += 2
    return lines

#print parse_file("script_curves", 0, 0, 0, 0)
