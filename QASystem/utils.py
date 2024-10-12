import os

from dotenv import load_dotenv

from haystack_integrations.document_stores.pinecone import PineconeDocumentStore

load_dotenv()
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["HF_API_TOKEN"] = os.getenv("HUGGINGFACE_TOKEN")


def pinecone_config():
    # configuring pinecone database
    document_store = PineconeDocumentStore(
        index="default",
        namespace="default",
        dimension=768
    )
    return document_store
