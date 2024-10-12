import os
from haystack import Pipeline
from haystack.utils import Secret
from haystack.components.builders import PromptBuilder
from QASystem.utils import pinecone_config
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.generators import HuggingFaceAPIGenerator

prompt_template = """
    Answer the following question based on the provided context. If the context
    does not have an answer, respond with I do not know.\n
    Query: {{query}}
    Documents:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
    Answer:
"""

HF_API_TOKEN = os.getenv("HUGGINGFACE_TOKEN")


def get_result(query):

    # Create new instances of components for every query
    generator = HuggingFaceAPIGenerator(
        api_type="serverless_inference_api",
        api_params={"model": "HuggingFaceH4/zephyr-7b-beta"},
        token=Secret.from_token(HF_API_TOKEN)
    )

    text_embedder = SentenceTransformersTextEmbedder()  # New instance
    retriever = PineconeEmbeddingRetriever(document_store=pinecone_config())  # New instance
    prompt_builder = PromptBuilder(template=prompt_template)  # New instance

    # Create a new pipeline for each request
    query_pipeline = Pipeline()
    query_pipeline.add_component("text_embedder", text_embedder)
    query_pipeline.add_component("retriever", retriever)
    query_pipeline.add_component("prompt_builder", prompt_builder)
    query_pipeline.add_component("llm", generator)

    # Connect components
    query_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
    query_pipeline.connect("retriever.documents", "prompt_builder.documents")
    query_pipeline.connect("prompt_builder", "llm")

    # Run the pipeline
    results = query_pipeline.run({
        "text_embedder": {"text": query},
        "prompt_builder": {"query": query},
    })

    return results["llm"]["replies"][0]
