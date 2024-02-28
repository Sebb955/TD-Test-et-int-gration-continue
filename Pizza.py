class Pizza:
    TOMATE = "tomate"
    CREME = "crème"

    def __init__(self, name, price, description, ingredients, base):
        self.name = name
        self.price = price
        self.description = description
        self.ingredients = ingredients
        self.base = base

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
