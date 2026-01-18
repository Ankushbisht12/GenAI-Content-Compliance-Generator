# 🛡️ GenAI-Powered Content Compliance Generator  
### Policy-Aware Content Validation & Generation using RAG + LLaMA-3 (Local)

A full-stack **AI content compliance system** that analyzes user-generated text against **real-world laws, regulations, and platform policies**, then safely rewrites or blocks content when required.

This project uses **Retrieval-Augmented Generation (RAG)** with a **local LLaMA-3 model via Ollama**, ensuring **privacy, zero API cost, and offline capability**.

---

## 🚀 Key Features

✅ Policy-aware content validation  
✅ Real-world laws & platform rules (GDPR, IT Act, YouTube, WHO, Meta, etc.)  
✅ Local **LLaMA-3** (no OpenAI / paid APIs)  
✅ Retrieval-Augmented Generation (FAISS + Embeddings)  
✅ Intelligent refusal for illegal or harmful requests  
✅ Neutral content passes without unnecessary policy flags  
✅ Interactive analytics dashboard  
✅ Modern UI with background image, logo & dark/light mode  
✅ Privacy-first & offline-capable  

---

## 🧠 System Architecture
-User Input
-↓
-Streamlit Frontend
-↓
-FastAPI Backend
-↓
-RAG Pipeline (FAISS + Embeddings)
-↓
-Relevant Laws & Policies Retrieved
-↓
-LLaMA-3 (Local via Ollama)
-↓
-Compliant Content + Applied Policies
-↓
-Analytics Dashboard

---

## 🖥️ Tech Stack

### 🔹 Backend
- **FastAPI**
- **LangChain**
- **FAISS** (Vector Store)
- **Sentence-Transformers** (Embeddings)
- **Ollama (LLaMA-3 local)**

### 🔹 Frontend
- **Streamlit**
- **Matplotlib**
- **Pandas**
- **Custom CSS**
- Local images (background & logo)

## 📁 Project Structure

GenAI-Content-Compliance-Generator/
│
├── backend/
│ ├── api.py
│ ├── compliance_checker.py
│ ├── rag_pipeline.py
│
├── frontend/
│ ├── app.py
│ └── assets/
│ ├── bg.png
│ └── logo.png
│
├── data/
│ └── policies/
│ └── policies.json
│
├── requirements.txt
├── README.md
├── .gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/GenAI-Content-Compliance-Generator.git
cd GenAI-Content-Compliance-Generator

### 2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Install & Run Ollama (LLaMA-3)
Download Ollama:
👉 https://ollama.com
Pull model:
ollama pull llama3
Run:
ollama run llama3

---

### ▶️ Run the Application
🔹 Start Backend (FastAPI)
python -m uvicorn backend.api:app --reload

Runs at:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

🔹 Start Frontend (Streamlit)
streamlit run frontend/app.py

Runs at:
http://localhost:8501

### 📊 Analytics Dashboard
The frontend automatically visualizes:
📕 Most Triggered Policies
⚠️ Risk Distribution
🌍 Platform-wise Issues
Charts dynamically update based on actual retrieved policies, not fixed values.

### 🧪 Example Use Cases
Input	Result
Ethical LinkedIn post	Allowed, no violations
Anti-vaccine captions	Blocked + health policies
Religious hate content	Blocked + hate speech laws
Ongoing court trial article	Neutral rewrite + media ethics

### 🎯 Use Cases
Academic projects & research
Media compliance systems
Social media moderation tools
Legal-tech prototypes
AI governance demonstrations

### 🔐 Privacy & Ethics
✅ No user data stored
✅ No cloud APIs used
✅ Fully local inference
✅ Transparent policy application

