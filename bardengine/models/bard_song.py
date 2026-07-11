from dataclasses import dataclass, field
from .bard_track import BardTrack

@dataclass(slots=True)
class BardSong:

    filename: str = ""

    midi_type: int = 1

    ticks_per_beat: int = 480

    tracks: list[BardTrack] = field(default_factory=list)

    @property
    def track_count(self):
        return len(self.tracks)

    @property
    def total_notes(self):
        return sum(track.note_count for track in self.tracks)