from classes.user_interface import UserInterface
from services.weather_service import WeatherService

def main():
    ui = UserInterface()
    service = WeatherService()

    try:
        city = ui.get_city_name()
        city_name, country, min_temp, max_temp, avg_temp = service.process_forecast(city)
        ui.display_forecast_summary(city_name, country, min_temp, max_temp, avg_temp)
    except Exception as e:
        ui.display_error(str(e))

if __name__ == "__main__":
    main()