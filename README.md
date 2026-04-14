# 🧠 AI RAG System – From Custom Pipeline to LangChain

This project demonstrates the evolution of a **Retrieval-Augmented Generation (RAG)** system:

* ✅ **Phase 1:** Custom-built RAG (full control, engineered pipeline)
* 🚀 **Phase 2:** LangChain-based RAG (framework-driven orchestration)

The goal is to understand both:

* **How RAG works under the hood**
* **When to use frameworks vs custom implementations**

---

# 🧱 Architecture Overview

## 🔹 Custom RAG (Before)

```
UI (Streamlit)
   ↓
Service Layer (rag_service.py)
   ↓
Query Expansion (LLM)
   ↓
Vector Search (ChromaDB)
   ↓
Keyword Search (BM25-like)
   ↓
Merge + Deduplicate
   ↓
Prompt Construction
   ↓
LLM (Ollama)
   ↓
Answer
```

---

## 🔹 LangChain RAG (After)

```
UI (Streamlit)
   ↓
LangChain Service (wiki_langchain_service.py)
   ↓
RetrievalQA Chain
   ↓
Retriever (ChromaDB)
   ↓
LLM (Ollama)
   ↓
Answer + Source Documents
```

---

# 🔍 Step-by-Step Flow Explanation

## 🟢 BEFORE (Custom RAG)

### 1. User Query (UI)

* Input collected via Streamlit
* Entry point for system

---

### 2. Query Expansion

* LLM generates variations of user query
* Example:

  ```
  "aws pricing"
  → ["aws pricing model", "aws cost structure"]
  ```

👉 **Why:** Improve recall (find more relevant documents)

---

### 3. Vector Search

* Convert query → embedding
* Compare with stored embeddings

👉 **Why:** Capture semantic meaning

---

### 4. Keyword Search

* Match exact words in documents

👉 **Why:** Improve precision (exact matches)

---

### 5. Merge + Deduplicate

* Combine results from multiple queries

👉 **Why:** Remove redundancy

---

### 6. Prompt Construction

```
Context:
<retrieved chunks>

Question:
<query>
```

👉 **Why:** Ground LLM with relevant data

---

### 7. LLM Generation

* Ollama generates answer based on context

👉 **Why:** Produce final response

---

### 8. Output to UI

* Display answer

---

## 🟢 AFTER (LangChain RAG)

### 1. User Query (UI)

Same as before

---

### 2. LangChain Chain Invocation

```python
qa_chain.invoke({"query": query})
```

👉 **Why:** Delegate pipeline to framework

---

### 3. Retrieval

* Uses ChromaDB via LangChain retriever

👉 Internally:

```
Query → Embedding → Similarity Search → Top-K docs
```

---

### 4. Context Assembly

* LangChain combines retrieved documents

👉 **Why:** Provide context automatically

---

### 5. Prompt (Default Template)

```
Use the following context to answer...
```

👉 **Why:** Standardized prompt

---

### 6. LLM Execution

* Ollama wrapped inside LangChain

---

### 7. Output

```json
{
  "result": "...",
  "source_documents": [...]
}
```

👉 **New Feature:** Source tracking

---

# ⚖️ Key Differences

## 🔍 Retrieval

| Feature        | Custom | LangChain |
| -------------- | ------ | --------- |
| Vector search  | ✅      | ✅         |
| Keyword search | ✅      | ❌         |
| Hybrid search  | ✅      | ❌         |

---

## 🔍 Query Handling

| Feature               | Custom | LangChain |
| --------------------- | ------ | --------- |
| Query expansion       | ✅      | ❌         |
| Multi-query retrieval | ✅      | ❌         |

---

## 🔍 Prompting

| Feature           | Custom | LangChain |
| ----------------- | ------ | --------- |
| Full control      | ✅      | ❌         |
| Default templates | ❌      | ✅         |

---

## 🔍 Output

| Feature     | Custom     | LangChain     |
| ----------- | ---------- | ------------- |
| Answer      | ✅          | ✅             |
| Source docs | ❌ (manual) | ✅ (automatic) |

---

# 🧠 What Changed Under the Hood

## ❌ Removed (in LangChain version)

* Query expansion
* Hybrid retrieval
* Custom reranking
* Manual prompt control

---

## ✅ Added

* Pre-built RAG pipeline
* Automatic source tracking
* Simplified orchestration

---

# 🧠 Key Learning

## 🔹 Custom RAG

```
Full control
Deep understanding
Better optimization
```

👉 You built:

* Hybrid retrieval
* Query expansion
* Evaluation pipeline

---

## 🔹 LangChain RAG

```
Fast development
Less boilerplate
Framework abstraction
```

---

# 🧠 Mental Model

```
Custom RAG = Engineered System
LangChain = Orchestration Framework
```

---

# 🚀 Best Practice (Recommended Approach)

Do NOT replace your system entirely.

👉 Instead:

```
Use LangChain
+ Add your custom enhancements
```

Example:

* Add query expansion before LangChain
* Add reranking after retrieval
* Customize prompt templates

---

# 📊 Current Capability

You now understand:

* RAG architecture
* Embeddings & vector DB
* Hybrid retrieval
* Query expansion
* Framework vs custom tradeoffs

---

# 🔥 Next Steps

* Add hybrid retrieval inside LangChain
* Add reranking layer
* Build Agentic RAG (LangGraph / CrewAI)
* Add evaluation dashboard

---

# 💡 Final Insight

> Building from scratch teaches **how systems work**
> Frameworks help you **build faster**

The real skill is knowing:
👉 **when to use each**

---

# 🧪 Run the Project

```bash
streamlit run ui/app.py
```

---

# 📁 Project Structure (Simplified)

```
common/
services/
ui/
rag_projects/
```

---

# 🙌 Outcome

You now have:

* A **custom-engineered RAG system**
* A **LangChain-powered RAG pipeline**
* A clear understanding of **trade-offs and architecture decisions**

---

🚀 This is **AI Engineer / Architect-level knowledge**
