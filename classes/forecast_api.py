from interfaces.api_interface import APIInterface
from config.config import API_KEY, BASE_URL

class ForecastAPI(APIInterface):
    def __init__(self):
        self.base_url = f"{BASE_URL}/forecasts/v1/daily"
        self.api_key = API_KEY

    def get_forecast_five_next_days(self, location_key: str):
        full_url = self._build_url(self.base_url, "5day",location_key)
        params = {"apikey": self.api_key, "metric": "true"}
        return self._get(url=full_url, params=params)
