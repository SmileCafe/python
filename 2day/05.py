Height = input("당신의 키는? ")
Current_Height = float(Height)
Man_StandardWeight = (Current_Height - 100) * 0.9
Woman_StandardWeight = (Current_Height - 105) * 0.9

StandardWeightRounded = round(Man_StandardWeight, 2)
print("당신의 표준 체중은 ", StandardWeightRounded, "(kg) 입니다.")

# Checking Variable types
print(type(Height))
print(type(Current_Height))
print(type(Man_StandardWeight))
print(type(Woman_StandardWeight))
print(type(StandardWeightRounded))