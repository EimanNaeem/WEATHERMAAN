from data import parse_date


class Readings:
    def maximum_temp(self, weather_data):
        max_temp = max(weather_data, key=lambda key: (key['max_temperature']))
        return max_temp['max_temperature'], parse_date(max_temp['date'])

    def minimum_temp(self, weather_data):
        min_temp = min(weather_data, key=lambda key: (key['min_temperature']))
        return min_temp['min_temperature'], parse_date(min_temp['date'])

    def maximum_humidity(self, weather_data):
        max_humidity = max(weather_data, key=lambda key: (key['max_humidity']))
        return max_humidity['max_humidity'], parse_date(max_humidity['date'])

    def avg_temp(self, weather_data):
        avg_temperature = 0
        avg_min_temperature = 0
        avg_humidity = 0


        for weather_info in weather_data:
            avg_temperature += weather_info['max_temperature']
            avg_min_temperature += weather_info['min_temperature']
            avg_humidity += weather_info['mean_humidity']


