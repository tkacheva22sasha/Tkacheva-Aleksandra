salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = spend - salary    # сумма финансовой подушки необходимая в 1-ый месяц
for i in range(months - 1):
    spend = spend + spend * increase
    deficis = spend - salary
    money_capital += deficis  # сумма финансовой подушки с 2-го по 10-ый месяц

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
