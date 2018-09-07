from flask import Flask 
app = Flask(__name__)  


print(__name__)          # Just for fun, print __name__ to see what it is
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.

# if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module

@app.route('/dojo') 
def Dojo():
	return "Dojo!"


@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    
    return "Hi "+ name.capitalize()


@app.route('/repeat/<number>/<words>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(number, words):
    return words * int(number)


if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.