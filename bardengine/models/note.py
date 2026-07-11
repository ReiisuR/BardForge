from dataclasses import dataclass

@dataclass
class BardNote:

    pitch: int

    velocity: int

    start: int

    end: int