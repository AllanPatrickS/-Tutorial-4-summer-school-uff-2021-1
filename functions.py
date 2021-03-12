def fatorial(n):
    n_fat = 1

    for i in range(2, n+1):
        n_fat = n_fat * i

    print("%d! = %d" % (n, n_fat))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


fibonacci(5)
fatorial(5)
