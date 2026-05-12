# TODO 
- Adicionar logs do LangSmith

- Adicionar PINECONE ao implementar RAG
    - dependencia
        - uv add langchain-pinecone

    - imports
        - from langchain_community.document_loaders import TextLoader
        - from langchain_text_splitters import CharacterTextSplitter
        - from langchain_pinecone import PineconeVectorStore

    - Insercao
        - loader = TextLoader("rag-pinecone-langsmith/data/data.txt")
        - document = loader.load()
        - settings = GCNNasaSettings()
        - embeddings = LLMClient()
        - pinecone_index_name = settings.INDEX_NAME
        - text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        - texts = text_splitter.split_documents(documents=document)
        - PineconeVectorStore.from_documents(texts, embeddings.embed(), index_name=pinecone_index_name) 