# Find integer with single occurance
# Solved using Bit manipulation

# XOR property where if two numbers are equal = 0 else 1 || if even 1's = 0  else 1

arr = [2, 1, 2, 5, 6, 5, 7, 7, 6]

xor = 0

for i in arr:
    xor = xor ^ i

print(xor)

