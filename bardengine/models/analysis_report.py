from dataclasses import dataclass


@dataclass(slots=True)
class AnalysisReport:

    filename: str

    track_count: int

    total_notes: int

    ticks_per_beat: int

    lowest_note: int | None

    highest_note: int | None

    duration: int