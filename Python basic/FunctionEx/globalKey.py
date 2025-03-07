array = [1, 2, 3, 4, 5]

def func():

    # 전역변수와 지역변수가 동일한 이름으로 존재한다면, 내부적으로는 전역변수가 우선시 된다!
    array = [3, 4, 5]
    array.append(6)
    print(array)


func()
