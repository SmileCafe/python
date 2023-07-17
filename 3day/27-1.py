#집합 set
setValue_2 = set(["TEST"])
setValue_3 = set(["Hello", "Python", "TEST"])

#교집합 => 두 집합에서 같은 것을 추출
print(setValue_2.intersection(setValue_3))
print(setValue_2 & setValue_3)

#합집합 => 두 집합을 합치는 것
print(setValue_2.union(setValue_3))
print(setValue_2 | setValue_3)

#차집합 => 좌변에 있는 집합기준으로 우변에 같은 값을 가진걸 뺀다
print(setValue_3.difference(setValue_2))
print(setValue_3 - setValue_2)