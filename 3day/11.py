ks = input("국어 점수는?")
es = input("영어 점수는?")
hs = input("역사 점수는?")

KS = float(ks)
ES = float(es)
HS = float(hs)

Score = [KS, ES, HS]

Total = KS + ES + HS

AVG = Total / len(Score)

print("합계는 {:.2f}, 평균은 {:.2f}" .format(Total, AVG))