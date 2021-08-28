# 문자열
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0번째 부터 2번째 직전 값 까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 값을 가져옴
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지



# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 문자열을 전부 소문자로 출력
print(python.upper()) # 문자열을 전부 대문자로 출력
print(python[0].isupper()) # 대문자면 True 소문자면 False
print(len(python)) # 문자열의 길이를 출력함
print(python.replace("Python", "Jave")) # 문자열을 바꾸어서 출력함

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 찾는 문자열이 없으면 -1 반환
print(python.index("Java")) # 찾는 문자열이 없으면 오류 출력

print(python.count("n")) # n 이 총 몇번 등장하는지 카운트



# 문자열 포맷

# 방법 1
print("나는 %d살 입니다." % 20) # 정수값을 집어 넣음
print("나는 %s을 좋아합니다." % "파이썬") # 문자열
print("Apple 은 %c로 시작합니다." % "A") # 한 문자

print("나는 %s색과 %s색을 좋아합니다." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아합니다." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아합니다." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아합니다." .format(age = 20, color="빨간"))


# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아합니다.")




# 탈출 문자

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \ 큰따옴표 출력하고 싶을 때
print("저는 \"도현우\"입니다.")


# \\ : 문장 내에서 \ 하나로 출력하게 됨
print("C:\\Users\\dogus\\OneDrive - Yaojushi\\바탕 화면\\Python")

# \r : 커서를 맨 앞으로 이동함
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

subway = [10,20,30]
print(subway)

subway = ["도현우", "고우현", " 심성훈"]

# 도현우가 몇 번째 칸에 타고 있는가?
print(subway.index("도현우"))

# 다음 정류장에서 임창정이 다음 칸에 탐
subway.append("임창정")

# 김연주를 도현우 / 고우현 사이에 태워봄
subway.insert(1, "김연주")

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())

# 같은 이름의 사람이 몇 명 있는지 확인함
subway.append("도현우")
print(subway.count("도현우"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()

# 다양한 자료형과 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["도현우", 20, True]


# 리스트 확장
num_list.extend(mix_list)
print(num_list)


# 사전
cabinet = {3:"도현우", 100:"고우현"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet[5]) # 오류를 발생하고 프로그램을 종료
print(cabinet.get(5)) # None 출력 후 오류를 발생하지는 않음
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False

# 문자열도 가능함
cabinet = {"A-3":"도현우", "B-100":"고우현"}

# 새로운 사람을 추가함
cabinet["C-20"] = "심성훈"

# 간 사람
del cabinet["A-3"]

# Key 들만 출력함
print(cabinet.keys())

# value 들만 출력함
print(cabinet.values())

# key, value 쌍으로 출력함
print(cabinet.items())

# 모든 값들을 삭제
cabinet.clear()
print(cabinet)


# 튜플
menu = ("돈까스", "치즈까스")

# menu.add("생선까스") -> 튜플은 고정된 값에서만 활용을 해야한다

(name, age, hobby) =  ("도현우", 25, "코딩")
print(name, age, hobby)


## 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}

java = {"도현우", "고우현", "심성훈"}
python = set(["도현우", "김형준"])

# 교집함 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 개발자 
python.add("김연주")

# java 를 잊어버림
java.remove("고우현")
