# Ne doit pas fonctionner (exemple de test unitaire pour une classe inexistante)

from stack import Stack
import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.pile = Stack()

    def test_len(self):
        self.failUnless(len(self.pile.items) == 0)

    def test_pop(self): #pop sur pile vide lève IndexError ?
        self.assertRaises(IndexError,self.pile.pop())

if __name__ == "__main__":
    unittest.main()
