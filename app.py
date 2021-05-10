from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        USERNAME = request.form['fname']
        searchword = request.args.get('fname', '')
        return str(rapid(USERNAME))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
