# if
weather = input("오늘 날씨는 어떤가요? ")

if weather == "비" or weather =="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요없습니다.")


temp = int(input("오늘 기온은 어떤가요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp & temp < 30:
    print("괜찮은 날씨네요! 산책을 해보는게 어떨까요?")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요!")


## 반복문

# 방법 1
for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

# 방법 2
for waiting_no in range(5): # 0~4 까지 숫자
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6): # 1~5 까지의 숫자
    print("대기번호 : {0}".format(waiting_no))

# 방법 3
starbucks = ["도현우", "고우현", "심성훈", "김연주", "김형준"]
for customer in starbucks:
    print("{}, 커피가 준비 되었습니다.".format(customer))


## while 반복문

# 방법 1
customer = "도현우"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분 되었습니다.")

# 방법 2
## 무한루프
customer = "아이언맨"
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1

# 방법 3
customer = "고우현"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


## continue / break
absent = [2, 5] # 결석
no_book = [7] # 책을 잊어버림

for student in range(1, 11): # 10명의 학생 출석번호 1 ~ 10번까지
    if student in absent: # 결석한 학생의 출석번호일 경우 스킵
        continue
    elif student in no_book:
        print("오늘 수업을 여기까지 입니다. {0}번 학생은 교무실로 오세요.".format(student))
        break
    print("{0}, 책을 읽어주세요.".format(student))

## 한줄 for문
# 출석번호가 1 2 3 4 -> 101 102 103 104 변경
students = [1,2,3,4,5]
print(student)
students = [i+100 for i in students]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
