def fib(n):
    a, b = 1, 1
    counter = 1
    while True:
        if counter == n:
            break

        print(f"a:{a}, b:{b}, c:{a+b}")

        a,b = b, a+b
        counter += 1

fib(10)

