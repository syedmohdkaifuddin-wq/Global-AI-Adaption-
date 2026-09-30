import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sn
import streamlit as st

df = pd.read_csv(r'C:\Users\HP\Desktop\mini project 1\respondents.csv')
df['respondent_id']= df['survey_year'].fillna(df['age'].median())

industry = df['industry'].value_counts().reset_index()

fig = px.bar(
    industry,
    x='industry',
    y='count',
    title='Respondents by Industry'
)
st.plotly_chart(fig)



