import httpx

"""Класс, который устанавливает соединение к сайту по url и получает response ответ"""


class Connect:

    def __init__(self, url, headers):
        self.response = httpx.get(url, headers=headers)
        self.status_code = self.response.status_code
