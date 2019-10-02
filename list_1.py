import math


''' zadanie 1 '''
def vat_faktura(lista):
    return sum(lista) * 0.23


def vat_paragon(lista):
    sum = 0
    for i in lista:
        sum += i * 0.23
    return sum


zakupy = [0.2, 0.5, 4.59, 6]
# print(vat_faktura(zakupy) == vat_paragon(zakupy))
# print(vat_faktura(zakupy))
# print(vat_paragon(zakupy))


''' zadanie 2 '''
def monety(cena):
    coins = [1, 2, 5, 10, 20]
    answer = []
    for i in reversed(coins):
        if cena >= i:
            answer.append((math.floor(cena / i), i))
            cena = cena % i
    return answer

# print(monety(123))


''' zadanie 3 '''
def romb(n):
    for i in range(n):
        for _ in range(n - i):
            print(" ", end='')
        for _ in range(2*i-1):
            print("#", end='')
        for _ in range(n - i):
            print(" ", end='')
        print()
    for _ in range(2*n-1):
        print("#", end='')
    print()
    for i in reversed(range(n)):
        for _ in range(n - i):
            print(" ", end='')
        for _ in range(2*i-1):
            print("#", end='')
        for _ in range(n - i):
            print(" ", end='')
        print()


# romb(4)

''' zadanie 4 '''
def zaszyfruj(tekst, klucz):
    pass

# for i in range(10):
#     for j in range(10):
#         print(i*j, end=' ')
#     print()