from flask import Flask, request, jsonify


app = Flask(__name__)

def calculate_sum(num1, num2):
    return num1 + num2


@app.route('/sum', methods=['POST'])
def sum_route():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = calculate_sum(num1, num2)
    return jsonify({'result': result})
