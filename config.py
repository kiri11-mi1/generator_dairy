import os


class Config:
    API_TOKEN = os.environ.get('API_TOKEN') or '3d2bd54f52ad3f7c013124d8f6bd374a8ea9026eb51819ecb3cdf486fe97b378'
    API_KEY = os.environ.get('API_KEY') or 'ba12babcba719e912b85e3a8e7ca4056'
    GROUP_ID = 5080
    BOARD_ID = '5fa5484fd6ce8d73af2b2e7a'