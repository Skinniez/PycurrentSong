# OBS Spotify Current Song

This script retrieves the currently playing song information from the Spotify desktop app and saves the song name, artist, and combined information to separate text files. This can be useful for displaying the current song information in OBS or other streaming software.

## Requirements

- Python 3.6 or higher
- `pywin32` package
- Spotify desktop app

## Installation

1. Install Python 3.6 or higher from the [official website](https://www.python.org/downloads/).

2. Install the required Python package `pywin32`:

## Usage

1. Save the provided script as `obscurrentsong.py` (or any other name you prefer) in a directory of your choice.

2. Open a command prompt or terminal, navigate to the directory containing the script, and run the script:


Replace `path/to/your/script` with the actual directory path where the script is saved.

3. The script will continuously check for the currently playing song in the Spotify desktop app and save the song and artist information to separate text files in the `./data` directory (relative to the script location). The text files will be named `artist.txt`, `song.txt`, `entire.txt`, and `entire-descending.txt`.

4. You can use these text files as sources in OBS or other streaming software to display the current song information on your stream.

## Notes

- Make sure the Spotify desktop app is running and a song is playing for the script to work correctly.
- If the script is not working as expected, please ensure you have installed the `pywin32` package and are running the script using Python 3.6 or higher.
