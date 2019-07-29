#Email
import smtplib, ssl
import re
from flask import Flask
app = Flask(__name__)

@app.route("/")

def email():
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "gibbytestman@gmail.com"  # Enter your address
	receiver_email = "gibbytestman@gmail.com"  # Enter receiver address
	password = "P@ssw0rd42"

	alert_file = open("/home/raddish18/Microserv/Youtube/analysis/output.txt", "r")
	blacklist = []
	bl = open("blacklist.txt").readlines()
	for ip in bl:
		blacklist.append(ip.strip())

	df = []
	for line in alert_file:
		#print line
		df.append(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line)))
		#print re.match(regex, line).groups()
	
	df = filter(None, df)
	
	regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

	# Create a secure SSL context
	context = ssl.create_default_context()
	last_entry_time = []
	fmt = "%d-%m-%Y %H:%M:%S +%d%d%d%d"

	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login("gibbytestman@gmail.com", password)
		
		for line in df:
			for ip in bl:
				if (ip not in last_entry_time):
					date_only = datetime.datetime.strptime(line[3], fmt)
					last_entry_time.append(ip, date_only)
					message = "ALERT BLACKLISTED IP TRIGGERED:\n" + ip + "\t" + line[3]
					server.sendmail(sender_email, receiver_email, message)

				elif(line[0] in last_entry_time):
					if(datetime.datetime.strptime(line[3], fmt) - last_entry_time[1] >= timedelta(hours=24)):
						#print( ip + "\t" + line[3])
						message = "ALERT BLACKLISTED IP TRIGGERED:\n" + ip + "\t" + line[3]
						server.sendmail(sender_email, receiver_email, message)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80, debug=True)
