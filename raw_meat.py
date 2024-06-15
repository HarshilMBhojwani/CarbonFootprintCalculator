

class RawFood:#in this class carbon emission of each raw food category is calculated 
    def __init__(self, red_meat=0, seafood=0, poultry=0, pork=0, lamb=0, eggs=0, dairy=0, vegetable=0, cheese=0, chocolate=0, coffee=0, oil=0):
        self.red_meat=red_meat#all the raw food category become an attibute which will have their owm methods to calculate Co2 emission
        self.seafood=seafood
        self.poultry=poultry
        self.lamb=lamb
        self.eggs=eggs
        self.pork=pork
        self.dairy=dairy
        self.vegetable=vegetable
        self.cheese=cheese
        self.chocolate=chocolate
        self.coffee=coffee
        self.oil=oil


    def redmeat(self):
        if not isinstance (self.seafood, float):
            raise TypeError("Data isn't numeric")
        
        if self.red_meat<0:
            raise ValueError("The numeric data isn't positive")
        
        redmeat_carbon=self.red_meat*60
        return redmeat_carbon#carbon emission  for beef
    
    def seafood_carbon(self):
        if not isinstance (self.seafood, float):
            raise TypeError("Data isn't numeric")
        
        if self.seafood<0:
            raise ValueError("The numeric data isn't positive")
        
        seafood_carbon=self.seafood*4.1
        return seafood_carbon#carbon emssion for seafood
    
    def poultry_carbon(self):
        if not isinstance (self.poultry, float):
            raise TypeError("Hlp Data isn't numeric")
        
        if self.poultry<0:
            raise ValueError("The numeric data isn't positive")
        poultry_carbon= self.poultry*6.1
        return poultry_carbon#carbon emisison for poultry



    def pork_carbon(self):
        if not isinstance (self.pork, float):
            raise TypeError("Data isn't numeric")
        
        if self.pork<0:
            raise ValueError("The numeric data isn't positive")
        pork_carbon=self.pork*7.3
        return pork_carbon#carbon emission for pork
    

    def carbon_lamb(self):
        if not isinstance (self.lamb, float):
            raise TypeError("Data isn't numeric")
        
        if self.lamb<0:
            raise ValueError("The numeric data isn't positive")
        lamb_carbon=self.lamb*61
        return lamb_carbon#carbon emision for lamb
    
    def carbon_eggs(self):
        if not isinstance (self.eggs, float):
            raise TypeError("Data isn't numeric")
        
        if self.eggs<0:
            raise ValueError("The numeric data isn't positive")
    
        eggs_carbon=self.eggs*4.5
        return eggs_carbon#carbon emission for eggs
    

    def dairy_carbon(self):
        if not isinstance (self.dairy, float):
            raise TypeError("Data isn't numeric")
        
        if self.dairy<0:
            raise ValueError("The numeric data isn't positive")
        dairy_carbon=self.dairy*2.8
        return dairy_carbon#carbon emisson for dairy
    
    def vegetable_carbon(self):
        if not isinstance (self.vegetable, float):
            raise TypeError("Data isn't numeric")
        
        if self.vegetable<0:
            raise ValueError("The numeric data isn't positive")
        carbon_vegetable=self.vegetable*2.0
        return carbon_vegetable#carbon emisson for raw vegetable produce
    
    def cheese_carbon(self):
        if not isinstance (self.cheese, float):
            raise TypeError("Data isn't numeric")
        
        if self.cheese<0:
            raise ValueError("The numeric data isn't positive")
        cheese_carbon=self.cheese*21
        return cheese_carbon#carbon emission for cheese
    
    def chocolate_carbon(self):
        if not isinstance (self.chocolate, float):
            raise TypeError("Data isn't numeric")
        
        if self.chocolate<0:
            raise ValueError("The numeric data isn't positive")
        chocolate_carbon=self.chocolate*19
        return chocolate_carbon#carbon emsison for chocolate
    
    def coffee_carbon(self):
        if not isinstance (self.coffee, float):
            raise TypeError("Data isn't numeric")
        
        if self.coffee<0:
            raise ValueError("The numeric data isn't positive")
        coffee_carbon=self.coffee*17
        return coffee_carbon#carbon emsission for coffee
    
    def oil_carbon(self):
        if not isinstance (self.oil, float):
            raise TypeError("Data isn't numeric")
        
        if self.oil<0:
            raise ValueError("The numeric data isn't positive")
        carbon_oil=self.oil*6
        return carbon_oil#carbon emission for cooking oil

    
    def raw_total(self, redmeat, seafood, poultry, pork, lamb, dairy, vegetable, chocolate, cheese, coffee, oil):
        total_raw=redmeat+seafood+poultry+pork+lamb+dairy+vegetable+chocolate+cheese+coffee +oil
        #statment="The carbon emission of all raw good"
        dict_raw=dict(("The carbon emission of all raw good"),total_raw)
        return dict_raw
    
