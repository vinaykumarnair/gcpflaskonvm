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

2) Create a new Gcloud VM instance with below command on Google cloud shell

```shell
gcloud compute instances create gcp-vm-instance-1 --project=gcp-flask-serv-02 --zone=us-east1-b --machine-type=f1-micro --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=MIGRATE --service-account=773175670425-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server --create-disk=auto-delete=yes,boot=yes,device-name=gcp-vm-instance-1,image=projects/debian-cloud/global/images/debian-10-buster-v20210916,mode=rw,size=10,type=projects/gcp-flask-serv-02/zones/us-west4-b/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any
```

2) Open google shell and clone this repository
**git clone https://github.com/vinaykumarnair/gcpvmflaskonvm.git**




3) Go into the gcpvmflaskserver folder



4) Install the required packages by below command on shell
   **pip install -r requirement.txt**
   
   run on shell 
   **python hello.py**
   
<img width="1440" alt="Screenshot 2021-09-22 at 10 17 34 AM" src="https://user-images.githubusercontent.com/21003585/134285693-81e87ba5-aa52-427d-a0d0-ec85cbb735dd.png">

5) Click on web preview port 5001
<img width="1440" alt="Screenshot 2021-09-22 at 2 14 19 PM" src="https://user-images.githubusercontent.com/21003585/134312257-e7c5b3a4-39fe-4ec8-9007-b4893f72f2b5.png">


