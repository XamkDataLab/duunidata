import streamlit as st
import pandas as pd
import plotly.express as px
from queries import *

df = get_duuni_data()

category = st.sidebar.selectbox('Select a Category', df['category'].unique())

filtered_df = df[df['category'] == category]

company_counts = filtered_df['company'].value_counts().reset_index()
company_counts.columns = ['company', 'count']
company_counts = company_counts.sort_values(by='count', ascending=False).head(20)

fig = px.bar(company_counts, y='company', x='count', orientation='h', title='Top 20 Companies in Selected Category')

fig.update_layout(
    yaxis={'categoryorder':'total ascending'},
    yaxis_title="Company",
    xaxis_title="Frequency",
    font=dict(size=10) # Adjust font size here
)
st.plotly_chart(fig, use_container_width=True, height=1200) # Adjust height as needed


