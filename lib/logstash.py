import requests
import os

class Logstash:

	def __init__(self):
		host = 'listener.logz.io'
		port = 8071
		log_token = os.environ['log_token']
		self.url = f"https://{host}:{port}/?token={log_token}"

	def log_and_print(self, message):
		body = {}
		body['message'] = message
		print(body)	
		resp = requests.post(
            		self.url,
            		json=body
        		)
