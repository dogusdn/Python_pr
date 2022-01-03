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
jumin = "990120-1234567" # 주민등록번호

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전 까지 (0,1 값만)
print("월 : " + jumin[2:4]) # 2, 3 값만
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 값
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝 까지
print("뒤 7자리 (뒤에부터계산) : " + jumin[-7:]) # 맨뒤에서 7번째부터 끝까지


# 문자열 처리 함수
python = "Python is Amazing"

print(python.lower())
print(python.upper())

print(python[0].isupper()) # 대문자인지 확인
print(len(python)) # 문자열의 길이를 반환
print(python.replace("Python", "Java")) # 문자열 치환

index = python.index("n")
print(index)

index = python.index("n", index + 1)
print(index)

print(python.find("Java"))  # 없으면 -1 값을 출력
print(python.index("Java")) # 없으면 오류

print(python.count("n")) # 총 n 이 몇번 등장하는지
