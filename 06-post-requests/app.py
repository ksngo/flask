from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here!
@app.route("/")
def hello():
	return render_template("index.template.html")
	
@app.route("/process",methods=['POST'])
def processHello():
    first=request.form.get('first-name')
    last=request.form.get('last-name')
    print(first)
    print(last)
    return render_template('process-hello.template.html', fn=first,ln=last)

@app.route('/calculate',methods=['GET','POST'])
def displayform():

    if request.method=='GET':
        return render_template('submitnumbers.html')
    elif request.method=='POST':
        first = int(request.form.get('first-number'))
        second = int(request.form.get('second-number'))
        sum = first + second
        return render_template('answer.html', s=sum)

#
# @app.route('/calculate',methods=['POST'])
# def displayanswer():
#     first=int(request.form.get('first-number'))
#     second=int(request.form.get('second-number'))
#     sum=first+second
#     return render_template('answer.html', s=sum)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)