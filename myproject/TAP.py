from flask import Flask, render_template, jsonify, request, redirect, url_for

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.sparta_project_DB # 'sparta_project_DB' 이름의 DB 생성(사진 자료용)
db_user = client.sparta_project_user # 회원가입, 로그인용 DB

app = Flask(__name__)

# JWT 토큰을 만들 때 필요한 비밀문자열입니다. 아무거나 입력해도 괜찮습니다.
# 이 문자열은 서버만 알고있기 때문에, 내 서버에서만 토큰을 인코딩(=만들기)/디코딩(=풀기) 할 수 있습니다.
SECRET_KEY = 'apple'

# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt

# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime

# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib

# 시작 페이지
@app.route('/')
def start():
    return render_template('시작페이지.html')

# 포토 스팟 및 사진 등록 페이지
@app.route('/regisphoto')
def regisphoto_html():
    return render_template('포토스팟사진등록.html')

# 갤러리 페이지
@app.route('/gallery')
def gallery_html():
    return render_template('갤러리.html')

# API 역할 하는 부분
@app.route('/regisphoto', methods=['POST'])
def upload_photo():
    lat_receive = request.form['lat_give']
    lng_receive = request.form['lng_give']
    siDoh_receive = request.form['siDoh_give']
    siGoonGu_receive = request.form['siGoonGu_give']
    photo_receive = request.form['photo_give']
    date_receive = request.form['date_give']
    time_receive = request.form['time_give']
    weather_recieve = request.form['weather_give']
    equipment_receive = request.form['equipment_give']
    program_receive = request.form['program_give']
    etc_receive = request.form['etc_give']
    photo_uuid_receive = request.form['photo_uuid_give']

    photo_inform = {
        'lat' : lat_receive,
        'lng' : lng_receive,
        'siDoh' : siDoh_receive,
        'siGoonGu' : siGoonGu_receive,
        'photo' : photo_receive,
        'date' : date_receive,
        'time' : time_receive,
        'weather' : weather_recieve,
        'equipment' : equipment_receive,
        'program' : program_receive,
        'etc' : etc_receive,
        'photo_uuid' : photo_uuid_receive
    }

    db.photos.insert_one(photo_inform)

    return jsonify({'result':'success', 'msg':'POST 성공'})

@app.route('/gallery', methods=['POST', 'DELETE'])
def open_gallery():
    photos = list(db.photos.find({}, {'_id':0}))
    return jsonify({'result':'success', 'photos':photos})

# 등록된 사진의 포토 스팟 및 정보를 보여주는 페이지
@app.route('/photo_inform')
def photo_inform_origin():
    return render_template('사진정보페이지.html')

@app.route('/photo_inform/<photo_uuid>')
def photo_inform_page(photo_uuid):
    return render_template('사진정보페이지.html', photoUUID = photo_uuid)

@app.route('/photo_inform/<photoUuid>', methods=['POST'])
def photo_inform(photoUuid):
    photo_inform = list(db.photos.find({'photo_uuid':photoUuid}, {'_id':0}))
    return jsonify(({'result':'success', 'photo_inform':photo_inform}))

@app.route('/photo_inform/<photoUuid>', methods=['DELETE'])
def photo_inform_del(photoUuid):
    db.photos.delete_one({'photo_uuid':photoUuid})
    return redirect('/gallery')

@app.route('/login')
def login_page():
    return render_template('로그인페이지.html')

@app.route('/regis_user')
def regis_user_page():
    return render_template('회원가입페이지.html')

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)