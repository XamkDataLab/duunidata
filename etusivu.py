import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from queries import *

df = get_duuni_data()

category = st.sidebar.selectbox('Select a Category', df['category'].unique())

filtered_df = df[df['category'] == category]

company_counts = filtered_df['company'].value_counts().reset_index()
company_counts.columns = ['company', 'count']
top_companies = company_counts.sort_values(by='count', ascending=False).head(20)

fig = px.bar(top_companies, y='company', x='count', orientation='h')

fig.update_layout(
    yaxis={'categoryorder':'total ascending'},
    yaxis_title="Company",
    xaxis_title="Frequency",
    font=dict(size=12),  # Adjust font size here
    margin=dict(l=10, r=10, t=10, b=10)  # Adjust margins to fit labels
)

bar_height = 30  # Height per bar, adjust as needed
total_bars = len(top_companies)
chart_height = bar_height * total_bars

st.plotly_chart(fig, use_container_width=True, height=chart_height)

titles = filtered_df['title'].dropna()
text = ' '.join(titles)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)
