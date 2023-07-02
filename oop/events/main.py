from oop.events.reminder import Reminder
from oop.events.workshop import Workshop
from oop.events.event import Event


class EventCreator(Event):
    def __new__(cls, *args, **kwargs):
        if kwargs.get("speaker"):
            self = Workshop(*args, **kwargs)
        elif kwargs.get("remind"):
            self = Reminder(*args, **kwargs)
        else:
            self = Event(*args, **kwargs)
        return self


# event_one = EventCreator(start_date="2023-09-01, 10:00", title="Good event", duration=55, participants=["Brunhilde", "Gunhilde"])
# print(event_one)
# print(repr(event_one))
# print(type(event_one).__name__)
#
# workshop_one = EventCreator(start_date="2023-09-01, 10:00", title="Good event", duration=55, participants=["Brunhilde", "Gunhilde"], speaker="Magister")
# print(workshop_one)
# print(repr(workshop_one))
# print(type(workshop_one).__name__)
#
# reminder_one = EventCreator(start_date="2023-09-01, 10:00", title="Good event", duration=55, participants=["Brunhilde", "Gunhilde"], remind=True)
# print(reminder_one)
# print(repr(reminder_one))
# print(type(reminder_one).__name__)
