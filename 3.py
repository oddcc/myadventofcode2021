from utils import *

lines = read_lines("input.txt")

bits_count= len(lines[0].strip())
bit_0_count = [0] * bits_count
bit_1_count = [0] * bits_count

for l in lines:
    n = int(l, 2)
    for count in range(bits_count):
        if n & 1:
            bit_1_count[count] += 1
        else:
            bit_0_count[count] += 1
        n >>= 1

print(0, bit_0_count)
print(1, bit_1_count)

gamma = ""
epsilon = ""
for i in range(bits_count):
    if bit_1_count[i] > bit_0_count[i]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
gamma = gamma[::-1]
epsilon = epsilon[::-1]
print(f"Gamma: gamma = {gamma}")
print(f"Epsilon: epsilon = {epsilon}")


print(int(gamma, 2) * int(epsilon, 2))