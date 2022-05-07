import requests


class YaUploader:
    host = "https://cloud-api.yandex.net:443"

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': True}
        upload_link = requests.get(url, params=params, headers=headers).json().get('href')
        requests.put(upload_link, data=open(file_path, 'rb'), headers=headers)


if __name__ == '__main__':
    path_to_file = 'hello_world.txt'
    token = "AQAAAAAdvyV6AADLW2spxmlI_EQehK_vgDHZL3M"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
