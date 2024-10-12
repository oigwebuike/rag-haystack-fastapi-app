# RAG with Haystack, Pinecone, and FastAPI

## Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline using Haystack, Pinecone, and FastAPI. The goal is to create a system that retrieves relevant documents based on a query and then generates a response using a language model. The FastAPI web framework is used to expose this functionality via a web interface.

## Features
- **Document Ingestion**: Convert PDF documents into chunks using sentence-based splitting.
- **Document Embedding**: Embed documents using SentenceTransformers for effective retrieval.
- **Query Processing**: Retrieve relevant documents from Pinecone and generate responses based on them using a Hugging Face LLM model.
- **FastAPI Web Interface**: Provides a user-friendly web interface for querying the system and getting responses.

