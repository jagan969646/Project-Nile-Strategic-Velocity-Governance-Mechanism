def org_recommendation(span_ratio):
    if span_ratio < 6:
        return "High Bureaucracy Risk — Consider Reducing Manager Layers"
    elif span_ratio < 10:
        return "Moderate Efficiency — Monitor Departments"
    else:
        return "Healthy Org Structure"


def ai_recommendation(utilization, fcf):
    if utilization < 60 and fcf < 0:
        return "AI Spend Risky — Reduce CapEx or Increase Adoption"
    elif utilization < 75:
        return "AI Adoption Moderate — Improve Customer Usage"
    else:
        return "AI Investment Healthy"


def compliance_recommendation(price_delta):
    if price_delta < -5:
        return "High Legal Risk — Amazon Undercutting Sellers"
    elif price_delta < 0:
        return "Moderate Compliance Risk"
    else:
        return "Low Risk — Fair Competition"