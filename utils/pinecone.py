import config
import os
from typing import List

import pinecone
from langchain.docstore.document import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.vectorstores.base import VST


def configure_environment() -> None:
    """Run this first before other functions here so that environment variables are properly set"""

    os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY
    pinecone.init(api_key=config.PINECONE_API_KEY, environment="us-west4-gcp-free")


def upload_docs(docs: List[Document]) -> None:
    embeddings = OpenAIEmbeddings()

    Pinecone.from_documents(
        documents=docs, embedding=embeddings, index_name=config.PINECONE_INDEX_NAME
    )


def get_vectorstore() -> VST:
    embeddings = OpenAIEmbeddings()

    docsearch = Pinecone.from_existing_index(
        index_name=config.PINECONE_INDEX_NAME, embedding=embeddings
    )

    return docsearch
