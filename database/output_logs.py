#from flask import Flask
#from flask_restful import Resource, Api

#app = Flask(__name__)
#api = Api(app)

def Log():
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

	
	with open('output.txt', 'w') as f:
    			for item in alerts:
        			f.write("%s\n" % item)

	


def main():	
	Log()

main()
