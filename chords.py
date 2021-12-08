from common import *
from interval import *

def interpret(root) -> list[int]:
    octaves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if type(root) == str:
        if len(root) == 1 and root in NAMES:
            return [NAME_TO_NOTE.get(root + '5')]
        if len(root) == 2 and root[0] in NAMES:
            if root[1] in ['#', 'b']:
                return [NAME_TO_NOTE.get(root + '5')]
            elif root[1] in octaves:
                return [NAME_TO_NOTE.get(root)]
        if len(root) == 3 and root[0] in NAMES:
            if root[1] in ['#', 'b'] and root[2] in octaves:
                return [NAME_TO_NOTE.get(root)]
    elif type(root) == int:
        return [root]
    else:
        raise ValueError(f'Bad input: {root}')

def minor(root: int) -> list[int]:
    notes = interpret(root)
    notes.append(minor_third(notes[0]))
    notes.append(perfect_fifth(notes[0]))
    return notes

def major(root: int) -> list[int]:
    notes = interpret(root)
    notes.append(major_third(notes[0]))
    notes.append(perfect_fifth(notes[0]))
    return notes

def diminished(root: int) -> list[int]:
    notes = interpret(root)
    notes.append(minor_third(notes[0]))
    notes.append(diminished_fifth(notes[0]))
    return notes

def augmented(root: int) -> list[int]:
    notes = interpret(root)
    notes.append(major_third(notes[0]))
    notes.append(augmented_fifth(notes[0]))
    return notes

def minor6(root: int) -> list[int]:
    notes = minor(root)
    notes.append(major_sixth(notes[0]))
    return notes

def major6(root: int) -> list[int]:
    notes = major(root)
    notes.append(major_sixth(notes[0]))
    return notes

def minor7(root: int) -> list[int]:
    notes = minor(root)
    notes.append(minor_seventh(notes[0]))
    return notes

def major7(root: int) -> list[int]:
    notes = major(root)
    notes.append(major_seventh(notes[0]))
    return notes

def dominant7(root: int) -> list[int]:
    notes = major(root)
    notes.append(minor_seventh(notes[0]))
    return notes

def halfdim7(root: int) -> list[int]:
    notes = diminished(root)
    notes.append(minor_seventh(notes[0]))
    return notes

def fulldim7(root: int) -> list[int]:
    notes = diminished(root)
    notes.append(diminished_seventh(notes[0]))
    return notes

def minor7_b9(root: int) -> list[int]:
    notes = minor7(root)
    notes.append(minor_ninth(notes[0]))
    return notes

def major7_b9(root: int) -> list[int]:
    notes = major7(root)
    notes.append(minor_ninth(notes[0]))
    return notes

def dominant7_b9(root: int) -> list[int]:
    notes = dominant7(root)
    notes.append(minor_ninth(notes[0]))
    return notes

def minor9(root: int) -> list[int]:
    notes = minor7(root)
    notes.append(major_ninth(notes[0]))
    return notes

def major9(root: int) -> list[int]:
    notes = major7(root)
    notes.append(major_ninth(notes[0]))
    return notes

def dominant9(root: int) -> list[int]:
    notes = dominant7(root)
    notes.append(major_ninth(notes[0]))
    return notes

def major69(root: int) -> list[int]:
    notes = major6(root)
    notes.append(major_ninth(notes[0]))
    return notes

def minor11(root: int) -> list[int]:
    notes = minor9(root)
    notes.append(major_eleventh(notes[0]))
    return notes

def major_sharp11(root: int) -> list[int]:
    notes = major9(root)
    notes.append(augmented_eleventh(notes[0]))
    return notes

def invert(chord, times=1, direction=UP):
    if direction == UP:
        for _ in range(times):
            chord = chord[1:] + [octave(chord[0])]
    elif direction == DOWN:
        for _ in range(times):
            chord = [octave(chord[-1], DOWN)] + chord[:-1]
    return chord