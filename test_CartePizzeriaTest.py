from CartePizzeria import CartePizzeria, CartePizzeriaException
import unittest
from unittest.mock import Mock

from Pizza import Pizza

class MockPizza(Pizza):
    def __init__(self, name):
        self.name = name

class CartePizzeriaTest(unittest.TestCase):
    def test_is_empty(self):
        carte_pizzeria = CartePizzeria()
        self.assertTrue(carte_pizzeria.is_empty())  # La carte devrait être vide initialement
        
        mock_pizza = MockPizza("Margherita")  # Créer une pizza mockée
        carte_pizzeria.add(mock_pizza)
        self.assertFalse(carte_pizzeria.is_empty())  # Après l'ajout d'une pizza, la carte ne devrait plus être vide

    def test_add_pizza(self):
        carte_pizzeria = CartePizzeria()
        mock_pizza = MockPizza("Pepperoni")  # Créer une pizza mockée
        carte_pizzeria.add(mock_pizza)
        self.assertEqual(carte_pizzeria.nb_pizzas(), 1)  # Vérifie que la pizza a été ajoutée à la carte

    def test_remove_pizza(self):
        carte_pizzeria = CartePizzeria()
        mock_pizza = Mock()
        mock_pizza.name = "Margherita"
        carte_pizzeria.add(mock_pizza)
        
        # Suppression d'une pizza existante
        carte_pizzeria.remove("Margherita")
        self.assertEqual(carte_pizzeria.nb_pizzas(), 0)  # Vérifie que la pizza a été retirée de la carte
        
        # Tentative de suppression d'une pizza inexistante
        with self.assertRaises(CartePizzeriaException):
            carte_pizzeria.remove("Quatre Fromages")

if __name__ == '__main__':
    unittest.main()
