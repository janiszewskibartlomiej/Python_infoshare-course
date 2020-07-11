import speed_cal


def avg_speed_input_data():
    input_dys = input("Proszę podać dystans w km: ")
    input_time = input("Proszę podać czas w godzinach: ")

    input_dys = input_dys.replace(",", ".")
    input_time = input_time.replace(",", ".")

    solution = speed_cal.avg_speed(dystance=float(input_dys), time=float(input_time))
    return print(round(solution, 2))


if __name__ == '__main__':
    avg_speed_input_data()
