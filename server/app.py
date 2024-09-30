#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to display a parameter passed in the URL and print to the console
@app.route('/print/<string:text>')
def print_text(text):
    print(text)  # Output the text to the console
    return text  # Return the text in the response

# Route to count from 0 to a given number
@app.route('/count/<int:number>')
def count(number):
    return '\n'.join(str(i) for i in range(number)) + '\n'

# Route to perform basic math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400  # Return 400 Bad Request for invalid operations
    
    return str(result)

# Entry point to run the app

if __name__ == '__main__':
    app.run(port=5555, debug=True)
