from colour import Color

start_colors = list(Color("#A0A0A0").range_to(Color("#404040"),7))
end_colors = list(Color("#00FF00").range_to(Color("#009900"),7))
for row in range(7):
    for column in start_colors[row].range_to(end_colors[row],7):
        print column.hex_l,
    print
