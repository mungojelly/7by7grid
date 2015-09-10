# Given a line containing one color,
# repeats that color 49 times
# (to form a full 7x7 grid).

color = raw_input()
for _ in range(7):
    for _ in range(7):
        print color,
    print
