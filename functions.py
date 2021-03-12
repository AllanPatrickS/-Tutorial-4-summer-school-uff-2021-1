class functions:
    def __init__(self, n: int):
        self.n = n

    def fatorial(self, n):
        n_fat = 1

        for i in range(2, n+1):
            n_fat = n_fat * i

        print("%d! = %d" % (n, n_fat))

    def fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return(self.fibonacci(n-1) + self.fibonacci(n-2))

    def __call__(self):
        n = self.n
        print("-- functions --")
        print("Fatorial: ", end='')
        self.fatorial(n)
        print("Fibonacci ", end='')
        for i in range(0, n):
            print("%d " % self.fibonacci(i), end='')

functions(5)()
