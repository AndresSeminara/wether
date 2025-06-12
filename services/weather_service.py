import statistics
from classes.location_api import LocationsAPI
from classes.forecast_api import ForecastAPI

class WeatherService:
    def __init__(self):
        self.location_api = LocationsAPI()
        self.forecast_api = ForecastAPI()

    def process_forecast(self, city_name):
        cities = self.location_api.get_city_autocomplete_search(city_name)
        if not cities:
            raise ValueError("No coincidence found for the city name")

        selected_city = cities[0]
        location_key = selected_city["Key"]
        city_name = selected_city['LocalizedName']
        country = selected_city['Country']['LocalizedName']

        forecast = self.forecast_api.get_forecast_five_next_days(location_key)

        min_temps = [d["Temperature"]["Minimum"]["Value"] for d in forecast["DailyForecasts"]]
        max_temps = [d["Temperature"]["Maximum"]["Value"] for d in forecast["DailyForecasts"]]
        min_temp = min(min_temps)
        max_temp = max(max_temps)
        avg_temp = statistics.mean(min_temps + max_temps)

        return city_name, country, min_temp, max_temp, avg_temp