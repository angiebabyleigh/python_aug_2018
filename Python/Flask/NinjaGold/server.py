from flask import Flask, render_template, redirect, request, session
import random
import time;

app = Flask(__name__)

app.secret_key = "alsdjf0283r7209urnvakn"

@app.route('/')
def ninja():
	if "total_gold" not in session:
		session['total_gold'] = 0

	# if 'activ' not in session:
	if "activity" not in session:
		session['activity'] = ""

	return render_template("index.html")

@app.route('/process_money', methods=["POST", "GET"])
def process_gold():
	localtime = time.asctime( time.localtime(time.time()) )
	if request.form['building'] == 'farm':
		#get a random number to determine how much gold is earned
		gold = random.randint(10,20)

		#add gold to the total gold
		session['total_gold'] += gold
		
		#add the new activity to the list
		activ = "<p style='color:green'>Earned " + str(gold) + " golds from the " + request.form['building'] + "! (" +localtime + ")</p>"
		session['activity'] = activ + session['activity']

	elif request.form['building'] == 'cave':
		#get a random number to determine how much gold is earned
		gold = random.randint(5,10)
		
		#add gold to the total gold
		session['total_gold'] += gold

		#add the new activity to the list
		activ = "<p style='color:green'>Earned " + str(gold) + " golds from the " + request.form['building'] + "! (" +localtime + ")</p>"
		session['activity'] = activ + session['activity']

	elif request.form['building'] == 'house':
		#get a random number to determine how much gold is earned
		gold = random.randint(2,5)
		
		#add gold to the total gold
		session['total_gold'] += gold

		#add the new activity to the list
		activ = "<p style='color:green'>Earned " + str(gold) + " golds from the " + request.form['building'] + "! (" +localtime + ")</p>"
		session['activity'] = activ + session['activity']

	elif request.form['building'] == 'casino':
		#get a random number to determine how much gold is earned or lost
		gold = random.randint(-50,50)
		
		#add gold to the total gold
		session['total_gold'] += gold
		
		#add the new activity to the list
		if gold >= 0:
			activ = "<p style='color:green'>Earned " + str(gold) + " from the " + request.form['building'] + "! (" +localtime + ")</p>"
		else:
			activ = "<p style='color:red'>Entered a casino and lost " + str(abs(gold)) + " golds....Ouch. (" +localtime + ")</p>"
		session['activity'] = activ + session['activity']

	return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    

