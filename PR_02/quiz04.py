# 댓글 이벤트를 통해서, 댓글 작성자들 중에 추첨을 통해 1명은 치킨 3명은 커피 쿠폰을 받게 된다.
# 추첨 프로그램을 작성

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정함
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 을 활용

# ex)
# -- 당첨자 발표 --
# 치킨 당첨자  : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다. --


from random import *
user = range(1, 21) # 1~20 까지 숫자를 생성
user = list(user)

winner = sample(user, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winner[0]))
print("커피 당첨자 : {0}" .format(winner[1:]))
print("-- 축하합니다 --")
