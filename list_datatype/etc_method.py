# append(), sort(), reverse(), insert(), count()), remove()

print("\n---------------------------")
print("< 리스트 관련 메소드 > \n")

# 기본 설정
a =[1,3,4]
print("기본 리스트: ",a)


# 리스트에 원소 삽입 == append() 사용
a.append(2)
print("\n삽입된 리스트: ",a)

# 오름차순 정렬 == sort() 사용
a.sort()
print("오름차순 정렬: ",a)

# 내림차순 정렬 == sort(reverse =True) 사용
a.sort(reverse =True)
print("내림차순 정렬: " ,a)

# 원소 뒤집기 == reverse() 함수 사용
a.reverse()
print("원소 뒤집기: " ,a)

# 특정 인덱스에 데이터 추가 == insert() 사용
a.insert(2,3)
print("인덱스 2에 3추가: ",a)

# 특정 값인 데이터 개수 세기 == count() 사용
print("값이 3인 데이터 개수: ",a.count(3))

# 특정 값 데이터 삭제 == remove() 사용
a.remove(1)
print("값이 1인 데이터 삭제",a)

print("\n---------------------------")
print("특정 값을 가지는 원소 모두 제거\n")

a=[1,2,3,4,5,5,5]
print("기본 리스트: ",a)

#집합 자료형 사용 가능 == 특정한 원소의 존재유무만을 체크 가능
remove_set={3,5}

#a라는 리스트를 i라는 변수가 하나씩 확인을 하면서,
#i가 remove_set에 포함되어 있지 않다면! 그때의 그 원소만을 담겨두겠다!!!
result = [i for i in a if i not in remove_set]
print("\n특정 원소 값 제거한 리스트: ",result)