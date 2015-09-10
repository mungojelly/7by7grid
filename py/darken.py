from colour import Color
from colour import web2hex

input = []
while (len(input) < 49):
    input.extend(raw_input().split())

output = []
for color_text in input:
    c = Color(color_text)
    c.luminance = c.luminance / 2
    output.append(web2hex(c.hex, force_long=True))

for _ in range(7):
    for _ in range(7):
        print output.pop() + " ",
    print
