import streamlit as st
import pandas as pd

st.set_page_config(page_title="NeuroBridge AI", layout="wide")

# =========================
# 🎨 STYLE (Hospital UI)
# =========================
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #1f3b57;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================
patients = {
    "Ahmed": {"risk": "🔴 Elevated", "memory": [85, 78, 70]},
    "Sara": {"risk": "🟡 Monitor", "memory": [88, 84, 80]},
    "Ali": {"risk": "🟢 Low", "memory": [90, 89, 88]},
}

# =========================
# HEADER
# =========================
st.title("🧠 NeuroBridge AI")
st.caption("Clinical Cognitive Monitoring System")

st.divider()

# =========================
# SIDEBAR (LIKE REAL HOSPITAL SYSTEM)
# =========================
with st.sidebar:
    st.header("🏥 Navigation")
    page = st.radio("Go to", ["Doctor Dashboard", "Patient View"])

# =========================
# DOCTOR DASHBOARD
# =========================
if page == "Doctor Dashboard":

    st.header("👨‍⚕️ Doctor Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Patients", "3")
    col2.metric("High Risk", "1")
    col3.metric("Follow-ups Needed", "2")

    st.divider()

    st.subheader("📌 Patient List")

    for name, data in patients.items():
        st.markdown(f"""
        <div class="card">
            <h4>{name}</h4>
            <p>Risk Level: {data['risk']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    selected = st.selectbox("Select Patient", list(patients.keys()))
    p = patients[selected]

    st.subheader(f"👤 Patient Detail: {selected}")

    df = pd.DataFrame({
        "Month": ["Jan", "Mar", "May"],
        "Memory": p["memory"]
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Memory Trend")
        st.line_chart(df.set_index("Month"))

    with col2:
        st.markdown("### 🧠 Clinical Status")
        st.info(f"Risk Level: {p['risk']}")
        st.warning("Gradual cognitive change detected")

    st.markdown("### 📩 Actions")
    st.button("Send Follow-up")
    st.button("Schedule Visit")


# =========================
# PATIENT VIEW
# =========================
else:

    st.header("👤 Patient Portal")

    st.markdown("### 🧠 Your Cognitive Status")

    col1, col2, col3 = st.columns(3)

    col1.metric("Memory Score", "78")
    col2.metric("Attention", "85")
    col3.metric("Risk", "🟡 Monitor")

    st.divider()

    st.markdown("### 💬 AI Explanation")

    st.info("""
Your cognitive patterns show mild changes over time.
This does NOT indicate a diagnosis.
We recommend periodic monitoring and follow-up evaluation.
""")

    st.markdown("### 📅 Next Step")
    st.success("Repeat assessment in 3 months")
    
