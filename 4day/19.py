#1부터 입력받은 숫자까지의 누적합계를 구하는 코드를 작성하시오.
number = int(input("Enter a number for cumulative sum: "))
sum = 0
for sum in range(number, 1, -1):
    sum += number
print(sum)


    
