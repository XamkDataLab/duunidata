import streamlit as st
import pandas as pd
import plotly.express as px
from queries import *

# Load the dataframe
df = get_duuni_data()

# Sidebar for category selection
category = st.sidebar.selectbox('Select a Category', df['category'].unique())

# Filter the dataframe based on the selected category
filtered_df = df[df['category'] == category]

# Count the frequency of companies in the selected category and sort in descending order
company_counts = filtered_df['company'].value_counts().reset_index()
company_counts.columns = ['company', 'count']
company_counts = company_counts.sort_values(by='count', ascending=False).head(20)

# Plotting with Plotly
fig = px.bar(company_counts, y='company', x='count', orientation='h', title='Top 20 Companies in Selected Category')
fig.update_layout(yaxis={'categoryorder':'total ascending'})

# Set the height of the chart for better scrolling experience
st.plotly_chart(fig, use_container_width=True, height=800)


