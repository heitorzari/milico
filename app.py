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



usuarios = {
    'admin' : 'admin',
    'usuario' : 'senha',
    'rafaela' : '111111',
    'heitor' : '1271'
}
@app.route('/') #rota para a página inicial
def home():
    return render_template('index.html')

@app.route('/login') #rota para a página de login
def login():
    return render_template('login.html')



#verificar login
@app.route('/verificar-login', methods=['POST   '])
def verificar_login():
   username = request.form['username']
   password = request.form['password']

    
#huiu
if __name__== '__main__':
    app.run(debug=True)

    