import pandas as pd
import os
from risk_calculator import Risk_Calculator

CSV_FILE = "_2.csv"

def read_doc():
    try:
        df = pd.read_csv(CSV_FILE)
        return df
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def avg_age_calculator():
    data=read_doc()
    #learned this from ai  how to find average inpandes just k
    avg_age = data.groupby("Risk_Level")["Age"].mean().to_dict()
    return avg_age


def write_doc(data):
    """Append new entry to cohort CSV"""
    new_data = {
        "userid":data["userid"],
        "Age": data["Age"],
        "bmi": data["bmi"],
        "glucose": data["glucose"],
        "hba1c": data["hba1c"],
        "Risk_Level": data["Risk_Level"]
    }

    # If file exists, append; else create new
    df=read_doc()
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    df.to_csv(CSV_FILE, index=False)
    return df
