'''
Final Project
Restaurant Carbon_emission Calcualtor
by HArshil Bhojwani
24/04/2023

'''
import unittest
from paper import Paper

class TestRawfood(unittest.TestCase):
    def test_raw_init(self):
        test_raw=Paper(10.0, 10.0, 10.0, 10.0,)
        self.assertEqual(test_raw.roll, 10.0)
        self.assertEqual(test_raw.tissue, 10.0)
        self.assertEqual(test_raw.paperbag, 10.0)
        self.assertEqual(test_raw.recycle, 10.0)
     # testing all the attribute value to check the value
   
    
    #testing the paper_roll function with bad data and expected data
    def test_roll(self):
        test_raw=Paper(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_roll(), 85.71428571428571 )
        roll=Paper(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            roll.carbon_roll()
        
        no_numeric=Paper("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            no_numeric.carbon_roll()
        


    
    #testing the tissue function with bad data and expected data
    def test_tissue(self):
        test_raw=Paper(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.carbon_tissue(), 22.0)
        roll=Paper(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            roll.carbon_tissue()
        
        no_numeric=Paper("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            no_numeric.carbon_tissue()
        
        


    #testing the peperbag function with bad data and expected data
    def test_paperbag(self):
        test_raw=Paper(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.paper_bag_carbon(), 55.0)
        roll=Paper(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            roll.paper_bag_carbon()
        no_numeric=Paper("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            no_numeric.paper_bag_carbon()
        
        

    #testing the paper_recycle function with bad data and expected data
    def test_recycle(self):
        test_raw=Paper(10.0, 10.0, 10.0, 10.0)
        self.assertEqual(test_raw.recycle_paper_carbon(), 60.0)
        roll=Paper(-1.0,-1.0,-1.0,-1.0)
        with self.assertRaises(ValueError):
            roll.recycle_paper_carbon()
        no_numeric=Paper("a", "a", "a", "a")
        with self.assertRaises(TypeError):
            no_numeric.recycle_paper_carbon()
        
        

   
   


def main():
    unittest.main()
if __name__ == "__main__":
 main()
