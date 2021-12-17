import chords
from common import UP, DOWN

def chord_difference(prv: list[int], nxt: list[int]) -> int:
    if len(prv) > len(nxt):
        prv = prv[:len(nxt)]
    elif len(nxt) > len(prv):
        nxt = nxt[:len(prv)]
    result = 0
    for i in range(len(prv)):
        result += abs(prv[i] - nxt[i])
    return result

def voice_by_rotation(prv: list[int], nxt: list[int]) -> list[int]:
    action = 0
    difference = chord_difference(prv, nxt)
    while True:
        invert_up = chord_difference(prv, chords.invert(nxt, direction=UP))
        invert_down = chord_difference(prv, chords.invert(nxt, direction=DOWN))
        if invert_up < invert_down and invert_up < difference:
            difference = invert_up
            nxt = chords.invert(nxt, direction=UP)
            action += 1
        elif invert_down < invert_up and invert_down < difference:
            difference = invert_down
            nxt = chords.invert(nxt, direction=DOWN)
            action -= 1
        else:
            break
    return nxt

def voice_score(score: list[list[int]], voice=voice_by_rotation) -> list[list[int]]:
    new_voicing = []
    last_voicing = None
    for i, item in enumerate(score):
        if i == 0:
            last_voicing = item
            new_voicing.append(last_voicing)
            continue
        if item != last_voicing:
            original = item[:]
            last_voicing = voice(last_voicing, item)
        new_voicing.append(last_voicing)
    return new_voicing
