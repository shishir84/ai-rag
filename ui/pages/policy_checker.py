import streamlit as st
from services.rag_service import rag_query

st.title("⚖️ Legal Document Q&A")

query = st.text_input("Ask policy question")

if st.button("Ask"):
    response = rag_query("policy", query)
    st.write(response)