'''
Final Project
Restaurant Carbon_emission Calcualtor
by HArshil Bhojwani
24/04/2023

'''
class Plastic:
# the main function of this class to is calculate the carbon emisison of different type of plastic commoditites
 def __init__(self, pet=0, pvc=0, ldpe=0, ps=0, recycle=0, foil=0):#all varieties of plastic is are an attributes
  self.pet=pet
  self.pvc=pvc
  self.ldpe=ldpe
  #self.gdpe=gdpe
  self.ps=ps
  self.recycle=recycle
  self.foil=foil


#carbon emision of pet category is calucalted
 def carbon_pet(self):
   if not isinstance (self.pet, float):#defensively programming the data
            raise TypeError("Data isn't numeric")
        
   if self.pet<0:
            raise ValueError("The numeric data isn't positive")
        
   carbon=self.pet*2.54#multiplying per kg carbon eisson
   return carbon
 
#carbon emision for pvc cartegory is calculated
 def carbon_pvc(self):
   if not isinstance (self.pvc, float):#defensive programmming
            raise TypeError("Data isn't numeric")#
        
   if self.pvc<0:
            raise ValueError("The numeric data isn't positive")
        
   carbon_pvc=self.pvc*1.8#multiplying per kg carbon emission
   return carbon_pvc
   
#carbon emsision for lpde type is calculated
 def carbon_ldpe(self):
    if not isinstance (self.ldpe, float):
            raise TypeError("Data isn't numeric")#defensive programming
        
    if self.ldpe<0:
            raise ValueError("The numeric data isn't positive")
        
    carbon_ldpe=self.ldpe*3#multiplying perkg carbon emission
    return carbon_ldpe
   

 #def carbon_hdpe(self):
 #    carbon_gdpe=self.hdpe*1.9
 #    return carbon_gdpe
  
#carbon emssion for ps type is calculated
 def carbon_ps(self):
    if not isinstance (self.ps, float):#defensive programming
            raise TypeError("Data isn't numeric")
        
    if self.ps<0:
            raise ValueError("The numeric data isn't positive")
        
    carbon_ps=self.ps*3.3#multiplying the carbon emission data 
    return carbon_ps
  

 def total_carbon(self, carbon_ps, carbon_gdpe, carbon_ldpe, carbon_pvc, carbon):
    carbon_total=carbon_ps+carbon_gdpe+carbon_ldpe+carbon_pvc+carbon
    return carbon_total
  #carbon emssion neutalised by recycing plastic.
 def plastic_recycled(self):
   if not isinstance (self.recycle, float):#defensive programing
            raise TypeError("Data isn't numeric")
        
   if self.recycle<0:
            raise ValueError("The numeric data isn't positive")
        
   recycled_carbon=self.recycle*2.54#multipying with per kg of carbon emission
   return recycled_carbon
  #carbon emsision for foil is calculated
 def carbon_foil(self):
    if not isinstance (self.foil, float):
            raise TypeError("Data isn't numeric")#defensive programming
        
    if self.foil<0:
            raise ValueError("The numeric data isn't positive")
        
    foil_carbon=self.foil*3.1#multiplying it per kg of carbon emission
    return foil_carbon


 def total_carbon_dict(self, total_carbon):
    dict_total=dict(zip("Total carbon emission from plastic:",total_carbon))
    return dict_total

   
   






