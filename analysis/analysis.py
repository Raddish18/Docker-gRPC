from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Product(Resource):
	def get(self):
	
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
		
		f = open("output.txt", "w")
		for line in alerts:
			#print("ALERT: Blaclisted IP detected \n" + line + "\n\n" )
			f.write(line)

		return{
			'products': [json.dumps(i) for i in alerts]
		}

api.add_resource(Product, '/')

        
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80, debug=True)
