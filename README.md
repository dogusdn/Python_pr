# Python
## yotube [나도코딩_파이썬](https://youtu.be/kWiCuklohdY)

### 숫자 처리 함수
```python
print(abs(-5)) # 절댓값 5
print(pow(4, 2)) # 4^2 = 4 * 4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 반올림 값 3
print(round(4.99))  # 5
````

### 랜덤함수
```python
print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값을 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성

print(randrange(1, 46)) # 1 ~ 46 미만/45 이하의 임의의 값을 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성
```
* randrange : 미만
* radnint : 헷갈리지 않게 두개의 숫자를 포함

### 슬라이싱
```python
jumin = "990120-1234567" # 주민등록번호

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전 까지 (0,1 값만)
print("월 : " + jumin[2:4]) # 2, 3 값만
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 값
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝 까지
print("뒤 7자리 (뒤에부터계산) : " + jumin[-7:]) # 맨뒤에서 7번째부터 끝까지
```

###문자열처리함수
```python
python = "Python is Amazing"
print(python.lower())   # 전부 대문자로 출력
print(python.upper())   # 전부 소문자로 출력
print(python[0].isupper()) # 대문자인지 확인
print(len(python)) # 문자열의 길이를 반환
print(python.replace("Python", "Java")) # 문자열 치환
```

### 문자열 포맷
```python
# 방법 1
print("나는 %s색과 %s색을 좋아합니다." % ("빨강", "파랑"))

# 방법 2
print("나는 {0}색과 {1}색을 좋아합니다." .format("빨강", "파랑"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아합니다." .format(age = 20 , color = "빨강"))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color} 색을 좋아합니다.")

# \\ : 문장 내에서 \
print("F:\\github\\Python_PR>")
```

### What is Git?
* 레시피 책
* 도넛 만들기
  * 케이크
    * 야채피자 만들기
