import streamlit as st
from services.rag_service import advanced_rag_query
from services.evaluator import evaluate_answer

st.title("🏢 Company QA (Advanced RAG)")

query = st.text_input("Ask question")

if st.button("Ask"):
    response, context = advanced_rag_query("company", query)

    st.subheader("Answer")
    st.write(response)

    # 👇 Evaluation
    st.subheader("Evaluation")
    eval_result = evaluate_answer(query, response, context)
    st.write(eval_result)