from flask import Flask
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] ='asdasdasd'
app.config['SESSION_TYPE'] ='redis'
app.config['SESSION_REDIS'] ='192.168.1.23:6379'
s = Session()
s.init_app(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

if __name__ == '__main__':
    app.run()