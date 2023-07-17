people1 = [input("이름:"),int(input("나이:")),float(input("왼쪽눈시력:")),float(input("오른쪽눈시력:"))]
people2 = [input("이름:"),int(input("나이:")),float(input("왼쪽눈시력:")),float(input("오른쪽눈시력:"))]
people3 = [input("이름:"),int(input("나이:")),float(input("왼쪽눈시력:")),float(input("오른쪽눈시력:"))]

agg_avg = (people1[1]+people2[1]+people3[1]) / 3
leye = (people1[2]+people2[2]+people3[2]) / 3
reye = (people1[2]+people2[2]+people3[2]) / 3

print("평균나이:{0}, 왼쪽눈시력:{1:.2f},오른쪽눈시력:{2:.2f}" .format(agg_avg,leye,reye))
