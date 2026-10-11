
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PadhAI Pro", layout="wide")

# Read the index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display full HTML app inside Streamlit
components.html(html_content, height=800, scrolling=True)

st.sidebar.title("PadhAI Pro")
st.sidebar.info("2nd to 7th fun learning & 7th to 12th real mode")
