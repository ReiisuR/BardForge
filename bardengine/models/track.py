from dataclasses import dataclass, field

@dataclass
class BardTrack:

    name: str = ""

    notes: list = field(default_factory=list)