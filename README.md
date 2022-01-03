# JazzRobot

Scripts to read chords from a file, and then generate MIDI data to be played by
a MIDI device.

So far, all chords are built from stacking thirds. There's no support for
quartal voicings, or anything else, just vanilla chords.

Voice leading is achieved by using inversions of chords until the difference
between one chord and the next is minimized. At the moment, the voicing for the
entire score is define deterministically from the voicing of the first chord,
which by default is in root position, in the fifth octave.


## Setup

This project includes a `requirements.txt`, so you can use it with a virtual
environment like so,

```bash
cd jazz
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To use this, you'll need to setup a MIDI device to play the MIDI data output by
the program.

To play MIDI music through Garage Band,

  1. Open the Audio MIDI Setup app
  2. Choose Window > Show MIDI Studio
  3. Double-click on IAC Driver
  4. Check Device is online
  5. Start Garage Band and add a software MIDI track
  6. Try to run app.py


## Usage

By default, this plays Blue in Green, but you can supply a file to be played.

```bash
python3 app.py blue-in-green.txt
```
