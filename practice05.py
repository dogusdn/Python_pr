## 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값
def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금 보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 백원
    return commission, balance - money - commission


# 함수의 사용
balance = 0 # 처음 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


## 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("도현우", 26, "파이썬")
profile("고우현", 25, "자바")

# 같은 학교, 학년, 반, 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어:{2}".format(name, age, main_lang))

# 이름만 넘겨도 같은 나이, 수업으로 출력 됨
profile("유재석")
profile("김태호")

# 방법 2
def profile(name, age, main_lang):
    print(name, age, main_lang)

# 순서가 섞여 있어도 상관 없다!
profile(name="도현우", age = 26, main_lang="파이썬")
profile(main_lang="자바", name="고우현", age=26)


## 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

## 지역변수와 전역변수
# 지역변수 : 함수 호출 될 때 만들어졌다가 끝나면 사라짐
# 전역변수 : 프로그램 어디에서든 부를 수 있는 변수

gun = 10

def checkpoint(soldiers): # 경계근무
    # 지역변수로 초기화를 시켜줘야지 변수를 사용할 수 있음
    global gun # 전역 공간에 있는 gun 을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
    

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무를 나감
print("남은 총 : {0}".format(gun))