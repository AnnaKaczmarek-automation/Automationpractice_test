import unittest
from tests.shopping_test import ShoppingTest


# Pobierz testy, które chcesz uruchomić
shopping_test = unittest.TestLoader().loadTestsFromTestCase(ShoppingTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([shopping_test])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
