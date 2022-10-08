# Solved using XOR (Bit manipulation)
a = 5
b = 7

print(a, b)

a = a ^ b # a = 5 ^ 7
b = a ^ b # b = 5 ^ 7 ^ 7 = 5
a = a ^ b # a = 5 ^ 7 ^ 5 = 7

print(a, b)
