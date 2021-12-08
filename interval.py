from common import UP, DOWN

def minor_second(note: int) -> int:
    return note + 1

def major_second(note: int) -> int:
    return note + 2

def augmented_second(note: int) -> int:
    return note + 3

def minor_third(note: int) -> int:
    return note + 3

def major_third(note: int) -> int:
    return note + 4

def perfect_fourth(note: int) -> int:
    return note + 5

def augmented_fourth(note: int) -> int:
    return note + 6

def diminished_fifth(note: int) -> int:
    return note + 6

def perfect_fifth(note: int) -> int:
    return note + 7

def augmented_fifth(note: int) -> int:
    return note + 8

def minor_sixth(note: int) -> int:
    return note + 8

def major_sixth(note: int) -> int:
    return note + 9

def diminished_seventh(note: int) -> int:
    return note + 9

def minor_seventh(note: int) -> int:
    return note + 10

def major_seventh(note: int) -> int:
    return note + 11

def octave(note: int, direction=UP) -> int:
    if direction == UP:
        return note + 12
    elif direction == DOWN:
        return note - 12
    else:
        raise ValueError('Expected "UP" or "DOWN".')

def minor_ninth(note: int) -> int:
    return minor_second(octave(note))

def major_ninth(note: int) -> int:
    return major_second(octave(note))

def augmented_ninth(note: int) -> int:
    return augmented_second(octave(note))

def major_eleventh(note: int) -> int:
    return perfect_fourth(octave(note))

def augmented_eleventh(note: int) -> int:
    return augmented_fourth(octave(note))

def minor_thirteenth(note: int) -> int:
    return minor_sixth(octave(note))

def major_thirteenth(note: int) -> int:
    return major_sixth(octave(note))
