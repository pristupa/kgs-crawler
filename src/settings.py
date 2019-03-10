from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host = 'localhost'
    db_name = 'kgs'
    db_user = 'kgs'
    db_password = 'kgs'
    download_games_only = '0'

    class Config:
        env_prefix = 'KGS_CRAWLER_'


settings = Settings()
