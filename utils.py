import sys
import time

import pygame
import pygame.midi

from common import *

def play(notes, device) -> ():
    for note in notes:
        device.note_on(note, MAX_VOLUME)
        time.sleep(STRUM)
    time.sleep(PAUSE)
    for note in notes: 
        device.note_off(note, MAX_VOLUME)
    time.sleep(PAUSE)

def init() -> pygame.midi.Output:
    pygame.init()
    pygame.midi.init()
    port = pygame.midi.get_default_output_id()
    device = pygame.midi.Output(port, 0)
    device.set_instrument(0)
    screen = pygame.display.set_mode((400, 400))
    return device

def exit() -> ():
    pygame.midi.quit()
    pygame.quit()
    sys.exit()

def quit_listener() -> ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()