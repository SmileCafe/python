#리스트 내장함수
a = [1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

a = [4,8,2,7,4,1]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1,2,3,4,5]
print(a.index(2))
a.insert(0, 7)
print(a)

a = [3,2,3,1,2,3]
a.remove(3) #모든 3을 제거하는 것이 아니라 처음 만나는 3을 제거
print(a)

a = [1,2,3,4,5]
a.pop() #마지막 요소 제거
print(a)

a = [1,2,3,4,5,2,2]
a.pop(2) #해당 인덱스에 있는 값을 제거
print(a)

a = [1,2,3,1,1,1,1,1]
a.extend([4,5])
print(a)
print(a.count(1)) #1인 값의 개수



