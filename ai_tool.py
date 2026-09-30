import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sn
import streamlit as st


df = pd.read_csv(r'C:\Users\HP\Desktop\mini project 1\ai_tool_usage.csv')

df['respondent_id']=df['productivity_change_pct'].fillna(df['satisfaction_score'].median())
tool_count = df['ai_tool'].value_counts().reset_index()
tool_count.columns = ['ai_tool', 'count']

fig = px.bar(
    tool_count,
    x='ai_tool',
    y='count',
    title='Most Used AI Tools',
    labels={
        'ai_tool': 'AI Tool',
        'count': 'Number of Respondents'
    }
)
st.plotly_chart(fig)