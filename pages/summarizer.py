import pandas as pd
import requests
import streamlit as st
import webbrowser
from streamlit_lottie import st_lottie
st.set_page_config(
    page_title="Summarizer",
    page_icon="🕸",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "## A content based Journal recommendation system build using cosine similarity"
    }
)

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation_1 = "https://assets5.lottiefiles.com/packages/lf20_m9hna20b.json"

lottie_anime_json = load_lottie_url(lottie_animation_1)
# Load Our Dataset
def load_data(data):
    df = pd.read_csv(data)
    return df

st.title(' Welcome to Summarizaro')

st_lottie(lottie_anime_json, key="hello", width=600)

st.markdown('#  Too much content to read ? Dont worry Summarizaro will make your reading easy ')
lottie_animation_2 = "https://assets2.lottiefiles.com/packages/lf20_ybiszbil.json"

lottie_anime_json2 = load_lottie_url(lottie_animation_2)
st_lottie(lottie_anime_json2, key="heqllo", width=600)


url = 'http://127.0.0.1:5000/'
if st.button('Lets Summarizee !!!'):
    webbrowser.open_new_tab(url)