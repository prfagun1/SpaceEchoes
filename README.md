# Space Echoes Group - NASA Space Apps Project

Welcome to the Space Echoes Group's project for NASA Space Apps! This project is a creative exploration of space-themed audio generation using Python.

## Table of Contents

- [Project Overview](#project-overview)
- [Team](#team)
- [Prerequisites](#prerequisites)
- [File Parameters](#file-parameters)https://github.com/prfagun1/SpaceEchoes/blob/main/README.md
- [Troubleshooting](#troubleshooting)

## Project Overview

This project consists of two Python scripts:

- **Composer**: Creates a data file from a video.
- **Orchestra**: Converts this data file into a .mid file for playback.

## Team

Meet the talented individuals behind this project:

- [Anderson Lopes](https://www.linkedin.com/in/andersondasilvalopes/)
- [Cristiane Adami Perozzo](https://www.linkedin.com/in/caperozzo/)
- [Herika Rodrigues de Oliveira](https://www.linkedin.com/in/herika-rodrigues-de-oliveira-174020217/)
- [Janete Formigheri](https://www.linkedin.com/in/janete-formigheri-87b82820/)
- [Matheus Frosi](https://www.linkedin.com/in/matheus-frosi-de-brito-a31743179/)
- [Pablo Rogério Fagundes](https://www.linkedin.com/in/prfagundes/)

## Prerequisites

Make sure you have the following Python packages installed:

```bash
pip install audiolazy
pip install pandas
pip install mapping
pip install midutil
pip install numpy
pip install python-opencv
pip install --upgrade dbus-python


# Configuration Parameters

Fine-tune your settings with these file parameters:

- **frames_per_second**: Determine how many frames from the video you want to capture per second.
- **quadrants**: Divide the video into parts; for example, setting it to 3 results in 9 quadrants.
- **desired_duration**: Choose to capture only a specific portion of the video if you prefer.
- **note_names**: We're using a set of musical notes, and there are two more examples included. Feel free to create your own.

```

We create a raw MIDI file with multiple channels, and these channels can be utilized by synthesizers to add an instrument to each channel and further enhance the final result. Use your creativity.

This project is licensed under the terms of the MIT License. Please refer to the [LICENSE](LICENSE) file for more details.
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green)](LICENSE)


## Attention

In case you encounter an error related to audiolazy, you'll need to make adjustments to the following files with the updated version of collections:

File: Python\site-packages\audiolazy\lazy_analysis.py
from collections import deque
from collections.abc import Sequence, Iterable

File: Python\site-packages\audiolazy\lazy_core.py
from collections.abc import Iterable


File: Python\site-packages\audiolazy\lazy_stream.py
from collections.abc import Iterable
from collections import deque

File: Python\site-packages\audiolazy\lazy_misc.py
from collections import deque
from collections.abc import Iterable


File: Python\site-packages\audiolazy\lazy_filters.py
from collections.abc import Iterable
from collections import OrderedDict


File: Python\site-packages\audiolazy\lazy_poly.py
from collections.abc import Iterable
from collections import deque, OrderedDict


File: Python\site-packages\audiolazy\lazy_itertools.py
from collections.abc import Iterator
