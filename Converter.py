class Converter:
    def __init__(self, units):
        self.__units = units

    def convert(self, unit1, unit2):
        try:
            return self.__units[unit2] / self.__units[unit1]
        except:
            return None