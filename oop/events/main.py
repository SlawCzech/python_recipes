from oop.events.reminder import Reminder
from oop.events.workshop import Workshop


class EventCreator:
    def __new__(cls, *args, **kwargs):
        if kwargs.get("type") == "music":
            self = Workshop()
        elif kwargs.get("type") == "video":
            self = Reminder()
        else:
            self = super().__new__(cls)
        return self