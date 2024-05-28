from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def make(self, inventory_manager):
        pass

class Coffee(Drink):
    def make(self, inventory_manager):
        required_ingredients = {'coffee bean': 1, 'water': 200}
        if inventory_manager.use_ingredients(required_ingredients):
            return "Coffee is made"
        return "Not enough ingredients"

class Latte(Drink):
    def make(self, inventory_manager):
        required_ingredients = {'coffee bean': 1, 'milk': 100, 'water': 100}
        if inventory_manager.use_ingredients(required_ingredients):
            return "Latte is made"
        return "Not enough ingredients"

class GreenTea(Drink):
    def make(self, inventory_manager):
        required_ingredients = {'green tea powder': 1, 'water': 200}
        if inventory_manager.use_ingredients(required_ingredients):
            return "Green Tea is made"
        return "Not enough ingredients"

class BlackTea(Drink):
    def make(self, inventory_manager):
        required_ingredients = {'black tea': 1, 'water': 200}
        if inventory_manager.use_ingredients(required_ingredients):
            return "Black Tea is made"
        return "Not enough ingredients"

class DrinkFactory:
    def create_drink(self, drink_type):
        if drink_type == 'coffee':
            return Coffee()
        elif drink_type == 'latte':
            return Latte()
        elif drink_type == 'green tea':
            return GreenTea()
        elif drink_type == 'black tea':
            return BlackTea()
        else:
            raise ValueError(f"Unknown drink type: {drink_type}")
