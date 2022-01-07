from pydantic import BaseSettings,Field

class Settings(BaseSettings):
    db_user: str = Field(...,env='DB_USER')
    db_password: str = Field(...,env='DB_PASSWORD')
    db_name: str = Field(...,env='DB_NAME')
    db_host: str = Field(...,env='DB_HOST')
    db_port: str = Field(...,env='DB_PORT')


    class Config():
        env_file = '.env'   