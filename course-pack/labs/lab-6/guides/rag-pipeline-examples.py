"""
RAG Pipeline Example - Sprint 1
Building AI-Powered Applications | Week 6

Minimal but complete RAG implementation.

Dependencies:
pip install openai faiss-cpu numpy python-dotenv --break-system-packages
"""

import os
from typing import List, Dict
from openai import OpenAI
import numpy as np
import faiss
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[Dict]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    chunk_id = 0
    
    while start < len(text):
        end = start + chunk_size
        chunks.append({
            "id": chunk_id,
            "text": text[start:end],
            "start_pos": start,
            "end_pos": end
        })
        start = end - overlap
        chunk_id += 1
    
    return chunks

def generate_embedding(text: str) -> List[float]:
    """Generate embedding using OpenAI."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

class FAISSVectorDB:
    """Simple FAISS vector database."""
    
    def __init__(self, dimension: int = 1536):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []
    
    def add_documents(self, chunks: List[Dict]):
        """Add chunks with embeddings to index."""
        embeddings = np.array([chunk["embedding"] for chunk in chunks]).astype('float32')
        self.index.add(embeddings)
        self.chunks.extend(chunks)
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search for relevant chunks."""
        query_embedding = generate_embedding(query)
        query_vector = np.array([query_embedding]).astype('float32')
        
        distances, indices = self.index.search(query_vector, top_k)
        
        results = []
        for distance, idx in zip(distances[0], indices[0]):
            chunk = self.chunks[idx].copy()
            chunk["score"] = float(1 / (1 + distance))
            results.append(chunk)
        
        return results

def answer_with_rag(query: str, vector_db: FAISSVectorDB) -> Dict:
    """Answer query using RAG."""
    # Retrieve context
    results = vector_db.search(query, top_k=3)
    context = "\n\n".join([f"[{i+1}] {r['text']}" for i, r in enumerate(results)])
    
    # Build prompt
    prompt = f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    
    # Get LLM response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer based on context. Cite sources."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return {
        "answer": response.choices[0].message.content,
        "sources": results
    }

# Example usage
if __name__ == "__main__":
    # Sample documents
    docs = [
        "Python is a high-level programming language created by Guido van Rossum in 1991.",
        "JavaScript runs in web browsers and was created by Brendan Eich in 1995.",
        "SQL is used for databases and was developed by IBM in the 1970s."
    ]
    
    # Chunk and embed
    chunks = []
    for doc in docs:
        doc_chunks = chunk_text(doc, chunk_size=100)
        for chunk in doc_chunks:
            chunk["embedding"] = generate_embedding(chunk["text"])
        chunks.extend(doc_chunks)
    
    # Build index
    db = FAISSVectorDB()
    db.add_documents(chunks)
    
    # Query
    result = answer_with_rag("Who created Python?", db)
    print(result["answer"])
