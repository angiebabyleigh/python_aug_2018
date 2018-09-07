from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key = "jfl39-2pjf@%-unnasdf;-239((*)3"

@app.route('/')
def enterinfo():
	return render_template("index.html")

@app.route('/return', methods=['POST'])
def display():
	
	return render_template("display.html", 
		name=request.form['name'],
		location=request.form['location'],
		language=request.form['language'],
		comment=request.form['comment'])


	print(name)
	print(location)
	print(language)
	print(comment)

@app.route('/danger')
def danger():
	print("a user tried to visit /danger.  we have redirected the user to /")
	return redirect('/')

if (__name__=="__main__"):
	app.run(debug=True)