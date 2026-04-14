import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

st.set_page_config(page_title="AI With RAG", layout="wide")

st.title("🧠 AI Projects Dashboard")

projects = [
  ("Company QA", "company_qa"),
("Legal QA", "legal_qa"),
("Policy Checker", "policy_checker"),
("Customer Support", "customer_support"),
("Research Assistant", "research"),
("Wiki Search", "wiki"),
("Resume Search", "resume"),
("Product Manual", "product"),
("Healthcare QA", "healthcare"),
("Multi PDF", "multi-pdf"),
]

cols = st.columns(3)

for i, (name, page) in enumerate(projects):
    if cols[i % 3].button(name):
        st.switch_page(f"pages/{page}.py")