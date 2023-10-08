
import ast
from midiutil import MIDIFile
from collections import deque
try:
    from collections.abc import Iterable, Sequence
except ImportError:
    from collections import Iterable, Sequence

from audiolazy import str2midi
import numpy as np
import pandas as pd


filename = "video_data.csv"
frames_per_second = 2


def normalize(number, min_value, max_value):
    # Find the corresponding index in the note_names list
    index = number % max_value
    # Return the corresponding musical note
    return index

# A voicing of a Cmaj13#11 chord, notes from C lydian
note_names = ['C1', 'C2', 'G2',
             'C3', 'E3', 'G3', 'A3', 'B3',
             'D4', 'E4', 'G4', 'A4', 'B4',
             'D5', 'E5', 'G5', 'A5', 'B5',
             'D6', 'E6', 'F#6', 'G6', 'A6']

# 4 octaves for a major scale
# note_names = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
#               'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
#               'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
#               'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']


# 4 octaves of a pentatonic scale
# note_names = ['C2', 'C2', 'E2', 'G2', 'A2',
#               'C3', 'D3', 'E3', 'G3', 'A3',
#               'C4', 'D4', 'E4', 'G4', 'A4',
#               'C5', 'D5', 'E5', 'G5', 'A5']

vel_min, vel_max = 35, 127  # Minimum and maximum note velocity

note_midis = [str2midi(n) for n in note_names]  # Make a list of MIDI note numbers
n_notes = len(note_midis)

#print(note_midis)

min_value = 1
max_value = 10
min_result = 10
max_result = 100

df = pd.read_csv(filename)

def map_value(value, min_value, max_value, min_result, max_result):
    result = min_result + (value - min_value) / (max_value - min_value) * (max_result - min_result)
    return result

duration = len(df)

y_scale = 0.5  # Scaling parameter for y-axis data (1 = linear)

# Map y-axis data to MIDI notes and velocity
midi_data = []
vel_data = []

data = []

for row in df.itertuples(index=False):
    time = row[0]
    instruments = [list(row[i:i + 4]) for i in range(1, len(row), 4)]
    data.append((time, instruments))

bpm = 60  # Tempo (beats per minute)
ppq_resolution = 480

midi = MIDIFile(9)  # One track
midi.addTempo(track=0, time=0, tempo=bpm)
time_change = 0

for time, instruments in data:
    time_change += 1
    #print(time)
    for instrument in instruments:
        array = ast.literal_eval(instrument[0])
        for quadrant in array:
            instrument_number = quadrant[0]
            channel = quadrant[0]
            #print(quadrant[1])
            array_midi = np.array(quadrant[1])

            velocity = int(array_midi[0])
            velocity = int(array_midi[1])
            
            duration = normalize(velocity, 0, 480) + 1

            pitch = int(array_midi[1])
            pitch = note_midis[normalize(pitch, 0, len(note_midis))]

            #pitch = int(array_midi[2])
            #pitch = note_midis[normalize(pitch, 0, len(note_midis))]

            volume = int(array_midi[2])
            volume = int(array_midi[1])
            
            velocity = normalize(velocity, 30, 127)
            scale = normalize(instrument_number, 0, 127)
            duration = 1 / frames_per_second
            track = channel - 1
            tempo_to_add = time

            midi.addNote(track=track, channel=channel, pitch=pitch, time=tempo_to_add, duration=duration, volume=volume)

            #print("track: " + str(track) + "  -- pitch: " + str(pitch) + " -- time: " + str(tempo_to_add) + "  -- duration: " + str(duration) + "  -- volume:" + str(volume))

with open('output.mid', "wb") as f:
    midi.writeFile(f)

#print('Saved', 'output.mid')
# https://www.youtube.com/watch?v=aysiMbgml5g
# Polarity - high numbers represent high notes or high numbers represent low notes
# Range of notes and volumes
# Transform data into note parameters, standardize
# Pitch and velocity

# pip install audiolazy
# pip install pandas
# pip install mapping
# pip install midutil
# pip install numpy
# pip install --upgrade dbus-python 

import ast
from midiutil import MIDIFile
from collections import deque
try:
    from collections.abc import Iterable, Sequence
except ImportError:
    from collections import Iterable, Sequence

from audiolazy import str2midi
import numpy as np
import pandas as pd
filename = "video_data.csv"

def normalize(number, min_value, max_value):
    # Find the corresponding index in the note_names list
    index = number % max_value
    # Return the corresponding musical note
    return index

# A voicing of a Cmaj13#11 chord, notes from C lydian
note_names = ['C1', 'C2', 'G2',
             'C3', 'E3', 'G3', 'A3', 'B3',
             'D4', 'E4', 'G4', 'A4', 'B4',
             'D5', 'E5', 'G5', 'A5', 'B5',
             'D6', 'E6', 'F#6', 'G6', 'A6']

# 4 octaves for a major scale
# note_names = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
#               'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
#               'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
#               'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']

duration = 33
frames_per_second = 2

# 4 octaves of a pentatonic scale
# note_names = ['C2', 'C2', 'E2', 'G2', 'A2',
#               'C3', 'D3', 'E3', 'G3', 'A3',
#               'C4', 'D4', 'E4', 'G4', 'A4',
#               'C5', 'D5', 'E5', 'G5', 'A5']

vel_min, vel_max = 35, 127  # Minimum and maximum note velocity

note_midis = [str2midi(n) for n in note_names]  # Make a list of MIDI note numbers
n_notes = len(note_midis)

print(note_midis)

min_value = 1
max_value = 10
min_result = 10
max_result = 100

df = pd.read_csv(filename)

def map_value(value, min_value, max_value, min_result, max_result):
    result = min_result + (value - min_value) / (max_value - min_value) * (max_result - min_result)
    return result

duration = len(df)

y_scale = 0.5  # Scaling parameter for y-axis data (1 = linear)

# Map y-axis data to MIDI notes and velocity
midi_data = []
vel_data = []

data = []

for row in df.itertuples(index=False):
    time = row[0]
    instruments = [list(row[i:i + 4]) for i in range(1, len(row), 4)]
    data.append((time, instruments))

bpm = 60  # Tempo (beats per minute)
ppq_resolution = 480

midi = MIDIFile(9)  # One track
midi.addTempo(track=0, time=0, tempo=bpm)
time_change = 0

for time, instruments in data:
    time_change += 1
    print(time)
    for instrument in instruments:
        array = ast.literal_eval(instrument[0])
        for quadrant in array:
            instrument_number = quadrant[0]
            channel = quadrant[0]
            print(quadrant[1])
            array_midi = np.array(quadrant[1])
            velocity = int(array_midi[0])
            velocity = int(array_midi[1])
            duration = normalize(velocity, 0, 480) + 1
            pitch = int(array_midi[1])
            pitch = note_midis[normalize(pitch, 0, len(note_midis))]
            pitch = int(array_midi[2])
            pitch = note_midis[normalize(pitch, 0, len(note_midis))]
            volume = int(array_midi[2])
            volume = int(array_midi[1])
            velocity = normalize(velocity, 30, 127)
            scale = normalize(instrument_number, 0, 127)
            duration = 1 / frames_per_second
            track = channel - 1
            tempo_to_add = time

            midi.addNote(track=track, channel=channel, pitch=pitch, time=tempo_to_add, duration=duration, volume=volume)

            #print("track: " + str(track) + "  -- pitch: " + str(pitch) + " -- time: " + str(tempo_to_add) + "  -- duration: " + str(duration) + "  -- volume:" + str(volume))

with open('output.mid', "wb") as f:
    midi.writeFile(f)

print('Saved', filename + '.mid')
