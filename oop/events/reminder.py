from oop.events.event import Event


class Reminder(Event):
    def __init__(self, start_date, title, duration, participants, remind=False):
        super().__init__(start_date, title, duration, participants)
        self._remind = bool(remind)

    @property
    def remind(self):
        return self._remind

    @remind.setter
    def remind(self, value):
        self._remind = bool(value)

    def __str__(self):
        return super().__str__() + f" Event reminder is set as {'ON' if self._remind else 'OFF'}."


reminder_1 = Reminder("2023-09-10, 10:00", "Future event", 30, ["Kasia", "Misiek"], True)

# print(reminder_1)
# print(reminder_1.greeting("robert"))
# print(reminder_1.get_remaining_time())
