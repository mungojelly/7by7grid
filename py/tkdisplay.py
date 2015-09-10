from Tkinter import *
master = Tk()
total_height = 350
total_width = 350
w = Canvas(master, width=total_width, height=total_height)
w.pack()

colors = []

while len(colors) < 49:
    colors.extend(raw_input().split())

cell_height = total_height / 7
cell_width = total_width / 7

current_color = 0

for row in range(7):
    for column in range(7):
        w.create_rectangle(cell_width * column, cell_height * row,
                           cell_width * (column + 1), cell_height * (row + 1),
                           fill=colors[current_color])
        current_color += 1

mainloop()
