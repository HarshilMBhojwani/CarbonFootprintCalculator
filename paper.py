class Paper:#carbon emssion for paper commodities

    def __init__(self, roll=0, tissue=0, paperbag=0, recycle_paper=0):
        self.roll=roll
        self.tissue=tissue
        self.paperbag=paperbag
        self.recycle=recycle_paper


    def carbon_roll(self):
        if not isinstance (self.roll, float):
            raise TypeError("Data isn't numeric")
        
        if self.roll<0:
            raise ValueError("The numeric data isn't positive")
        roll_carbon=self.roll*(600*0.06)/4.2#this formula is to calculate the paper carbon emisson of kitvhen roll per kg
        return roll_carbon
    
    def carbon_tissue(self):
        if not isinstance (self.tissue, float):
            raise TypeError("Data isn't numeric")
        
        if self.tissue<0:
            raise ValueError("The numeric data isn't positive")
        tissue_carbon=self.tissue*2.2#calcualting the carbon emission of tissue
        return tissue_carbon
    
    def paper_bag_carbon(self):
        if not isinstance (self.paperbag, float):
            raise TypeError("Data isn't numeric")
        
        if self.paperbag<0:
            raise ValueError("The numeric data isn't positive")
        carbon_bag=self.paperbag*5.5
        return carbon_bag#the carbon emission of paper bag
    
    def recycle_paper_carbon(self):
        if not isinstance (self.recycle, float):
            raise TypeError("Data isn't numeric")
        
        if self.recycle<0:
            raise ValueError("The numeric data isn't positive")
        paper_recycle=self.recycle*6.0#carbon emssion neutralised from recycling paper
        return paper_recycle


    def total_papercarbon(self, roll, tissue):
        total_paper=roll+tissue
        paper_dict=dict(zip("Total Paper Carbon:", total_paper))
        return paper_dict



