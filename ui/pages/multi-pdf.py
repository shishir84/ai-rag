import streamlit as st
from services.rag_service import hybrid_rag_query

st.title("⚖️ Legal Document Q&A")

query = st.text_input("Ask multipdf question")

if st.button("Ask"):
    response = hybrid_rag_query("multipdf", query)
    st.write(response)