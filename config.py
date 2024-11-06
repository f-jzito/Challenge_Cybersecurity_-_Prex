from os import getenv

from dotenv import load_dotenv

load_dotenv()

class Config:
    TOOL: str = getenv('TOOL')
    USER_TOKEN : str = getenv('USER_TOKEN')