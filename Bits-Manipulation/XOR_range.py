#find a XOR from L - > R
from XOR_n import find_xor

l = 2
r = 6

print(find_xor(r) ^ find_xor(l - 1))