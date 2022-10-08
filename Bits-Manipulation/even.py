# Even using '&' operator because '&' < '%'


n = 5

if n & 1 == 0:
    print("even")
else:
    print("odd")    


# 12 = 1100 & 1 = 0000
# 13 = 1101 & 1 = 0001  1 & 1 = 1