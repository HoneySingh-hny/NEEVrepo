import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from csvHandler import read_doc
def scatter_table(data):
    fig, ax = plt.subplots()

    # Scatter plot of BMI vs Glucose, colored by Risk_Level
    sns.scatterplot(data=data, x="bmi", y="glucose", hue="Risk_Level", palette="Set1", ax=ax)

    ax.set_title("BMI vs Blood Glucose")
    ax.set_xlabel("BMI")
    ax.set_ylabel("Blood Glucose")

    st.pyplot(fig)
def pi_chart(data):
    sizes = data["Risk_Level"].value_counts()
    labels = sizes.index

    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Risk Level Distribution")

    st.pyplot(fig) 
def bar_chart(data):
    fig, ax = plt.subplots()
    Labels = list(data.keys())
    values = list(data.values())
    sns.barplot(data=data, x=Labels, y=values, palette="Set1", ax=ax)

    ax.set_title("Average Age per Risk Level")
    ax.set_xlabel("Risk Level")
    ax.set_ylabel("Average Age")

    st.pyplot(fig)
def box_table(data):
    fig, ax = plt.subplots()

    # Scatter plot of BMI vs Glucose, colored by Risk_Level
    sns.boxenplot(data=data, x="hba1c", y="Risk_Level", hue="Risk_Level", palette="Set1", ax=ax)

    ax.set_title("hbA1c vs Risk_Level")
    ax.set_xlabel("hbA1c")
    ax.set_ylabel("Risk_Level")

    st.pyplot(fig)