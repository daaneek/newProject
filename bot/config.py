from pydantic import BaseSettings


class Config(BaseSettings):
    token: str
    version: str = "0.0.1"
    admin_list_id: list = []
    path_dir_dictionaries: str = "bot/data"

    class Config:
        env_file = ".env"
