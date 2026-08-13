from abc import ABC, abstractmethod

class InsufficientBatteryError(Exception):
    pass

class Robot(ABC):
    manufacturer = "Robots"
    population  = 0

    def __init__(self, name: str, battery: int = 100):
        self.name = name
        self._battery = 0
        self.battery = battery

        Robot.population += 1

    @property
    def battery(self) -> int:
        return self._battery
    @battery.setter
    def battery(self, value: int):
        if value < 0:
            self._battery = 0
        elif value > 100:
            self._battery = 100
        else:
            self._battery = value

    def __str__(self) -> str:
        return f"{self.name} ({self.battery}%battery)"
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', battery={self.battery})"

    @abstractmethod
    def perform_task(self):
        pass