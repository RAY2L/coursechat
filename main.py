#!/usr/bin/env python3
from utils import generate_major_docs


def main():
    major = "computerscience"

    # Generate a list of Document's to upload to Pinecone index
    docs = generate_major_docs(major)

    print(docs[36])


if __name__ == "__main__":
    main()
