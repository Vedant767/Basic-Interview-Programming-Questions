def checkIntPalindrome(no):
    result = 0
    backup_no = no
    while no:
        rem = no % 10
        result = result * 10 + rem
        no = no // 10
    return result == backup_no

print(checkIntPalindrome(2002))