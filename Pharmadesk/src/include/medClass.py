from .countryEnum import Country

class med:
    def __init__(self, name:str, price:float, ammount:int, lab:str, country:Country):
        self.__name = name
        self._price = price
        self._ammount = ammount
        self.__lab = lab
        self.__country = country