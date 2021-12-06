from utils import *

lines = read_lines("input.txt")

res = 0
current = int(lines[0])
for l in lines[1:]:
    i = int(l)
    if i > current:
        res+=1
    current = i

print(res)

