a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def check_mail(s):
	## 여기에 코딩을 해주세요
    if '@' in s:
        return True
    else:
        return False

print(check_mail(a))