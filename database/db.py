from flask import Flask
from flask_restful import Resource, Api
import json
import time
import redis

app = Flask(__name__)

@app.route('/')
def print_logs():
	output = ''
	df = []
	lines = open("access.log").readlines()

	for line in lines:
		df.append(line)

	blacklist = []
	bl = open("blacklist.txt").readlines()

	for ip in bl:
		blacklist.append(ip.strip())

	alerts = []
	for log in df:
		for ip in blacklist:
			if ip in log:
				alerts.append(log)
	
	for log in alerts:
		try:
			conn = redis.StrictRedis(host='redis', port=6379)
			for key in conn.scan_iter("ALERT :*"):
            			value = log
            			output += value + '<br>'

			return output


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80, debug=True)
