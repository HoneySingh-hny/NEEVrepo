import streamlit as st
def Input_Handler():
    # User inputs
    Patient_id=st.number_input("Enter your userid")
    Age = st.slider("Enter your age", min_value=1, max_value=120,value=5)
    Gender=st.text_input("Enter your gender")
    Country =st.text_input("Enter your country")
    Height_cm = st.slider("Enter your height in cm", min_value=0, max_value=300,value=170)
    Weight_kg = st.slider("Enter your weight in kg", min_value=0, max_value=500,value=50)
    bmi = Weight_kg/(Height_cm*Height_cm)
    Waist_Circumference =st.slider("Enter your waist size",min_value=0,max_value=150,value=103)
    Blood_Glucose = st.slider("Enter your Blood Glucose (mg/dL)", min_value=50, max_value=300,value=60)
    HbA1c = st.slider("Enter your HbA1c (%)", min_value=4.0, max_value=15.0,value=5.0)
    if st.button("Submit"):
        return {
            "Patient_id":Patient_id,
            "Age": Age,
            "Gender":Gender,
            "Countery":Country,
            "Height_cm":Height_cm,
            "Weight_kg":Weight_kg,
            "BMI": bmi,
            "Waist_Circumference":Waist_Circumference,
            "Blood_Glucose": Blood_Glucose,
            "Hb1Ac": HbA1c
        }
    else:
        return None
