import requests


class JsonPlaceHolderSite:

    def __init__(self, base_url="https://jsonplaceholder.typicode.com/"):
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_all_posts(self):
        response = self.session.get(url=f"{self.base_url}/posts",
                                    headers=self.session.headers)
        return response

    def get_user_by_id(self, id_: int):
        response = self.session.get(url=f"{self.base_url}/users/{id_}",
                                    headers=self.session.headers)
        return response

    def get_posts_by_id(self, id_: int):
        response = self.session.get(url=f"{self.base_url}/posts/{id_}",
                                    headers=self.session.headers)
        return response

    def post_create_post_by_user(self, data):
        response = self.session.post(url=f"{self.base_url}/posts",
                                    headers=self.session.headers,
                                    json=data)
        return response

    def patch_post_by_post_id(self, id_: int, data):
        response = self.session.get(url=f"{self.base_url}/posts/{id_}",
                                    headers=self.session.headers,
                                    json=data)
        return response
