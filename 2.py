from utils import *

lines = read_lines("input.txt")

# part 1
F = "forward"
D = "down"
U = "up"

final_f = 0
final_d = 0
for line in lines:
    i, v = line.split(" ")
    if i == F:
        final_f += int(v)
    elif i == D:
        final_d += int(v)
    elif i == U:
        final_d -= int(v)

print(final_f, final_d)
print("part 1:" + str(final_f * final_d))

# part 2
final_f = 0
final_d = 0
aim = 0
for line in lines:
    i, v = line.split(" ")
    if i == F:
        final_f += int(v)
        final_d += aim * int(v)
    elif i == D:
        aim += int(v)
    elif i == U:
        aim -= int(v)

print(final_f, final_d)
print("part 2:" + str(final_f * final_d))
