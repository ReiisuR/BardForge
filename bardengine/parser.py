"""
BardForge

parser.py

Responsável por converter arquivos MIDI
em objetos internos do BardForge.
"""

from pathlib import Path

from mido import MidiFile

from bardengine.models.bard_song import BardSong
from bardengine.models.bard_track import BardTrack
from bardengine.models.bard_note import BardNote
from bardengine.models.active_note import ActiveNote


class MidiParser:
    """
    Classe responsável pela leitura de arquivos MIDI.
    """

    def load(self, filename: str) -> BardSong:
        """
        Carrega um arquivo MIDI e retorna um BardSong.
        """

        midi = MidiFile(filename)

        song = BardSong(
            filename=Path(filename).name,
            midi_type=midi.type,
            ticks_per_beat=midi.ticks_per_beat,
        )

        for midi_track in midi.tracks:

            track = BardTrack(
                name=midi_track.name or "Unnamed Track"
            )

            self._parse_track(track, midi_track)

            song.tracks.append(track)

        return song

    def _parse_track(
        self,
        bard_track: BardTrack,
        midi_track
    ) -> None:

        active_notes: dict[tuple[int, int], ActiveNote] = {}

        current_time = 0

        for message in midi_track:

            current_time += message.time

            # Ignora tudo que não for nota
            if message.type not in ("note_on", "note_off"):
                continue

            if message.type == "note_on" and message.velocity > 0:
                self._handle_note_on(
                    active_notes,
                    message,
                    current_time,
                )

            else:
                self._handle_note_off(
                    active_notes,
                    bard_track,
                    message,
                    current_time,
                )

    def _handle_note_on(
        self,
        active_notes: dict,
        message,
        current_time: int,
    ) -> None:

        key = (message.channel, message.note)

        active_notes[key] = ActiveNote(
            start=current_time,
            velocity=message.velocity,
        )

    def _handle_note_off(
        self,
        active_notes: dict,
        bard_track: BardTrack,
        message,
        current_time: int,
    ) -> None:

        key = (message.channel, message.note)

        active = active_notes.pop(key, None)

        if active is None:
            return

        bard_track.notes.append(
            BardNote(
                note=message.note,
                velocity=active.velocity,
                start=active.start,
                end=current_time,
            )
        )