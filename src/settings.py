from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host = 'localhost'
    db_name = 'kgs'
    db_user = 'kgs'
    db_password = 'kgs'

    class Config:
        env_prefix = 'KGS_CRAWLER_'


settings = Settings()
