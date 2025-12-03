class Product:
    pay_rate = 0.8 # pay rate after 20% dicount
    all = []

    def __init__(self, name: str, price = 0, quantity = 0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        Product.all.append(self)

    def calc_total(self):
        total = self.price * self.quantity
        return total
    
    def get_dicount(self):
        discount = self.price * self.pay_rate
        return discount 
    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"
    
prod_1 = Product("laptop", 1200, 5)

prod_2 = Product("mouse", 500.89, 12)

print(f"product name: '{prod_1.name}'") # accessing object attributes

print(f"product price: £{prod_1.price:,}")

print(f"product quantity: {prod_1.quantity}")

value_a = prod_1.calc_total() # functiona call

print(f"the total value of {prod_1.name} is: £{value_a:,}")

print("-" * 40)

print(f"product name: '{prod_2.name}'")

print(f"product price: £{prod_2.price}")

print(f"product quantity: {prod_2.quantity}")

value_b = prod_2.calc_total()

print(f"the total value of {prod_2.name} is: £{value_b:,.2f}")

value_c = prod_1.get_dicount()
print(f"the dicount on {prod_1.name} is: £{value_c:,.2f}")

value_d = prod_2.get_dicount()
print(f"the discount on {prod_2.name} is £{value_d:,.2f}")

for item in Product.all:
    (print(item.name, item.price, item.quantity))
print(repr(prod_1))
print(repr(prod_2)) 