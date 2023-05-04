class Car:
    color = "Black"
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def car_start (self):
        return f"my {self.color} car has started "
    def accerelate (self):
        return f"my {self.color} car I bought it in the year {self.year}."
    def deccerelate (self):
        return f"{self.model}, deccerelate when the fuel is up."
