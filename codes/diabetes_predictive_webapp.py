# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 05:19:40 2023

@author: Anuruddha
"""

import pickle
import numpy as np
import streamlit as st

# save model file named as trainned_model.sav
filename='C:\\Users\\Anuruddha\\Desktop\\ML_projects\\2.Diabetes_Prediction\\codes\\trainned_model.sav'

# load the saved file

loaded_model = pickle.load(open(filename,'rb')) # read  as binary file


# creating a function for prediction

def diabetes_prediction(input_data):
    
    # changing the input data as numpy array

    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the data

    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

    # standarized the input data

    #std_data = scaler.transform(input_data_reshape)

    prediction  = loaded_model.predict(input_data_reshape)


    if prediction[0] == 0:
        return 'The persion is not diabetes'
    else:
        return 'The persion is diabetes'


def main():
    
    # givin a title
    st.title('Diabatis Prediction Web App')
    
    # getting the input dat from the user

    Pregnancies =  st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age Of The Person')
    
    # code for Prediction
    
    diagonsis = ''
    
    # create a button for prediction
    
    # if button is press
    if st.button("Diabetis Test Result"):
        diagonsis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    
    st.sucess(diagonsis) # give the output
    
    
if __name__ =='__main__':
    main()    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
    