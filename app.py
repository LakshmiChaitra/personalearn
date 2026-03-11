"""
ML-Powered Personalized Learning Path Recommendation System
IBM SkillsBuild | CSRBOX Boot Camp 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PersonaLearn – ML Learning Paths",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CUSTOM CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {font-size:2.2rem; font-weight:800; color:#003366; margin-bottom:0.2rem;}
    .sub-header  {font-size:1.0rem; color:#555; margin-bottom:1.5rem;}
    .metric-box  {background:#003366; color:white; padding:1rem; border-radius:10px; text-align:center;}
    .metric-val  {font-size:2rem; font-weight:bold; color:#F9C74F;}
    .rec-card    {background:#EEF4FB; border-left:4px solid #003366; padding:0.8rem 1rem; border-radius:6px; margin:0.4rem 0;}
    .risk-low    {color:#228B22; font-weight:bold;}
    .risk-med    {color:#B8860B; font-weight:bold;}
    .risk-high   {color:#CC2200; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 👩‍💻 Chaitra")
    st.markdown("### 🎓 PersonaLearn")
    st.caption("ML-Powered Personalized Learning Paths")
    st.divider()
    page = st.radio("Navigate", ["🏠 Home", "📊 Dashboard", "🎓 My Learning Path", "⚠️ At-Risk Students", "ℹ️ About"])
    st.divider()
    st.divider()
    st.markdown("### 👥 Team")
    st.markdown("👩‍💻 **Chaitra** (Lead)")
    st.markdown("👩‍💻 **K. Shivani**")
    st.markdown("👨‍💻 **A. Pranav**")
    st.markdown("👨‍💻 **J.S.S. Abhiram**")
    st.divider()
    st.divider()
    st.markdown("### 👥 Team")
    st.markdown("👩‍💻 **P.L.Chaitra**")
    st.markdown("👩‍💻 **K. Shivani**")
    st.markdown("👨‍💻 **A. Pranav**")
    st.markdown("👨‍💻 **J.S.S. Abhiram**")
    st.divider()
    st.caption("IBM SkillsBuild | CSRBOX 2026")

# ── HOME PAGE ─────────────────────────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown('<div class="main-header">ML-Powered Personalized Learning Paths</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">IBM SkillsBuild · CSRBOX Boot Camp 2026 · SDG 4 – Quality Education</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-box"><div class="metric-val">32K+</div>Students in Dataset</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-box"><div class="metric-val">7</div>Course Modules</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-box"><div class="metric-val">~80%</div>Target Accuracy</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-box"><div class="metric-val">3</div>Learner Personas</div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("🔍 Get Personalised Recommendations")

    c1, c2, c3 = st.columns(3)
    with c1:
        student_id = st.text_input("Student ID", placeholder="e.g. 2024001")
        module = st.selectbox("Course Module", ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"])
    with c2:
        quiz_score = st.slider("Average Quiz Score (%)", 0, 100, 65)
        time_spent = st.slider("Weekly Study Hours", 0, 40, 12)
    with c3:
        interactions = st.slider("Resource Interactions / Week", 0, 100, 30)
        prev_result = st.selectbox("Previous Result", ["Pass", "Fail", "Distinction", "No Previous"])

    if st.button("🚀 Generate Learning Path", use_container_width=True, type="primary"):
        # Simple rule-based mock recommendation (replace with real model)
        score = quiz_score * 0.5 + (time_spent / 40) * 100 * 0.3 + (interactions / 100) * 100 * 0.2
        if score >= 75:
            segment, risk, color_class = "Fast Tracker 🚀", "Low", "risk-low"
            recs = ["Advanced Machine Learning Techniques", "Deep Learning with TensorFlow", "Capstone: Real-World ML Project"]
            next_mod = "Capstone Project"
        elif score >= 50:
            segment, risk, color_class = "Steady Learner 📘", "Medium", "risk-med"
            recs = ["Intermediate Python Programming", "Statistics for Data Science", "Feature Engineering Fundamentals"]
            next_mod = "Feature Engineering"
        else:
            segment, risk, color_class = "Needs Support 🛟", "High", "risk-high"
            recs = ["Python Basics for Beginners", "Mathematics for ML", "Introduction to Programming Logic"]
            next_mod = "Foundations Module"

        st.divider()
        r1, r2, r3 = st.columns(3)
        r1.metric("Student Segment", segment)
        r2.metric("Predicted Score", f"{score:.0f}%")
        r3.metric("Risk Level", risk)

        st.subheader("📚 Recommended Learning Path")
        for i, rec in enumerate(recs, 1):
            st.markdown(f'<div class="rec-card">📖 <b>Step {i}:</b> {rec}</div>', unsafe_allow_html=True)

        st.info(f"⏭️ **Next Module:** {next_mod}")

        # Mini performance chart
        st.subheader("📊 Predicted Performance Across Modules")
        modules = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
        np.random.seed(int(score))
        scores = np.clip(np.random.normal(score, 10, 7), 0, 100)
        fig, ax = plt.subplots(figsize=(8, 3))
        colors = ["#228B22" if s >= 75 else "#B8860B" if s >= 50 else "#CC2200" for s in scores]
        ax.bar(modules, scores, color=colors, alpha=0.85, edgecolor="white", linewidth=0.5)
        ax.axhline(75, color="#003366", linestyle="--", linewidth=1, label="Pass Threshold")
        ax.set_ylim(0, 110)
        ax.set_ylabel("Predicted Score (%)")
        ax.set_title("Module-wise Performance Prediction", fontweight="bold")
        ax.legend()
        ax.spines[["top", "right"]].set_visible(False)
        st.pyplot(fig)
        plt.close()

# ── DASHBOARD ────────────────────────────────────────────────────────────────
elif page == "📊 Dashboard":
    st.header("📊 Cohort Analytics Dashboard")
    np.random.seed(42)
    n = 200
    df = pd.DataFrame({
        "student_id": range(1, n + 1),
        "quiz_score": np.random.normal(65, 15, n).clip(0, 100),
        "time_spent": np.random.normal(15, 6, n).clip(1, 40),
        "segment": np.random.choice(["Fast Tracker", "Steady Learner", "Needs Support"], n, p=[0.25, 0.50, 0.25]),
    })

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Learner Segment Distribution")
        seg_counts = df["segment"].value_counts()
        fig, ax = plt.subplots()
        colors_pie = ["#003366", "#2E75B6", "#CC4444"]
        ax.pie(seg_counts, labels=seg_counts.index, autopct="%1.0f%%", colors=colors_pie, startangle=90)
        st.pyplot(fig); plt.close()
    with c2:
        st.subheader("Score vs. Time Spent")
        fig, ax = plt.subplots()
        seg_color_map = {"Fast Tracker": "#003366", "Steady Learner": "#2E75B6", "Needs Support": "#CC4444"}
        for seg, grp in df.groupby("segment"):
            ax.scatter(grp["time_spent"], grp["quiz_score"], alpha=0.6, label=seg, color=seg_color_map[seg], s=25)
        ax.set_xlabel("Weekly Study Hours"); ax.set_ylabel("Quiz Score (%)")
        ax.legend(fontsize=8); ax.spines[["top", "right"]].set_visible(False)
        st.pyplot(fig); plt.close()

    st.subheader("Sample Student Data")
    st.dataframe(df.head(20).style.format({"quiz_score": "{:.1f}", "time_spent": "{:.1f}"}), use_container_width=True)

# ── MY LEARNING PATH ─────────────────────────────────────────────────────────
elif page == "🎓 My Learning Path":
    st.header("🎓 Personalised Learning Path Viewer")
    st.info("Enter your Student ID on the Home page to generate your personalised path.")
    st.markdown("""
    **How the recommendation works:**
    1. 📊 Your quiz scores, time-on-task, and interaction data are fed into the hybrid model.
    2. 🤝 **Collaborative Filtering** finds students similar to you and surfaces what helped them.
    3. 📚 **Content-Based Filtering** matches your knowledge profile to appropriate resources.
    4. 🌲 **XGBoost Predictor** estimates your score in upcoming modules.
    5. 🎯 **K-Means Segmentation** assigns your learner persona for the right support level.
    """)

# ── AT-RISK ──────────────────────────────────────────────────────────────────
elif page == "⚠️ At-Risk Students":
    st.header("⚠️ At-Risk Student Monitoring")
    np.random.seed(7)
    n = 30
    risk_df = pd.DataFrame({
        "Student ID": [f"S{1000+i}" for i in range(n)],
        "Module": np.random.choice(["AAA", "BBB", "CCC", "DDD", "EEE"], n),
        "Quiz Score (%)": np.random.normal(42, 10, n).clip(10, 65).round(1),
        "Study Hours/Wk": np.random.normal(6, 3, n).clip(1, 15).round(1),
        "Risk Level": np.random.choice(["High", "Medium"], n, p=[0.4, 0.6]),
        "Recommended Action": np.random.choice(["Schedule Tutoring", "Review Module 1", "Attend Drop-in Session", "Peer Study Group"], n),
    })
    st.warning(f"⚠️ {len(risk_df)} students flagged this week")
    st.dataframe(risk_df.style.applymap(
        lambda v: "color: red; font-weight: bold" if v == "High" else "color: orange; font-weight: bold" if v == "Medium" else "",
        subset=["Risk Level"]
    ), use_container_width=True)

# ── ABOUT ────────────────────────────────────────────────────────────────────
elif page == "ℹ️ About":
    st.header("ℹ️ About This Project")
    st.markdown("""
    **Project:** ML-Powered Personalized Learning Path Recommendation System  
    **Goal:** SDG 4 – Quality Education  
    **Dataset:** [OULAD – Open University Learning Analytics Dataset](https://analyse.kmi.open.ac.uk/open_dataset)  
    **Team:** [Your Team Name] | [Your College Name]  
    **Boot Camp:** IBM SkillsBuild × CSRBOX 2026  

    ### Tech Stack
    | Component | Technology |
    |-----------|-----------|
    | Language | Python 3.10+ |
    | ML Framework | scikit-learn, XGBoost, Surprise |
    | Web App | Streamlit |
    | Data Processing | pandas, NumPy |
    | Visualisation | Matplotlib |

    ### Architecture
    - **Collaborative Filtering** (SVD via Surprise) — peer-based recommendations
    - **Content-Based Filtering** (TF-IDF + Cosine Similarity) — profile matching
    - **Performance Predictor** (XGBoost) — score forecasting
    - **Student Segmentation** (K-Means) — learner personas
    """)
