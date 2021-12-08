# Jazz

Scripts to read chords from a file, and then generate MIDI data to be played by
a MIDI device.

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