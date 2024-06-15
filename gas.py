'''
Final Project
Restaurant Carbon_emission Calcualtor
by HArshil Bhojwani
24/04/2023

'''
class Gas:#carbon emission from different commodity of energy exalmple col, gas, wood etc
    def __init__(self, cooking_gas=0, electricity=0, coal=0, wood=0):#each category of emission is an attribute
        self.cooking_gas=cooking_gas
        self.coal=coal
        self.electricity=electricity
        self.wood=wood
    



    def carbon_gas(self):#carbon emssion from cooking gas
        if not isinstance (self.cooking_gas, float):
            raise TypeError("Data isn't numeric")# defensiv programming
        
        if self.cooking_gas<0:#multiplying to calculte the total carbon emission
            raise ValueError("The numeric data isn't positive")
        gas_carbon=self.cooking_gas*0.7
        return gas_carbon
    
    def carbon_coal(self):#carbon emssion from electricity produced from coal
        if not isinstance (self.electricity, float):
            raise TypeError("Data isn't numeric")
        
        if self.electricity<0:
            raise ValueError("The numeric data isn't positive")
        coal_carbon=self.electricity*3.3
        return coal_carbon
    

    def carbon_oil(self):#carbon emssion from electricity produced from oil
        if not isinstance (self.electricity, float):#defensive programming
            raise TypeError("Data isn't numeric")
        
        if self.electricity<0:#multiplying to calculate the total carbon emission
            raise ValueError("The numeric data isn't positive")
        oil_carbon=self.electricity*0.84
        return oil_carbon


    def carbon_natural_gas(self):#carbon emssion from electricity produced from natural_gas
        if not isinstance (self.electricity, float):#defensive programming
            raise TypeError("Data isn't numeric")
        
        if self.electricity<0:#multiolying to calcualte total carbon emission
            raise ValueError("The numeric data isn't positive")
        natural_carbon=self.electricity*0.47
        return natural_carbon
    
    def wood_carbon(self):#if there are commodities operated from alternative fuel such as  woodfire ven or griiler
        if not isinstance (self.wood, float):#defensive programming
            raise TypeError("Data isn't numeric")
        
        if self.wood<0:
            raise ValueError("The numeric data isn't positive")
        carbon_wood=self.wood*1.8#multiplying to calculate the total carbon_emission 
        return carbon_wood
    
    def alternative_coal(self):##if there are commodities operated from alternative fuel such as  woodfire ven or coal griller
        if not isinstance (self.coal, float):#defensive programming
            raise TypeError("Data isn't numeric")
        
        if self.coal<0:
            raise ValueError("The numeric data isn't positive")
        coal_carbon=self.coal*1.25#multiplying to calculate the total carbon emission
        return coal_carbon

    def total_gas(self, cooking_gas, coal=0, oil=0, natural_gas=0):
        total_carbon=cooking_gas+coal+oil+natural_gas
        return total_carbon
    

    



    def gas_dict(self, cooking_gas, coal=0, oil=0, natural_gas=0):
        total_gas=cooking_gas+coal+oil+natural_gas
        gas_dict=dict(zip("Total gas carbon emission:", total_gas))
        return gas_dict


