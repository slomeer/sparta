from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.sparta_project_DB # 'sparta_project_DB' 이름의 DB 생성

app = Flask(__name__)

# 시작 페이지
@app.route('/')
def start():
    return render_template('startPage.html')

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
    doh_receive = request.form['doh_give']
    siGoonGu_receive = request.form['siGoonGu_give']
    photo_receive = request.form['photo_give']
    date_receive = request.form['date_give']
    weather_recieve = request.form['weather_give']
    equipment_receive = request.form['equipment_give']
    program_receive = request.form['program_give']
    etc_receive = request.form['etc_give']
    photo_uuid_receive = request.form['photo_uuid_give']

    photo_inform = {
        'lat' : lat_receive,
        'lng' : lng_receive,
        'doh' : doh_receive,
        'siGoonGu' : siGoonGu_receive,
        'photo' : photo_receive,
        'date' : date_receive,
        'weather' : weather_recieve,
        'equipment' : equipment_receive,
        'program' : program_receive,
        'etc' : etc_receive,
        'photo_uuid' : photo_uuid_receive
    }

    db.photos.insert_one(photo_inform)

    return jsonify({'result':'success', 'msg':'POST 성공'})

@app.route('/gallery', methods=['POST'])
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

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)