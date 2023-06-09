# flask 웹 서버 
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')  # http://localhost:5000/
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True)