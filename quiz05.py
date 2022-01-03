# 당신은 택시 매칭 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해진다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 한다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 15번째 손님 (소요시간 : 16분)


# 총 탑승 승객 :  2명 


## 직접 작성한 코드

from random import * # 랜덤함수

count = 0

for customer in range(1, 51): # 1~50 까지의 수

    time = randrange(5,51) # 5 ~ 50 사이의 임의의 값을 생성함

    if (time >= 5 and time <= 15):
        check = "O"
        count += 1
    else:
        check = "X"
    
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, customer, time))

print("총 탑승 승객 : {0} 명".format(count))


## 강사 코드

from random import *
cnt = 0 # 총 탑승 승객의 수
for i in range(1, 51): # 1~50 이라는 수
    time = randrange(5, 51) # 5분 ~ 50분 소요시간
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))

