# Bibliotecas necessárias
import flask
from flask import request, jsonify

# Iniciando o aplicativo Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Criando a rota para o agendamento de serviços
@app.route('/agendar', methods=['GET', 'POST'])
def agendar_servico():
    if request.method == 'POST':
        servico = request.form['servico']
        profissional = request.form['profissional']
        horario = request.form['horario']

        # Adicionando o agendamento ao banco de dados
        # (este passo depende da implementação escolhida para o banco de dados)

        return 'Serviço agendado com sucesso!'
    return '''
        <form method="post">
            Serviço: <input type="text" name="servico">
            Profissional: <input type="text" name="profissional">
            Horário: <input type="text" name="horario">
            <input type="submit" value="Agendar">
        </form>
    '''

# Executando o aplicativo
app.run()
