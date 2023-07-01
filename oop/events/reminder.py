from oop.events.event import Event


class Reminder(Event):
    def __init__(self, start_date, title, duration, participants, remind):
        super().__init__(start_date, title, duration, participants)
        self.remind = remind

