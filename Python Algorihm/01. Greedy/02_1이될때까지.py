# 아이디어: 주어진 N에 대하여 최대한 많이 나누기
# 정당한가? 2이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있다.
n,k=map(int,input().split())
count = 0

while n != 1:
    count += (n % k)
    n -= (n % k)
    
    if n<k:
        break
    
    count+=1 
    n//=k

print(count+(n-1))