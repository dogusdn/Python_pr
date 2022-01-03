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

### 문자열처리함수
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

### 리스트 []
```python
subway = ["유재석", "조세호", "박명수"]

# 조세호 는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하 가 다음 정류장에 다음 칸에 탐
subway.append("하하")

# 정형돈을 유재석과 조세호 사이에 넣음
subway.insert(1, "정형돈")

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼낸다.
print(subway.pop())
```

### 사전
```python
cabinet = {3 : "유재석", 100 : "김태호"}
cabinet = {"A-3" : "유재석" , "B-100" : "김태호"} # key에 문자열도 가능
print(cabinet[3]) # 유재석
print(cabinet.get(3)) # 유재석
print(cabinet[5]) # 오류 발생 후 프로그램 종료
print(cabinet.get(5)) # NONE 오류발생 X 프로그램 종료되지 않음
print(cabinet.get(5, "사용가능"))   # None 대신 사용가능 메시지 표출
print(3 in cabinet) # 키가 있는지 확인 True
print(5 in cabinet) # False

# 새로운 손님
cabinet["C-20"] = "조세호"
# 나간 손님
del cabinet["A-3"]
# key 들만 출력함
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력함
print(cabinet.items())
# 목욕탕을 폐점
cabinet.clear()
```

### 튜플
* 내용을 추가하거나 변경할 수 없다.
* 대신 리스트보다 속도가 빠르다
* 변경되지 않는 값들을 다룰 때 유용함
```python
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스
# menu.add("생선까스") # 튜플은 add라는 기능을 제공하지 않음
# 값을 추가하던지 변경할 수 없음

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
```

### 집합 (set)
* 중복 안됨, 순서 없음
```python
my_set = {1,2,3,3,3} # {1,2,3} 만 출력! 중복이 안되기 때문에

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")

# java를 까먹었음
java.remove("김태호")
```

### 자료구조의 변경
```python
menu = {"커피", "우유", "주스"}
menu = list(menu)
menu = tuple(menu)
menu = set(menu)
```


### What is Git?
* 레시피 책
* 도넛 만들기
  * 케이크
    * 야채피자 만들기
