from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    if power <3:
        return False
    total = sum(int(d) ** power for d in digits)
    return total == abs(n)

def get_digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        if response.status_code == 200:
            return response.text
    except:
        pass
    
    # Fallback fun facts
    if is_armstrong(n):
        digits = str(abs(n))
        power = len(digits)
        calculation = " + ".join([f"{d}^{power}" for d in digits])
        return f"{n} is an Armstrong number because {calculation} = {n}"
    return f"{n} is a number."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    # Validate input
    try:
        num = int(number)
    except (TypeError, ValueError):
        return jsonify({"number": number, "error": True}), 400
    
    # Determine properties
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    # Build response
    result = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": get_digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }
    
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
