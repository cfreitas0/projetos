from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DOM123'


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    nome = request.form.get('nome')
    senha = request.form.get('senha')
    print(nome)
    print(senha)

    if nome == 'cesar' and senha == '1234':
        return render_template("aces_liberado.html") 
    else:
        return redirect('/')



if __name__ in "__main__":
    app.run(debug=True)