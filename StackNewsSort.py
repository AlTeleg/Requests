import requests
from pprint import pprint
import datetime


class StackOverFlow():

    def get_headers(self):

        return {
            'Content-Type': 'application/json'
        }

    def get_questions(self):

        url = "https://api.stackexchange.com/2.2/questions"
        headers = self.get_headers()
        params = {"site": "stackoverflow.com"}
        response = requests.get(url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()


def make_sorted_q_list(obj, tag):

    dt_now = int(datetime.datetime.now().timestamp())
    new_json = []
    for q in obj['items']:
        if tag.lower() in q['tags'] and ((dt_now - q['creation_date']) <= 172800):
            new_json.append(q)
    pprint(new_json)
    return new_json


if __name__ == '__main__':
    client1 = StackOverFlow()
    make_sorted_q_list(client1.get_questions(), 'Python')




