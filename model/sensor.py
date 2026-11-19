import random
from abc import ABC, abstractmethod
from datetime import datetime

from .mesure import Mesure


class Sensor(ABC):

    def __init__(self, id, name, unit):
        self.__id = id
        self.__name = name
        self.__unit = unit
        self.__measures = []

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_unit(self):
        return self.__unit

    def get_measures(self):
        return list(self.__measures)

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_unit(self, unit):
        self.__unit = unit

    @abstractmethod
    def read_value(self):
        pass

    @abstractmethod
    def is_valid(self, value):
        pass

    def produce_measure(self, mesure_id):
        value = self.read_value()
        now = datetime.now()
        m = Mesure(mesure_id, value, self.__unit, now.date(),
                   now.time().replace(microsecond=0), self, self.is_valid(value))
        self.__measures.append(m)
        return m


class TemperatureSensor(Sensor):

    def __init__(self, id, name, unit="°C"):
        super().__init__(id, name, unit)

    def read_value(self):
        return round(random.uniform(-15, 65), 1)

    def is_valid(self, value):
        return -10 <= value <= 60


class WaterLevelSensor(Sensor):

    def __init__(self, id, name, unit="%", reserve=None):
        super().__init__(id, name, unit)
        self.__reserve = reserve

    def get_reserve(self):
        return self.__reserve

    def set_reserve(self, reserve):
        self.__reserve = reserve

    def read_value(self):
        return round(random.uniform(-5, 105), 1)

    def is_valid(self, value):
        return 0 <= value <= 100


class MoistureSensor(Sensor):

    def __init__(self, id, name, unit="%"):
        super().__init__(id, name, unit)

    def read_value(self):
        return round(random.uniform(-5, 105), 1)

    def is_valid(self, value):
        return 0 <= value <= 100
