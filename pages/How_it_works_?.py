import streamlit as st
import pandas as pd

st.sidebar.markdown(f"<h3 style='text-align: left;'>💻 Our work</h3>", unsafe_allow_html=True)
st.sidebar.info("GitHub Repository: <https://github.com/ceptln/ntxs-servers-optimization>")

st.sidebar.markdown(f"<h3 style='text-align: left;'>📬 Contact</h3>", unsafe_allow_html=True)
markdown = """
camille.epitalon@hec.edu
charles.proye@hec.edu
martin.quievre@hec.edu
nathan.aim@hec.edu
sarah.mayer@hec.edu
"""
st.sidebar.info(markdown)

### MAIN PAGE
col1, col2, col3 = st.columns(3)
col1.write("")
col2.image(
    ".streamlit/natixis.png",
    width=200,
)
col3.write("")

st.markdown(f"<h1 style='text-align: center;'>HOW IT WORKS ?</hc1>", unsafe_allow_html=True)

### SLIDES

st.image(".streamlit/cap1.png")
st.image(".streamlit/cap2.png")
st.image(".streamlit/cap3.png")
st.image(".streamlit/cap4.png")
st.image(".streamlit/cap5.png")
st.image(".streamlit/cap6.png")
st.image(".streamlit/cap7.png")