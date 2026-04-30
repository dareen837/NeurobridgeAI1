import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG + UI STYLE
# =========================
st.set_page_config(page_title="NeuroBridge AI", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# FAKE PATIENT DATABASE
# =========================
patients = {
    "Ahmed": {
        "risk": "Elevated",
        "memory": [85, 78, 70],
        "attention": [90, 85, 80],
        "mri": "Mild hippocampal atrophy"
    },
    "Sara": {
        "risk": "Monitor",
        "memory": [88, 84, 80],
        "attention": [92, 90, 88],
        "mri": "No acute abnormalities"
    },
    "Ali": {
        "risk": "Low",
        "memory": [90, 89, 88],
        "attention": [95, 94, 93],
        "mri": "Normal brain structure"
    }
}

# =========================
# SIMPLE RISK ENGINE
# =========================
def get_risk(memory_scores):
    if memory_scores[-1] < 75:
        return "Elevated"
    elif memory_scores[-1] < 85:
        return "Monitor"
    return "Low"

# =========================
# AI EXPLANATION (SIMULATED)
# =========================
def ai_explanation(symptoms, score, mri):
    return f"""
Cognitive analysis based on input:

- Symptoms: {', '.join(symptoms) if symptoms else 'None'}
- Cognitive score: {score}
- MRI: {mri}

Interpretation:
Mild changes in cognitive performance may indicate early cognitive drift.

Note: This is NOT a diagnosis. Clinical follow-up is recommended if symptoms persist.
"""

# =========================
# AI INSIGHT FOR DOCTOR
# =========================
def ai_insight(name):
    p = patients[name]
    decline = p["memory"][0] - p["memory"][-1]
    return f"Memory decline of {decline}% detected over time. Pattern suggests gradual cognitive drift."

# =========================
# UI HEADER
# =========================
st.title("🧠 NeuroBridge AI")
st.caption("Clinical Cognitive Monitoring System (Prototype)")

tab1, tab2 = st.tabs(["👩‍⚕️ Patient View", "👨‍⚕️ Doctor Dashboard"])

# =========================
# PATIENT VIEW
# =========================
with tab1:
    st.header("Patient Cognitive Check")

    name = st.selectbox("Select Patient", list(patients.keys()))

    symptoms = st.multiselect(
        "Symptoms",
        ["Memory loss", "Confusion", "Difficulty focusing"]
    )

    score = st.slider("Cognitive Score", 0, 100, 85)

    mri_text = st.text_area("MRI Report (text)", patients[name]["mri"])

    if st.button("Analyze Patient"):
        risk = get_risk(patients[name]["memory"])

        st.subheader("📊 Result")
        st.metric("Risk Level", risk)

        if risk == "Low":
            st.success("Stable cognitive status. Continue routine monitoring.")
        elif risk == "Monitor":
            st.warning("Mild changes detected. Follow-up recommended.")
        else:
            st.error("Significant decline detected. Clinical evaluation advised.")

        st.markdown("### 💬 AI Explanation")
        st.info(ai_explanation(symptoms, score, mri_text))

        st.markdown("### 📅 Next Step")
        st.write("Recommended follow-up in 3 months")

# =========================
# DOCTOR DASHBOARD
# =========================
with tab2:
    st.header("Doctor Dashboard")

    st.subheader("📌 Patient Overview")

    for name, data in patients.items():
        st.write(f"👤 {name} → **{data['risk']}**")

    st.divider()

    selected = st.selectbox("Select Patient", list(patients.keys()))
    p = patients[selected]

    st.subheader(f"👤 Patient: {selected}")

    df = pd.DataFrame({
        "Month": ["Jan", "Mar", "May"],
        "Memory": p["memory"],
        "Attention": p["attention"]
    })

    st.markdown("### 📈 Cognitive Timeline")
    st.line_chart(df.set_index("Month"))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧠 MRI Summary")
        st.info(p["mri"])

    with col2:
        st.markdown("### 🤖 AI Insight")
        st.warning(ai_insight(selected))

    st.divider()

    st.markdown("### 📨 Follow-up System")

    action = st.selectbox(
        "Choose action",
        [
            "Repeat cognitive test in 3 weeks",
            "Schedule clinic visit",
            "No action needed"
        ]
    )

    if st.button("Send Follow-up"):
        st.success(f"Follow-up sent to {selected}: {action}")
