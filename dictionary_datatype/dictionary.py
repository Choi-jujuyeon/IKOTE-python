data = dict()

data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
print("-------------------------\n")

# 키 값이 있는지 체크하기 
if '사과' in data:
  print("'사과'를 키로 가지고 있는 데이터가 존재합니다.")

print("-------------------------\n")

# 키 데이터만 담은 리스트
key_list = data.keys()
print(key_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])


# 값 데이터만 담은 리스트
value_list = data.values()
print(value_list)


