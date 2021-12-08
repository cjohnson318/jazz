import pygame.midi

from common import *
import chords


def lead_sheet(filename: str) -> list[list[int]]:
    '''Take a file of chord names, and return a list of list of ints.
    '''
    score = open(filename, 'r').readlines()
    score = [line.strip() for line in score]
    score = ' '.join(score)
    score = score.split(' ')
    expanded = []
    for item in score:
        if item == '/':
            expanded.append(previous)
        else:
            expanded.append(item)
        previous = expanded[-1]
    score = list(map(parse_chord, expanded))
    return score

def parse_chord(chord: str) -> list[int]:
    '''Turn a chord name into a list of ints, representing MIDI pitches.
    '''
    token = _parse_chord_parts(chord)
    print(token)
    name = token.get('name')
    quality = token.get('quality')
    if quality == 'MIN':
        return _resolve_minor_chord(token)
    elif quality == 'MAJ':
        return _resolve_major_chord(token)
    elif quality == 'DOM':
        return _resolve_dominant_chord(token)
    elif quality == 'HDIM':
        return chords.halfdim7(name)
    elif quality == 'FDIM':
        return chords.fulldim7(name)
    else:
        return None

def _parse_chord_parts(chord: str) -> dict:
    '''Convert a chord name to a token dict.
    '''
    result = {'chord': chord}
    chord = list(chord)
    result['name'], chord = _parse_chord_name(chord)
    result['quality'], chord = _parse_chord_quality(chord)
    result['extension'], chord = _parse_chord_extension(chord)
    result['alteration'] = _parse_chord_alteration(chord)
    if result['quality'] == None:
        result['quality'] = 'DOM'
    return result

def _parse_chord_name(chord: list[str]) -> tuple[str, list]:
    name = chord.pop(0)
    if chord[0] in ['#', 'b']:
        name += chord.pop(0)
    return name, chord

def _parse_chord_quality(chord: list[str]) -> tuple[str, list]:
    quality = None
    if len(chord) >= 4:
        quality = ''.join(list(map(str.upper, chord[:4])))
        if quality in ['HDIM', 'FDIM']:
            return quality, chord[4:] 
    if len(chord) >= 3:
        quality = ''.join(list(map(str.upper, chord[:3])))
        if quality in ['MAJ', 'MIN', 'DOM', 'DIM', 'AUG', 'SUS']:
            return quality, chord[3:]
    if len(chord) >= 1: 
        if chord[0] == 'm':
            return 'MIN', chord[1:]
        elif chord[0] == 'M':
            return 'MAJ', chord[1:]
    return None, chord

def _parse_chord_extension(chord: list[str]) -> tuple[str, list]:
    if len(chord) >= 3:
        extension = ''.join(chord[:3])
        if extension in ['6/9']:
            return extension, chord[3:]
    if len(chord) >= 2:
        extension = ''.join(chord[:2])
        if extension in ['11', '13']:
            return extension, chord[2:]
    if len(chord) >= 1:
        if chord[0] in ['6', '7', '9']:
            return chord[0], chord[1:]
    return None, chord
    
def _parse_chord_alteration(chord: list[str]) -> list[str]:
    alterations = []
    while len(chord) > 0:
        if len(chord) >= 3:
            alteration = ''.join(chord[:3])
            if alteration in ['#11', 'b13']:
                alterations.append(alteration)
                chord = chord[3:]
        elif len(chord) >= 2:
            print(f'chord: {chord}')
            alteration = ''.join(chord[:2])
            if alteration in ['b5', '#5', 'b9', '#9']:
                alterations.append(alteration)
                chord = chord[2:]
    return alterations

def _resolve_minor_chord(token):
    name = token.get('name')
    quality = token.get('quality')
    extension = token.get('extension')
    alteration = token.get('alteration')
    if extension == '6':
        return chords.minor6(name)
    elif extension == '7':
        if alteration == ['b5']:
            return chords.halfdim7(name)
        elif alteration == ['b9']:
            return chords.minor7_flat9(name)
        elif alteration == ['#9']:
            return chords.minor7_sharp9(name)
        return chords.minor7(name)
    elif extension == '9':
        return chords.minor9(name)
    else:
        return chords.minor(name)

def _resolve_major_chord(token):
    name = token.get('name')
    quality = token.get('quality')
    extension = token.get('extension')
    alteration = token.get('alteration')
    if extension == '6':
        return chords.major6(name)
    elif extension == '7':
        if alteration == ['b9']:
            return chords.major7_flat9(name)
        elif alteration == ['#9']:
            return chords.major7_sharp9(name)
        elif alteration == ['#11']:
            return chords.major_sharp11(name)
        return chords.major7(name)
    elif extension == '9':
        return chords.major9(name)
    else:
        return chords.major(name)

def _resolve_dominant_chord(token):
    name = token.get('name')
    quality = token.get('quality')
    extension = token.get('extension')
    alteration = token.get('alteration')
    if extension == '7':
        if alteration == ['b9']:
            return chords.dominant7_flat9(name)
        elif alteration == ['#9']:
            return chords.dominant7_sharp9(name)
        return chords.dominant7(name)
    elif extension == '9':
        return chords.dominant9(name)
    else:
        return chords.dominant(name)