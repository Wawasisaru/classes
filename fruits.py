class Fruits:
    its_fresh = "true"
    def __init__(self,sweet,color,shape,its_fresh):
        self.sweet = sweet
        self.color = color
        self.shape = shape
        self.its_fresh = its_fresh
    def eat(self):
        return f"I like eating {self.sweet} fruits"
    def buy(self):
        return f"I want to buy a {self.color} fruits"
    def price(self):
        return f"The prie of {self.sweet} fruit is expensive"
    