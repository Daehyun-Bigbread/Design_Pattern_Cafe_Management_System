class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class InventoryManager(metaclass=MetaSingleton):
    def __init__(self):
        self.inventory = {}
        self.order = {}

    def add_item(self, item, quantity, threshold=0):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        self.order[item] = threshold
        print(f"Added {item}: {quantity}, Threshold: {threshold}")

    def update_inventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
            if self.inventory[item] < 0:
                self.inventory[item] = 0
                print(f"Inventory for {item} cannot be negative. Set to 0.")
            self.check_order(item)
        else:
            print(f"Error: {item} not found in inventory.")

    def use_ingredients(self, ingredients):
        for item, quantity in ingredients.items():
            if self.inventory.get(item, 0) < quantity:
                print(f"Error: Not enough {item} in inventory.")
                return False
        for item, quantity in ingredients.items():
            self.inventory[item] -= quantity
            if self.inventory[item] < 0:
                self.inventory[item] = 0
                print(f"Inventory for {item} went negative. Set to 0.")
        return True

    def check_order(self, item):
        if self.inventory[item] <= self.order[item]:
            self.order_item(item)

    def order_item(self, item):
        print(f"Order more of {item}!")

    def get_inventory(self):
        return self.inventory
