from colour import Color

input = []
while (len(input) < 49):
    input.extend(raw_input().split())

output = []
for color_text in input:
    c = Color(color_text)
    c.luminance = c.luminance / 2
    output.append(c.hex_l)

for _ in range(7):
    for _ in range(7):
        print output.pop(0) + " ",
    print
