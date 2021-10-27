# imports
from flask import Flask, jsonify, request, render_template, redirect

# create instance of Flask app
app = Flask(__name__)

# Use flask to set up db connection

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

# Test route
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200


if __name__ == "__main__":
    app.run(debug=True)