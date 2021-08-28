## 표준 입출력
print("Python", "Java") # Python Java
print("Python" + "Java") # PythonJava
print("Python", "Java", sep=",") # Python,Java
print("Python", "Java", "JavaScript", sep=" VS ") # Python VS Java Vs JavaScript
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준출력
print("Python", "Java", file=sys.stderr) # 표준에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    
# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21): # 1~20 까지의 범위
    print("대기번호 : " + str(num).zfill(3)) #zfill(3) 3개 만큼의 크기를 확보하고 넣는데 빈공간은 0으로 채움
    
# 표준 입력
answer = input("아무 값이나 입력해주세요 : ") # 입력을 받았을 때 항상 문자열 형태로 저장이 된다.
print("입력하신 값은 {0} 입니다.".format(answer))




## 다양한 출력포맷

# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보함
print("{0: >10}".format(500))

# 양수일 땐 + 로 표시, 음수일 땐 -로 표시함
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬을 하고, 빈칸으로 _ 로 채운다.
print("{0:_<+10}".format(500))


# 3자리마다 콤마(,)를 찍어주기
print("{0:,}".format(1000000000))

# 3자리마다 콤마찍기, + - 부호도 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

print("{0:^<+30,}".format(1000000000))

# 소수점 출력
print("{0:f}".format(5/3)) # 1.666667
# 소수점을 특정 자리수 까지만 표시(소수점 3째 자리수에서 반올림함)
print("{0:f.2}".format(5/3)) # 1.67

## 파일입출력
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 파일을 닫아주는것까지 해줘야함 

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()


# 파일을 읽어옴
score_file = open("score.txt","r", encoding="utf8")
print(score_file.read())
score_file.close()

# 방법 2
score_file = open("score.txt","r", encoding="utf8")
print(score_file.readline(), end="") # 한줄만 읽어오고 나서, 커서를 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline() # 한줄 씩 불러올건데
    if not line: # 읽어 올 내용이 없으면 break
        break
    print(line)
    score_file.close()

# 다른 방법
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 가지고 와서 리스트 형태로 저장함
for line in lines:
    print(line, end="")

score_file.close()




## pickle
# 프로그램 상에서 데이터를 파일 형태로 저장함
import pickle
profile_file = open("pofile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile)
