from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DOM123'


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    return redirect('/')