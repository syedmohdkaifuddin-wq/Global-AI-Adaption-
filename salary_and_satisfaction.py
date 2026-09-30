import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sn
import streamlit as st

df = pd.read_csv(r'C:\Users\HP\Desktop\mini project 1\salary_and_satisfaction.csv')
df['respondent_id']= df['annual_salary_usd'].fillna(df['job_search_status'].mode(2))

fig = px.bar(
    df["ai_job_replacement_fear"].value_counts().reset_index(),
    x="ai_job_replacement_fear",
    y="count",
    title="AI Job Replacement Fear"
)
st.plotly_chart(fig)