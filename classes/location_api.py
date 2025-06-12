from interfaces.api_interface import APIInterface
from config.config import API_KEY, BASE_URL

class LocationsAPI(APIInterface):
    def __init__(self):
        self.base_url = f"{BASE_URL}/locations/v1/cities"
        self.api_key = API_KEY

    def get_city_autocomplete_search(self, city_query: str):
        full_url = self._build_url(self.base_url, "autocomplete")
        params = {"apikey": self.api_key, "q": city_query}
        return self._get(url=full_url, params=params)
