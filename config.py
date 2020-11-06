import os


class Config:
    API_TOKEN = os.environ.get('API_TOKEN')
    API_KEY = os.environ.get('API_KEY')
    GROUP_ID = 5080
    BOARD_ID = '5fa5484fd6ce8d73af2b2e7a'