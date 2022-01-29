from pymongo import MongoClient
import certifi ## 보안 관련 추가 설정

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.6syxk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca) ## 보안 관련 추가 설치
db = client.dbsparta


# 퀴즈 1번
quiz_result = db.movies.find_one({'title': '가버나움'})
print(quiz_result['star'])
print()



# 퀴즈 2번
quiz_result2 = list(db.movies.find({'star': quiz_result['star']}, {'_id': False}))

for elem in quiz_result2:
    print(elem['title'])

print()


# 퀴즈 3번
db.movies.update_one({'title':'가버나움'},{'$set':{'star': str(0.0)}})