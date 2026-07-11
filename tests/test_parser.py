from bardengine.parser import MidiParser

def test_parser():

    parser = MidiParser()

    song = parser.load("samples/Evangelion - Cruel Angel's Thesis.mid")

    assert song.track_count == 2

    assert song.total_notes > 0