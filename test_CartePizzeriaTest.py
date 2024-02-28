import unittest
from unittest.mock import Mock
from CartePizzeria import CartePizzeria, CartePizzeriaException

class CartePizzeriaTest(unittest.TestCase):
    def test_is_empty(self):
        carte_pizzeria = CartePizzeria()
        self.assertTrue(carte_pizzeria.is_empty())  # La carte devrait être vide initialement
        
        mock_pizza = Mock()
        carte_pizzeria.add_pizza(mock_pizza)
        self.assertFalse(carte_pizzeria.is_empty())  # Après l'ajout d'une pizza, la carte ne devrait plus être vide

    def test_nb_pizzas(self):
        carte_pizzeria = CartePizzeria()
        self.assertEqual(carte_pizzeria.nb_pizzas(), 0)  # La carte devrait être vide initialement
        
        mock_pizza1 = Mock()
        mock_pizza2 = Mock()
        carte_pizzeria.add_pizza(mock_pizza1)
        carte_pizzeria.add_pizza(mock_pizza2)
        self.assertEqual(carte_pizzeria.nb_pizzas(), 2)  # Après l'ajout de deux pizzas, la carte devrait contenir 2 pizzas

    def test_add_pizza(self):
        carte_pizzeria = CartePizzeria()
        mock_pizza = Mock()
        carte_pizzeria.add_pizza(mock_pizza)
        self.assertEqual(carte_pizzeria.nb_pizzas(), 1)  # Vérifie que la pizza a été ajoutée à la carte

    def test_remove_pizza(self):
        carte_pizzeria = CartePizzeria()
        mock_pizza = Mock()
        mock_pizza.name = "Margherita"
        carte_pizzeria.add_pizza(mock_pizza)
        
        # Suppression d'une pizza existante
        carte_pizzeria.remove_pizza("Margherita")
        self.assertEqual(carte_pizzeria.nb_pizzas(), 0)  # Vérifie que la pizza a été retirée de la carte
        
        # Tentative de suppression d'une pizza inexistante
        with self.assertRaises(CartePizzeriaException):
            carte_pizzeria.remove_pizza("Quatre Fromages")

if __name__ == '__main__':
    unittest.main()
