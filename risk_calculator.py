def Risk_Calculator(data):
    # Default risk
    risk = "Low"
    bmi=data["bmi"]
    glucose=data["glucose"]
    hba1c=data["hba1c"]

    # High risk conditions
    if bmi >= 30 or glucose >= 140 or hba1c >= 6.5:
        risk = "High"
    # Moderate risk conditions
    elif bmi >= 25 or glucose >= 120 or hba1c >= 5.7:
        risk = "Moderate"
    # Otherwise remains Low
    return risk