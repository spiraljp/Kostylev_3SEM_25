from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

    @classmethod
    def getName(cls):
        return cls.name
