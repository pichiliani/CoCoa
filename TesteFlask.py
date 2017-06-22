from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/RFID",methods=['GET', 'POST'])
def hello():
    
	tag_rfid = request.args.get('tag')
	
	print("Tag RDIF:" + tag_rfid.upper())
	return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=80)