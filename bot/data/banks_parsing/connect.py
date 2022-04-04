import httpx


class Connect:
    response = ""
    status_code = 0

    def __init__(self, url, headers):
        self.response = httpx.get(url, headers=headers)
        self.status_code = self.response.status_code
