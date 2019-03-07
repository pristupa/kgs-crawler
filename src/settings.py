from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_prefix = 'KGS_CRAWLER_'

    db_host = 'localhost'
    db_name = 'kgs'
    db_user = 'kgs'
    db_password = 'kgs'


settings = Settings()
