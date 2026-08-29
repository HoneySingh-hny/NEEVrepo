import streamlit as st
from risk_calculator import Risk_Calculator
from input_handler import Input_Handler
from csvHandler import read_doc,write_doc,avg_age_calculator


def  main ():
    # st.title("GLoBAL DATA")
    # avg=avg_age_calculator()
    # st.line_chart(avg)
    # data=read_doc()
    # st.line_chart(data[["Age", "bmi"]])
     # Title
    st.title("Metabolic Risk Calculator")

    data= Input_Handler()#got a dictionary of {userid ,bmi, age, glucose, hba1c} 
    
    if data:
        risk = Risk_Calculator(data)
        data = {**data, "Risk_Level": risk}
        write_doc(data)
        avg=avg_age_calculator()
        
        st.write(f"your metabolic risk is {risk}")
        
    else:
        st.info("Fill the form and click Submit")
    

if __name__ == "__main__":
    main()
