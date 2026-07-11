from bardengine.models.bard_song import BardSong
from bardengine.models.analysis_report import AnalysisReport


class MidiAnalyzer:

    def analyze(self, song: BardSong) -> AnalysisReport:

        notes = []

        for track in song.tracks:
            notes.extend(track.notes)

        if notes:

            lowest = min(note.note for note in notes)

            highest = max(note.note for note in notes)

            duration = max(note.end for note in notes)

        else:

            lowest = None
            highest = None
            duration = 0

        return AnalysisReport(

            filename=song.filename,

            track_count=song.track_count,

            total_notes=song.total_notes,

            ticks_per_beat=song.ticks_per_beat,

            lowest_note=lowest,

            highest_note=highest,

            duration=duration,
        )