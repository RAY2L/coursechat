from typing import Dict

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores.base import VST


def answer_query(docsearch: VST, query: str) -> Dict[str, str]:
    similar_docs = docsearch.similarity_search(query)
    context = None

    if similar_docs:
        context = "\n\n".join(doc.page_content for doc in similar_docs)

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )

    prompt = f"""\
        You are the summarizer of http://collegecatalog.uchicago.edu/thecollege/computerscience/
        With this context: {context}
        Please answer this: {query}
    """
    print(prompt)
    # print(similar_docs)

    result = qa({"query": prompt})

    return result
