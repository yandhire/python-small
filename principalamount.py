def financial_calc(amount, interest, years):
    future_money = round(amount*((1+(0.01*interest)) ** years), 3)
    return future_money

print(financial_calc(10000, 3.5, 7))