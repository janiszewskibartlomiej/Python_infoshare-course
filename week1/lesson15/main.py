import calculations.deposit_cal as calculation


def caunt():
    start_capital = input("Proszę podać kapitał początkowy: ")
    percent = input("Proszę podać oprocentowanie: ")
    year = input("Proszę podać okres w latach: ")
    solution = calculation.deposit_calculator(start_capital=start_capital, percent=percent, year=year)
    return print(f'{solution:.2f}')


if __name__ == '__main__':
    caunt()
