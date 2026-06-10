# =====================================================
# KNOWLEDGE INTELLIGENCE SYSTEM
# Main Flask Application
# =====================================================

# =========================
# Project Imports
# =========================

# Vector database service (ChromaDB)
from models.vector_store import VectorStore

# MinIO storage service
from services.storage_service import S3Storage

# Groq LLM service
from services.llm_service import LLMService

# Application configuration
from config import Config


# =========================
# Python Built-in Imports
# =========================

import os
import tempfile
import logging


# =========================
# Flask Imports
# =========================

from flask import (
    Flask,
    request,
    render_template,
    jsonify
)


# =========================
# LangChain Imports
# =========================

# PDF Loader
from langchain_community.document_loaders import (
    PyPDFLoader
)

# Text Loader
from langchain_community.document_loaders import (
    TextLoader
)

# Text Chunking
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)


# =====================================================
# APPLICATION INITIALIZATION
# =====================================================

# Create Flask application
app = Flask(__name__)

# Initialize Vector Store
vector_store = VectorStore(
    Config.VECTOR_DB_PATH
)

# Initialize MinIO Storage
storage_service = S3Storage()

# Initialize Groq LLM Service
llm_service = LLMService(
    vector_store
)


# =====================================================
# LOGGING CONFIGURATION
# =====================================================

logging.basicConfig(
    level=logging.DEBUG
)

logger = logging.getLogger(
    __name__
)


# =====================================================
# HOME PAGE
# =====================================================

@app.route('/')
def index():
    """
    Render application homepage.
    """

    return render_template(
        'index.html'
    )


# =====================================================
# DOCUMENT PROCESSING
# =====================================================

def process_document(file):
    """
    Process uploaded file.

    Supported Formats:
    ------------------
    - PDF
    - TXT

    Workflow:
    ---------
    Upload File
        ↓
    Extract Text
        ↓
    Split Into Chunks
        ↓
    Return Chunks

    Returns:
        List[Document]
    """

    # Create temporary folder
    temp_dir = tempfile.mkdtemp()

    # Temporary file path
    temp_path = os.path.join(
        temp_dir,
        file.filename
    )

    try:

        logger.info(
            f"Processing file: {file.filename}"
        )

        # Save file temporarily
        file.save(temp_path)

        # =================================
        # PDF Processing
        # =================================

        if file.filename.endswith(".pdf"):

            loader = PyPDFLoader(
                temp_path
            )

            documents = loader.load()

        # =================================
        # Text File Processing
        # =================================

        elif file.filename.endswith(".txt"):

            loader = TextLoader(
                temp_path
            )

            documents = loader.load()

        else:

            raise ValueError(
                "Unsupported file type"
            )

        # =================================
        # Text Chunking
        # =================================

        text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
        )

        text_chunks = (
            text_splitter.split_documents(
                documents
            )
        )

        logger.info(
            f"Created {len(text_chunks)} chunks"
        )

        return text_chunks

    except Exception as e:

        logger.error(
            f"Error processing document: {e}"
        )

        raise

    finally:

        # Remove temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

        # Remove temporary directory
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)


# =====================================================
# FILE UPLOAD ENDPOINT
# =====================================================

@app.route(
    '/upload',
    methods=['POST']
)
def upload_document():
    """
    Upload document endpoint.

    Workflow:
    ---------

    User Uploads File
            ↓
    Validate File
            ↓
    Extract Text
            ↓
    Create Chunks
            ↓
    Upload Original File
            ↓
    Store Embeddings
            ↓
    Success Response
    """

    try:

        logger.info(
            "Upload endpoint called"
        )

        # Validate file exists
        if 'file' not in request.files:

            return jsonify({
                "error":
                "No file provided"
            }), 400

        file = request.files['file']

        # Empty file validation
        if file.filename == '':

            return jsonify({
                "error":
                "No file selected"
            }), 400

        # Supported file types
        if not file.filename.endswith(
            (
                '.pdf',
                '.txt'
            )
        ):

            return jsonify({
                "error":
                "Only PDF and TXT files are supported"
            }), 400

        # Process document
        text_chunks = process_document(
            file
        )

        # Reset file pointer
        file.seek(0)

        # Upload original file to MinIO
        upload_success = (
            storage_service.upload_file(
                file,
                file.filename
            )
        )

        if not upload_success:

            return jsonify({
                "error":
                "Failed to upload file to MinIO"
            }), 500

        # Store vectors in ChromaDB
        vector_store.add_documents(
            text_chunks
        )

        return jsonify({
            "message":
            "Document uploaded successfully",

            "chunks_processed":
            len(text_chunks)
        })

    except Exception as e:

        logger.error(
            f"Upload error: {e}"
        )

        return jsonify({
            "error": str(e)
        }), 500


# =====================================================
# QUESTION ANSWERING ENDPOINT
# =====================================================

@app.route(
    '/query',
    methods=['POST']
)
def query():
    """
    RAG Question Answering

    Workflow:
    ---------

    User Question
          ↓
    Chroma Retriever
          ↓
    Relevant Chunks
          ↓
    Groq LLM
          ↓
    Final Answer
    """

    try:

        data = request.json

        if (
            not data
            or
            'question'
            not in data
        ):

            return jsonify({
                "error":
                "Question is required"
            }), 400

        response = (
            llm_service.get_response(
                data['question']
            )
        )

        return jsonify({
            "response":
            response
        })

    except Exception as e:

        logger.error(
            f"Query error: {e}"
        )

        return jsonify({
            "error":
            str(e)
        }), 500


# =====================================================
# APPLICATION ENTRY POINT
# =====================================================

if __name__ == "__main__":

    logger.info(
        "Starting Knowledge Intelligence System"
    )

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
