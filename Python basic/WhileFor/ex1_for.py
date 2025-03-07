# 학생들의 합격 여부 판단 예제- 점수가 80점만 넘으면 합격

scores = [90, 85, 77, 65, 97]
# 2번학생과 4번 학생은 부정행위를 저지른 학생이다~!!!
cheating_student_list = {2, 4}

#0부터 4 인덱스까지 돌면서 원소를 하나씩 추출해 i에 저장
for i in range(5):
  if i + 1 in cheating_student_list:
    continue
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")
