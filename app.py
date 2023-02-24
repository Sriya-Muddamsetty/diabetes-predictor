import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

model = pickle.load(open('svm.pkl','rb'))
df = pd.read_csv('diabetes.csv')

st.title('DIABETES PREDICTION')
#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
age = st.text_input("Enter your Age")
pregnancies = st.text_input("Enter number of Pregnancies you have gone through")
glucose = st.text_input("Enter the Glucose Level")
bloodpressure = st.text_input("Enter the Blood Pressure Level")
skinthickness = st.text_input("Enter Skin Thickness value")
insulin = st.text_input("Enter Insulin level")
bmi = st.text_input("Enter the Body Mass Index")
dpf = st.text_input("Enter the Diabetes Pedigree Function")

result = 0
if st.button("Result"):
    input = pd.DataFrame([[pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,dpf,age]],columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
    result = model.predict(input)

    if result == 0:
        st.success("You are not Diabetic")
    else:
        st.success("You are Diabetic")
