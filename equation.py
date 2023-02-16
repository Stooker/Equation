import math


class Equation:
    """
    A class to represent equation

    ...

    Attributes
    ----------
    a: float
        factor a of equation *(x**2)
    b: float
        factor b of equation *(x)
    c: float
        factor c of equation *(1)
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_delta(self):
        """Calculate delta of equation"""

        delta = self.b**2 - 4*self.a*self.c
        return delta

    def solve(self):
        """
        Calculate equation if there is factor "a"

        Returns
        -------
        None
            If there is no solving to equation
        Float
            If there is solution to equation
        Tuple(float)
            If there are two solutions to equation
        """

        if self.a == 0:
            self.solve_normal_equation()
        else:
            delta = self.calculate_delta()
            print(f'Delta = {delta}')
            if delta < 0:
                print(f'Równanie: {self.__str__()} nie posiada rozwiązań')
                return None
            elif delta == 0:
                x = -self.b / (2*self.a)
                print(f'Równanie: {self.__str__()} ma jedno rozwiązanie: x = {x}')
                return x
            else:
                x_1 = (-self.b - math.sqrt(delta)) / (2*self.a)
                x_2 = (-self.b + math.sqrt(delta)) / (2*self.a)
                print(f'Równanie: {self.__str__()} ma dwa rozwiązania: x1 = {x_1}, x2 = {x_2}')
                return x_1, x_2

    def solve_normal_equation(self):
        """
        Calculate equation if there is no factor "a" and returns solution

        Returns
        -------
            None
                If there is no solving to equation
            Float
                If there is solution to equation
        """

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
        """Asks user for value until input can be cast to float"""

        while True:
            try:
                num = float(input(f"Podaj współczynnik {char}: "))
                return num
            except ValueError:
                print("Podana wartość musi być liczbą")

    @staticmethod
    def ask_for_continue():
        """Asks user for value until input is valid"""

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
