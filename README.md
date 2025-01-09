

# **Retrieval-Augmented Generation (RAG) QA System**

This project implements a Retrieval-Augmented Generation (RAG) QA System using FastAPI for the backend and Streamlit for the frontend. The system retrieves relevant documents based on user queries, generates responses, and displays them in a user-friendly interface. The backend uses large language models (LLMs) like Mistral and Hugging Face embeddings, while the frontend provides a simple interface for interacting with the backend.

## **Features**

- **FastAPI Backend**: A high-performance RESTful API for serving the RAG model.
- **Streamlit Frontend**: A simple user interface to interact with the backend.
- **Document Retrieval**: Retrieves relevant documents based on the user's question.
- **Answer Generation**: Uses a language model to generate responses based on retrieved documents.
- **Model Integration**: Supports integration with Hugging Face models like Mistral and Sentence-Transformers for embeddings.

## **Directory Structure**

```
Sriram2226-rag-qasystem/
├── app.py              # FastAPI Backend API
├── frontend.py         # Streamlit Frontend
└── requirements.txt     # Required dependencies
```

## **Technologies Used**

- **FastAPI**: For building the backend API.
- **Streamlit**: For building the interactive frontend.
- **Hugging Face Transformers**: For using pre-trained models like Mistral and Sentence-Transformers for document embedding.
- **Chroma**: A vector store to hold document embeddings and perform similarity search.
- **Langchain**: A framework for managing and interacting with machine learning models and documents.
- **Docker**: For containerizing the application.

## **Installation & Setup**

### **1. Clone the Repository**

Start by cloning the repository:

```bash
git clone https://github.com/your-username/Sriram2226-rag-qasystem.git
cd Sriram2226-rag-qasystem
```

### **2. Install Dependencies**

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries, including FastAPI, Streamlit, Hugging Face Transformers, Langchain, and others.

### **3. Set Up Environment Variables**

Create a `.env` file at the root of the project and add the following environment variables:

```
HF_TOKEN=<your-huggingface-token>
MISTRAL_API_KEY=<your-mistral-api-key>
LANGCHAIN_API_KEY=<your-langchain-api-key>
```

These API keys are required to authenticate the use of Hugging Face models and Langchain services.

### **4. Running the Application**

#### **Backend (FastAPI)**

To run the backend (FastAPI), execute the following command:

```bash
uvicorn app:app --reload
```

This will start the backend server on `http://127.0.0.1:8000/`.

#### **Frontend (Streamlit)**

To run the frontend (Streamlit), execute the following command:

```bash
streamlit run frontend.py
```

This will start the frontend on `http://127.0.0.1:8501/`, where you can interact with the QA system.



## **How It Works**

1. **User Input**: The user inputs a question in the Streamlit interface.
2. **Document Retrieval**: The FastAPI backend queries the vector store (Chroma) for documents that are most similar to the question.
3. **Answer Generation**: The relevant documents are passed to the Mistral language model, which generates an answer.
4. **Display Answer**: The generated answer is returned to the frontend and displayed to the user.

## **Model and Embeddings**

- **Mistral Model**: A large language model (LLM) used for generating answers based on retrieved documents.
- **Sentence-Transformers**: Used for embedding documents and finding the most relevant ones based on similarity search.

The model and embeddings can be swapped with other Hugging Face models or custom models by modifying the relevant sections in `app.py`.

## **Environment Variables**

- **HF_TOKEN**: Hugging Face API token for using their models and services.
- **MISTRAL_API_KEY**: API key for accessing Mistral services.
- **LANGCHAIN_API_KEY**: Key for using Langchain services and documents.

![image](https://github.com/user-attachments/assets/66b00a51-f963-455b-b058-bc6b11593d3d)


## **Contributing**

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. We welcome contributions to improve the codebase, fix bugs, and enhance the user experience.

