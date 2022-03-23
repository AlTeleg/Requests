import requests


class SuperHero:
    url = "https://superheroapi.com/api/"

    def __init__(self, token):
        self.token = token

    def get_char_id(self, name):
        response = requests.get(SuperHero.url + self.token + "/search/" + name)
        print(f'id-{response.json()["results"][0]["id"]}')
        return response.json()['results'][0]['id']

    def get_char_int(self, name):
        char_id = SuperHero.get_char_id(self, name)
        response = requests.get(SuperHero.url + self.token + "/" + char_id)
        print(f'{name}: int-{response.json()["powerstats"]["intelligence"]}')
        return response.json()['powerstats']['intelligence']

    def top_int(self, char_list):
        char_dict = {}
        winner_list = []
        for char in char_list:
            char_int = self.get_char_int(char)
            char_dict[char] = char_int
        char_dict = dict(sorted(char_dict.items(), key=lambda x: int(x[1]), reverse=True))
        winner_list.append(list(char_dict.keys())[0])
        for key, value in char_dict.items():
            if list(char_dict.values())[0] == value and list(char_dict.keys())[0] != key:
                winner_list.append(key)
        print(f'\nТоп по характеристике <интеллект> - {",".join(winner_list)} ! ')
        return list(char_dict.keys())[0]


if __name__ == "__main__":
    new_client1 = SuperHero("2619421814940190")
    heroes = ["Hulk", "Captain America", "Thanos"]
    new_client1.top_int(heroes)
