from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
 return 'Hello, World!'

if __name__ == '\_\_main\_\_':
 app.run(host='0.0.0.0', port=80)
