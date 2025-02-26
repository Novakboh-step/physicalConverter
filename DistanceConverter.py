from Converter import Converter

class DistanceConverter(Converter):
    def __init__(self):
        super().__init__({"km": 1, "m": 1000, "dm": 10000, "cm": 100000, "mm": 1000000, "ml": 0.6213712, "ft": 3280.839936})