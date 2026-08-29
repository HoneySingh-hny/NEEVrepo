def Risk_Calculator(data):
    # Default risk
    risk = "Low"
    bmi=data["BMI"]
    glucose=data["Blood_Glucose"]
    hba1c=data["HbA1c"]

    # High risk conditions
    if bmi >= 30 or glucose >= 140 or hba1c >= 6.5:
        risk = "High"
    # Moderate risk conditions
    elif bmi >= 25 or glucose >= 120 or hba1c >= 5.7:
        risk = "Moderate"
    # Otherwise remains Low
    return risk