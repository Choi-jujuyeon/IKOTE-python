# 아이디어: 가장 큰 화폐 단위부터 돈을 거슬러 주자!
# 정당한가? 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없다.

n=1260
count=0

arr=[500,100,50,10]
for coin in arr:
    count+=(n//coin)
    n%=coin

print(count)   