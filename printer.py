import abjad

import chords
import common
import parse

def name_to_lilypond_pitch(name: str) -> str:
    return str(abjad.NamedPitch(name))

def names_to_lilypond_pitches(names: list[str]) -> str:
    pitches = [name_to_lilypond_pitch(name) for name in names]
    pitches =  ' '.join(pitches)
    return pitches

def pitches_to_lilypond_chord(pitches: list[str], duration=None) -> str:
    if duration is None:
        return f'<{pitches}>'
    else:
        return f'<{pitches}>{duration}'

def note_to_lilypond_pitch(note: int) -> str:
    name = common.note_to_name(note)
    pitch = name_to_lilypond_pitch(name)
    return pitch

def notes_to_lilypond_pitches(notes: list[int]) -> str:
    names = common.notes_to_names(notes)
    pitches = names_to_lilypond_pitches(names)
    return pitches

def notes_to_lilypond_chord(notes: list[int], duration:int=None) -> str:
    pitches = notes_to_lilypond_pitches(notes)
    chord = pitches_to_lilypond_chord(pitches, duration)
    return chord

def print_score(score: list[list[int]]) -> ():
    voice = abjad.Voice(score, name="RH_Voice")
    staff = abjad.Staff([voice], name="RH_Staff")
    score = abjad.Score([staff], name="Score")
    abjad.show(score)

def condense_score(score) -> list[list[list[int]]]:
    condensed = []
    previous = None
    for i, item in enumerate(score):
        if i == 0:
            previous = item
            condensed.append([previous, 1])
            continue
        else:
            if item == previous:
                condensed[-1][1] += 1
            else:
                condensed.append([item, 1])
                previous = item
    return condensed

def condensed_score_to_lilypond_chords(score: list[list[int]]) -> list[str]:
    result = []
    for item in score:
        print(item)
        chord, duration = item
        chord = notes_to_lilypond_chord(chord)
        if duration == 4:
            result.append(chord+'1')
        elif duration == 3:
            result.append(chord+'2')
            result.append(chord)
        elif duration == 2:
            result.append(chord+'2')
        else:
            result.append(chord)
    return result
            

if __name__ == '__main__':
    filename = 'autumn-leaves.txt'
    score = parse.lead_sheet(filename, voice_lead=True)
    score = condense_score(score)
    score = condensed_score_to_lilypond_chords(score)
    print_score(score)