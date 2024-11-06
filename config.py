from os import getenv

from dotenv import load_dotenv

load_dotenv()

class Config:
    TOOL: str = getenv('TOOL')
    USER_TOKEN : str = getenv('USER_TOKEN')
    DB_NAME: str = getenv('DB_NAME')
    DB_USER: str = getenv('DB_USER')
    DB_PASSWORD: str = getenv('DB_PASSWORD')
    DB_HOST: str = getenv('DB_HOST')
    DB_PORT: str = getenv('DB_PORT')