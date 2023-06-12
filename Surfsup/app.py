# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import timedelta, datetime
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    """List all the available routes."""
    return (
        f"Available Routes:<br/>"
        f"&nbsp<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precip_analysis():
    """Gather precipitation data from the most recent date to 12 months prior"""
    
    # Find the most recent date in the data set.
    most_recent_date = session.query(func.max(measurement.date)).scalar()
    
    # Convert scalar latest date to datetime object
    most_recent_date_dt = datetime.strptime(most_recent_date, '%Y-%m-%d')
    
    # Calculate the date one year from the last date in data set.
    one_year_prior = most_recent_date_dt - timedelta(days=365)

    # Perform a query to retrieve the date and precipitation scores
    precip_scores = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date.between(one_year_prior, most_recent_date_dt)).all()
    # convert above query to that yields date and precipitation data to a dictionary with 
    # date as key and precipitation as value
    precip_scores_dict = {t[0]: t[1] for t in precip_scores}

    return jsonify(precip_scores_dict)

@app.route("/api/v1.0/stations")
def station_list():
    """Display a list of stations from the dataset"""
    # query a list of station IDs from the dataset
    list_of_stations = session.query(station.station).all()
    # iterate over the above query result in order to return a readable format for the jsonify function
    stations = [result.station for result in list_of_stations]

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temp_data():
    """Query the temperature observations from the most active station"""
    #Query the measurment table for temperature data for only the most active station that was identified in testing.
    most_active_station = session.query(measurement.station, measurement.date, measurement.tobs).\
        filter(measurement.station == "USC00519281").all()
    
     # iterate over the above query result in order to return a readable format for the jsonify function
    temps = [(result.station, result.date, result.tobs) for result in most_active_station]
    
    return jsonify(temps)





session.close()

if __name__ == '__main__':
    app.run(threaded=False, debug=True)