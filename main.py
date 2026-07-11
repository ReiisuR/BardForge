from bardengine.parser import MidiParser

print("=" * 40)
print(" BardForge v0.1.0")
print("=" * 40)

parser = MidiParser()

song = parser.load("samples/Evangelion - Cruel Angel's Thesis.mid")

print(f"Arquivo : {song.filename}")
print(f"Tipo    : {song.midi_type}")
print(f"PPQ     : {song.ticks_per_beat}")
print(f"Trilhas : {song.track_count}")
print(f"Notas   : {song.total_notes}")