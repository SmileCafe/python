my_tuple = 1,2,3 #Packing
print(my_tuple)
num1, num2, num3 = my_tuple #Unpacking
print(num1) #1
print(num2) #2
print(num3) #3

num1, num2 = num2, num1
print(num1) #2
print(num2) #1

