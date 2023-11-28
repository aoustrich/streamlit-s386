import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.title('Popular Names')
url = "https://raw.githubusercontent.com/esnt/Data/main/Names/popular_names.csv"
df = pd.read_csv(url)

selected_name = st.text_input("Enter a name to see its popularity over time", "")

name_df = df[df['name'] == selected_name]
if name_df.empty:
    st.write("No data found. Check your spelling and try again.")
else:
    fig = px.line(name_df, x="year", y="n", color='sex',
                  color_discrete_sequence=['#F8766D', '#00BA38'],
                  title=f"Popularity of name {selected_name}")
    st.plotly_chart(fig)

st.markdown("---")

selected_year = st.selectbox("Select a year to see its most popular boy and girl names!", df['year'].unique())

year_df = df[df['year'] == selected_year]
girl_names = year_df[year_df['sex']=='F'].sort_values(by='n', ascending=False).head(5)['name'].reset_index(drop=True)    
boy_names = year_df[year_df['sex']=='M'].sort_values(by='n', ascending=False).head(5)['name'].reset_index(drop=True)    
top_names = pd.concat([girl_names, boy_names], axis=1).reset_index(drop=True)
top_names.columns = ['girl','boy']
st.write(f"The top names in {selected_year} are:")
st.dataframe(top_names)

# import pandas as pd
# import streamlit as st
# import plotly.express as px

# url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
# df = pd.read_csv(url)

# st.title('Popular Names')

# st.header('Name Trend')
# selected_name = st.text_input('Enter a name to plot', 'John')
# name_df = df[df['name'] == selected_name]
# if name_df.empty:
#     st.write('Name not found')
# else:
#     fig = px.line(name_df, x='year', y='n', color='sex',
#                   color_discrete_sequence=px.colors.qualitative.Set2)
#     st.plotly_chart(fig)

# st.header('Popular Names by Year')
# year = st.slider('Select Year', 1910, 2021, 2000)

# year_df = df[df['year'] == year]

# girls_names = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
# boys_names = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']

# top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)], 
#           ignore_index=True, axis=1)

# top_names.columns = ['Girls','Boys']

# st.write(f"Top Names in {year}")

# st.dataframe(top_names)