# 문자열 포맷

# 방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple 은 %c 로 시작합니다." % "A")

# %s -> 정수, 문자 상관없이 출력할 수 있음
print("나는 %d살 입니다." % 21)

print("나는 %s색과 %s색을 좋아합니다." % ("빨강", "파랑"))

# 방법 2
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다." .format("빨강", "파랑"))
print("나는 {0}색과 {1}색을 좋아합니다." .format("빨강", "파랑"))
print("나는 {1}색과 {0}색을 좋아합니다." .format("빨강", "파랑"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아합니다." .format(age = 20 , color = "빨강"))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color} 색을 좋아합니다.")

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 따옴표
print("저는 '도현우' 입니다.")
print('저는 "도현우" 입니다.')
print("저는 \"도현우\" 입니다.")

# \\ : 문장 내에서 \
print("F:\\github\\Python_PR>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 ( 한 글자를 지움 )
print("Redd\bApple")

# \t : 탭 역할
