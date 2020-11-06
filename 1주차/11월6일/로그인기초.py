id = 'aaa'
pw = '111'

while True:
    input_id = input('id 입력:')
    input_pw = input('pw 입력:')

    if input_id == id and input_pw == pw:
        print('로그인 되었습니다.')
        break
    else:
        print('틀렸습니다')
