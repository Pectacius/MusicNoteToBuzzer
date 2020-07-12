from dataclasses import dataclass


# represents a musical note
@dataclass
class Note(object):
    name: str  # name of note, ie "middle C" as C4
    frequency: int  # in Hertz
    time: int  # in milliseconds
