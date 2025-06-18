import unittest

def add(a,b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 2), 4)
        
        
if __name__ == '__main__':
    unittest.main()
        
        