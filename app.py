#ffffff
from flask import Flask, render_template, request

app = Flask(__name__)

#hjhjh
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')



#huiu
if __name__== '__main__':
    app.run(debug=True)