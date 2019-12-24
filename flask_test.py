from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route("/test")
def hello():
	sleep(10)
	return {'body': 'hello'}

if __name__ == '__main__':
   app.run(threaded=True, port=5000)
