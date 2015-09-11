from colour import Color

colors = []
while len(colors) < 49:
    colors.extend(raw_input().split())

print """
<!DOCTYPE html>
<html>
    <head>
        <style>
           table {
               border-collapse:collapse; 
               border: none;
           }
           td {
               padding: 0;
               width: 52px;
               height: 52px;
           }
        </style>
        <title></title>
    </head>
    <body>
"""
print "<table>"
current_color = 0
for _ in range(7):
    print "    <tr>"
    for _ in range(7):
        print "        <td style=\"background-color:{}\"></td>".format(colors[current_color])
        current_color += 1
    print "    </tr>"
print "</table>"
print "</body>"
print "</html>"
