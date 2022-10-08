def armstrong(no):
    power = len(str(no))
    print(power)
    backup_no = no
    result = 0

    while int(no):
        rem = no % 10
        result = result + pow(rem, int(power))
        no = no // 10
    return result == backup_no

print(armstrong(1634))