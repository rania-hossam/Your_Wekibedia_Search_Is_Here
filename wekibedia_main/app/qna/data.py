from typing import List

from langchain.schema import Document
from langchain.document_loaders import WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_wikibidia_docs(paper_topic_query, num_docs=10) -> List[Document]:
    loader = WikipediaLoader(
        paper_topic_query,
        load_max_docs=num_docs,
        load_all_available_meta=True
    )
    raw_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 500,
    chunk_overlap  = 20,
    length_function = len,
    add_start_index = True,
    )
    documents = text_splitter.split_documents(raw_documents)
    return documents