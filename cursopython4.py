from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return 'Pagina principal'

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return 'Olá,'+ nome +'!'

if __name__== '__main__':
    app.run()


from flask import Flask
app= Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas= <h1>Olá, programador!</h1>
    return boas_vindas + link

@app.route('/user/')
@app.route('/user/<nome>')
def user(nome='Usuario'):
    personalizar= f'<h1>Olá, {nome}!</h1>'
    instrucao= '<p>Altere o nome <em> endereço do brower</em> e recarregue a pagina. </p>'
    return personalizar + instrucao

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask
app= Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas= <h1>Olá, programador!</h1>
    instr= '<p>Entre com dois numeros</p>'
    return boas_vindas + instr

@app.route('/somar/')
@app.route('/somar/<num01>/<num02>')
def soma(num01=0, num02=0):
    resultado= float(num01)+ float(num02)
    return str(resultado)

if __name__=='__main__':
    app.run(debug=True)
    