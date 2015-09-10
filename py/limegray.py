from colour import Color
from colour import web2hex

for row in range(7):
    for column in Color("gray").range_to(Color("lime"),7):
        print web2hex(column.hex, force_long=True),
    print
    
