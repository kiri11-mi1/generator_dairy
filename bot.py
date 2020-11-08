import requests


class Bot:
    '''Бота дла работы с Trello'''

    def __init__(self, token, key):
        self.api_token = token
        self.api_key = key
        self.url = "https://api.trello.com/1/"
    

    def add_list(self, idBoard, name_list):
        method = 'lists/'
        params = {
            'key': self.api_key,
            'token': self.api_token,
            'name': name_list,
            'idBoard': idBoard
        }
        response = requests.post(self.url+method, params=params)
        return response


    def delete_list(self, id_list):
        method = f'lists/{id_list}'
        params = {
            'key': self.api_key,
            'token': self.api_token,
            'closed': 'true'
        }
        response = requests.put(self.url+method, params=params)
        return response
    

    def get_lists(self, board_id):
        method = f'boards/{board_id}/lists'
        params = {
            'key': self.api_key,
            'token': self.api_token,
        }
        response = requests.get(self.url+method, params=params)
        return response
    

    def create_card(self, list_id, name_card):
        method = 'cards'
        params = {
            'key': self.api_key,
            'token': self.api_token,
            'idList': list_id,
            'name': name_card
        }
        response = requests.post(self.url+method, params=params)
        return response


    def add_comment(self, id_card, text):
        method = f'cards/{id_card}/actions/comments'
        params = {
            'key': self.api_key,
            'token': self.api_token,
            'text': text
        }
        response = requests.post(self.url+method, params=params)
        return response


    def get_cards(self, list_id):
        method = f'lists/{list_id}/cards'
        params = {
            'key': self.api_key,
            'token': self.api_token,
        }
        response = requests.get(self.url+method, params=params)
        return response
