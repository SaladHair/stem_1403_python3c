"""
[Homework]
Date: 2021-11-06
Due date: 2021-11-12
1. Describe the lifecycle of object in python using your own words
2. Programming practice
File name:  j3_2020_yourname.py

- Problem description
Mahima has been experimenting with a new style of art.
She stands in front of a canvas and, using her brush, flicks drops of paint onto the canvas.
When she thinks she has created a masterpiece, she uses her 3D printer to print a frame to surround the canvas.

Your job is to help Mahima by determining the coordinates of the smallest possible rectangular frame such that each drop of paint lies inside the frame.
Points on the frame are not considered inside the frame.


- Input specification
The first line of input contains the number of drops of paint, N, where 2 =< N => 100 and N is an integer.
Each of the next N lines contain exactly two positive integers X and Y separated by one comma (no spaces).
Each of these pairs of integers represents the coordinates of a drop of paint on the canvas.
Assume X < 100 and Y < 100, and that there will be at least two distinct points.
The coordinates (0, 0) represent the bottom-left corner of the canvas.

For 12 of the 15 available marks, X and Y will both be two-digit integers.

- Output specification
Output two lines.
Each line must contain exactly two non-negative integers separated by a single comma (no spaces).
The first line represents the coordinates of the bottom-left corner of the rectangular frame.
The second line represents the coordinates of the top-right corner of the rectangular frame.

Time for resolution of the problem: Around 10 mins
"""

y_coords = []
x_coords = []

for i in range(int(input())):
    num = input()
    coord_value = ""
    for a in num:
        if a != ",":
            coord_value += a
        else:
            x_coords.append(coord_value)
            coord_value = ""
    y_coords.append(coord_value)

lowest_y = y_coords[0]
for i in y_coords:
    if i < lowest_y:
        lowest_y = i

lowest_x = x_coords[0]
for i in x_coords:
    if i < lowest_x:
        lowest_x = i

highest_y = y_coords[0]
for i in y_coords:
    if i > highest_y:
        highest_y = i

highest_x = x_coords[0]
for i in x_coords:
    if i > highest_x:
        highest_x = i

print(f"{int(lowest_x)-1},{int(lowest_y)-1}")
print(f"{int(highest_x)+1},{int(highest_y)+1}")
