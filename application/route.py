from application import app
from models import example

@app.route('/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def _index():
	return example.start();
