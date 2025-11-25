from car import Cars
# creating objects automatically invokes the constructor
car1 = Cars("Burgundy", "Bentley", "Bentayaga s", 2025, True)
car2 = Cars("Black", "Mercedes", "G 63", 2026, False)
car3 = Cars("Olive green", "Porsche", "Cayenne", 2024, True)
# access or modify object attributes
print(car1.colour, car1.name, car1.model, car1.year, car1.for_sale)
print(car2.colour, car2.name, car2.model, car2.year, car2.for_sale)
print(car3.colour, car3.name, car3.model, car3.year, car3.for_sale)
print("-" * 30)
car1.drive()
car1.stop()
car2.drive()
car2.stop()
car3.drive()
car3.stop()
car1.describe()