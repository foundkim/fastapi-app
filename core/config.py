"""Config module"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Env variables"""

    # General
    API_TITLE: str
    API_HOST: str
    API_PORT: int
    
    # Model
    MODEL_URI: str
    

    model_config = SettingsConfigDict(env_file=".env")


config = Config()