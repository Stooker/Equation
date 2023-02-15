import math


class Equation:
    def __init__(self):
        self.a = self.ask_for_input()
        self.b = self.ask_for_input('b')
        self.c = self.ask_for_input('c')
        self.delta = self.calculate_delta()

    def calculate_delta(self):
        delta = self.b**2 - 4*self.a*self.c
        return delta

    def solve(self):
        if self.delta < 0:
            print(f'Równanie: {self.__str__()} nie posiada rozwiązań')
            return None
        elif self.delta == 0:
            x = self.b / 2*self.a
            print(f'Równanie: {self.__str__()} ma jedno rozwiązanie: x = {x}')
            return x
        else:
            x_1 = (-self.b + math.sqrt(self.delta)) / (2*self.a)
            x_2 = (-self.b - math.sqrt(self.delta)) / (2*self.a)
            print(f'Równanie: {self.__str__()} ma dwa rozwiązania: x1 = {x_1}, x2 = {x_2}')
            return x_1, x_2

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
