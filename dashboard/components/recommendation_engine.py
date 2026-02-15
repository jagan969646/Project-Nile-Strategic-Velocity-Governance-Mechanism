def get_strategic_advice(span, bureaucracy_tax, ai_yield):
    recommendations = []
    
    # 1. Organizational Recommendation
    if span < 10:
        recommendations.append({
            "principle": "Frugality",
            "impact": "CRITICAL",
            "action": "Freeze all L5-L7 management backfills.",
            "rationale": f"Current span ({span}:1) is below S-Team mandate. Increasing to 10:1 would reduce OpEx by estimated 12%."
        })
    
    # 2. Bureaucracy Tax Recommendation
    if bureaucracy_tax > 15:
        recommendations.append({
            "principle": "Bias for Action",
            "impact": "HIGH",
            "action": "De-layer 'Approval Chains' in Retail & Ops.",
            "rationale": "Bureaucracy Tax exceeds 15% threshold. Decision latency is currently impacting Q4 delivery speed."
        })

    # 3. AI CapEx Recommendation
    if ai_yield < 1.2:
        recommendations.append({
            "principle": "Insist on the Highest Standards",
            "action": "Pivot H100 clusters from 'Training' to 'Inference'.",
            "rationale": "Revenue yield per unit is sub-optimal. Inference-ready models show 40% higher immediate FCF return."
        })
        
    return recommendations