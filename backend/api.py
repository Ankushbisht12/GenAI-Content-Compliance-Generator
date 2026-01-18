from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.compliance_checker import generate_compliant_content

app = FastAPI(title="GenAI Content Compliance API")

# -------------------------------
# REQUEST / RESPONSE MODELS
# -------------------------------
class ContentRequest(BaseModel):
    prompt: str


class ContentResponse(BaseModel):
    compliant_content: str
    applied_policies: list


# -------------------------------
# API ENDPOINT
# -------------------------------
@app.post("/generate", response_model=ContentResponse)
def generate_content(request: ContentRequest):
    try:
        content, policies = generate_compliant_content(request.prompt)

        # ✅ ALWAYS return policies if they exist
        applied_policies = []

        for p in policies:
            applied_policies.append({
                "policy_id": p.metadata.get("policy_id", "UNKNOWN"),
                "platform": p.metadata.get("platform", "N/A"),
                "risk": p.metadata.get("risk", "N/A"),
                "rule": p.page_content
            })

        return {
            "compliant_content": content,
            "applied_policies": applied_policies
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
