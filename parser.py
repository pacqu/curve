from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    fi =  open(fname, "r")
    lines = []
    for line in fi:
        lines.append(line.strip('\n'))
    return lines

print parse_file("script_curves", 0, 0, 0, 0)
