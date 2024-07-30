from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'OPENAI_API_KEY')

embeddings = OpenAIEmbeddings()

#video_url = "https://youtu.be/-Osca2Zax4Y?si=iyOiePxzUy_bUayO"
def yt_vectordb(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)

    return db

def query_response(db, query, k=4):
    # text-davinci can handle 4097 tokens
    # be mindful of how many tokens a model can handle

    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = ChatOpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY, max_tokens=5000, model_name='gpt-4o-mini')

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful YouTube assistant that can answer questions about videos based on the video's transcript.

        Answer the following question: {question}
        By searching the following video transcript: {docs}

        Only use the factual information from the transcript to answer the question.

        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be detailed.
        """
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"question": query, "docs": docs_page_content})
    response = response.replace("\n", "")
    return response

# print(query_response(yt_vectordb("https://youtu.be/-Osca2Zax4Y?si=iyOiePxzUy_bUayO"), "What did they talk about Ransomware"))