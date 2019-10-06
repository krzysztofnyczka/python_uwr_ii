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
    enc = [chr(ord(a) ^ klucz) for a in tekst]
    return enc


def odszyfruj(szyfr, klucz):
    dec = [chr(ord(a) ^ klucz) for a in szyfr]
    return dec


# print(zaszyfruj('Python', 7))
# print(odszyfruj(zaszyfruj('Python', 7), 7))


''' zadanie 5 '''
def rozklad(n):
    ans = []
    i = 2
    while n > 1:
        existance = 0
        while n % i == 0:
            existance += 1
            n = n/i
            print(n)
        ans.append((i, existance))
        i += 1
    return ans


# print(rozklad(756))


''' zadanie 6 '''
def tabliczka(x1, x2, y1, y2):
    def spaces(num, l):
        new_l = len(str(num))
        if new_l == l:
            print(num, end=' ')
            return
        for i in range(l-new_l):
            print(' ',end='')
        print(num,end=' ')
        return

    max_len = len(str(x2*y2))
    for i in range(x1-1, x2+1):
        if i == x1-1:
            spaces(' ',max_len)
            for j in range(y1, y2+1):
                spaces(j, max_len)
        else:
            for j in range(y1-1, y2+1):
                spaces(i*j, max_len)
        print()


# tabliczka(3,5,2,4)