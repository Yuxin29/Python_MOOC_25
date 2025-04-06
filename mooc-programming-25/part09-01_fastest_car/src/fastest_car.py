# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed
    
    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

def fastest_car(car_list):
    car_spead = []
    max_speed = 0
    for car in car_list:
         car_spead.append(car.top_speed)
    max_speed = max(car_spead)
    for car in car_list:
        if max_speed == car.top_speed:
            return car.make
         

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))