from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route("/")
def hello():
	sleep(10)
	return {'body': 'hello'}

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=6289)