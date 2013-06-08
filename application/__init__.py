import logging
from flask import Flask
from redis_session import RedisSessionInterface

app = None
app_run_args = {}

def create_app(mode = "production"):
	global app
	app = Flask("application")
	global app_run_args
	app_run_args = {'port': 5000, 'host': '127.0.0.1'}

	if mode == "production":
		app.debug = False
	elif mode == "dev":
		app.debug = True
	else:
		logging.error("Did not recognize mode '%s'" % mode)


def run_app():
	app.run(**app_run_args)
