from ast import main
from crypt import methods
from re import template
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pickle

app = Flask(__name__)

model = pickle.load(open("/Users/mohand/Desktop/University/CSC 462 /Project/test2/pik.pkl", "rb"))

@app.route('/')
def root():
    return render_template("index2.html")

@app.route('/submit', methods=["POST", "GET"])
def submit():
    
    CType = request.form['CType']
    TravelType = request.form['TravelType']
    Class = request.form.get('Class')
    Flightdistance = request.form['Flightdistance']
    inflightWifi = request.form['inflightWifi']
    DAtime = request.form['DAtime']
    EaseBooking = request.form['EaseBooking']
    GLocation = request.form['GLocation']
    FoodDrink = request.form['FoodDrink']
    OnlineBoarding = request.form['OnlineBoarding']
    Seat = request.form['Seat']
    Inflightentertainment = request.form['Inflightentertainment']
    OnBoardservice = request.form['OnBoardservice']
    LegRoom = request.form['LegRoom']
    Baggage = request.form['Baggage']
    Checkin = request.form['Checkin']
    Inflightservice = request.form['Inflightservice']
    Cleanliness = request.form['Cleanliness']
    DepartureDelay = request.form['DepartureDelay']
    ArrivalDelay = request.form['ArrivalDelay']
   
    print(CType)
    print(TravelType)
    print(Class)
    CType = 0 if CType == 'Loyal customer' else 1
    TravelType = 0 if TravelType == "Business travel" else 1
    if Class == "Eco":
        Class = 1
    elif Class == "Business":
        Class = 0
    else:
        Class = 2
        
    mod = model.predict([[CType, TravelType, Class, Flightdistance, inflightWifi,
                        DAtime, EaseBooking, GLocation, FoodDrink,  OnlineBoarding,
                        Seat, Inflightentertainment, OnBoardservice, LegRoom, 
                        Baggage, Checkin, Inflightservice, Cleanliness, DepartureDelay, ArrivalDelay]])
    mod = "satisfied" if mod[0] == 1 else "neutral or dissatisfied"
    return render_template("result.html", result = " {}".format(mod)) 



if __name__ == "__main__":
    app.run(debug=True)
