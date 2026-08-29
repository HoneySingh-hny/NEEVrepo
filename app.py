import streamlit as st
from risk_calculator import Risk_Calculator
from input_handler import Input_Handler
from csvHandler import read_doc,write_doc,avg_age_calculator
from table import pi_chart,bar_chart,scatter_table,box_table


def  main ():
    # st.title("GLoBAL DATA")
    # avg=avg_age_calculator()
    # st.line_chart(avg)
    # data=read_doc()
    # st.line_chart(data[["Age", "bmi"]])
     # Title
    # st.title("Metabolic Risk Calculator")

    
    doc_data=read_doc()
    scatter_table(doc_data)
    avg=avg_age_calculator()
    bar_chart(avg)
    box_table(doc_data)
    pi_chart(doc_data)
    data= Input_Handler()#got a dictionary of {userid ,bmi, age, glucose, hba1c} 
        
    if data:
        risk = Risk_Calculator(data)
        data = {**data, "Risk_Level": risk}
        write_doc(data)
        st.write(f"your metabolic risk is {risk}")
    else:
        st.info("Fill the form and click Submit")

    
    

if __name__ == "__main__":
    main()
