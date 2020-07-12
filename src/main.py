import sys
import getopt
from utils import ROOT_DIR


class InvalidArgument(Exception):
    pass


if __name__ == "__main__":
    full_cmd_args = sys.argv
    argument_list = full_cmd_args[1:]
    short_options = "b:n:d:"
    long_options = ["bpm=", "file_name=", "file_dir="]

    bpm = 60
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

    
