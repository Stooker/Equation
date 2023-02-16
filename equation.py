import math


class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_delta(self):
        delta = self.b**2 - 4*self.a*self.c
        return delta

    def solve(self):
        if self.a == 0:
            self.solve_normal_equation()
        else:
            delta = self.calculate_delta()
            print(f'Delta = {delta}')
            if delta < 0:
                print(f'Równanie: {self.__str__()} nie posiada rozwiązań')
                return None
            elif delta == 0:
                x = self.b / 2*self.a
                print(f'Równanie: {self.__str__()} ma jedno rozwiązanie: x = {x}')
                return x
            else:
                x_1 = (-self.b - math.sqrt(delta)) / (2*self.a)
                x_2 = (-self.b + math.sqrt(delta)) / (2*self.a)
                print(f'Równanie: {self.__str__()} ma dwa rozwiązania: x1 = {x_1}, x2 = {x_2}')
                return x_1, x_2

    def solve_normal_equation(self):
        if self.b == 0:
            if self.c == 0:
                print(f'Równanie: 0 = 0 jest prawdą i nie potrzebuje być rozwiązywane')
                return None
            x = self.c
            print(f'Równanie: {x} = 0 jest nieprawdą i nie ma rozwiązań')
            return None
        x = self.c / self.b
        if x != 0:
            x = -x
        print(f'Równanie: {self.__str__()} ma jedno rozwiązanie: x = {x}')
        return x

    @staticmethod
    def ask_for_input(char='a'):
        while True:
            try:
                num = float(input(f"Podaj współczynnik {char}: "))
                return num
            except ValueError:
                print("Podana wartość musi być liczbą")

    @staticmethod
    def ask_for_continue():
        answer = ''
        while answer not in ('T', 'N', 't', 'n'):
            answer = input("Czy rozwiązać kolenjne równanie? [T/N]: ")

        if answer == 'T' or answer == 't':
            return True
        else:
            return False

    def __str__(self):
        if self.a == 0:
            a = ''
        else:
            a = f'{self.a}x^2'

        if self.b == 0:
            b = ''
        elif self.b > 0:
            b = f'+{self.b}x'
        else:
            b = f'{self.b}x'

        if self.c == 0:
            c = ''
        elif self.c > 0:
            c = f'+{self.c}'
        else:
            c = self.c

        return f'{a}{b}{c} = 0'
