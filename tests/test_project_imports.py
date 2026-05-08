from lc_learning.config import get_settings


def test_settings_loads_defaults() -> None:
    settings = get_settings()
    assert settings.model_provider == "deepseek"
    assert settings.model_name
    assert settings.model_base_url == "https://api.deepseek.com"
