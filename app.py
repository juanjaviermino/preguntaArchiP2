from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/question', methods=['GET'])
def get_question():
    return 'Sigue intentando', 200

@app.route('/question', methods=['PUT'])
def put_question():
    return 'Correcto! PUT es el método necesario para obtener la respuesta.', 200

@app.route('/question', methods=['POST'])
def post_question():
    return 'Sigue intentando', 200

@app.route('/question', methods=['PATCH'])
def patch_question():
    return 'Sigue intentando', 200

@app.route('/question_2', methods=['POST'])
def post_question_2():
    # Checking for a specific key-value pair in the request body
    data = request.json
    if data and data.get('respuesta') == '¿Será esta la respuesta correcta?':
        return '¡Sí es!', 200
    else:
        return 'No creo...sigue intentando', 200

if __name__ == '__main__':
    app.run(debug=True)
