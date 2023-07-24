num = int(input("정수 입력:"))
count = 1
sum = 0
while count <= num:
    sum += count
    count += 1
    
print("1부터 %d까지의 누적합계: %d" %(num, sum))