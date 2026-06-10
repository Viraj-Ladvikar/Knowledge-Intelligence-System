
# Import Chroma vector database from LangChain Community
from langchain_community.vectorstores import Chroma

# Import HuggingFace embedding model
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorStore:
    """
    Handles document embeddings and vector storage.

    Responsibilities:
    - Convert text into embeddings
    - Store embeddings in ChromaDB
    - Perform similarity search
    """

    def __init__(self, path):

        # Embedding model used to convert text into vectors
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
        Add documents to ChromaDB.
        """

        self.vectorstore.add_documents(documents)

    def similarity_search(self, query, k=4):
        """
        Search similar chunks.
        """

        return self.vectorstore.similarity_search(
            query,
            k=k
        )

