from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def board():
	return render_template("index.html", rows=4, cols=4)

@app.route('/<num_of_rows>/<num_of_cols>')
def rows(num_of_rows, num_of_cols):
	print(num_of_rows)
	print(num_of_cols)
	return render_template("index.html", rows=int(int(num_of_rows)/2), cols=int(int(num_of_cols)/2))

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
