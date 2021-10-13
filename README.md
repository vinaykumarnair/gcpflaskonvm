Add a Flask based web app to GCP Shell

1) Just basic flask program

```python
# File name: hello.py 
from flask import Flask, render_template # include the flask library 

app = Flask(__name__) 

@app.route("/") 
def index(): 
   return render_template('index.html')

if __name__ == '__main__': 
   app.run(host='0.0.0.0') # application will start listening for web request on port 5000
```

2) Create a new Gcloud VM instance with below command on Google cloud shell, main thing is you should allow http traffic

```shell
gcloud compute instances create gcp-vm-instance-1 --project=gcp-flask-serv-02 --zone=us-east1-b --machine-type=f1-micro --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=MIGRATE --service-account=773175670425-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server --create-disk=auto-delete=yes,boot=yes,device-name=gcp-vm-instance-1,image=projects/debian-cloud/global/images/debian-10-buster-v20210916,mode=rw,size=10,type=projects/gcp-flask-serv-02/zones/us-west4-b/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any
```

3) Set firewall rule as shown below
Name: gcp-vm-instance-1 , source filter : IP ranges 0.0.0.0/0, open TCP port 5000

4)  SSH into your VM instance and use command nano update.sh , this will open a blank file. Copy below code into it and save. This will install all the necessary software required .

```shell
#! /bin/bash


#
# Make sure installed packages are up to date with all security patches.
#
sudo apt-get -yq update


#
# Install python3
#
sudo apt-get install python3

#
# Install python pip
#
sudo apt-get install python3-pip

#
# Install git 
#
sudo apt-get install git
```

6) Check if python and git are installed using below commands
```shell
python3 --version
```

```shell
git --version
```

7) Clone below repositery

```shell
https://github.com/vinaykumarnair/gcpflaskonvm.git
```

8) Go into the gcpflaskonvm folder

```shell
cd gcpflaskonvm
```

9) Install the required pyhton packages by below command

```shell
   pip3 install -r requirement.txt
```
10) run the hello.py to start the web server

```shell
   python3 hello.py
```
  
11) You will see a message like this

```comment

 * Serving Flask app "hello" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```




