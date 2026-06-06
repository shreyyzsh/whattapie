import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from dataProcess import process_data

st.set_page_config(
    page_title="WhattaPie",
    page_icon="🥧",
    layout="centered"
)

st.header("WhattaPie 📊")
st.text("Convert CSV files to Pie Chart.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])


if uploaded_file:
    df_melted = process_data(uploaded_file)
    
    for question in df_melted["ques"].unique():
        question_df = df_melted[df_melted["ques"] == question]
        
        answer_counts = (
            question_df["ans"]
            .dropna()
            .astype(str)
            .value_counts()
        )
        
        if len(answer_counts) == 0:
            continue
        
        fig, ax = plt.subplots(figsize=(8, 6))

        
        ax.pie(
            answer_counts.values,
            labels=answer_counts.index,
            autopct="%1.1f%%",
            startangle=90
        )
        
        ax.set_title(question, pad=20)
        ax.axis("equal")
        
        st.pyplot(fig)
        plt.close(fig)