import requests


class Bot:

    def __init__(self, token, key):
        self.api_token = token
        self.api_key = key
        self.url = "https://api.trello.com/"
    

    def add_list(self, idBoard, name_list):
        method = '1/lists/'
        params = {
            'key': self.api_key,
            'token': self.api_token,
            'name': name_list,
            'idBoard': idBoard
        }
        response = requests.post(self.url+method, params=params)
        return response


    def delete_list(self, id_list):
        method = f'1/lists/{id_list}'
        params = {
            'key': self.api_key,
            'token': self.api_token,
            'closed': 'true'
        }
        response = requests.put(self.url+method, params=params)
        return response
    

    def get_lists(self, board_id):
        method = f'1/boards/{board_id}/lists'
        params = {
            'key': self.api_key,
            'token': self.api_token,
        }
        response = requests.get(self.url+method, params=params)
        return response