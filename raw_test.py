import unittest
from raw_meat import RawFood

class TestRawfood(unittest.TestCase):
    def test_raw_init(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.red_meat, 10.0)
        self.assertEqual(test_raw.seafood, 10.0)
        self.assertEqual(test_raw.poultry, 10.0)
        self.assertEqual(test_raw.lamb, 10.0)
        self.assertEqual(test_raw.eggs, 10.0)
        self.assertEqual(test_raw.pork, 10.0)
        self.assertEqual(test_raw.dairy, 10.0)
        self.assertEqual(test_raw.vegetable, 10.0)
        self.assertEqual(test_raw.cheese, 10.0)
        self.assertEqual(test_raw.chocolate, 10.0)
        self.assertEqual(test_raw.coffee, 10.0)
        self.assertEqual(test_raw.oil, 10.0)

    
    def test_redmeat(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.redmeat(), 600.0)

        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.redmeat()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.redmeat()

    
    def test_seafood(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.seafood_carbon(), 41.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0,-1.0)
        with self.assertRaises(ValueError):
            raw_neg.seafood_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.seafood_carbon()


    def test_poultry(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.poultry_carbon(), 61.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.poultry_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.poultry_carbon()

    def test_lamb(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.carbon_lamb(), 610.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.carbon_lamb()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.carbon_lamb()

    def test_eggs(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.carbon_eggs(), 45.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.carbon_eggs()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.carbon_eggs()
    
    def test_pork(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.pork_carbon(), 73.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.pork_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.pork_carbon()

    def test_dairy(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.dairy_carbon(), 28.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            raw_neg.dairy_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.dairy_carbon()
    
    def test_vegetable(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.vegetable_carbon(), 20.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.vegetable_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.vegetable_carbon()

    def test_cheese(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.cheese_carbon(), 210.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.cheese_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a", "a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.cheese_carbon()

    def test_chocolate(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.chocolate_carbon(), 190.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0, -1.0, -1.0)
        with self.assertRaises(ValueError):
            raw_neg.chocolate_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a","a", "a")
        with self.assertRaises(TypeError):
            raw_alpha.chocolate_carbon()

    def test_coffee(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.coffee_carbon(), 170.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            raw_neg.coffee_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a","a","a")
        with self.assertRaises(TypeError):
            raw_alpha.coffee_carbon()

    def test_oil(self):
        test_raw=RawFood(10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ,10.0, 10.0, 10.0 ,10.0 ,10.0)
        self.assertEqual(test_raw.oil_carbon(), 60.0)
        raw_neg=RawFood(-1.0,-1.0, -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            raw_neg.oil_carbon()

        raw_alpha=RawFood("a","a", "a", "a", "a", "a", "a","a","a", "a","a","a")
        with self.assertRaises(TypeError):
            raw_alpha.oil_carbon()



def main():
    unittest.main()
if __name__ == "__main__":
 main()
