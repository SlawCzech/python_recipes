from oop.events.abs_event import EventAbc
from datetime import datetime, timedelta


class Event(EventAbc):
    def __init__(self, start_date, title, duration, participants):
        self._start_date = datetime.strptime(start_date, "%Y-%m-%d, %H:%M")
        self._title = title
        self._duration = duration
        self._participants = participants

    @classmethod
    def create_default_event(cls, start_date=datetime.today() + timedelta(days=1), title="Default meeting", duration=15,
                             participants=None):
        return cls(start_date=start_date, title=title, duration=duration, participants=participants)

    @staticmethod
    def greeting(name):

        return f"Hello {name}! This is your event planner. "

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        try:
            self._start_date = datetime.strptime(value, "%Y-%m-%d, %H:%M")
        except ValueError:
            print("Cannot set new starting date. Please provide new date in the following format: YYYY-MM-DD, hh:mm")

    @property
    def duration(self):
        return f'{self._duration} minutes'

    @duration.setter
    def duration(self, value):
        if value < 15:
            raise ValueError("Duration cannot be shorter than 15 minutes.")
        self._duration = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._participants = value

    @title.deleter
    def title(self):
        del self._title

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value):
        self._participants = value

    @participants.deleter
    def participants(self):
        self._participants = []

    def get_remaining_time(self):
        time_left = self._start_date - datetime.now()
        return f"{time_left.days} days and {time_left.seconds // 3600} hours remaining until {self._title}."

    def __str__(self):
        event_participants = None
        if self._participants is not None:
            event_participants = ", ".join(self._participants)
        return f'{self._title} planned on {self._start_date} with {event_participants}. Estimated time: {self._duration} minutes.'

    def __repr__(self):
        attrs = ', '.join(
            f'{key[1:] if key.startswith("_") else key}={repr(value)}' for key, value in vars(self).items())
        return f'{type(self).__name__}({attrs})'


event_1 = Event('2023-07-05, 13:00', 'My meeting', 60, ['Myself', 'Janek'])
# print(vars(event_1))
# print(repr(event_1))
print(event_1)
print(event_1.start_date)
# event_1.start_date = "2020-08-12"
# print(event_1.start_date)
print(event_1.get_remaining_time())

# default_event = Event.create_default_event()
# print(default_event)
# print(repr(default_event))
