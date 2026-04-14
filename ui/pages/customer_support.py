import streamlit as st
from services.rag_service import rag_query

st.title("⚖️ Legal Document Q&A")

query = st.text_input("Ask support question")

if st.button("Ask"):
    response = rag_query("support", query)
    st.write(response)