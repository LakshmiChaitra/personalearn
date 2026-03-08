# 🎓 ML-Powered Personalized Learning Path Recommendation System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://[YourApp].streamlit.app)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![IBM SkillsBuild](https://img.shields.io/badge/IBM-SkillsBuild-blue)](https://skillsbuild.org)

> **IBM SkillsBuild × CSRBOX Boot Camp 2026 | SDG 4 – Quality Education**

---

## 📌 Project Overview

This project develops a **hybrid ML recommendation system** that generates personalised learning paths for students based on their quiz scores, study time, interaction patterns, and knowledge gaps.

**Dataset:** [OULAD – Open University Learning Analytics Dataset](https://analyse.kmi.open.ac.uk/open_dataset)  
32,000+ student records across 7 course modules.

---

## 🚀 Live Demo

> 👉 [Open the Streamlit App](https://[YourApp].streamlit.app)

---

## 🧠 ML Architecture

| Component | Algorithm | Purpose |
|-----------|-----------|---------|
| Collaborative Filtering | SVD (via Surprise) | Peer-based recommendations |
| Content-Based Filtering | TF-IDF + Cosine Similarity | Profile-to-resource matching |
| Performance Predictor | XGBoost | Score forecasting |
| Student Segmentation | K-Means | Learner persona assignment |
| Model Validation | 5-Fold Cross-Validation | Generalisation check |

---

## 📊 Key Metrics

- **Target Accuracy:** ~80% (Performance Predictor)
- **Evaluation:** Precision@K, Recall@K, NDCG, RMSE, F1-Score
- **Learner Personas:** Fast Tracker 🚀 · Steady Learner 📘 · Needs Support 🛟

---

## ⚙️ Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/[YourUsername]/ml-learning-paths.git
cd ml-learning-paths

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```

---

## 📁 Project Structure

```
ml-learning-paths/
├── app.py                  # Streamlit web application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── model/
│   ├── train_model.py      # Model training pipeline
│   └── evaluate.py         # Evaluation metrics
└── data/
    └── preprocessing.py    # OULAD data preprocessing
```

---

## 📄 Citation

Open University Learning Analytics Dataset (OULAD):
> Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4(1), 1–8. https://doi.org/10.1038/sdata.2017.171

---

## 👥 Team

| Name | Role |
|------|------|
| [Member Name 1] | ML Model Development |
| [Member Name 2] | Data Preprocessing & EDA |
| [Member Name 3] | Streamlit App & Deployment |

**College:** [Your College Name]  
**Boot Camp:** IBM SkillsBuild × CSRBOX 2026  
**Submission:** March 12, 2026

---

## 📜 License

MIT License — free to use and adapt with attribution.
