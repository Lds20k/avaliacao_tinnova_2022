
class Voter:
    __total: int
    __valids: int
    __white: int
    __null: int

    def __init__(self, valids: int, white: int, null: int) -> None:
        self.__total = valids + white + null
        self.__valids = valids
        self.__white = white
        self.__null = null

    def valid_percentual(self):
        return self.__valids / self.__total
    
    def white_percentual(self):
        return self.__white / self.__total

    def null_percentual(self):
        return self.__null / self.__total
