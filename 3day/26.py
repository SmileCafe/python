mart = {"다이제":800, "메로나":500, "코카콜라":500, "츄파츄스":200}

menu = tuple(mart.keys())
print(menu)

price = sum(mart.values())
print(price)

mart[input("과자:")] = int(input("가격:"))
a, b = int("과자:"), int(input("가격:"))
mart[a] = b
price(mart)
