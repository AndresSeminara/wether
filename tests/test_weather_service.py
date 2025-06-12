from services.weather_service import WeatherService

import pytest

@pytest.fixture
def mock_forecast(monkeypatch):
    def mock_get(*args, **kwargs):
        return {
            "DailyForecasts": [
                {"Temperature": {"Minimum": {"Value": 10}, "Maximum": {"Value": 20}}},
                {"Temperature": {"Minimum": {"Value": 12}, "Maximum": {"Value": 22}}},
                {"Temperature": {"Minimum": {"Value": 14}, "Maximum": {"Value": 24}}},
                {"Temperature": {"Minimum": {"Value": 16}, "Maximum": {"Value": 26}}},
                {"Temperature": {"Minimum": {"Value": 18}, "Maximum": {"Value": 28}}},
            ]
        }
    from classes.forecast_api import ForecastAPI
    monkeypatch.setattr(ForecastAPI, "get_forecast_five_next_days", mock_get)

def test_process_forecast(monkeypatch, mock_forecast):
    service = WeatherService()

    monkeypatch.setattr(service.location_api, "get_city_autocomplete_search", lambda city_name: [
        {"Key": "123", "LocalizedName": "TestCity", "Country": {"LocalizedName": "TestCountry"}}
    ])

    city, country, temp_min, temp_max, temp_avg = service.process_forecast("test")

    assert city == "TestCity"
    assert country == "TestCountry"
    assert temp_min == 10
    assert temp_max == 28
    assert round(temp_avg, 2) == 19.0
