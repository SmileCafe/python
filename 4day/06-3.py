# 두 수를 입력받아 더 큰 수가 짝수이면 출력하시오.
num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

if num1 > num2:
    if (num1 % 2) == 0:
        print("Even")

