class ElementYagudin:
    def __init__(self, name: str, symbol: str, number: int):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def dump(self):
        print(f"Name: {self.__name}, Symbol: {self.__symbol}, Number: {self.__number}")

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number
    
if __name__ == "__main__":
    cobalt = ElementYagudin(name="Кобальт", symbol="Co", number=27)
    cobalt.dump()