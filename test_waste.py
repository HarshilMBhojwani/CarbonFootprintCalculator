import unittest
from waste_food import Waste

class TestRawfood(unittest.TestCase):
    def test_raw_init(self):
        test_raw=Waste(10.0)
        self.assertEqual(test_raw.foodwaste, 10.0)
  
     
   
    
    def test_wastefood(self):
        test_raw=Waste(10.0)
        self.assertEqual(test_raw.carbon_foodwaste(), 25)
        
        raw_negative=Waste(-1.0)
        with self.assertRaises(ValueError):
           raw_negative.carbon_foodwaste()
        
        raw_alpha=Waste("a")
        with self.assertRaises(TypeError):
           raw_alpha.carbon_foodwaste()

    
 
   
   


def main():
    unittest.main()
if __name__ == "__main__":
 main()
