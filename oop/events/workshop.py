from oop.events.event import Event


class Workshop(Event):
    def __init__(self, start_date, title, duration, participants, speaker):
        super().__init__(start_date, title, duration, participants)
        self._speaker = speaker

    @property
    def speaker(self):
        return self._speaker

    @speaker.setter
    def speaker(self, value):
        self._speaker = value

    def __str__(self):
        return super().__str__() + f" Invited speaker: {self._speaker}."


workshop_1 = Workshop(start_date="2023-07-10, 10:00", title="Interesting workshop", duration=120,
                      participants=["Tomek", "Basia"], speaker="Znany profesor")
print(repr(workshop_1))
workshop_1.title = "New title"
print(workshop_1)
