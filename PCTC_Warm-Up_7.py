#21.06.25
price = float(input())
perc_change = int(input())
if price > 9.99:
    if price + price*(perc_change/100) > 99.99:
        price = round(price, 2)
    else:
        price = round(price + price*(perc_change/100), 2)
elif price < 10.00:
    if price - price*(perc_change/100) < 1.00:
        price = round(price, 2)
    else:
        price = round(price - price*(perc_change/100), 2)
print('$' + str(price))