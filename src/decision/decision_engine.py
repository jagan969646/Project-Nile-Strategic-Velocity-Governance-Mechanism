def hiring_decision(span_of_control):
    if span_of_control > 12:
        return "Hire Managers"
    elif span_of_control < 6:
        return "Overstaffed"
    else:
        return "Optimal"

def ai_spend_decision(roi):
    if roi < 0:
        return "Reduce AI Spend"
    elif roi < 0.15:
        return "Optimize AI Usage"
    else:
        return "Increase AI Investment"

def compliance_decision(risk_score):
    if risk_score > 70:
        return "Immediate Audit Needed"
    elif risk_score > 40:
        return "Monitor Closely"
    else:
        return "Low Risk"