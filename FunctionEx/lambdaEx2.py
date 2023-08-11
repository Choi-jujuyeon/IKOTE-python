array = [('a', 50), ('b',40),('c',20)]

# x변수를 사용해 두번째 원소를 기준으로 정렬을 하고자 한다~!!
def my_key(x):
    return x[1]
print(sorted(array, key=my_key))

#람다 표현식 사용 == 함수선언 없이 1회용으로 사용가능
print(sorted(array, key=lambda x: x[1]))