from flask import Flask

app = Flask("meu app")
# comentário
@app.route('/')
def hello():
    return "Olá Mundo!"

@app.route('/novo')
def novo():
    return "<h1> Nova Pagina</h1>"