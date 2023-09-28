import pandas as pd
import numpy as np
import datetime
import pickle
import streamlit as st

df = pd.read_excel('Data_Train.xlsx')
pipe = pickle.load(open('pipe.pkl','rb'))

def model():
    airline = np.sort(df['Airline'].unique())
    source = np.sort(df['Source'].unique())
    dest = np.sort(df['Destination'].unique())

    times = []
    for hours in range(0, 23):
        for minutes in range(0, 60, 5):
            times.append(datetime.time(hours, minutes))
    #dep_time = st.selectbox("Time", times, key="time", format_func=lambda t: t.strftime("%H:%M"))
    #arr_time = st.selectbox("Time1", times, key="time", format_func=lambda t: t.strftime("%H:%M"))

    #t = st.time_input('Set an alarm for', datetime.time(8, 45), step=0:15:00)
    #st.write('Alarm is set for', t)

    st.header(":airplane_departure: Airplane Ticket Price Predictor :airplane_arriving: ")
    col1, col2, col3 = st.columns(3)
    with col1:
        airline = st.selectbox('Airline', airline)
    with col2:
        source = st.selectbox("From", source)
    with col3:
        dest = st.selectbox("To", dest)

    day = st.date_input("Journey Date",datetime.date(2019,7,6))

    col4, col5 = st.columns(2)
    with col4:
        dep_time = st.selectbox("Departure Time From Source", times, key="time", format_func=lambda t: t.strftime("%H:%M"))
    with col5:
        arr_time = st.selectbox("Arrival Time To Destination", times, key="times", format_func=lambda t: t.strftime("%H:%M"))

    col6, col7, col8 = st.columns(3)
    with col6:
        stop = st.number_input('Stops',step=1, min_value=0, max_value=5)
    with col7:
        jour = st.number_input("Hour", step=1, min_value=0, max_value=47)
    with col8:
        jour1 = st.number_input("Minutes", step=5, min_value=0, max_value=55)

    jour_date = day.day
    jour_month = day.month
    dep_min = dep_time.minute
    dep_hour = dep_time.hour
    arr_min = arr_time.minute
    arr_hour = arr_time.hour

    # Predict button
    if st.button('Predict Score'):
        input_df = pd.DataFrame({'Airline': [airline], 'Source': [source],'Destination':[dest],
                             'Total_Stops': [stop],'Journey_date': [jour_date],'Journey_month': [jour_month],
                             'Dep_hour':[dep_hour], 'Dep_min':[dep_min], 'Arrival_hour':[arr_hour], 'Arrival_min':[arr_min],
                             'Duration_hours':[jour], 'Duration_mins':[jour1]})
        result = pipe.predict(input_df)
        st.header("Predicted Ticket Price :dollar: - Rs " + str(int(result[0])))

    