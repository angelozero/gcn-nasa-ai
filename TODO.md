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


PYTHON
MODELS
PROMPT
PROMPT ENGINEERING
CONTEXT ENGINEERING
TEMPLATES
EMBEDDING
POSTGRES (com pgvector)
DATABRICKS
RAG
PINECONE
SDK
SKILLS
TOOLS
HyDE (Hypothetical Document Embeddings)
GRAPHRAG (Neo4j)
AI GATEWAY (LiteLLM / Fallback / Rate Limiting)
MCP (Model Context Protocol)
LANGCHAIN
LANGGRAPH
AGENTES
HOOKS
HALF-LOOP
LONG-TERM MEMORY (Episodic & Semantic)
EVENT STREAMING (SSE / UI Tracing)
ARQUITETURA
PII SERVICE
ANONIMIZAÇÃO
PROMPT INJECTION SHIELD
GUARDRAILS
OTEL (OpenTelemetry)
EXPERIMENTS
MLFLOW
JUDGES (LLM-as-a-Judge)
EVAL SERVICE
E2E (End-to-End Testing)
HARNESS (https://www.youtube.com/watch?v=uezD0dRdz9Q)
RATE LIMIT
DEEP AGENT
MELHORES PRATICAS
CLEAN ARCH