# 두 수를 입력받아 합이 짝수이고 3의 배수인 수를 출력하시오
num1, num2 = int(input("Enter a number1: ")), int(input("Enter a number2: "))
sum = num1 + num2

if sum % 2 == 0 and sum % 3 == 0:
        print("%d는 합은 짝수이고 3의 배수이다." %sum)