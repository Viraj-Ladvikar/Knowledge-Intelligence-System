
# Knowledge Intelligence System

## Overview

Knowledge Intelligence System is a Retrieval-Augmented Generation (RAG) application built using Flask, LangChain, ChromaDB, Groq LLM, HuggingFace Embeddings, and MinIO Object Storage.

The system allows users to:

* Upload PDF and TXT documents
* Store original files in MinIO
* Convert document content into vector embeddings
* Store embeddings in ChromaDB
* Ask natural language questions
* Retrieve relevant document chunks
* Generate context-aware answers using Groq LLM

---

# Features

### Document Upload

Supports:

* PDF Files
* Text Files

### Document Processing

* Extract text from documents
* Split documents into chunks
* Generate embeddings
* Store vectors in ChromaDB

### Retrieval-Augmented Generation (RAG)

* Semantic Search
* Context Retrieval
* LLM-based Answer Generation

### Object Storage

Uses MinIO as an S3-compatible storage solution.

### Conversational Memory

Maintains conversation history using LangChain memory.

---

# System Architecture

```text
User
 │
 ▼
Flask UI
 │
 ├────────────── Upload Document
 │                      │
 │                      ▼
 │              Document Loader
 │                      │
 │                      ▼
 │              Text Splitter
 │                      │
 │                      ▼
 │          HuggingFace Embeddings
 │                      │
 │                      ▼
 │                 ChromaDB
 │
 │
 └────────────── Ask Question
                        │
                        ▼
                  Retriever
                        │
                        ▼
               Relevant Chunks
                        │
                        ▼
                    Groq LLM
                        │
                        ▼
                    Response
```

---

# Project Structure

```text
Knowledge-Intelligence-System
│
├── app
│   │
│   ├── main.py
│   ├── config.py
│   │
│   ├── models
│   │   └── vector_store.py
│   │
│   ├── services
│   │   ├── llm_service.py
│   │   └── storage_service.py
│   │
│   ├── templates
│   │   └── index.html
│   │
│   └── static
│       └── style.css
│
├── vector_db
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md
```

---

# Technologies Used

## Backend

* Python 3.11
* Flask

## LLM

* Groq
* Llama 3.3 70B Versatile

## RAG Framework

* LangChain

## Vector Database

* ChromaDB

## Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

## Object Storage

* MinIO

## Document Processing

* PyPDF
* TextLoader

---

# Setup Guide

## Step 1: Clone Repository

```bash
git clone <repository-url>

cd Knowledge-Intelligence-System
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv llmapp
```

Activate:

### Windows PowerShell

```powershell
.\llmapp\Scripts\Activate.ps1
```

### CMD

```cmd
llmapp\Scripts\activate.bat
```

---

## Step 3: Upgrade Pip

```bash
python -m pip install --upgrade pip
```

---

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key

MINIO_ENDPOINT=http://localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin123
MINIO_BUCKET_NAME=knowledge-intelligence-system
```

---

# MinIO Setup

## Run MinIO Using Docker

```powershell
docker run -p 9000:9000 -p 9001:9001 `
-e MINIO_ROOT_USER=minioadmin `
-e MINIO_ROOT_PASSWORD=minioadmin123 `
minio/minio server /data --console-address ":9001"
```

---

## Open MinIO Console

```text
http://localhost:9001
```

Login:

```text
Username:
minioadmin

Password:
minioadmin123
```

Create bucket:

```text
knowledge-intelligence-system
```

---

# Run Application

```bash
python app/main.py
```

Expected Output:

```text
Running on:
http://127.0.0.1:8080
```

Open Browser:

```text
http://localhost:8080
```

---

# Upload Flow

```text
User Uploads PDF
        │
        ▼
Flask Upload API
        │
        ▼
Save Temporary File
        │
        ▼
PDF/Text Loader
        │
        ▼
Text Extraction
        │
        ▼
Chunk Creation
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
Upload Original File to MinIO
```

---

# Query Flow

```text
User Question
       │
       ▼
Retriever
       │
       ▼
Relevant Chunks
       │
       ▼
Groq LLM
       │
       ▼
Generated Answer
```

---

# API Endpoints

## Home

```http
GET /
```

Loads application UI.

---

## Upload Document

```http
POST /upload
```

Request:

```form-data
file : PDF/TXT
```

Response:

```json
{
  "message": "Document uploaded successfully",
  "chunks_processed": 44
}
```

---

## Query

```http
POST /query
```

Request:

```json
{
  "question": "What is machine learning?"
}
```

Response:

```json
{
  "response": "Generated answer"
}
```

---

# Vector Database

ChromaDB stores:

```text
Chunk Text
Embedding Vector
Metadata
```

Used for:

* Semantic Search
* Similarity Search
* Context Retrieval

---

# Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

Advantages:

* Lightweight
* Fast
* Open Source
* Good Semantic Search Performance

---

# Groq LLM

Model:

```text
llama-3.3-70b-versatile
```

Purpose:

* Context Understanding
* Question Answering
* RAG Response Generation

---

# Error Handling

The application handles:

* Invalid Files
* Unsupported Formats
* Missing Documents
* MinIO Upload Failures
* Groq API Errors
* ChromaDB Errors

---

# Future Improvements

* Multi-file upload
* Streaming responses
* User authentication
* Document deletion
* Citation support
* Hybrid search
* Re-ranking
* Conversation history persistence

---

# Resume Project Description

Knowledge Intelligence System is a Retrieval-Augmented Generation (RAG) application developed using Flask, LangChain, ChromaDB, Groq LLM, HuggingFace Embeddings, and MinIO. The system enables users to upload PDF/TXT documents, perform semantic search, retrieve contextually relevant information, and generate accurate responses using large language models. Implemented document ingestion, chunking, vector embedding generation, object storage, and conversational retrieval pipelines.

```

```
