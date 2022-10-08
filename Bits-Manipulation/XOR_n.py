# Given N, Print XOR of all no's below i.e (1, n-1)

# n = 5
# n(1) = 1
# n(2) = 3
# n(3) = 0
# n(4) = 4
# There is a pattern which is repeating after every 4 number's
# n(5) = 1
# n(6) = 7
# n(7) = 0
# n(8) = 8
n= 5
def find_xor(n):
    if n % 4 == 0:  return(n)
    if n % 4 == 1:  return(1)
    if n % 4 == 2:  return(n + 1)
    if n % 4 == 3:  return(0)


# TC :- O(1) 