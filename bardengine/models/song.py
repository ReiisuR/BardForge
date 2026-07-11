from dataclasses import dataclass, field

@dataclass
class BardSong:

    filename: str = ""

    tracks: list = field(default_factory=list)