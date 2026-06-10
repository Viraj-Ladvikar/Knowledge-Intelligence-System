# Groq LLM integration
from langchain_groq import ChatGroq

# Conversational RAG Chain
from langchain.chains import ConversationalRetrievalChain

# Chat Memory
from langchain.memory import ConversationBufferMemory

# Application Config
from config import Config


class LLMService:

    def __init__(self, vector_store):

        # Initialize Groq LLM
        self.llm = ChatGroq(
            api_key=Config.GROQ_API_KEY,
            model="llama-3.3-70b-versatile",
            temperature=0.5
        )

        # Store conversation history
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # Create RAG Chain
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.vectorstore.as_retriever(),
            memory=self.memory
        )

    def get_response(self, query):

        try:

            response = self.chain.invoke(
                {"question": query}
            )

            return response["answer"]

        except Exception as e:

            print(
                f"Error getting response: {e}"
            )

            return (
                "I encountered an error "
                "processing your request."
            )

