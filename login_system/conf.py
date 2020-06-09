from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    '''
    Loads the secret key from the env file
    '''
    SECRET_KEY = os.getenv('KEY')
    SQLALCHEMY_DATABASE_URI = 'sql:///site.db'

    #Currently debug is set to true. It will be removed in the future
    DEBUG = True