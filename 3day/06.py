a = "현재 통장의 잔고는 1억원입니다."
print(a)
a = a[:11] + "3" + a[-6:]
print(a)
print(a.replace ("3", "10"))

#문자열 내에 올 수 없는 변수와 같은 역할의 ()을 넣어두는 것 = formatting
b = "현재 나의 통장 잔고는 %d억원입니다."
print(b%15)
print(b%100)
print(b%9)

print("나는 케이크를 %d개 먹었다." %3)
print("나는 케이크를 %s개 먹었다." % "세")
print("나는 케이크를 %f개 먹었다." %3.5)

number = 5
print("나는 케이크를 %d개 먹었다." %number)
disert = "파이"
print("나는 %s를 %d개 먹었다." %(disert, number))


