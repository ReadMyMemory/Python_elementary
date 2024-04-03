id = input("아이디를 입력하시오 : ")

if(id != "KUTIS"):
    print("아이디를 찾을 수 없습니다.")
else:
    pw = input("패스워드를 입력하시오 : ")
    if(pw != "12345"):
        print("비밀번호가 잘못되었습니다.")
    else:
        print("환영합니다.")
