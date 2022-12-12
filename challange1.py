import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

with st.sidebar:
    selected = option_menu(' Disease Prediction System with Multiple Models',

                           [ 'SVC', 'KNN', 'RandomForest'],
                           icons=['activity', 'neighbors', 'person'],
                           default_index=0)
name = st.text_input("Name")
Fo = st.text_input("MDVP:Fo(Hz)")
Fhi = st.text_input("MDVP:Fhi(Hz)")
Flo = st.text_input("MDVP:Flo(Hz)")
Jitter1 = st.text_input("MDVP:Jitter(%)")
Jitter2 = st.text_input("MDVP:Jitter(Abs)")
RAP = st.text_input("MDVP:RAP")
PPQ = st.text_input("MDVP:PPQ")
DDP = st.text_input("Jitter:DDP")
Shimmer = st.text_input("MDVP:Shimmer")
ShimmerdB1 = st.text_input("MDVP:Shimmer(dB)")
APQ3 = st.text_input("Shimmer:APQ3")
APQ5 = st.text_input("Shimmer:APQ5")
APQ = st.text_input("MDVP:APQ")
DDA = st.text_input("Shimmer:DDA")
NHR = st.text_input("NHR")
HNR = st.text_input("HNR")
RPDE = st.text_input("RPDE")
DFA = st.text_input("DFA")
spread1 = st.text_input("spread1")
spread2 = st.text_input("spread2")
D2 = st.text_input("D2")
PPE = st.text_input("PPE")


def prediction(input_data,loaded_model):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return 'The person is not affected by Parkinson'
    else:
        return 'The person is affected Parkinson'

if (selected=='SVC'):
    filename="SVC.sav"
    data=pickle.load(open(filename,"rb"))
    final_Prediction = ''
    if st.button("Parkinson Prediction Result using SVC"):
        final_Prediction = prediction([Fo,Fhi,Flo,Jitter1,Jitter2,RAP,PPQ,DDP,Shimmer,ShimmerdB1,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE],data)
    st.success(final_Prediction)

if (selected == 'KNN'):

    filename = "KNN.sav"
    data = pickle.load(open(filename, "rb"))
    final_Prediction = ''
    if st.button("Parkinson Prediction Result using KNN"):
        final_Prediction = prediction([Fo,Fhi,Flo,Jitter1,Jitter2,RAP,PPQ,DDP,Shimmer,ShimmerdB1,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE], data)
    st.success(final_Prediction)
if (selected == 'RandomForest'):
    filename = "Random.sav"
    data = pickle.load(open(filename, "rb"))
    final_Prediction = ''
    if st.button("Parkinson Prediction Result using Random Forest"):
        final_Prediction = prediction([Fo,Fhi,Flo,Jitter1,Jitter2,RAP,PPQ,DDP,Shimmer,ShimmerdB1,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE], data)
    st.success(final_Prediction)