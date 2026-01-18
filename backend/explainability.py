def generate_explanation(policies):
    explanation = []
    for p in policies:
        explanation.append({
            "policy_id": p.metadata["policy_id"],
            "risk": p.metadata["risk"],
            "rule_applied": p.page_content
        })
    return explanation
