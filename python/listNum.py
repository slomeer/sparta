from collections import Counter
#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
	## 여기에 코딩을 해주세요
    # for i in range(a_list):
    s = dict()
    for elem in a_list:
        if elem in s:
            s[elem] = s[elem] + 1
        else:
            s[elem] = 1
    return s
    # result = Counter(a_list)
    # return result


#결과값
print(count_list(a))