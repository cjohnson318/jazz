MAX_VOLUME = 127
PAUSE = 0.2
STRUM = 0.04

UP   = 'UP'
DOWN = 'DOWN'
MIDDLE_C = 72
NAMES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
ACCIDENTALS = ['b', '', '#']
NOTES_5TH_OCTAVE = [
    71, 72, 73, # C
    73, 74, 75, # D
    75, 76, 77, # E
    76, 77, 78, # F
    78, 79, 80, # G
    80, 81, 82, # A
    82, 83, 84, # B
]

def generate_names(octave: int):
    result = []
    for name in NAMES:
        for accidental in ACCIDENTALS:
            result.append(f'{name}{accidental}{octave}')
    return result

def generate_notes(octave: int):
    diff = octave - 5
    result = []
    for note in NOTES_5TH_OCTAVE:
        result.append(note + diff * 12)
    return result

ALL_NAMES = generate_names(octave=4) + generate_names(octave=5) + generate_names(octave=6)
ALL_NOTES = generate_notes(octave=4) + generate_notes(octave=5) + generate_notes(octave=6)
NAME_TO_NOTE = dict(zip(ALL_NAMES, ALL_NOTES))