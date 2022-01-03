# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호 는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하 가 다음 정류장에 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 넣음
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼낸다.
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능함
num_list = [5,2,4,3,1]
num_list.sort()
num_list.reverse()
num_list.clear()


# 다양한 자료형과 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]

# 리스트의 확장
num_list.extend(mix_list)
print(num_list)



# 5-2 사전
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])

print(cabinet.get(3))

print(cabinet[5]) # 오류 발생 후 프로그램 종료
print(cabinet.get(5)) # NONE 오류발생 X 프로그램 종료되지 않음
print(cabinet.get(5, "사용가능"))   # None 대신 사용가능 메시지 표출

print(3 in cabinet) # 키가 있는지 확인 True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석" , "B-100" : "김태호"}

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


# 5-3 튜플 ( 내용을 변경이나 추가 할 수 없음 // 대신, 속도가 리스트보다 빠르다 )
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# menu.add("생선까스") # 튜플은 add라는 기능을 제공하지 않음
# 값을 추가하던지 변경할 수 없음

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)


(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


# 5-4 집합 (set)
# 중복안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

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
print(python)

# java를 까먹었음
java.remove("김태호")
print(java)


# 5-5 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
menu = tuple(menu)
menu = set(menu)

