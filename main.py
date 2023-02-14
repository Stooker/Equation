from equation import Equation


if __name__ == '__main__':

    answer = True

    while answer:
        eq = Equation()
        print(f'Delta = {eq.delta}')
        eq.solve()
        answer = Equation.ask_for_continue()

