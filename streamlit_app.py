import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open("pfp.png"))

st.header("Jayce Beck, B.S. in Computer Science")

st.info(
    "Welcome! Here you will find all the links to my social media, projects, and more!"
)

icon_size = 20

# st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
# st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button(
    "linkedin",
    "https://www.linkedin.com/in/jaycebeck/",
    "Follow me on LinkedIn",
    icon_size,
)
st_button(
    "document",
    "https://docs.google.com/document/d/1k506sz9hTXpEWVtKe9fbTclvK8_KFtgJ__8Unt-Z74w/edit?usp=sharing",
    "Queer Science Fair Handout",
    icon_size + 2,
)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
