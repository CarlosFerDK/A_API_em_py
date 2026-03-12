from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calcular', methods=['POST']) #método utilizado 
def calcular(): 
    dados = request.get_json() #vai receber os dados JSON

    num1 = dados.get('num1') #extrai os valores
    num2 = dados.get('num2')
    operacao = dados.get('operacao')

    if num1 is None or num2 is None or operacao is None: #validaçao
        return jsonify({"erro": "Parâmetros faltando: num1,num2 e operacao são obrigatórios"}), 400

    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subtracao":
        resultado = num1 - num2
    elif operacao == "multiplicacao":
        resultado = num1 * num2
    elif operacao == "divisao":
        if num2 == 0:
            return jsonify({"erro": "Divisao por zero nao é permitida"}), 400
        resultado = num1 / num2
    else:
        return jsonify({"erro": "Operacao invalida. Use: soma, subtracao, multiplicacao ou divisao"}), 400

    return jsonify({ #retorna em Json o resultado
        "num1": num1,
        "num2": num2,
        "operacao": operacao,
        "resultado": resultado
    })
if __name__ == '__main__':
    app.run(debug=True, port=5000)

#Postman>novo>HTPP>Método Post>