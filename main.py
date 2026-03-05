def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

budget = float(input("Ingresa tu presupuesto: "))
exchange_rate = float(input("Ingresa la tasa de cambio: "))

resultado = exchange_money(budget, exchange_rate)

print("El equivalente en la moneda extranjera es:", resultado)