import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataframe
df = get_duuni_data()
st.DataFrame(df)
# Sidebar for category selection
category = st.sidebar.selectbox('Select a Category', df['category'].unique())

# Filter the dataframe based on the selected category
filtered_df = df[df['category'] == category]

# Count the frequency of companies in the selected category
company_counts = filtered_df['company'].value_counts().reset_index()
company_counts.columns = ['company', 'count']

# Plotting with Plotly
fig = px.bar(company_counts, x='company', y='count', title='Company Frequencies in Selected Category')
st.plotly_chart(fig)

