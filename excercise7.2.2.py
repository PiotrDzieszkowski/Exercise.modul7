#Method __repr__
class Car():
       
    def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
       
    
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    def __str__(self):
        return f"{self.color} {self.make} {self.model_name}"

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car.__repr__)
print(car)