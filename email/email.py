from flask import Flask
import json

app = Flask(__name__)

class Product(Resource):
	def get(self):
	
		alert_file = open("/home/raddish18/Microserv/Youtube/analysis/output.txt").readlines()
		alerts = []
		
		for line in alert_file:
			alerts.append(line)				
					
		with open('emails.txt', 'w') as f:
    			for alert in alerts:
        			f.write("%s\n" % alert)

        
if __name__ == '__main__':
    app.run( host='0.0.0.0', debug=True)
