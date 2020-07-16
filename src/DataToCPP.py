class DataCPPConverter:
    FIRST_LINE = '#include <Arduino.h>\n'
    CONSTANTS = ''
    PLAY_METHOD = ''
    SETUP = ''
    LOOP = ''

    def __init__(self, notes, name, location):
        self.LIST_OF_NOTES = notes
        self.file_name = name
        self.file_location = location

    def initialize_cons(self):
        set_of_sounds = {}
        for note in self.LIST_OF_NOTES:
            set_of_sounds[note.name] = note.frequency
        for key, value in set_of_sounds.items():
            note_name = self.replace_note(key)
            self.CONSTANTS = self.CONSTANTS + f'#define {note_name} {int(value)}\n'

    def initialize_play(self):
        note_values = ""
        note_durations = ""
        counter = 1
        for note in self.LIST_OF_NOTES:
            note_name = self.replace_note(note.name)
            note_values = note_values + note_name + ", "
            note_durations = note_durations + str(note.time) + ", "
            if counter == 5:
                note_values = note_values + '\n  '
                note_durations = note_durations + '\n  '
                counter = 0
            counter += 1

        note_values = note_values[:-1]
        note_durations = note_durations[:-1]

        notes = "int notes[] = {\n  " + note_values + "\n  };"
        times = "int times[] = {\n  " + note_durations + "\n  };"

        play = """void play(){\n  """ + notes + "\n\n  " + times + "\n\n  " + "int len = *(&notes + 1) - notes;" + \
               "\n\n  for (int i = 0; i < len; i++){\n  tone(SCL, notes[i]);\n  delay(times[i]*7/8);\n  noTone(SCL);" + \
               "delay(times[i]/8);}\n} "
        self.PLAY_METHOD = play

    def initialize_setup(self):
        self.SETUP = """void setup(){\n  pinMode(SCL, OUTPUT)\n}"""

    def initialize_loop(self):
        self.LOOP = """void loop(){}"""

    def create_file(self):
        with open(f'{self.file_location}\\{self.file_name}.cpp', 'w') as file:
            content = self.FIRST_LINE + '\n\n' + self.CONSTANTS + '\n\n' + self.SETUP + '\n\n' + self.LOOP + '\n\n' + \
                      self.PLAY_METHOD
            file.write(content)
            file.close()

    def replace_note(self, note):
        if '#' in note:
            return note.replace('#', 's')
        return note
