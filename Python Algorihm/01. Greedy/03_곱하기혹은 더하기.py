# 아이디어: 0 or 1이 아닐경우 곱하기 연산자를 넣기

a=input()
start=int(a[0])

for i in range(1,len(a)):
    n=int(a[i])
    if n<=1 or start<=1:
        start+=n
    else:
        start*=n
print(start)