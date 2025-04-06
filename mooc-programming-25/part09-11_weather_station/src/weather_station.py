class WeatherStation:
    def __init__(self, name: str):
        self.name = name
        self.observations = []
    def add_observation(self, observation: str):
        self.observations.append(observation)
    def number_of_observations(self):
        return len(self.observations)
    def latest_observation(self):
        if len(self.observations) == 0:
            return ""
        else:
            return self.observations[len(self.observations)-1]
    def __str__(self):
        return f"{self.name}, {len(self.observations)} observations" 
        
if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())
    station.add_observation("Thunderstorm")
    print(station.latest_observation())
    print(station.number_of_observations())
    print(station)