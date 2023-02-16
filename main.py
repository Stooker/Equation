from equation import Equation


if __name__ == '__main__':

    answer = True

    while answer:

        a = Equation.ask_for_input('a')
        b = Equation.ask_for_input('b')
        c = Equation.ask_for_input('c')

        eq = Equation(a, b, c)
        eq.solve()
        answer = Equation.ask_for_continue()
