__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain import hub
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# Load environment variables
HF_TOKEN = os.getenv("HF_TOKEN")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

if not HF_TOKEN or not MISTRAL_API_KEY:
    raise EnvironmentError("Required environment variables are missing in .env file")

# Initialize services
llm = ChatMistralAI(model="mistral-large-latest")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector_store = Chroma(embedding_function=embeddings)

# Define FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class QuestionRequest(BaseModel):
    question: str

# Define prompt loader
prompt = hub.pull("rlm/rag-prompt")

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Retrieve documents from vector store
        retrieved_docs = vector_store.similarity_search(request.question)
        docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

        # Generate answer
        messages = prompt.invoke({"question": request.question, "context": docs_content})
        response = llm.invoke(messages)
        return {"answer": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))