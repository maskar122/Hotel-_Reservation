#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:55:22 2023

@author: elsayed
"""
#Import Liberaries
import numpy as np
from flask import Flask, request, jsonify, render_template
import   pickle
import pandas as pd

#Define App
app = Flask(__name__, template_folder='templates')
#an object of class Flask which would do all the heavy lifting for us, like handling the incoming requests from the browser 
# and providing with appropriate responses (in this case our model prediction) in some nice form using html,css. 

#load Model
model = pickle.load(open(r'C:/Users/LAP-STORE/Desktop/Amit/Hotel/SaveModels/model.pkl',"rb"))




input_names=['no_of_adults', 'no_of_children', 'no_of_weekend_nights',
       'no_of_week_nights', 'type_of_meal_plan', 'required_car_parking_space',
       'room_type_reserved', 'lead_time', 'arrival_year', 'arrival_month',
       'arrival_date', 'market_segment_type', 'repeated_guest',
       'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled',
       'avg_price_per_room', 'no_of_special_requests']

room_type_reserved=['Room_Type 4','Room_Type 5','Room_Type 7']
market_segment_type=['Aviation','Complementary']

cat_features=['type_of_meal_plan','room_type_reserved','market_segment_type']



    

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features=[]
    for col in input_names:
            
        value=request.form.get(col)
        if col in cat_features:
            if col in cat_features:
                le=pickle.load(open(r'C:\Users\LAP-STORE\Desktop\Amit\Hotel\SaveModels\market_segment_type_le.pkl'.format(col),'rb'))
    
                features.append(le.transform(np.array([[value]])))
            else:  
                features.append(float(value))
                    
        else:  
            features.append(float(value))
    
    X=np.array(features).reshape(1,17)
    pred=model.predict(X)
    output=""
    
    if pred == 1:
        output="The Customer May Confirm Reservation"
    else:
        output="The Customer May Cancel  Reservation"
            
    return render_template('result.html', prediction_text='{} '.format(output))



if __name__ == "__main__":
    app.run(debug=True)
