import time

def zad1k():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    # 1

    def primes_imp(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def primes_lst_cmp(n):
        return [i for i in range(2, n + 1) if is_prime(i)]

    def primes_fun(n):
        return list(filter(is_prime, range(2, n + 1)))

    x = 500000
    t = time.time()
    print(primes_imp(x))
    print(time.time() - t)
    t = time.time()
    print(primes_lst_cmp(x))
    print(time.time() - t)
    t = time.time()
    print(primes_fun(x))
    print(time.time() - t)

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
        pass

    print(pierwsze_imperatywna(100))

# zad1k()


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

zad2()
