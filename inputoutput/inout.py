# 데이터의 개수 입력
a = int(input())

#각 데이터를 공백을 기준으로 구분하여 입력
b = list(map(int,input().split()))

b.sort(reverse=True)
print(b)
        