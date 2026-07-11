from dataclasses import dataclass, field
from .bard_note import BardNote

@dataclass(slots=True)
class BardTrack:

    name: str = ""

    channel: int = 0

    program: int = 0

    notes: list[BardNote] = field(default_factory=list)

    @property
    def note_count(self):
        return len(self.notes)