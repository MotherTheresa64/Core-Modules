class WeatherStation:
    def __init__(self, location, temperature_f):
        self.location = location
        self.temperature_f = temperature_f

    def __repr__(self):
        return f"WeatherStation(location={self.location}, temperature_f={self.temperature_f})"

    @staticmethod
    def fahrenheit_to_celsius(f_temp):
        return (f_temp - 32) * 5.0 / 9.0

    @staticmethod
    def celsius_to_fahrenheit(c_temp):
        return (c_temp * 9.0 / 5.0) + 32


# Test
temp_f = 77
temp_c = WeatherStation.fahrenheit_to_celsius(temp_f)
print(f"{temp_f}F is {temp_c:.2f}C")  # 77F is 25.00C

temp_back_f = WeatherStation.celsius_to_fahrenheit(temp_c)
print(f"{temp_c:.2f}C is {temp_back_f:.2f}F")  # 25.00C is 77.00F
