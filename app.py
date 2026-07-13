import streamlit as st
import pandas as pd

st.set_page_config(page_title="Company Funnel Analytics", layout="wide")

st.title("📊 Company Funnel Analytics Dashboard")

uploaded_file = st.file_uploader(
    "Upload company_funnel_dataset.xlsx",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    total_students = len(df)
    viewed = df["Viewed"].sum()
    applied = df["Applied"].sum()
    shortlisted = df["Shortlisted"].sum()
    hired = df["Hired"].sum()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Students", total_students)
    col2.metric("Viewed", viewed)
    col3.metric("Applied", applied)
    col4.metric("Shortlisted", shortlisted)
    col5.metric("Hired", hired)

    st.subheader("Company Funnel")

    funnel = pd.DataFrame({
        "Stage": [
            "Students",
            "Viewed",
            "Applied",
            "Shortlisted",
            "Hired"
        ],
        "Count": [
            total_students,
            viewed,
            applied,
            shortlisted,
            hired
        ]
    })

    st.bar_chart(funnel.set_index("Stage"))

    st.subheader("Job Category Distribution")
    st.bar_chart(df["Job_Category"].value_counts())

    st.subheader("Match Score Distribution")
    st.line_chart(df["Match_Score"])

    st.success("Dashboard Loaded Successfully")
else:
    st.info("Please upload the dataset to view the dashboard.")
