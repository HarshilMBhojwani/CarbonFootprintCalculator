class Waste:# global food waste overtakes India as the thrid biggert contributer to carbon footprint only behind Usa and china

    def __init__(self, foodwaste):
        self.foodwaste=foodwaste


    def carbon_foodwaste(self):
        carbon_waste=self.foodwaste*2.5
        return carbon_waste
    

    def foodwaste_dict(self, carbon_waste):
        waste_dict=dict(zip("Food wastage carbon emission:", carbon_waste))
        return waste_dict