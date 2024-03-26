import requests


class DogCeoSite:

    def __init__(self, base_url="https://dog.ceo/api/breed"):
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_list_all_pets(self):
        response = self.session.get(url=f"{self.base_url}s/list/all",
                                    headers=self.session.headers)
        return response

    def get_random_image(self):
        response = self.session.get(url=f"{self.base_url}s/image/random",
                                    headers=self.session.headers)
        return response

    def get_random_image_by_breed(self, breed: str):
        response = self.session.get(url=f"{self.base_url}/{breed}/images/random",
                                    headers=self.session.headers)
        return response

    def get_image_by_breed(self, breed: str):
        response = self.session.get(url=f"{self.base_url}/{breed}/images",
                                    headers=self.session.headers)
        return response

    def get_list_by_sub_breed(self, breed: str):
        response = self.session.get(url=f"{self.base_url}/{breed}/list",
                                    headers=self.session.headers)
        return response
