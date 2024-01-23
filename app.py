from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db = SQLAlchemy(app)

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tocar = db.Column(db.Integer)
    cantar = db.Column(db.Integer)
    de_manha = db.Column(db.Integer)
    a_tarde = db.Column(db.Integer)
    receber_email = db.Column(db.Integer)
    email = db.Column(db.String(100))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    tocar = 1 if 'tocar' in request.form else 0
    cantar = 1 if 'cantar' in request.form else 0
    de_manha = 1 if 'de_manha' in request.form else 0
    a_tarde = 1 if 'a_tarde' in request.form else 0
    receber_email = 1 if 'receberEmailCheckbox' in request.form else 0
    email = request.form['email'] if receber_email else None

    resposta = Resposta(nome=nome, tocar=tocar, cantar=cantar, de_manha=de_manha, a_tarde=a_tarde, receber_email=receber_email, email=email)
    db.session.add(resposta)
    db.session.commit()

    return "Dados enviados com sucesso!"



@app.route('/form.html/<domingo>', methods=['GET', 'POST'])
def form(domingo):
    if request.method == 'POST':
        # Lógica de processamento do formulário, se necessário
        return redirect(url_for('index'))  # Redireciona para a página inicial após o envio do formulário
    return render_template('form.html', domingo=domingo)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
