import streamlit as st
from services.rag_service import hybrid_rag_query

st.title("⚖️ Legal Document Q&A")

query = st.text_input("Ask legal question")

if st.button("Ask"):
    response = hybrid_rag_query("legal", query)
    st.write(response)