"""Wrapper do cliente LLM que roteia requisições pelo proxy LiteLLM."""

import logging
from openai import OpenAI
from app.llm.llm_settings import LLMSettings
from app.config.llm_models import LLMModels

logger = logging.getLogger(__name__)


class LLMClient:
    """Wrapper fino sobre o SDK da OpenAI apontando para o proxy LiteLLM local.

    Responsabilidades:
    - Carregar suas próprias configurações de conexão (LLMSettings) do .env.
    - Manter uma única instância ``openai.OpenAI`` configurada para o LiteLLM.
    - Expor ``chat()`` para geração de texto (usado por classificadores / agentes).
    - Expor ``embed()`` para embeddings vetoriais (usado pelo pipeline RAG).

    Nenhuma lógica de negócio vive aqui — quem chama decide qual modelo usar
    e quais mensagens enviar.
    """

    def __init__(self) -> None:
        # Carrega configurações exclusivas do LLM diretamente do .env
        settings = LLMSettings()
        self._client = OpenAI(
            base_url=settings.LITELLM_BASE_URL,
            api_key=settings.LITELLM_API_KEY.get_secret_value(),
        )
        logger.debug(
            "LLMClient inicializado — base_url=%s", settings.LITELLM_BASE_URL
        )

    # ── Geração de texto ─────────────────────────────────────────────────────

    def chat(self, model: str, messages: list[dict]) -> str:
        """Envia uma requisição de chat e retorna o conteúdo da resposta do assistente.

        Args:
            model: Alias do modelo no LiteLLM (ex: ``LLMModels.CLASSIFIER``).
            messages: Lista de mensagens no formato OpenAI, ex:
                ``[{"role": "user", "content": "..."}]``.

        Returns:
            A resposta do assistente como string simples.
        """
        logger.debug("chat() model=%s mensagens=%d", model, len(messages))
        response = self._client.chat.completions.create(
            model=model,
            messages=messages,  # type: ignore[arg-type]
        )
        content = response.choices[0].message.content or ""
        logger.debug(
            "chat() tokens_resposta=%d",
            response.usage.total_tokens if response.usage else 0,
        )
        return content

    # ── Embeddings ───────────────────────────────────────────────────────────

    def embed(self, text: str) -> list[float]:
        """Gera embedding usando o modelo remoto (LiteLLM proxy)."""
        return self._embed(text=text, llm_model=LLMModels.EMBEDDER)

    def ollama_embed(self, text: str) -> list[float]:
        """Gera embedding usando o modelo local (Ollama)."""
        return self._embed(text=text, llm_model=LLMModels.OLLAMA_EMBEDDER)

    def _embed(self, text: str, llm_model: str) -> list[float]:
        """Gera um embedding vetorial para o *texto* fornecido.

        Args:
            text: A string de entrada a ser transformada em vetor.

        Returns:
            Lista de floats representando o vetor de embedding.
        """
        logger.debug(
            "embed() model=%s tamanho_texto=%d", llm_model, len(text)
        )
        response = self._client.embeddings.create(
            model=llm_model,
            input=text,
        )
        return response.data[0].embedding