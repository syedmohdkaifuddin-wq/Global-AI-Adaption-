import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sn
import streamlit as st

df = pd.read_csv(r'C:\Users\HP\Desktop\mini project 1\ai_policy_and_ethics.csv')
df["respondent_id"]= df["company_has_ai_policy"].fillna(df["ai_bias_concern_level"].median())


fig = px.bar(
    df['company_has_ai_policy'].value_counts(),
    title='Companies with AI polacy'
)
st.plotly_chart(fig)