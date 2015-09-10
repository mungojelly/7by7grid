from colour import Color

for row in range(7):
    for column in Color("gray").range_to(Color("lime"),7):
        print column.hex_l,
    print
    
