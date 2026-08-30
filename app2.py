import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pycountry

def main():
    st.title("Interactive Metabolic Risk Dashboard And Calculator")
    st.subheader("YOUR HEALTH, YOUR JOURNEY")
    st.markdown("""
    <style>
    .card {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 15px;
      margin: 10px;
      text-align: center;
      transition: background-color 0.3s ease;
    }
    .card:hover {
      background-color: #f0f8ff;
    }
    .hidden {
      display: none;
    }
    .card:hover .hidden {
      display: block;
      margin-top: 10px;
      color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="card">
            <h3>🍎 Nutrition</h3>
           <div class="hidden">Eating more fruits and vegetables daily lowers your risk of chronic diseases.</div>
       </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="card">
            <h3>🏃 Exercise</h3>
            <div class="hidden">Just 30 minutes of brisk walking can improve cardiovascular health and reduce stress.</div>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="card">
            <h3>😴 Sleep</h3>
            <div class="hidden">Regular sleep of 7 to 8 hours improves insulin sensitivity and boosts memory.</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown(
        "<div style='text-align:center; font-size:20px; color:#FF5733;'>💬 Small steps lead to big changes. Start today!</div>",
        unsafe_allow_html=True,
    )
    st.write("---")

    # Tabs for Global Dashboard and Personal Calculator
    tab1, tab2 = st.tabs(["Global Dashboard", "Personal Calculator"])

    with tab1:
        st.title("GLOBAL DATA")
        doc_data = read_doc()
        doc_data["Risk_Level"] = doc_data.apply(Risk_assigner, axis=1)
        avg = avg_age_calculator(doc_data)
        col1, col2 = st.columns(2)
        with col1:
            box_table(doc_data)
        with col2:
            bar_chart(avg)    
        col1, col2 = st.columns(2)
        with col1:
            hexbin_plot(doc_data)
        with col2:
            pi_chart(doc_data)

    with tab2:
        st.title("PERSONAL METABOLIC CHECK")
        data = Input_Handler()
        if data:
            risk = Risk_Calculator(data)
            st.write(f"your metabolic risk is {risk}")
            percentile = bmi_percentile(doc_data, data["BMI"])
            if percentile is not None:
                st.write(f"📊 Your BMI is higher than {percentile:.1f}% of the population")
            if risk == "High":
                st.warning("⚠️ Consult a healthcare provider. Focus on diet and exercise.")
            elif risk == "Moderate":
                st.info("💡 Increase physical activity and monitor glucose regularly.")
            else:
                st.success("✅ Maintain your current lifestyle and keep monitoring.")
            write_doc(data)
        else:
            st.info("Fill the form and click Submit")

def read_doc():
    try:
        df = pd.read_csv("_2.csv")
        # Median imputation for required columns
        for col in ["Height_cm", "Weight_kg", "Blood_Glucose", "HbA1c"]:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].median())
        return df
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def avg_age_calculator(data):
    avg_age = data.groupby("Risk_Level")["Age"].mean().to_dict()
    return avg_age

def write_doc(data):
    new_data = {
        "Patient_ID": data["Patient_ID"],
        "Age": data["Age"],
        "Gender": data["Gender"],
        "Country": data["Country"],
        "Height_cm": data["Height_cm"],
        "Weight_kg": data["Weight_kg"],
        "BMI": data["BMI"],
        "Waist_Circumference_cm": data["Waist_Circumference_cm"],
        "Blood_Glucose": data["Blood_Glucose"],
        "HbA1c": data["HbA1c"]
    }
    df = read_doc()
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("_2.csv", index=False)
    return df

def Input_Handler():
    Patient_ID = st.number_input("Enter your userid")
    Age = st.slider("Enter your age", min_value=1, max_value=120, value=5)
    Gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    countries = [c.name for c in pycountry.countries]
    Country = st.selectbox("Select your country", countries)
    Height_cm = st.slider("Enter your height in cm", min_value=0, max_value=300, value=170)
    Weight_kg = st.slider("Enter your weight in kg", min_value=0, max_value=500, value=50)
    bmi = (Weight_kg*100) / (Height_cm * Height_cm)
    Waist_Circumference_cm = st.slider("Enter your waist size", min_value=0, max_value=150, value=103)
    Blood_Glucose = st.slider("Enter your Blood Glucose (mg/dL)", min_value=50, max_value=300, value=60)
    HbA1c = st.slider("Enter your HbA1c (%)", min_value=4.0, max_value=15.0, value=5.0)
    if st.button("Submit"):
        return {
            "Patient_ID": Patient_ID,
            "Age": Age,
            "Gender": Gender,
            "Country": Country,
            "Height_cm": Height_cm,
            "Weight_kg": Weight_kg,
            "BMI": bmi,
            "Waist_Circumference_cm": Waist_Circumference_cm,
            "Blood_Glucose": Blood_Glucose,
            "HbA1c": HbA1c
        }
    else:
        return None

def Risk_assigner(row):
    if row["HbA1c"] >= 6.5 or row["Blood_Glucose"] >= 140 or row["BMI"] >= 30:
        return "High Risk"
    elif row["HbA1c"] >= 5.7 or row["Blood_Glucose"] >= 100 or row["BMI"] >= 25:
        return "Moderate Risk"
    else:
        return "Low Risk"

def Risk_Calculator(data):
    bmi = data["BMI"]
    glucose = data["Blood_Glucose"]
    hba1c = data["HbA1c"]
    if bmi >= 30 or glucose >= 140 or hba1c >= 6.5:
         return "High"
    elif bmi >= 25 or glucose >= 120 or hba1c >= 5.7:
        return "Moderate"
    else:
        return "Low"

def bmi_percentile(data, bmi):
    try:
        return (data["BMI"] < bmi).mean() * 100
    except Exception:
        return None

def hexbin_plot(data):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.hexbin(data["BMI"], data["Blood_Glucose"], gridsize=40, cmap="Set1")
    ax.set_title("BMI vs Blood Glucose (Hexbin)")
    ax.set_xlabel("BMI")
    ax.set_ylabel("Blood Glucose")
    st.pyplot(fig)

def pi_chart(data):
    sizes = data["Risk_Level"].value_counts()
    labels = sizes.index
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Risk Level Distribution")
    st.pyplot(fig)

def bar_chart(data):
    fig, ax = plt.subplots()
    Labels = list(data.keys())
    values = list(data.values())
    sns.barplot(x=Labels, y=values, hue=Labels, palette="Set1", legend=False, ax=ax)
    ax.set_title("Average Age per Risk Level")
    ax.set_xlabel("Risk Level")
    ax.set_ylabel("Average Age")
    st.pyplot(fig)

def box_table(data):
    fig, ax = plt.subplots()
    sns.boxenplot(data=data, x="HbA1c", y="Risk_Level", hue="Risk_Level", palette="Set1", ax=ax)
    ax.set_title("HbA1c vs Risk_Level")
    ax.set_xlabel("HbA1c")
    ax.set_ylabel("Risk_Level")
    st.pyplot(fig)

if __name__ == "_main_":
    main()