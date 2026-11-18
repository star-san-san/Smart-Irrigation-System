import random
from abc import ABC, abstractmethod

from .mesure import Mesure


class Sensor(ABC):

    def __init__(self, id: int, name: str, unit: str):
        self._id = id
        self._name = name
        self._unit = unit
        self._measures = []                    

    # ---------- getters / setters ----------
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def unit(self) -> str:
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        self._unit = unit

    @property
    def measures(self) -> list:
        return list(self._measures)

    # ---------- operations ----------
    @abstractmethod
    def read_value(self) -> float:
        """Lit la valeur du capteur (simulation)."""

    @abstractmethod
    def is_valid(self, value: float) -> bool:
        """Chaque capteur a son propre intervalle de validite."""

    def produce_measure(self, mesure_id: int) -> Mesure:
        value = self.read_value()
        m = Mesure(mesure_id, value, self._unit, self, self.is_valid(value))
        self._measures.append(m)
        return m


class TemperatureSensor(Sensor):
    def __init__(self, id: int, name: str, unit: str = "°C"):
        super().__init__(id, name, unit)

    def read_value(self) -> float:
        return round(random.uniform(-15, 65), 1)       

    def is_valid(self, value: float) -> bool:
        return -10 <= value <= 60


class WaterLevelSensor(Sensor):
    def __init__(self, id: int, name: str, unit: str = "%", reserve=None):
        super().__init__(id, name, unit)
        self._reserve = reserve                         

    @property
    def reserve(self):
        return self._reserve

    @reserve.setter
    def reserve(self, reserve):
        self._reserve = reserve

    def read_value(self) -> float:
        return round(random.uniform(-5, 105), 1)       

    def is_valid(self, value: float) -> bool:
        return 0 <= value <= 100


class MoistureSensor(Sensor):
    def __init__(self, id: int, name: str, unit: str = "%"):
        super().__init__(id, name, unit)

    def read_value(self) -> float:
        return round(random.uniform(-5, 105), 1)       

    def is_valid(self, value: float) -> bool:
        return 0 <= value <= 100