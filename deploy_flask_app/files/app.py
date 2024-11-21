from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome in app working in Docker on RHEL9!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
