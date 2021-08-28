from random import *
users = range(1, 21) # 1 부터 20까지 숫자를 생성

# range 타입인 users 를 list 형식으로 변경
users = list(users)

shuffle(users)

# 4명의 당첨자를 뽑아 값을 저장
winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0} ".format(winners[0]))
print("커피 당첨자 : {0} ".format(winners[1:]))
print(" -- 축하합니다! -- ")
