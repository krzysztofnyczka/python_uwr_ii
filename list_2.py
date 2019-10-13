import itertools


class Formula:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def oblicz(self, x):
        pass

    def get_vars(self, ans):
        if isinstance(self, Zmienna):
            ans.add(self.wartosc)
            return ans
        elif isinstance(self, Negacja):
            return self.wartosc.get_vars(ans)
        elif isinstance(self, Tru):
            return ans
        else:
            return self.a.get_vars(ans) | self.b.get_vars(ans)

    def is_taut(self):
        variables = self.get_vars(set())
        # possibilities = (list(itertools.permutations(com)) for com in list(itertools.combinations_with_replacement([0, 1], len(variables))))
        possibilities = []
        for i in range(len(variables)+1):
            possibilities.extend(list(itertools.combinations(variables, i)))

        for poss in possibilities:
            w = {}
            for v in variables:
                if v in poss:
                    w[v] = True
                else:
                    w[v] = False
            if not self.oblicz(w):
                return False
        return True


class Zmienna(Formula):
    def __init__(self, wartosc):
        self.wartosc = wartosc
        super().__init__()

    def __str__(self):
        return self.wartosc

    def oblicz(self, tab):
        return tab[self.wartosc]


class Negacja(Formula):
    def __init__(self, x):
        self.wartosc = x
        super().__init__()

    def __str__(self):
        return 'not ' + self.wartosc.__str__()

    def oblicz(self, x):
        return not(self.wartosc.oblicz(x))


class Impl(Formula):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def oblicz(self, zmienne):
        return not self.a.oblicz(zmienne) or self.b.oblicz(zmienne)

    def __str__(self):
        return '( ' + self.a.__str__() + ' ==> ' + self.b.__str__() + ' )'


class Tru(Formula):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'true'

    def oblicz(self, x):
        return True


class And(Formula):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        super().__init__()

    def oblicz(self, x):
        return self.a.oblicz(x) and self.b.oblicz(x)

    def __str__(self):
        return '( ' + self.a.__str__() + ' v ' + self.b.__str__() + ' )'


class Or(Formula):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        super().__init__()

    def oblicz(self, x):
        return self.a.oblicz(x) or self.b.oblicz(x)

    def __str__(self):
        return '( ' + self.a.__str__() + ' v ' + self.b.__str__() + ' )'


x, y = Zmienna('x'), Zmienna('y')
test = Impl(x, And(y, Tru()))
test2 = Or(x, Negacja(x))
print(test.__str__())
print(test.is_taut())
print(test2.__str__())
print(test2.is_taut())
