class Car:
    def __init__(self, make, model, year_of_manufacture):
        self.make = make
        self.model = model
        self.year_of_manufacture = year_of_manufacture

    def describe(self):
       print(f"This car is a {self.year_of_manufacture} {self.make}  {self.model} ")

car1 = Car("Honda","Civic",2021)
car2 =Car("Toyota","Camry",2020)

car1.describe()
car2.describe()