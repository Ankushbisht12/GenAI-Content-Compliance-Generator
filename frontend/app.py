import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import base64
from pathlib import Path

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(
    page_title="GenAI Content Compliance Generator",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/generate"

# -------------------------------
# LOAD LOCAL IMAGES
# -------------------------------
def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

BASE_DIR = Path(__file__).parent
BG_IMAGE = load_image_base64(BASE_DIR / "assets/bg.png")
LOGO_IMAGE = load_image_base64(BASE_DIR / "assets/logo.png")

# -------------------------------
# THEME TOGGLE
# -------------------------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# -------------------------------
# CUSTOM CSS (UNCHANGED)
# -------------------------------
bg_color = "#0f172a" if st.session_state.dark_mode else "#f8fafc"
text_color = "#e5e7eb" if st.session_state.dark_mode else "#0f172a"
card_bg = "#020617cc" if st.session_state.dark_mode else "#ffffffcc"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(
            rgba(0,0,0,0.6),
            rgba(0,0,0,0.6)
        ), url("data:image/png;base64,{BG_IMAGE}");
        background-size: cover;
        background-attachment: fixed;
        color: {text_color};
    }}

    .card {{
        background: {card_bg};
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }}

    textarea {{
        border-radius: 10px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# HEADER
# -------------------------------
col1, col2 = st.columns([1, 5])

with col1:
    st.image(f"data:image/png;base64,{LOGO_IMAGE}", width=120)

with col2:
    st.markdown("## 🛡️ GenAI-Powered Content Compliance Generator")
    st.markdown("### Policy-Aware Content Validation using **LLaMA-3 (Local)**")

st.button("🌗 Toggle Light / Dark Mode", on_click=toggle_theme)

st.markdown("---")

# -------------------------------
# INPUT SECTION
# -------------------------------
st.markdown("### ✍️ Enter Content")

user_input = st.text_area(
    "Write content to generate or validate",
    height=150,
    placeholder="Example: Write a LinkedIn post about ethical advertising practices."
)

# -------------------------------
# GENERATE BUTTON
# -------------------------------
if st.button("🚀 Analyze Content"):
    if not user_input.strip():
        st.warning("Please enter content first.")
    else:
        with st.spinner("Analyzing with AI + Policies..."):
            response = requests.post(
                API_URL,
                json={"prompt": user_input}
            )

        if response.status_code != 200:
            st.error("Backend error")
        else:
            data = response.json()

            # -------------------------------
            # OUTPUT
            # -------------------------------
            st.markdown("## ✅ Compliant Content")
            st.markdown(
                f"<div class='card'>{data['compliant_content']}</div>",
                unsafe_allow_html=True
            )

            st.markdown("## 📜 Applied Policies")

            policies = data.get("applied_policies", [])

            # ✅ FIX 1: Proper neutral handling
            if not policies:
                st.success("✅ No legal or policy violations detected.")
            else:
                df = pd.DataFrame(policies)

                # Safety check
                if df.empty:
                    st.success("✅ No legal or policy violations detected.")
                else:
                    st.dataframe(df, use_container_width=True)

                    # -------------------------------
                    # ANALYTICS DASHBOARD
                    # -------------------------------
                    st.markdown("---")
                    st.markdown("## 📊 Compliance Analytics Dashboard")

                    colA, colB, colC = st.columns(3)

                    # -------------------------------
                    # Most Triggered Policies
                    # -------------------------------
                    with colA:
                        st.markdown("### 📕 Most Triggered Policies")
                        law_counts = df["policy_id"].value_counts()

                        if len(law_counts) == 1:
                            st.info("Only one policy triggered for this content.")

                        st.bar_chart(law_counts)

                    # -------------------------------
                    # Risk Distribution (REAL)
                    # -------------------------------
                    with colB:
                        st.markdown("### ⚠️ Risk Distribution")
                        risk_counts = df["risk"].value_counts()

                        if len(risk_counts) == 1:
                            st.info("Single risk category detected.")
                        else:
                            fig, ax = plt.subplots()
                            ax.pie(
                                risk_counts.values,
                                labels=risk_counts.index,
                                autopct="%1.1f%%",
                                startangle=90
                            )
                            ax.axis("equal")
                            st.pyplot(fig)

                    # -------------------------------
                    # Platform-wise Issues
                    # -------------------------------
                    with colC:
                        st.markdown("### 🌍 Platform-wise Issues")
                        platform_counts = df["platform"].value_counts()

                        if len(platform_counts) == 1:
                            st.info("Single platform affected.")

                        st.bar_chart(platform_counts)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown(
    "<center>⚡ Built with FastAPI + Streamlit + LLaMA-3 (Local) | Academic & Industry-Ready Project</center>",
    unsafe_allow_html=True
)
