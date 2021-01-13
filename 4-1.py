from sys import argv

script_name, hours_worked, rate_in_hour, premium = argv


def donat():
    """Данная функция считает размер заработной платы на основании следующих данных:
    выработка часов, ставка в час и премия"""
    x = float(hours_worked)
    y = float(rate_in_hour)
    z = float(premium)
    return x * y + z


print("Размер заработной платы составляет: ", donat())
