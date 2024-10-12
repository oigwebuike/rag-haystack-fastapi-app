from setuptools import find_packages, setup

setup(
    name="RAG with Haystack",
    version="v0.0.1",
    author="Igwebuike Onyeka Daniel",
    packages=find_packages(),
    install_requires=["pinecone_haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib"]
)