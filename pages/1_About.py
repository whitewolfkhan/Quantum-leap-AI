# pages/1_About.py
import streamlit as st
from lang import EN, BN

def get_text(lang_code):
    return EN if lang_code == 'EN' else BN

# Get the language from session state
lang_code = st.session_state.get('lang', 'EN')
texts = get_text(lang_code)

st.set_page_config(page_title=texts["about_title"], page_icon="ℹ️")

st.title(f"ℹ️ {texts['about_title']}")

st.write(texts['about_intro'])

st.subheader(texts['about_mission_header'])
st.write(texts['about_mission_text'])

st.subheader(texts['about_tech_header'])
st.write(texts['about_tech_text'])

st.subheader(texts['about_contribute_header'])
st.write(texts['about_contribute_text'])