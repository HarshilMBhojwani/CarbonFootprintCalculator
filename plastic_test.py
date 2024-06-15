'''
Final Project
Restaurant Carbon_emission Calcualtor
by HArshil Bhojwani
24/04/2023

'''
import unittest
from plastic import Plastic

class TestRawfood(unittest.TestCase):
    def test_raw_init(self):
        test_raw=Plastic(10.0, 10.0, 10.0, 10.0, 10.0, 10.0,)
        self.assertEqual(test_raw.pet, 10.0)
        self.assertEqual(test_raw.pvc, 10.0)
        self.assertEqual(test_raw.ldpe, 10.0)
        self.assertEqual(test_raw.ps, 10.0)
        self.assertEqual(test_raw.recycle, 10.0)
        self.assertEqual(test_raw.foil, 10.0)
   #testing all the attribute values
    
    #testing the pet function with bad data and expected data
    def test_pet(self):
        test_raw=Plastic(10.0, 10.0, 10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_pet(), 25.4)

        plastic_negative=Plastic(-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            plastic_negative.carbon_pet()

        plastic_alpha=Plastic("a", "a", "a", "a", "a")
        with self.assertRaises(TypeError):
            plastic_alpha.carbon_pet()

    
    #testing the pvc function with bad data and expected data
    def test_pvc(self):
        test_raw=Plastic(10.0, 10.0, 10.0, 10.0, 10.0, 10.0,)
        self.assertEqual(test_raw.carbon_pvc(), 18.0)

        plastic_negative=Plastic(-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            plastic_negative.carbon_pvc()

        plastic_alpha=Plastic("a", "a", "a", "a", "a")
        with self.assertRaises(TypeError):
            plastic_alpha.carbon_ps()



    #testing the lpde function with bad data and expected data
    def test_ldpe(self):
        test_raw=Plastic(10.0, 10.0, 10.0, 10.0, 10.0, 10.0,)
        self.assertEqual(test_raw.carbon_ldpe(), 30.0)

        plastic_negative=Plastic(-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            plastic_negative.carbon_ldpe()

        plastic_alpha=Plastic("a", "a", "a", "a", "a")
        with self.assertRaises(TypeError):
            plastic_alpha.carbon_ldpe()


    #testing the ps function with bad data and expected data
    def test_ps(self):
        test_raw=Plastic(10.0, 10.0, 10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_ps(), 33.0)

        plastic_negative=Plastic(-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            plastic_negative.carbon_ps()

        plastic_alpha=Plastic("a", "a", "a", "a", "a")
        with self.assertRaises(TypeError):
            plastic_alpha.carbon_ps()


    #testing the plastic recycle function with bad data and expected data
    def test_recycle(self):
        test_raw=Plastic(10.0, 10.0, 10.0, 10.0, 10.0, 10.0,)
        self.assertEqual(test_raw.plastic_recycled(), 25.4)
        plastic_negative=Plastic(-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            plastic_negative.plastic_recycled()

        plastic_alpha=Plastic("a", "a", "a", "a", "a")
        with self.assertRaises(TypeError):
            plastic_alpha.plastic_recycled()

    
    #testing the foil function with bad data and expected data
    def test_foil(self):
        test_raw=Plastic(10.0, 10.0, 10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_foil(), 31.0)
        plastic_negative=Plastic(-1.0,-1.0,-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            plastic_negative.carbon_foil()

        plastic_alpha=Plastic("a", "a", "a", "a", "a")
        with self.assertRaises(TypeError):
            plastic_alpha.carbon_foil()


   


def main():
    unittest.main()
if __name__ == "__main__":
 main()
