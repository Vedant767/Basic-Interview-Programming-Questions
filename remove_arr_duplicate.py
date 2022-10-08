def remove_duplicate(arr):
    result = []

    for i in arr:
        if i in result:
            return i
        else:
            result.append(i)
    return "No duplicate"

arr = [1,2,3,4]
print(remove_duplicate(arr))