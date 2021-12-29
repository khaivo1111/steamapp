import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from random import choices
import string

st.set_page_config(page_title='Python App')

# App 1: Password generator
st.header('Password genrator')
st.image('./Image/Password.jpg',width=400)

number = string.digits # 0~9
letter = string.ascii_letters # a-zA-Z
symbol = string.punctuation # !@#$%^&*
all_char = number + letter + symbol

def get_pass(number):
        return ''.join(choices(all_char,k=number))

a = st.slider('Pick a lengh', 4, 20, value=6)
st.write('Pass lengh:', a)

col1, col2, col3 = st.columns(3)
click = col1.button('Get password')
copy = None
if click:
        col2.subheader(get_pass(a))
        copy = col3.button('Copy')
if copy:
        st.write('Copied')

#st.text('Fixed width text')
# st.markdown('_Markdown_') # see *


### --- LOAD DATAFRAME
# excel_file = 'Survey_Results.xlsx'
# sheet_name = 'DATA'

# df = pd.read_excel(excel_file,
#                    sheet_name=sheet_name,
#                    usecols='B:D',
#                    header=3)

# df_participants = pd.read_excel(excel_file,
#                                 sheet_name= sheet_name,
#                                 usecols='F:G',
#                                 header=3)
# df_participants.dropna(inplace=True)

# # --- STREAMLIT SELECTION
# department = df['Department'].unique().tolist()
# ages = df['Age'].unique().tolist()

# age_selection = st.slider('Age:',
#                         min_value= min(ages),
#                         max_value= max(ages),
#                         value=(min(ages),max(ages)))

# department_selection = st.multiselect('Department:',
#                                     department,
#                                     default=department)

# # --- FILTER DATAFRAME BASED ON SELECTION
# mask = (df['Age'].between(*age_selection)) & (df['Department'].isin(department_selection))
# number_of_result = df[mask].shape[0]
# st.markdown(f'*Available Results: {number_of_result}*')

# # --- GROUP DATAFRAME AFTER SELECTION
# df_grouped = df[mask].groupby(by=['Rating']).count()[['Age']]
# df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
# df_grouped = df_grouped.reset_index()

# # --- PLOT BAR CHART
# bar_chart = px.bar(df_grouped,
#                    x='Rating',
#                    y='Votes',
#                    text='Votes',
#                    color_discrete_sequence = ['#F63366']*len(df_grouped),
#                    template= 'plotly_white')
# st.plotly_chart(bar_chart)

# # --- DISPLAY IMAGE & DATAFRAME
# col1, col2 = st.beta_columns(2)
# image = Image.open('images/survey.jpg')
# col1.image(image,
#         caption='Designed by slidesgo / Freepik',
#         use_column_width=True)
# col2.dataframe(df[mask])

# # --- PLOT PIE CHART
# pie_chart = px.pie(df_participants,
#                 title='Total No. of Participants',
#                 values='Participants',
#                 names='Departments')

# st.plotly_chart(pie_chart)
