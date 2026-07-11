from dataclasses import dataclass


@dataclass(slots=True)
class ActiveNote:
    start: int
    velocity: int