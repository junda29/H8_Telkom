from flask  import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dunia yang Semu!'

@app.route('/hello')
def hello():
    return 'Hello world page 2'

