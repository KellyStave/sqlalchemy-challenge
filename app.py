from flask import Flask, jsonify
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

#Database set-up
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
base = automap_base()
base.prepare(autoload_with=engine)
#reference to tables
base.classes.keys()
measurement = base.classes.measurement
station = base.classes.station
session = Session(engine)

#Flask set-up
app = Flask(__name__)

#Flask routes:
@app.route("/")
def home():
    return(
        f"Welcome to Hawaii<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/7.7.2014/7.7.2015<br/>"
        f"/api/v1.0/tobs<br/>"
    )
#Query Last 12 months of precipitation
@app.route('/api/v1.0/precipitation')
def precipitation(): 
    session = Session(engine)
    previous_year = dt.date(2017, 8, 23)-dt.timedelta(days = 365)
    precip = session.query(measurement.prcp, measurement.date).\
       filter(measurement.date >= previous_year).all()
    precip_rows = [{'Date': result[1], 'prcp': result[0]} for result in precip]

    session.close()
    return jsonify(precip_rows) 
if __name__ == "__main__":
    app.run(debug=True)

#Query all stations
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    activity = [measurement.station,
    func.count(measurement.station)]
    station_activity = session.query(*activity).\
        group_by(measurement.station).all()
   
        
    session.close()
    return jsonify(station_activity)
if __name__=='__main__':
    app.run(debug=True)

#Query temperatures for  12 months
@app.route('/api/v1.0/7.7.2014/7.7.2015')
def temperatures():
    year = dt.date(2015,7,7) - dt.timedelta(days=365)
    temp = session.query(measurement.tobs, measurement.date).\
        filter(measurement.station=='USC00519281').all().\
        filter(measurement.date >= year).all()
    temp_rows = [{'Date': result[1], 'tobs': result[0]} for result in temp]
        
#    session.close()
#    return jsonify(temp_rows) 
#if __name__ == "__main__":
#    app.run(debug=True)

#Query minimum, maximum and average temperature for one year beginning 7/7/2014
@app.route('/api/v1.0/tobs')
def temperature_activity():
    year = dt.date(2015,7,7) - dt.timedelta(days=365)
    temperature_activity = session.query(func.min(measurement.tobs),
        func.max(measurement.tobs),
        func.avg(measurement.tobs)).\
            filter(measurement.date >= year).all()
    session.close()
    return jsonify(temperature_activity) 
if __name__ == "__main__":
    app.run(debug=True)

    