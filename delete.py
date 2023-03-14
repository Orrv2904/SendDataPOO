import os

from flask import Flask, render_template, request
from models import *
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    
    # flight = Flight(origin="Masaya",
    #             destination="RioSanJuan",
    #             duration=90)
    # db.session.add(flight)
    # db.session.commit()
  

    flight = db.session.query(Flight).filter_by(id=2).first()
    db.session.delete(flight)
    db.session.commit()
    

    # vuelos = Flight.query.all()
    # for flight in vuelos:
    #     print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()