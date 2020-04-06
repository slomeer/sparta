from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
avg = db.movies.find({'title':'어벤져스: 엔드게임'},{'title':0, '_id':0, 'rank':0})

target_star = avg[0]['star']
same_movies = db.movies.find({'star': target_star})

db.movies.update_many({'star': target_star}, {'$set':{'star':0}})

