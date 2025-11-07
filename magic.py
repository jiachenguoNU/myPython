class ShoppingCart:
    def __init__(self):
        self.items = []

    def __add__(self, another_cart):
        new_cart = ShoppingCart(self.items + another_cart.items)
        return new_cart

    def __str__(self):
        return f"ShoppingCart with {len(self.items)} items."

    def __len__(self):
        return len(self.items)
    
    def __call__(self, item):
        self.items.append(item)
    # use class name to call the method