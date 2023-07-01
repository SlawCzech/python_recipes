from abc import ABC, abstractmethod


class EventAbc(ABC):  # klasa abstrakcyjna
    @property  # ustawia pole!
    @abstractmethod
    def start_date(self):
        pass

    @property
    @abstractmethod
    def duration(self):
        pass

    @property
    @abstractmethod
    def participants(self):
        pass
