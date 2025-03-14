class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}\n")



car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Honda", "Civic", 2022, "Red")
car3 = Car("Ford", "Mustang", 2021, "Black")
car4 = Car("Tesla", "Model 3", 2023, "White")


car1.display_details()
car2.display_details()
car3.display_details()
car4.display_details()
