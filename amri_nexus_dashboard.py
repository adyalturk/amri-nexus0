
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title="Amri Nexus - Strategic Success Dashboard", layout="wide")
st.title("📊 Amri Nexus | Strategic Success Prediction Dashboard")
st.markdown("**Project Name:** Rukn Al Amri | Amri Nexus - Strategic Advisory Office")

# Sidebar Inputs
st.sidebar.header("🔍 Input Parameters")
influence = st.sidebar.slider("Influence Score", 0, 100, 60)
network_strength = st.sidebar.slider("Network Strength", 0, 100, 70)
strategic_alignment = st.sidebar.slider("Strategic Alignment", 0, 100, 75)
operational_readiness = st.sidebar.slider("Operational Readiness", 0, 100, 65)
team_experience = st.sidebar.slider("Team Experience", 0, 100, 80)

# Compute Success Score
weights = np.array([0.25, 0.20, 0.20, 0.15, 0.20])
inputs = np.array([influence, network_strength, strategic_alignment, operational_readiness, team_experience])
success_score = np.dot(weights, inputs)

# Show Score
st.metric(label="Predicted Success Score", value=f"{success_score:.2f} / 100")

# Visualization
st.subheader("📈 Success Factor Breakdown")
fig, ax = plt.subplots()
factors = ["Influence", "Network", "Strategy", "Operations", "Team"]
ax.barh(factors, inputs, color="#006699")
ax.set_xlim(0, 100)
ax.set_xlabel("Score")
st.pyplot(fig)

# Interpretation
st.subheader("📌 Recommendation")
if success_score >= 80:
    st.success("High chance of success. Project is well-positioned.")
elif success_score >= 60:
    st.warning("Moderate chance of success. Consider strengthening strategic or operational areas.")
else:
    st.error("Low chance of success. Major improvements are needed before proceeding.")
