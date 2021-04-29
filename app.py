from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GETUSERNAME'])
def getUsername():
    text = request.form['text']
    processed_text = text.trim()
    return processed_text

if __name__ == '__main__':
    app.run(debug=True)
