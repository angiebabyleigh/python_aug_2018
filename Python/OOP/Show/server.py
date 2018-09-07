from flask import Flask, render_template
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/animals')
def show():
	mysql = connectToMySQL('animaldb')
	query = "SELECT * 	from Animal"
	result = mysql.query_db(query
	return render_template('index.html')