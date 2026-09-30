import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sn
import streamlit as st


df = pd.read_csv(r'C:\Users\HP\Desktop\mini project 1\skills_and_training.csv')
df["respondent_id"]= df["num_skills"].fillna(df["weekly_learning_hours"].median())

platform_counts = df['primary_learning_platform'].value_counts().reset_index()
platform_counts.columns = ['platform', 'count']

fig = px.bar(
    platform_counts,
    x='platform',
    y='count',
    title='Most Common Primary Learning Platforms',
    labels={'platform': 'Learning Platform', 'count': 'Number of Respondents'}
)
st.plotly_chart(fig)