# Vectorify – Universal Data to Vector Embedding Engine

## Overview
**Vectorify** is an end-to-end system that converts structured and semi-structured data (Excel, CSV, DOCX, SQL) into **high-dimensional vector embeddings**, making the data ready for **semantic search, retrieval-augmented generation (RAG), and AI pipelines**.

The project supports **local, free embedding models** as well as optional **API-based providers**, with a clean frontend UI and a scalable backend architecture.

---

## Key Features
- File ingestion: **Excel, CSV, DOCX**
- Optional SQL ingestion: **PostgreSQL / MySQL / SQLite**
- Vector embedding generation (**384 / 768 / 1024 dimensions**)
- Local embedding models (**no cost, CPU-based**)
- JSON / JSONL output compatible with vector databases
- Modular backend + React frontend
- Fully runnable **locally** for proof of concept

---

## Architecture Overview
```
Frontend (React + TypeScript)
↓
REST API (Flask)
↓
Embedding Engine
↓
JSON / JSONL Output
```

---

## Supported Embedding Providers

| Provider | Type | Dimensions |
|--------|------|------------|
| sentence-transformers-mini | Local | 384 |
| sentence-transformers-mpnet | Local | 768 |
| sentence-transformers-bge | Local | 1024 |
| OpenAI (optional) | API | 1536 / 3072 |
| Cohere (optional) | API | 1024 |

> **Note:** Local providers are used for the proof of concept and do not require any API key.

---

## Local Setup (Proof of Concept)

### Backend Setup
```bash
cd Backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend runs at:
```
http://127.0.0.1:5000
```

Frontend Setup
```
cd Frontend
npm install
npm run dev
```

Frontend runs at:
```
http://localhost:5173
```

---

## How It Works

1. Upload a file (**Excel / CSV / DOCX**)
2. Choose output type: **Vector Embeddings**
3. Select embedding dimension (e.g. **1024**)
4. Generate embeddings
5. Download output as **JSON**

---

## Output Format (Example)

```json
{
  "id": 1,
  "text": "Sample sentence",
  "embedding": [0.021, -0.882, "..."],
  "dimension": 1024,
  "provider": "sentence-transformers-bge"
}
```

---

## This format is directly ingestible into:
- FAISS
- Pinecone
- Milvus
- Weaviate
- Custom RAG pipelines

---

## Screenshots (Proof of Concept)

| Step | Description | Link |
|-----|------------|------|
| 01 | Frontend Home UI | [View Screenshot](screenshots/01_frontend_home.png) |
| 02 | File Upload | [View Screenshot](screenshots/02_file_upload.png) |
| 03 | Output Selection | [View Screenshot](screenshots/03_output_selection.png) |
| 04 | Embedding Generation | [View Screenshot](screenshots/04_embeddings_generated.png) |
| 05 | Downloaded JSON Output | [View Screenshot](screenshots/05_downloaded_json.png) |
| 06 | Backend Running (Local) | [View Screenshot](screenshots/06_backend_running.png) |

---

## Technologies Used

### Backend
- Python
- Flask
- SQLAlchemy

### Machine Learning
- Sentence-Transformers
- ONNX-ready inference

### Frontend
- React
- TypeScript
- Vite

### Data Processing
- Pandas
- NumPy

### Deployment (Optional)
- Render

---

## Use Cases

- Semantic Search
- Document Similarity
- AI Chatbots (RAG)
- Knowledge Base Indexing
- Enterprise Data Vectorization


---

## Future Enhancements

- Vector database integration (FAISS / Pinecone)
- Authentication
- Batch processing
- Streaming JSONL output

    
---