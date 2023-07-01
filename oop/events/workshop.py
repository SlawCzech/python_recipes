from oop.events.event import Event


class Workshop(Event):
    def __init__(self, idx, start_date, duration, title, description, owner, participants):
        super().__init__(start_date, title, duration, participants)
        self.participants = participants

