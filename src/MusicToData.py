from utils import ROOT_DIR


class MusicDataConverter(object):
    MUSIC_SCORE_DIR = f'{ROOT_DIR}\\data\\music_score.csv'
    MUSIC_MAPPER_DIR = f'{ROOT_DIR}\\data\\music_note_mapper.csv'
    NOTE_FREQUENCY_MAPPER = {}
    QUARTER_NOTE_LENGTH = 1000  # in milliseconds for 60 bpm

    def __init__(self, bpm):
        self.bpm = bpm
        self.NEW_NOTE_LENGTH = self.QUARTER_NOTE_LENGTH/(self.bpm/60)

    # opens both files
    def open_files(self):
        with open(self.MUSIC_MAPPER_DIR, 'r') as mapper, open(self.MUSIC_SCORE_DIR, 'r') as score:
            # make table into dictionary for easier note mapping
            for line in mapper:
                # strip via commas
                list_of_values = line.strip(',')

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




    def apply_transformation(self):
        pass