import requests


class OpenBrewerySite:

    def __init__(self, base_url="https://api.openbrewerydb.org/v1/breweries"):
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_list_all_breweries(self):
        response = self.session.get(url=f"{self.base_url}",
                                    headers=self.session.headers)
        return response

    def get_brewery_by_id(self, id_: str):
        response = self.session.get(url=f"{self.base_url}/{id_}",
                                    headers=self.session.headers)
        return response

    def get_random_any_breweries(self, size: int):
        response = self.session.get(url=f"{self.base_url}/random?size={size}",
                                    headers=self.session.headers
                                    )
        return response

    def get_search_brewery_by_id(self, id_: str):
        response = self.session.get(url=f"{self.base_url}/search?query={id_}",
                                    headers=self.session.headers)
        return response

    def get_search_brewery_by_another_params(self, params: str, value: str):
        response = self.session.get(url=f"{self.base_url}?{params}={value}",
                                    headers=self.session.headers)
        return response
