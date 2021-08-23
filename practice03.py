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
