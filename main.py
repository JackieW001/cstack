from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []

t = new_matrix() 
ident(t)
stack = [t]

transform = new_matrix()

parse_file( 'script2', stack, edges, polygons, transform, screen, color )
