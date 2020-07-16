import sys
import getopt
from utils import ROOT_DIR
from MusicToData import MusicDataConverter
from DataToCPP import DataCPPConverter


class InvalidArgument(Exception):
    pass


if __name__ == "__main__":
    full_cmd_args = sys.argv
    argument_list = full_cmd_args[1:]
    short_options = "b:n:d:"
    long_options = ["bpm=", "file_name=", "file_dir="]

    bpm = 100
    file_name = 'music_score'
    file_dir = '{}\\data'.format(ROOT_DIR)

    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
    except getopt.error as e:
        print(str(e))
        sys.exit(2)

    for current_argument, current_value in arguments:
        try:
            if current_argument in ("-b", "--bpm"):
                bpm = int(current_value)
            elif current_argument in ("-n", "--file_name"):
                file_name = current_value
            elif current_argument in ("-d", "--file_dir"):
                file_dir = current_value
            else:
                raise InvalidArgument
        except InvalidArgument as e:
            print("Invalid argument")
            sys.exit(2)
        except ValueError as e:
            print("Not a valid number")
            sys.exit(2)

    music_converter = MusicDataConverter(bpm)
    music_converter.open_files()
    music_writer = DataCPPConverter(music_converter.LIST_OF_NOTES, file_name, file_dir)
    music_writer.initialize_cons()
    music_writer.initialize_play()
    music_writer.initialize_setup()
    music_writer.initialize_loop()
    music_writer.create_file()
