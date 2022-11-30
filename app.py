from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1> Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def display_fahrenheit(celsius):
    result = celsius_to_fahrenheit(float(celsius))
    return f"{celsius} C in fahrenheit is {result:.2f} F"

@app.route('/c')
@app.route('/c/<fahrenheit>')
def display_celsius(fahrenheit):
    result = fahrenheit_to_celsius(float(fahrenheit))
    return f"{fahrenheit} F in celsius is {result:.2f} C"


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

if __name__ == '__main__':
    app.run()
