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

2) Open google shell and clone this repository
**git clone https://github.com/vinaykumarnair/gcpvmflaskserver.git**

<img width="1440" alt="Screenshot 2021-09-22 at 9 37 26 AM" src="https://user-images.githubusercontent.com/21003585/134285296-aae18d0e-dff0-45bc-a76a-547aa2dfe370.png">


3) Go into the gcpvmflaskserver folder

<img width="1440" alt="Screenshot 2021-09-22 at 9 38 06 AM" src="https://user-images.githubusercontent.com/21003585/134285533-3fcabcb9-a801-4098-8739-435b0e3da51c.png">


4) Install the required packages by below command on shell
   **pip install -r requirement.txt**
   
   run on shell 
   **python hello.py**
   
<img width="1440" alt="Screenshot 2021-09-22 at 10 17 34 AM" src="https://user-images.githubusercontent.com/21003585/134285693-81e87ba5-aa52-427d-a0d0-ec85cbb735dd.png">

5) Click on web preview port 5001
<img width="1440" alt="Screenshot 2021-09-22 at 2 14 19 PM" src="https://user-images.githubusercontent.com/21003585/134312257-e7c5b3a4-39fe-4ec8-9007-b4893f72f2b5.png">


