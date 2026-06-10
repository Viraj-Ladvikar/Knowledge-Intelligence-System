# Import Chroma vector database
from langchain.vectorstores import Chroma

# Import HuggingFace embedding model
from langchain.embeddings import HuggingFaceEmbeddings


class VectorStore:
    """
    Handles document embeddings and vector storage.

    Responsibilities:
    - Convert text into embeddings
    - Store embeddings in ChromaDB
    - Perform similarity search
    """

    def __init__(self, path):
        """
        Initialize vector database.
        """

        # Local embedding model
        # Converts text into vectors
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Initialize Chroma vector database
        self.vectorstore = Chroma(
            persist_directory=path,
            embedding_function=self.embeddings
        )

    def add_documents(self, documents):
        """
        Add processed documents to ChromaDB.

        Parameters:
            documents : List of LangChain Document objects
        """

        self.vectorstore.add_documents(documents)

        # Persist vectors to disk
        self.vectorstore.persist()

    def similarity_search(self, query, k=4):
        """
        Retrieve most relevant document chunks.

        Parameters:
            query : User question
            k     : Number of chunks to retrieve

        Returns:
            List of relevant document chunks
        """

        return self.vectorstore.similarity_search(
            query,
            k=k
        )
