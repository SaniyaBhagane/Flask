from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_worls():
    return '<p>Hello World !!</p>'

@app.route('/hello')
def hello():
    return '<p> Hello Flask !!</p>'

if __name__ == '__main__':
    app.run()
