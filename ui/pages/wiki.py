import streamlit as st
from services.wiki_langchain_service import wiki_query

st.title("📖 Wiki Search (LangChain)")

query = st.text_input("Ask something")

if st.button("Search"):
    answer, sources = wiki_query(query)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for doc in sources:
        st.caption(doc.metadata)