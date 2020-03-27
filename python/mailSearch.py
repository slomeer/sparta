a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def get_mail(s):
	## 여기에 코딩을 해주세요
    a1 = s.split('@')[1]
    result = a1.split('.')[0]
    return result

#결과값
print(get_mail(a))