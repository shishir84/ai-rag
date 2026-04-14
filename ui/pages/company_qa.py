import streamlit as st
from services.rag_service import rag_query

st.title("🏢 Company Knowledge Assistant")

query = st.text_input("Ask about company")

if st.button("Ask"):
    response = rag_query("company", query)
    st.write(response)