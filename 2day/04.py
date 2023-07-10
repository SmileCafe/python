Weight1 = input("첫번째 물건의 무게를 입력하세요: ")
Object1 = float(Weight1)
Weight2 = input("두번째 물건의 무게를 입력하세요: ")
Object2 = float(Weight2)

Max_Weight = 600
Current_Weight = Max_Weight - (Object1 + Object2)

print("현재 엘리베이터의 허용무게는 ", Current_Weight, "kg 입니다.")

# Checking types up
print(type(Current_Weight))
print(type(Max_Weight))