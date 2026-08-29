import streamlit as st
def Input_Handler():
    # User inputs
    userid=st.number_input("Enter your userid")
    age = st.slider("Enter your age", min_value=1, max_value=120,value=5)
    height = st.slider("Enter your height in cm", min_value=0, max_value=400,value=170)
    weight = st.slider("Enter your weight in kg", min_value=0, max_value=400,value=50.0)
    bmi = weight/(height*height)
    glucose = st.slider("Enter your Blood Glucose (mg/dL)", min_value=50, max_value=300,value=60)
    hba1c = st.slider("Enter your HbA1c (%)", min_value=4.0, max_value=15.0,value=5.0)
    if st.button("Submit"):
        return {
            "userid": userid,
            "Age": age,
            "bmi": bmi,
            "glucose": glucose,
            "hba1c": hba1c
        }
    else:
        return None
