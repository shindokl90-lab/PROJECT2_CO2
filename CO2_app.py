# imports
from flask import Flask, jsonify, request, render_template, redirect
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
# create instance of Flask app
app = Flask(__name__)

# Use flask to set up db connection
engine = create_engine("postgresql://postgres:postgres@localhost/CO2")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Table references
dirty30 = Base.classes.co2_dirty30

# Create route that renders index.html template
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/loadcharts")
def load():
    #Read data from database and pass it to template/js
    if request.method == 'GET':
        countriestotal = []
        session = Session(engine)
        countriestotal = session.query(dirty30.country, dirty30.total).all()
        session.close()
        return json.dumps([dict(r) for r in countriestotal])

@app.route("/reloadcharts")
def reload():
    #Read data from database and pass it to template/js
    if request.method == 'GET':
        countrytotal = []
        r = request.get_json()
        country = r["country"]
        session = Session(engine)
        countrytotal = session.query(dirty30.country, dirty30.total).filter(dirty30.country == country)
        session.close()
        return json.dumps([dict(r) for r in countrytotal])


if __name__ == "__main__":
    app.run(debug=True)