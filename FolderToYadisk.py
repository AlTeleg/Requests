import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload(self, file_path: str, disk_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_list = os.listdir(file_path)
        for file in file_list:
            href = self._get_upload_link(disk_file_path=disk_path+file).get("href", "")
            response = requests.put(href, data=open(file_path+file, 'rb'))
            if response.status_code == 201:
                print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:/Users/Саня/Documents/1/"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, "/Proj/")