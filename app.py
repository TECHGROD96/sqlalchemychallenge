# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.automap import automap_base

app=Flask(__name__)




#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base=automap_base()
Base.prepare(engine,reflect=True)

Station=Base.classes.station
Measurements=Base.classes.measurement
# reflect the tables
session=Session(engine)


# Create our session (link) from Python to the DB
session=Session(engine)


#################################################
# Flask Setup
#################################################

Station=Base.classes.station 
Measurements=Base.classes.measurements

session_factory=sessionmaker(bind=engine)
session=scoped_session(session_factory)

@app.teardown_appcontext
def remove_session(exception=None):

#################################################
# Flask Routes
#################################################
