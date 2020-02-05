from flask import Flask, render_template, request, flash, redirect, url_for

import redis

import string

import random 

app = Flask(__name__)

#app.debug = True
#app.secret_key = 'kdud743ldsksjdlff092dsjd632skdjhfdd'



@app.route('/')
def connect_redis():
	#contenty = {}
        #r = redis.StrictRedis(host='192.168.58.150', port=6379, db=0)
        #for key in r.scan_iter("*"):
	#for key,val in r.hscan("*"):
        #	val = r.get(key)
	 #       contenty[key]=val
	#contenty = r.hgetall("mydict")
        contenty = {"1":"234567"}	
	#print str(type(contenty))
	return render_template('index.html', title='Home', contenty=contenty)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)
