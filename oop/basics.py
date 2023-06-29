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
    def attendees(self):
        pass


class Event(EventAbc):
    def __init__(self, start_date, duration, attendees):
        self._attendees = attendees
        self._duration = duration
        self._start_date = start_date

    @property
    def start_date(self):
        return self._start_date

    @property
    def duration(self):  # formatowanie w getterze
        return f'{self._duration} minutes'

    @duration.setter
    def duration(self, value):  # walidacja w setterze
        if value < 50:
            raise ValueError("Duration cannot be shorter than 50 minutes.")
        self._duration = value

    @property
    def attendees(self):
        return self._attendees



event = Event('2023-07-07', 56, ['Everybody'])

print(event)
print(event.start_date)
print(event.duration)
print(event.attendees)

# event.duration = 42  # triggeruje błąd
event.duration = 60
print(event.duration)


