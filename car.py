class Cars:
    """
    define contrustor

    """
    def __init__(self, colour, name, model, year, for_sale): 
        """
        define and initialize instance (object) attributes

        """
        self.colour = colour
        self.name = name
        self.model = model
        self.year = year
        self.for_sale = for_sale
    def drive(self):
        print(f"you drive the {self.colour} {self.model}")
    def stop(self):
        print(f"you stopped the {self.colour} {self.model}")
    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")