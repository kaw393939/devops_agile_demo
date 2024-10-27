from flask import Flask, render_template, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# API endpoints for calculator operations
@app.route('/add', methods=['POST'])
def add_route():
    data = request.get_json()
    result = add(data['a'], data['b'])
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract_route():
    data = request.get_json()
    result = subtract(data['a'], data['b'])
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply_route():
    data = request.get_json()
    result = multiply(data['a'], data['b'])
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide_route():
    data = request.get_json()
    try:
        result = divide(data['a'], data['b'])
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
