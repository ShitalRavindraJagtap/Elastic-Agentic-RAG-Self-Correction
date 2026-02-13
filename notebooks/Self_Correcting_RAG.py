import os
from elasticsearch import Elasticsearch
from jinaai import JinaAi
from dotenv import load_dotenv

# Load credentials from your .env file
load_dotenv()
ELASTIC_CLOUD_ID = os.getenv("ELASTIC_CLOUD_ID")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

# 1. Initialize Clients
es = Elasticsearch(cloud_id=ELASTIC_CLOUD_ID, api_key=ELASTIC_API_KEY)
jina = JinaAi(api_key=JINA_API_KEY)

def agentic_search(user_query):
    print(f"🔍 Agent received query: {user_query}")
    
    # 2. Hybrid Retrieval (Elasticsearch)
    # This searches both text and vectors
    response = es.search(
        index="agentic-knowledge-base",
        query={
            "multi_match": {
                "query": user_query,
                "fields": ["text_data"]
            }
        }
    )
    
    docs = [hit["_source"]["text_data"] for hit in response["hits"]["hits"]]
    
    # 3. JinaAI Reranking
    rerank_result = jina.rerank(
        model="jina-reranker-v3",
        query=user_query,
        documents=docs,
        top_n=3
    )
    
    # 4. Self-Correction Logic
    top_score = rerank_result[0]['relevance_score']
    print(f"📊 Top Rerank Score: {top_score}")
    
    if top_score < 0.65:
        print("⚠️ Score too low! Triggering Self-Correction...")
        # Refine query (Simulated Agent thought process)
        refined_query = f"Detailed explanation of {user_query}"
        return agentic_search(refined_query) # Recursive loop
    else:
        print("✅ Confidence high. Generating answer...")
        return docs[0]

# Example Run
# result = agentic_search("How does Elastic Agent Builder work?")
# print(result)