# 두 수를 입력받아 더 큰 수가 짝수이면 출력하시오.
num1, num2 = int(input("Enter a number1: ")), int(input("Enter a number2: "))

if num1 > num2:
    if (num1 % 2) == 0:
        print("%d는 %d보다 크고 짝수입니다." %(num1,num2))
if num2 > num1 and num2 % 2 == 0:
    print("%d는 %d보다 크고 짝수입니다." %(num2,num1))

