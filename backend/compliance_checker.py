from langchain_community.llms import Ollama
from backend.rag_pipeline import retrieve_policies

# -------------------------------
# LLM CONFIG
# -------------------------------
llm = Ollama(
    model="llama3",
    temperature=0.2
)

# -------------------------------
# COMPLIANCE LOGIC
# -------------------------------
def generate_compliant_content(user_prompt: str):
    """
    Steps:
    1. Retrieve relevant policies using RAG
    2. Decide if content is violating
    3. If violating -> rewrite safely
    4. If neutral -> return original content
    """

    # 1️⃣ Retrieve policies
    policies = retrieve_policies(user_prompt)

    # 2️⃣ Decide if violation exists
    violation_policies = []

    for p in policies:
        # If policy semantic relevance exists, treat as violation
        # (RAG already filtered relevance)
        violation_policies.append(p)

    # 3️⃣ If NO violations → return original content
    if not violation_policies:
        return user_prompt, []

    # 4️⃣ Build policy context
    policy_text = "\n".join(
        [
            f"- ({p.metadata['policy_id']}) {p.page_content}"
            for p in violation_policies
        ]
    )

    # 5️⃣ Ask LLM to rewrite SAFELY (not decide legality)
    prompt = f"""
You are a content compliance rewriting assistant.

The following content violates one or more legal or platform policies.

Applicable Policies:
{policy_text}

User Content:
{user_prompt}

Instructions:
- Do NOT generate illegal, harmful, or unsafe content
- Rewrite in a neutral, legal, and informative manner
- If rewriting is impossible, politely refuse with a reason
- Do NOT mention policy names or IDs in the final output

Return ONLY the final compliant content.
"""

    rewritten_content = llm.invoke(prompt)

    return rewritten_content, violation_policies
