# Q2) 정수 하나를 입력받아 짝수, 홀수를 구분하시오.
number = int(input("Enter an Integer: "))
if (number % 2) == 0:
    print("Even")
else:
    print("Odd")