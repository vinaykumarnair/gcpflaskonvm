# File name: hello_webapp.py 
from flask import Flask, render_template # include the flask library 

app = Flask(__name__) 

@app.route("/") 
def index(): 
   return render_template('index.html')

if __name__ == '__main__': 
   app.run(port=5001, debug=True) # application will start listening for web request on port 5000