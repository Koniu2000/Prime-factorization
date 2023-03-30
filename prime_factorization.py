
def prime_factorization():
    number = int(input("Enter a number:"))
    list = []
    for i in range(2, number):
        while number% i == 0:
            list.append(i)
            number = number / i
        if i == number:
            list.append(i)
        else:
            pass

    print(*list, sep="*")

prime_factorization()
