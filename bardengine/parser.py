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


class MidiParser:
    """
    Classe responsável pela leitura de arquivos MIDI.
    """

    def load(self, filename: str) -> BardSong:
        """
        Carrega um arquivo MIDI e retorna um BardSong.

        Parameters
        ----------
        filename : str
            Caminho do arquivo MIDI.

        Returns
        -------
        BardSong
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

            song.tracks.append(track)

        return song