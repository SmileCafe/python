mart = {"다이제":1000, "메로나":500, "코카콜라":700, "츄파춥스":500}
print(mart["메로나"])
print("'과자 가격인상!!'")
mart["다이제"] = 2000
print(mart)

#딕셔너리 유의사항
a = {1:'a', 2:'b', 1:'c'}
print(a)
#중복된 키 값을 사용할 수 없다(value는 가능)