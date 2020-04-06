from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('onePageShop.html')

# 주문하기(POST) : 주문 목록을 mongodb에 추가
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    etc_receive = request.form['etc_give']

    order = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'phone' : phone_receive,
        'etc' : etc_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '배달, 성공적'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({}, {'_id':0}))
    return jsonify({'result': 'success', 'orders':orders})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)