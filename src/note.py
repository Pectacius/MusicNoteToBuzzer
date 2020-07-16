from dataclasses import dataclass


# represents a musical note
@dataclass
class Note:
    name: str  # name of the note ie C4 for "middle C"
    frequency: int  # in Hertz
    time: int  # in milliseconds
