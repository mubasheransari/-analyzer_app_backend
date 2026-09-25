from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str = "dev-secret-change-me"
    gemini_api_key: str = ""
    cryptocompare_api_key: str = ""
    admin_api_key: str = "change-this-admin-key"
    database_url: str = "sqlite:///./crypto_app.db"
    allowed_origins: str = "*"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 * 7  # 7 days

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
