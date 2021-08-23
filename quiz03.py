site = "http://google.com"

site = site[7:]
site = site[:-4]

password = site[:3] + str(len(site)) + str(site.count("e")) + "!"

print(f"생성된 비밀번호는 {password}입니다.")




# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙 1
# my_str = my_str[:my_str.index(".")] # 규칙 2
