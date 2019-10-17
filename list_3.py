import math
import random


# zad2
def zad2():
    def pierwiasterk(n):
        ans = 0
        i = 1
        while n >= ans:
            ans += 2*i - 1
            i += 1
        return i-2

    print(pierwiasterk(16))
    print(pierwiasterk(14))
    print(pierwiasterk(9))
    print(pierwiasterk(7))

# zad2()


def zad3():
    f_dict = {}

    def sudan(x,y,n):
        if str([x,y,n]) in f_dict:
            return f_dict[str([x,y,n])]
        if n == 0:
            # f[str([x,y,n])] = x+y
            return x+y
        elif y == 0:
            # f[str([x,y,n])] = x
            return x

        f_dict[str([x,y,n])] = sudan(sudan(x,y-1,n),sudan(x,y-1,n)+y,n-1)
        return f_dict[str([x,y,n])]

    print(sudan(2, 2, 2))

# zad3()



def zad4():
    def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
        ans = []
        for slowo in tekst.split():
            if len(slowo) <= dl_slowa :
                ans.append(slowo)
        to_throw_away = list(range(len(ans)))
        random.shuffle(to_throw_away)
        to_throw_away = to_throw_away[:liczba_slow]
        ans2 = []
        for i in range(len(ans)):
            if i not in to_throw_away:
                ans2.append(ans[i])

        return ans2
    print(uprosc_zdanie('"Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej.', 10, 5))

# zad4()