from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    sqlalchemy_uri:str = "mysql+aiomysql://avnadmin:AVNS_Iikg04VtR779Zq_RmtE@mysql-14a9ee6a-serhii-4322.j.aivencloud.com:11907/Tournaments"
    secret_key:str = "your_secret"
    exp_time_minutes:int = 30


settings = Settings()
