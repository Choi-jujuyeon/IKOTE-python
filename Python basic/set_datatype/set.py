a = set([1, 1, 2, 2, 3, 4, 5])
print(a)

a = {1, 1, 2, 2, 3, 4, 5}
print(a)

# 기본 세팅
c = set([1,2,3])
# c = {1,2,3}

# 새로운 원소 추가 == add() 사용
c.add(4)
print(c)

# 새로운 원소 여러 개 추가 == updata() 사용
c.update([5, 6])
print(c)

# 특정한 값을 갖는 원소 삭제 == remove() 사용
c.remove(3)
print(c)
