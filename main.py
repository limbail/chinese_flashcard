import streamlit as st
from streamlit import session_state
import random, time
import pandas as pd

#st.set_page_config(layout='wide')

st.title('Chinese HSK Flashcard')

# Lets gain some space :)
#with st.expander("Show options:"):
with st.sidebar: # sidebar looks better


    options = st.selectbox(
    'Select the HSK level you want practice:',
    ['HSK-1', 'HSK-2', 'HSK-3', 'HSK-4', 'HSK-5', 'HSK-6'],)

    #st.write('You selected:', options)
    if options == 'HSK-1':level='hsk1'
    if options == 'HSK-2':level='hsk2'
    if options == 'HSK-3':level='hsk3'
    if options == 'HSK-4':level='hsk4'
    if options == 'HSK-5':level='hsk5'
    if options == 'HSK-6':level='hsk6'

    st.divider()

    user_lang = st.selectbox(
        'Your language:',
        ('english', 'spanish'))
    
    st.divider()
        
    show_answer_time = st.slider('Time before answer: ', 0, 10, 5)

    # lets read the file with the data
    df = pd.read_excel('HSK.xlsx', sheet_name=level)
    df = df.dropna(how='all')
    df = df.sample()
    
    hanzi=df['hanzi'].item()
    pinyin=df['pinyin'].item()
    user_lang=df[user_lang].item()
    #spanish=df['spanish'].item()

    #st.write('You selected:', user_lang)

st.divider()

def generate_new():
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">{} - {}</p>'.format(hanzi, pinyin), unsafe_allow_html=True)

    st.divider()

    with st.empty():
        time.sleep(show_answer_time)
        
        st.write('English: {}'.format(user_lang))

# the lonely button:
st.button("Next", key="1", on_click=generate_new())