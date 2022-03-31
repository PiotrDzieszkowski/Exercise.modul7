#Method sorted()
class Car():
       
    def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

    def __str__(self):
        return f"{self.color} {self.make} {self.model_name}"

    def __gt__(self, other):
        return self.top_speed > other.top_speed

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
by_speed = sorted(cars, key=lambda car: car.top_speed)

print(by_speed[0], by_speed[1],by_speed[2])

by_make = sorted(cars, key=lambda car: car.make)

print(by_make[0], by_make[1],by_make[2])