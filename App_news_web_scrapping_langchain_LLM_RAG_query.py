
import os
from dotenv import load_dotenv

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from langchain.document_loaders import WebBaseLoader
from html2text import html2text


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(temperature=0.6, model_name="gpt-3.5-turbo")
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)


def langchain_rag(url, query):
    
    loader = WebBaseLoader(url)
    scrape_data = loader.load()
    data = text_splitter.split_documents(scrape_data)
    
    vectorstore = FAISS.from_documents(data, embedding=embeddings)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever(), 
                                                               memory=memory)
    
    result = conversation_chain({"question": query})
    answer = result["answer"]
    
    return answer

