import streamlit as st
from services.rag_service import hybrid_rag_query

st.title("⚖️ Legal Document Q&A")

query = st.text_input("Ask resume question")

if st.button("Ask"):
    response = hybrid_rag_query("resume", query)
    st.write(response)