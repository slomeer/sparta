from pymongo import MongoClient # 진짜 필요한 패키지만 가져오는게 좋은 것이다
client = MongoClient('localhost', 27017)
db = client.dbsparta

#users 라는 컬렉션을 만들고 거기에 한개의 문서를 넣는다 (각 줄마다)
# db.users.insert_one({'name':'bobby', 'age':21}) #여기서 컬렉션이 생성
# db.users.insert_one({'name':'kay', 'age':27})
# db.users.insert_one({'name':'john', 'age':30})

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find({'name':'bobby'})
print(list(user))