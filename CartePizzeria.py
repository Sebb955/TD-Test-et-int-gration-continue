from CartePizzeriaException import CartePizzeriaException
from Pizza import Pizza  

class CartePizzeria:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def nb_pizzas(self):
        return sum(1 for element in self.elements if isinstance(element, Pizza))

    def nb_drinks(self):
        return sum(1 for element in self.elements if isinstance(element, Drink))

    def nb_desserts(self):
        return sum(1 for element in self.elements if isinstance(element, Dessert))

    def add(self, element):
        for existing_element in self.elements:
            if existing_element.name == element.name:
                if isinstance(existing_element, Pizza) and isinstance(element, Pizza):
                    if hasattr(element, 'ingredients') and hasattr(element, 'base'):
                        if existing_element.ingredients == element.ingredients and existing_element.base == element.base:
                            raise CartePizzeriaException("La pizza {} est déjà présente dans la carte avec les mêmes ingrédients et base.".format(element.name))
                    else:
                        raise CartePizzeriaException("L'élément {} est déjà présent dans la carte.".format(element.name))
        self.elements.append(element)

    def remove(self, name):
        for element in self.elements:
            if element.name == name:
                self.elements.remove(element)
                return
        raise CartePizzeriaException("L'élément {} n'existe pas dans la carte.".format(name))
