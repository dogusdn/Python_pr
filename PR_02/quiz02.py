# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프로아인으로 함
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성

# 조건1 : 랜덤으로 날짜를 뽑아야 한다.
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 결정
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.


from random import *
studyDate = randint(4, 28) # 4 ~ 28 이하의 임의의 값을 생성함


print("오프라인 스터디 모임 날짜는 매월"+ str(studyDate) + "일로 선정되었습니다.")
