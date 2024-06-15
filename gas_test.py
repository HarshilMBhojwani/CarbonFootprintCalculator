import unittest
from gas import Gas

class TestRawfood(unittest.TestCase):
    def test_raw_init(self):
        test_raw=Gas(10.0, 10.0, 10.0, 10.0,)
        self.assertEqual(test_raw.cooking_gas, 10.0)
        self.assertEqual(test_raw.coal, 10.0)
        self.assertEqual(test_raw.electricity, 10.0)
        self.assertEqual(test_raw.wood, 10.0)
     # testing all the class attributes
   
    
    #testing the cooking function with bad data and expected data
    def test_cookinggas(self):
        test_raw=Gas(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_gas(), 7.0 )
        gas_neg=Gas(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            gas_neg.carbon_gas()

        gas_alph=Gas("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            gas_alph.carbon_gas()


    
    #testing the electricity coal function with bad data and expected data
    def test_electricity_coal(self):
        test_raw=Gas(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_coal(), 33.0)
        gas_neg=Gas(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            gas_neg.carbon_coal()

        gas_alph=Gas("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            gas_alph.carbon_coal()



    #testing the electricity oil function with bad data and expected data
    def test_elect_oil(self):
        test_raw=Gas(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_oil(), 8.4)
        gas_neg=Gas(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            gas_neg.carbon_oil()

        gas_alph=Gas("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            gas_alph.carbon_oil()



    #testing the electricity gas function with bad data and expected data
    def test_elec_gas(self):
        test_raw=Gas(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_natural_gas(), 4.699999999999999)
        gas_neg=Gas(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            gas_neg.carbon_natural_gas()

        gas_alph=Gas("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            gas_alph.carbon_natural_gas()




    #testing the alternative_coal function with bad data and expected data
    def test_coal(self):
        test_raw=Gas(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.wood_carbon(), 18.0)
        gas_neg=Gas(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            gas_neg.wood_carbon()

        gas_alph=Gas("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            gas_alph.wood_carbon()



    #testing the wood energy function with bad data and expected data
    def test_wood(self):
        test_raw=Gas(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.alternative_coal(), 12.5)
        gas_neg=Gas(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            gas_neg.alternative_coal()

        gas_alph=Gas("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            gas_alph.alternative_coal()



   
   


def main():
    unittest.main()
if __name__ == "__main__":
 main()
