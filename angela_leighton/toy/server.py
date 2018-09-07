from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

print(__name__)

app.secret_key = "uiaefjhgureahgrioajgljgfklejglvkae"

@app.route('/toyform')
def page():
	return render_template('infopage.html')

@app.route('/process', methods=['POST'])
def process():
	toyname=request.form['name']
	age=request.form['agegroup']
	session['a'] = age #{'a':"10"}
	#session.pop('a')
	print(toyname)
	print(age)
	return redirect('/display')
	#return "Success!" + session['a']

@app.route('/display')
def display():
	return "Success!"
 
if __name__=="__main__":
	app.run(debug=True)
