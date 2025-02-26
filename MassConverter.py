from Converter import Converter

class MassConverter(Converter):
    def __init__(self):
        super().__init__({"t": 1, "kg": 1000, "g": 1000000, "mg": 1000000000, "lb": 2204.6, "oz": 35273.6})