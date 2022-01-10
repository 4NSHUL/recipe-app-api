from django.test import TestCase
from app.calc import add, subtract

class ClassTests(TestCase):
    """docstring for ."""

    def test_add(self):
        self.assertEqual(add(3,8),11)

    def test_subtract(self):
        """values are substracted and returned"""
        self.assertEqual(subtract(4,2),2)
