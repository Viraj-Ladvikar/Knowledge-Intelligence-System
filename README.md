
# Knowledge Intelligence System

A Retrieval-Augmented Generation (RAG) based Knowledge Intelligence System that enables users to upload documents, store embeddings in a vector database, and query information using Large Language Models (LLMs).

## Features

* Document Upload and Processing
* Vector Embeddings with ChromaDB
* Retrieval-Augmented Generation (RAG)
* Groq LLM Integration
* Local File Storage
* Flask-based Web Interface

---

## Project Structure

```text
Knowledge-Intelligence-System/
│
├── app/
│   ├── models/
│   ├── services/
│   ├── static/
│   ├── template/
│   ├── .env
│   ├── config.py
│   └── main.py
│
├── demo/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Prerequisites

* Python 3.11
* Git
* Groq API Key

---

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Knowledge-Intelligence-System
```

### Step 2: Create Virtual Environment

```bash
py -3.11 -m venv llmapp311
```

### Step 3: Activate Virtual Environment

#### Windows PowerShell

```powershell
.\llmapp311\Scripts\Activate.ps1
```

#### Git Bash

```bash
source llmapp311/Scripts/activate
```

### Step 4: Upgrade Pip

```bash
python -m pip install --upgrade pip setuptools wheel
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file inside the `app` directory.

```env
GROQ_API_KEY=your_groq_api_key
```

> Replace `your_groq_api_key` with your actual Groq API key.

---

## Run the Application

```bash
python app/main.py
```

Application will start on:

```text
http://localhost:5000
```

---

## Git Ignore

Do not commit virtual environments or secrets.

Example:

```gitignore
llmapp311/
.env
__pycache__/
```

---

## Tech Stack

* Python 3.11
* Flask
* LangChain
* ChromaDB
* Groq
* PyPDF
* Unstructured

---

## Notes

* Python 3.11 is recommended.
* Do not commit API keys to GitHub.
* Keep the `.env` file private.
* Virtual environments should not be pushed to GitHub.

```

```
