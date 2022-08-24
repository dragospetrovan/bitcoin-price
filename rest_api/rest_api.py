from flask import Flask
import flask


app = Flask(__name__)
@app.route('/health-check')
def health():
	status_code = flask.Response(status=200)
	return status_code

if __name__ == '__main__':
    app.run('0.0.0.0', '80')