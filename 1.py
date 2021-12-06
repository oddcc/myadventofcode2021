from utils import *

lines = read_lines("input.txt")

# part 1
res = 0
current = int(lines[0])
for l in lines[1:]:
    i = int(l)
    if i > current:
        res += 1
    current = i
print("part 1 answer: " + str(res))

# part 2
res = 0
for i, l in enumerate(lines[0:-2]):
    if i == 0:
        current = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        continue
    sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if sum > current:
        res += 1
    current = sum

print("part 2 answer: " + str(res))
