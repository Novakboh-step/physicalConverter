from Converter import Converter

class TimeConverter(Converter):
    def __init__(self):
        super().__init__({"y": 1, "mon": 30.436875,"d": 365.2425, "h": 8765.82, "min": 525949.2, "s": 31556952, "ms": 31556952000})