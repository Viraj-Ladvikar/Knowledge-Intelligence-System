# Import Groq LLM integration for LangChain
from langchain_groq import ChatGroq

# Import Conversational Retrieval Chain for RAG
from langchain.chains import ConversationalRetrievalChain

# Import memory to store previous chat conversations
from langchain.memory import ConversationBufferMemory

# Import application configuration variables
from config import Config


class LLMService:

    # Constructor method called when object is created
    def __init__(self, vector_store):

        # Initialize Groq LLM
        self.llm = ChatGroq(

            # Read API key from Config class
            groq_api_key=Config.GROQ_API_KEY,

            # Groq model to use
            model_name="llama-3.3-70b-versatile",

            # Controls creativity of response
            # 0 = deterministic
            # 1 = more creative
            temperature=0.5
        )

        # Store chat history in memory
        self.memory = ConversationBufferMemory(

            # Key used internally by LangChain
            memory_key="chat_history",

            # Store messages as HumanMessage and AIMessage objects
            return_messages=True
        )

        # Create RAG conversational chain
        self.chain = ConversationalRetrievalChain.from_llm(

            # LLM used to generate answers
            llm=self.llm,

            # Retrieve relevant chunks from ChromaDB
            retriever=vector_store.vectorstore.as_retriever(),

            # Attach conversation memory
            memory=self.memory
        )

    # Method used to get answer from LLM
    def get_response(self, query):

        try:

            # Send user question to RAG pipeline
            response = self.chain({
                "question": query
            })

            # Return generated answer
            return response["answer"]

        except Exception as e:

            # Print error in terminal for debugging
            print(f"Error getting LLM response: {e}")

            # Return friendly message to user
            return "I encountered an error processing your request."

