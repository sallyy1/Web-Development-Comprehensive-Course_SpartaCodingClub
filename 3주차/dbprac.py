from pymongo import MongoClient
import certifi ## 보안 관련 추가 설정

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.6syxk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca) ## 보안 관련 추가 설치
db = client.dbsparta

'''
# 1. 데이터 넣어보기
# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})


# 2. 모든 데이터 뽑아보기
all_users = list(db.users.find({},{'_id':False}))

print(all_users[0])         # 0번째 결과값을 보기
print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기


for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(user)

## 1명의 값만 가져오기
print()
user2 = db.users.find_one({'name': 'bobby'})
print(user2['age'])


# 3. 값 바꾸기
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)


# 4. 값 삭제
db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user)
'''


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})