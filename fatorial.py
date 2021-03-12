def main():
    n = int(input("Digite um numero inteiro: "))

    n_fat = 1

    for i in range(2, n+1):
        n_fat = n_fat * i

    print("%d! = %d" % (n, n_fat))


main()
