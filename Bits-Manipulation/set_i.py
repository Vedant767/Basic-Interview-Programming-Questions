# Check if ith bit is set
# Input: n = 75 and k = 4
# temp = 1 << (k-1) = 1 << 3 = 8 
# Binary Representation of temp = 0..00001000 
# Binary Representation of n = 0..01001011 
# Since bitwise AND of n and temp is non-zero, result is SET. 
def isKthBitSet(n, k):
    mask = 1 << (k - 1)
    if (n & mask):
        print("SET")
    else:
        print("NOT SET")

def toSet(i, n):
    mask = 1 << (i - 1)
    print(n)
    n = n | mask
    print(n)

def removeLastSet(n):
    # 13 = 1101
    # 12 = 1100
    # 13 & 12 = 1100

    # 11 = 1011
    # 12 & 11 = 1000
    return n & n - 1 

def CountSet1(n):
    cnt = 0
    while n != 0:
        if (n & 1 == 1):
            cnt += 1
        n = n >> 1
    
    print(cnt)

def CountSet2(n):
    cnt = 0
    while n != 0:
        n = n & (n - 1)
        cnt += 1
    
    print(cnt)

 
 
# Driver code
if __name__ == "__main__":
    n = 5
    k = 2
 
    # Function call
    isKthBitSet(n, k)
    toSet(2, 13)
 