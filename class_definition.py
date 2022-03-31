class Car:
   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color


mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
print(mustang.make)

car_1 = Car("Toyota", "Aygo","White", 120)
print(car_1.make)