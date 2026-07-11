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
    
    @property
    def duration(self):

        if not self.notes:
            return 0

        return max(note.end for note in self.notes)
    
    @property
    def lowest_note(self):

        if not self.notes:
            return None

        return min(note.note for note in self.notes)

    @property
    def highest_note(self):

        if not self.notes:
            return None

        return max(note.note for note in self.notes)