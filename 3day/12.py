a = input("Your first number is: ")
b = input("Your second number is: ")

A = float(a)
B = float(b)

print("첫번째 수의 거듭제곱은 %f" %(A**A))
print("첫번째 수의 거듭제곱은 %f" %(B**B))

print("첫번째/두번째의 몫은 {}이고 나머지는 {}이다" .format(A//B, A%B))
print("%d %% %d = %d" % (A, B, A%B)) #%% => %를 출력하려고


