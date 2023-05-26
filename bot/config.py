from pydantic import BaseSettings

class Config(BaseSettings):
    token: str
    version: str = "0.0.1"
    admin_list_id: list = []
  
    class Config:
        env_file = ".env"

