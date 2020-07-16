from utils import ROOT_DIR
from note import Note


class MusicDataConverter:
    MUSIC_SCORE_DIR = f'{ROOT_DIR}\\data\\music_score.csv'
    MUSIC_MAPPER_DIR = f'{ROOT_DIR}\\data\\music_note_mapper.csv'
    NOTE_FREQUENCY_MAPPER = {}
    QUARTER_NOTE_LENGTH = 1000  # in milliseconds for 60 bpm
    LIST_OF_NOTES = []

    def __init__(self, bpm):
        self.bpm = bpm
        self.NEW_NOTE_LENGTH = self.QUARTER_NOTE_LENGTH / (self.bpm / 60)
        self.NOTE_LENGTH_MAPPER = {
            "doublewhole": 8 * self.NEW_NOTE_LENGTH,
            "whole": 4 * self.NEW_NOTE_LENGTH,
            "half": 2 * self.NEW_NOTE_LENGTH,
            "quarter": self.NEW_NOTE_LENGTH,
            "eighth": 1 / 2 * self.NEW_NOTE_LENGTH,
            "sixteenth": 1 / 4 * self.NEW_NOTE_LENGTH,
            "thirtysecond": 1 / 8 * self.NEW_NOTE_LENGTH,
            "sixtyfourth": 1 / 16 * self.NEW_NOTE_LENGTH
        }

    # opens both files
    def open_files(self):
        with open(self.MUSIC_MAPPER_DIR, 'r') as mapper, open(self.MUSIC_SCORE_DIR, 'r') as score:
            # make table into dictionary for easier note mapping
            for line in mapper:
                # strip via commas
                list_of_values = line.split(',')

                # if cannot convert to float, means the row is a header, therefore skip to next row
                try:
                    frequency = round(float(list_of_values[1]))
                except ValueError:
                    continue

                # handle the note name portion
                # remove extra encoding if any
                note_name = list_of_values[0].strip('Â ')
                # split sharps and flats into two portions if any
                list_of_notes = note_name.split('/')
                self.NOTE_FREQUENCY_MAPPER[list_of_notes[0]] = frequency
                if len(list_of_notes) == 2:
                    self.NOTE_FREQUENCY_MAPPER[list_of_notes[1]] = frequency

            mapper.close()

            for line in score:
                # see if line is header, if so skip to next line
                if 'note length' in line or 'note sound' in line:
                    continue

                result = line.replace("\n", "")
                result = result.replace('ï»¿', "")
                result = result.split(',')
                length = result[0].replace(" ", "")
                sound = result[1].strip()

                list_of_length = length.split("+")

                note_length = self.NOTE_LENGTH_MAPPER.get(list_of_length[0])

                if len(list_of_length) > 1:
                    indexes = list(range(1, len(list_of_length)))
                    for i in indexes:
                        duration = self.NOTE_LENGTH_MAPPER.get(list_of_length[i])
                        note_length = note_length + duration

                note_frequency = self.NOTE_FREQUENCY_MAPPER.get(sound)

                note = Note(sound, note_frequency, note_length)
                self.LIST_OF_NOTES.append(note)
