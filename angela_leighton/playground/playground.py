from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')

def playground():
	return render_template("index.html", color="purple", num=8)
	
@app.route('/play/<num_of_blox>')
def blox(num_of_blox):
	return render_template("index.html", num=int(num_of_blox))

@app.route('/play/<num_of_blox>/<color_of_blox>')
def bloxnumcolor(num_of_blox, color_of_blox):	
	return render_template("index.html", num=int(num_of_blox), color=color_of_blox)

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
