from bardengine.parser import MidiParser
from bardengine.analyzer import MidiAnalyzer

print("=" * 40)
print(" BardForge v0.1.0")
print("=" * 40)

parser = MidiParser()
analyzer = MidiAnalyzer()

song = parser.load("samples/Evangelion - Cruel Angel's Thesis.mid")

report = analyzer.analyze(song)

print(f"Arquivo........: {report.filename}")
print(f"Trilhas........: {report.track_count}")
print(f"Notas..........: {report.total_notes}")
print(f"PPQ............: {report.ticks_per_beat}")
print(f"Nota mínima....: {report.lowest_note}")
print(f"Nota máxima....: {report.highest_note}")
print(f"Duração........: {report.duration} ticks")