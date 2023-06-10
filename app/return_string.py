from flask import Flask

app = Flask(__name__)


@app.route('/name')
def get_name():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# http://localhost:5000/name
