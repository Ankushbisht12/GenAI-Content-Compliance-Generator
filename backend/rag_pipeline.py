import json
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

# -------------------------------
# CONFIG
# -------------------------------
BASE_DIR = Path(__file__).parent.parent
POLICY_PATH = BASE_DIR / "data" / "policies" / "policies.json"

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

_vectorstore = None


# -------------------------------
# LOAD POLICIES FROM JSON
# -------------------------------
def load_policies():
    with open(POLICY_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    for policy in data:
        documents.append(
            Document(
                page_content=policy["rule"],
                metadata={
                    "policy_id": f"LAW_{policy['id']}",
                    "law_or_policy": policy["law_or_policy"],
                    "jurisdiction": policy["jurisdiction"],
                    "platform": policy["platform"],
                    "content_type": policy["content_type"],
                    "risk": policy["risk"]
                }
            )
        )

    return documents


# -------------------------------
# VECTOR STORE
# -------------------------------
def create_or_load_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        docs = load_policies()
        _vectorstore = FAISS.from_documents(docs, embeddings)
    return _vectorstore


# -------------------------------
# RETRIEVE POLICIES
# -------------------------------
def retrieve_policies(query: str, k: int = 8):
    """
    Retrieves relevant policies based on semantic similarity.
    k is intentionally higher to avoid 'always 3 policies' issue.
    """
    vectorstore = create_or_load_vectorstore()
    return vectorstore.similarity_search(query, k=k)
