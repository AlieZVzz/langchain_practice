from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from lc_learning.config import get_settings


def build_chat_model(temperature: float = 0.2) -> ChatOpenAI:
    settings = get_settings()
    if settings.model_provider not in {"deepseek", "openai-compatible"}:
        raise ValueError(f"Unsupported MODEL_PROVIDER: {settings.model_provider}")
    if not settings.api_key:
        raise ValueError("Missing API key. Set DEEPSEEK_API_KEY in .env.")

    return ChatOpenAI(
        model=settings.model_name,
        temperature=temperature,
        api_key=SecretStr(settings.api_key),
        base_url=settings.model_base_url,
    )
