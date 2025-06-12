class UserInterface:
    @staticmethod
    def get_city_name():
        return input("Please, enter the city name: ")

    @staticmethod
    def display_forecast_summary(city, country, temp_min, temp_max, temp_avg):
        print("\n")
        print(f"City: {city}, {country}")
        print("Forecast for the next 5 days:")
        print(f"Minimum temperature: {temp_min} °C")
        print(f"Maximum temperature: {temp_max} °C")
        print(f"Average temperature: {round(temp_avg, 2)} °C")

    @staticmethod
    def display_error(msg):
        print(f"Error: {msg}")