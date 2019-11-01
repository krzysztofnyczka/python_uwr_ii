import time


def zad1():
    def pierwsze_imperatywna(n):
        ans = []
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                ans.append(i)
        return ans

    def pierwsze_skladana(n):
        return list(filter(lambda x: x is not None, [i if i > 1 and all([i % j != 0 for j in range(2, i)]) else None for i in range(2, n+1)]))

    def pierwsze_funkcyjna(n):
        def is_prime(i, n):
            if i < n and n > 1:
                if n % i == 0:
                    return False
                return is_prime(i+1, n)
            return True
        return list(filter(lambda x: is_prime(2, x), range(2, n+1)))

    x = 500
    t = time.time()
    print(pierwsze_imperatywna(x))
    print(time.time() - t)
    t = time.time()
    print(pierwsze_skladana(x))
    print(time.time() - t)
    t = time.time()
    print(pierwsze_funkcyjna(x))
    print(time.time() - t)

zad1()


def zad2():
    def doskonala(n):
        dzielniki = []
        for i in range(1, n):
            if n % i == 0:
                dzielniki.append(i)
        if sum(dzielniki) == n:
            return True
        return False

    def doskonale_imperatywna(n):
        ans = []
        for i in range(1, n):
            if doskonala(i):
                ans.append(i)
        return ans

    def doskonale_skladana(n):
        def dosk(n):
            return [i for i in range(1, n) if n % i == 0]
        return [i for i in range(1, n) if sum(dosk(i)) == i]

    def doskonale_funkcyjna(n):
        def summy(n):
            return sum(filter(lambda y: n % y == 0, range(1, n)))

        return list(filter(lambda x: x == summy(x), range(1, n + 1)))

    x = 10000
    t = time.time()
    print(doskonale_imperatywna(x))
    print(time.time() - t)
    t = time.time()
    print(doskonale_skladana(x))
    print(time.time() - t)
    t = time.time()
    print(doskonale_funkcyjna(x))
    print(time.time() - t)

# zad2()
