from flask import Flask, send_from_directory, request
import random
import json, os

app = Flask(__name__, static_url_path='/../../client/public')

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('../../client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../../client/public', path)

# Tests Python Flask connection
@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

# Tests Python Flask Svelte connection
@app.route("/randData")
def randData():
    print('randData')
    params = request.args.get('params')
    randomNumber = random.randint(0, 100)

    data = json.dumps({
        "randomNumber": str(randomNumber), 
        "params": str(int(params)), 
        "sumRandomParams": str(randomNumber + int(params))
        })
    
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
