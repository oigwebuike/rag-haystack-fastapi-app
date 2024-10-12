from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack.components.converters import PyPDFToDocument
from QASystem.utils import pinecone_config

from pathlib import Path


def ingest(document_store):
    indexing = Pipeline()
    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))
    indexing.connect("converter", "splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    indexing.run({"converter": {"sources": [Path("../data/comprehensive_overview_llm.pdf")]}})


if __name__ == "__main__":
    ds = pinecone_config()
    ingest(ds)
