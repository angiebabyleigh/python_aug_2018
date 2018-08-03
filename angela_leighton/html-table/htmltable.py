from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

users = (
	{'first_name' : 'Michael', 'last_name' : 'Choi'},
	{'first_name' : 'John', 'last_name' : 'Supsupin'},
	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'}
);


@app.route('/')
def table():
	print(users)
	return render_template("index.html", students=users)


if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
