# Elastic Agentic RAG: Self-Correction with JinaAI Reranker v3

This repository contains the implementation for a **Self-Correcting Agentic RAG** system, submitted for the **Elastic Blogathon 2026: Vectorized Thinking**.

## 🚀 Overview
Standard RAG systems often suffer from hallucinations due to poor retrieval relevance. This project uses **Elastic Agent Builder** to orchestrate a "Self-Correction" loop:
- **Hybrid Search:** Combines BM25 and Dense Vector search in Elasticsearch.
- **JinaAI Reranker v3:** A list-wise reranker that validates the top-k results.
- **Agentic Logic:** If the reranked confidence score is **< 0.65**, the agent triggers a query refinement and second retrieval pass.

## 🛠️ Tech Stack
- **Database:** Elasticsearch (Vector Store & Hybrid Search)
- **Orchestration:** Elastic Agent Builder
- **Reranking:** JinaAI Reranker v3 (via Open Inference API)
- **Embeddings:** `jina-embeddings-v3`

## 📂 Project Structure
```text
├── data/               # Sample dataset for indexing
├── mappings/           # Elasticsearch index & inference configurations
├── notebooks/          # Main implementation: Self_Correcting_RAG.ipynb
└── requirements.txt    # Python dependencies
