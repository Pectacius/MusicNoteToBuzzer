# Music Score Generator for Buzzers on Arduino
## Description:
Allows a music score to be played on an Arduino buzzer. 
Converts a music score to buzzer frequencies and duration. Music score is converted to the
`void play()` method in the outputted `.cpp` file

## Usage:
1. Input music score in `music_score.csv`
2. run `main.py -b <song bpm> -n <generated file name> -d <generated file location>`
    - `<song bpm>` defaults to 60 bpm
    - `<generated file name>` defaults to `music_score.cpp`
    - `<generated file location` defaults to `.\MusicNoteToBuzzer\data\`
3. Generates a `.cpp` file with music score generated in `void play()` method

## Music score input guide
