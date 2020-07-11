
def deposit_calculator(start_capital, percent, year):

    solution = float(start_capital) * (1 + float(percent)/100) ** float(year)
    return solution
