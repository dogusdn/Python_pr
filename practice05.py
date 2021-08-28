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
