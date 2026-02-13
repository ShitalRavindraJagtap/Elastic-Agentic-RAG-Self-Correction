🚀 Elastic Agentic RAG: Self-Correction with JinaAI Reranker v3
This repository contains the official implementation of a Self-Correcting Agentic RAG system, submitted for the Elastic Blogathon 2026: Vectorized Thinking.

📖 Project Overview
Standard RAG systems often suffer from hallucinations due to poor retrieval relevance. This project leverages Elastic Agent Builder to orchestrate a "Self-Correction" loop. By integrating JinaAI Reranker v3, the agent evaluates the quality of retrieved context in real-time. If the confidence score is too low, the agent autonomously refines the search query and attempts a second, high-precision retrieval pass.

Core Innovation: The Self-Correction Loop

graph TD
    A[User Query] --> B{Elastic Hybrid Search}
    B --> C[Top-K Results]
    C --> D[JinaAI Reranker v3]
    D --> E{Score > 0.65?}
    E -- No: Low Confidence --> F[Agent Refines Query]
    F --> B
    E -- Yes: High Confidence --> G[Final Context Delivered]
    G --> H[LLM Response Generation]
    
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#ff9,stroke:#333,stroke-width:2px

    🛠️ Tech Stack
Vector Database: Elasticsearch (Hybrid Search: BM25 + Dense Vector)

Orchestration: Elastic Agent Builder

Reranking: JinaAI Reranker v3 (via Elastic Inference API)

Embeddings: jina-embeddings-v3 (Multilingual support)

├── data/               # Sample dataset for indexing
├── mappings/           # Elasticsearch index & inference configurations
│   ├── index_settings.json
│   └── hybrid_retrieval.json
├── notebooks/          # Main implementation
│   └── Self_Correcting_RAG.py
├── .env.example        # Environment variables template
├── requirements.txt    # Python dependencies
└── README.md
⚙️ Getting Started
1. Prerequisites
An Elastic Cloud account (Serverless or Stack 8.12+)

A JinaAI API Key

2. Setup Environment
   # Clone the repository
git clone https://github.com/ShitalRavindraJagtap/Elastic-Agentic-RAG-Self-Correction.git
cd Elastic-Agentic-RAG-Self-Correction

# Install dependencies
pip install -r requirements.txt

3. Configuration
Create a .env file in the root directory based on .env.example:
ELASTIC_CLOUD_ID="your_cloud_id"
ELASTIC_API_KEY="your_api_key"
JINA_API_KEY="your_jina_key"

🚀 Key Features
Hybrid Retrieval: Unifies lexical (BM25) and semantic (Vector) search for maximum recall.

List-wise Reranking: Uses JinaAI v3 to reason across the entire candidate set simultaneously.

Autonomous Query Refinement: If initial results are irrelevant, the agent uses an LLM to "rewrite" the search intent for a better second attempt.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Acknowledgments
Elastic Team for the Agent Builder framework.

Jina AI for the state-of-the-art Reranker v3.

Ashish Tiwari for the inspiration during the Blogathon 2026.
