from flask import Flask, render_template
app = Flask(__name__)
# 플라스크 앱을 실행할 대상이 __name__이구요. 그걸 플라스크에 알려주면 거기서 플라스크를 실행가능

@app.route('/') # 앱의 기본 경로에 접속했을 때 어떤 함수를 실행할 것이냐이다.
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('localhost',port=5000,debug=True)
   # 주소 '0.0.0.0'으로 하면 페이지가 안 떴다
   # debug true 하면 콘솔에 기록이 많이 남는다
   # 0.0.0.0:5000/ 이 기본 주소