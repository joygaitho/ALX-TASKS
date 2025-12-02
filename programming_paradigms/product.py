class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calc_total(self):
        total = self.price * self.quantity
        return total
prod_1 = Product("laptop", 1200, 5)
prod_2 = Product("mouse", 500.89, 12)
print(f"product name: '{prod_1.name}'") # accessing object attributes
print(f"product price: {prod_1.price:,}")
print(f"product quantity: {prod_1.quantity}")
value_a = prod_1.calc_total() # functiona call
print(f"the total value of {prod_1.name} is: {value_a:,}")
print("-" * 40)
print(f"product name: '{prod_2.name}'")
print(f"product price: {prod_2.price}")
print(f"product quantity: {prod_2.quantity}")
value_b = prod_2.calc_total()
print(f"the total value of {prod_2.name} is: {value_b:,.2f}")


