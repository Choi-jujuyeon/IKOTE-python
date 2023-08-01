# 반복문을 포함한 리스트 컴프리헨션
array = [i for i in range(10)]
print(array)

# ------

# 반복문 + 조건문을 포함 리스트 컴프리헨션

# i가 0부터 19까지 반복을 하되, 홀수만 포함되도록 리스트를 구성해라.
array2 = [i for i in range(20) if i % 2 == 1]
print(array2)

#i가 1부터 9까지 반복을 하되, 제곱 값을 포함하는 리스트를 구성해라.
array3 = [i * i for i in range(1, 10)]
print(array3)