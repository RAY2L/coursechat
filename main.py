#!/usr/bin/env python3
import os
from utils.pinecone import configure_environment
from utils.evaluations import fetch_json, data_to_str_list
from CustomSplitter import CustomSplitter

from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain


def main():
    configure_environment()

    eval_json_path = os.path.join(
        os.getcwd(), "instructors/timng/CMSC_28000-Spring_2023.json"
    )

    data = fetch_json(eval_json_path)
    str_list = data_to_str_list(data)

    text_splitter = CustomSplitter()
    docs = text_splitter.create_documents(str_list)

    llm = OpenAI()

    chain = load_summarize_chain(llm, chain_type="refine", verbose=True)
    final_response = chain.run(docs)

    print(final_response)


if __name__ == "__main__":
    main()
