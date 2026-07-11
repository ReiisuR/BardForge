from dataclasses import dataclass

@dataclass(slots=True)
class BardNote:
    note: int
    velocity: int
    start: int
    end: int

    @property
    def duration(self):
        return self.end - self.start