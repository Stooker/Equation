import math


class Equation:
    def __init__(self):
        self.a = self.ask_for_input('a')
        self.b = self.ask_for_input('b')
        self.c = self.ask_for_input('c')
        self.delta = self.calculate_delta()

    def calculate_delta(self):
        delta = self.b**2 - 4*self.a*self.c
        return delta

    def solve(self):
        if self.delta < 0:
            print(f'Równanie: {self.__str__()} nie posiada rozwiązań')
        elif self.delta == 0:
            x = -self.b / 2*self.a
            print(f'Równanie: {self.__str__()} ma jedno rozwiązanie: x = {x}')
        else:
            x_1 = (-self.b + math.sqrt(self.delta)) / (2*self.a)
            x_2 = (-self.b - math.sqrt(self.delta)) / (2*self.a)
            print(f'Równanie: {self.__str__()} ma dwa rozwiązania: x1 = {x_1}, x2 = {x_2}')

    @staticmethod
    def ask_for_input(char):
        num = input(f"Podaj współczynnik {char}: ")
        return int(num)

    def __str__(self):
        return f'{self.a}x^2 + {self.b}x + {self.c} = 0'