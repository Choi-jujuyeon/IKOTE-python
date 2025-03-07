# while문을 활용 1부터 9까지 홀수의 합 구하기

i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)