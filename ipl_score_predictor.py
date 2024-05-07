#import the libraries

import math
import numpy as np
import pickle
import streamlit as st

#Page config 
st.set_page_config(page_title='IPL_Score_Predictor',layout="centered")

#Loading the ML model
filename='TrainedModel.pkl'
model = pickle.load(open(filename,'rb'))    # store model in read binary mode

#Title of the page with CSS
st.markdown("<h1 style='text-align: center; color: white;'> IPL Score Predictor 2024 </h1>", unsafe_allow_html=True)

#Add background image
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/realistic-soccer-football-stadium-illustration_52683-60377.jpg?w=1380&t=st=1713330590~exp=1713331190~hmac=a999dbd19a7a5be33557fd49e7c49a9f2ea12a1d20ebc249102c0b0b83f15315");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# SELECT THE BATTING TEAM
st.markdown("<h3 style='text-align: center; color: white;'> Batting Team </h3>", unsafe_allow_html=True)
batting_team= st.selectbox('Select the Batting Team ',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))

prediction_array = []

# Batting Team
if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif batting_team == 'Delhi Daredevils':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif batting_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]

#SELECT BOWLING TEAM
st.markdown("<h3 style='text-align: center; color: white;'> Bowling Team </h3>", unsafe_allow_html=True)
bowling_team = st.selectbox('Select the Bowling Team ',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))
if bowling_team==batting_team:
    st.error('Bowling and Batting teams should be different')
# Bowling Team
if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
elif bowling_team == 'Delhi Daredevils':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
elif bowling_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]

col1, col2 = st.columns(2)

#Enter the Current Ongoing Over
with col1:
    st.markdown("<h6 style='color: white;'> Enter current Over </h6>", unsafe_allow_html=True)
    overs = st.number_input(',',min_value=5.1,max_value=19.5,value=5.1,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')
with col2:
    st.markdown("<h6 style='color: white;'> Enter Current Runs </h6>", unsafe_allow_html=True)
    #Enter Current Run
    runs = st.number_input('.,',min_value=0,max_value=354,step=1,format='%i')

#Wickets Taken till now
st.markdown("<h6 style='color: white;'> Wickets taken till now </h6>", unsafe_allow_html=True)
wickets =st.slider('/',0,9)
wickets=int(wickets)

col3, col4 = st.columns(2)

with col3:
    #Runs in last 5 over
    st.markdown("<h6 style='color: white;'> Runs scored in the last 5 overs </h6>", unsafe_allow_html=True)
    runs_in_prev_5 = st.number_input('',min_value=0,max_value=runs,step=1,format='%i')

with col4:
    #Wickets in last 5 over
    st.markdown("<h6 style='color: white;'> Wickets taken in the last 5 overs </h6>", unsafe_allow_html=True)
    wickets_in_prev_5 = st.number_input('.',min_value=0,max_value=wickets,step=1,format='%i')

#Get all the data for predicting
prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5,wickets_in_prev_5]
prediction_array = np.array([prediction_array])     # Convert array to numpy array
predict = model.predict(prediction_array)           # Pass it to our model as input

if st.button('Predict Score'):
    #Call the ML Model
    my_prediction = int(round(predict[0]))          # 1st obj of the predict var will contain the ans
    #Display the predicted Score Range
    x=f'PREDICTED MATCH SCORE : {my_prediction-5} to {my_prediction+5}'
    st.success(x)

# CSS for select boxes
css = """
<style>
/* Customizing the select box options */
.selectbox-container .stSelectbox span {
    color: white; /* Change text color to white */
    font-weight: bold; /* Make text bold */
}

/* Customizing the label */
.selectbox-container .stSelectbox label {
    /* Your CSS styles for the select box label */
    color: #333 !important; /* Change the color to your desired value */
    font-weight: normal !important; /* Change the font weight if needed */
}
</style>
"""

# Display CSS
st.markdown(css, unsafe_allow_html=True)
