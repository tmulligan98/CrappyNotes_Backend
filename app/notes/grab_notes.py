from typing import List
from .sample_notes import SAMPLE_NOTES

# Given a get request to something like /my-notes... Return the 10 most recent notes
# For now, just return the top x notes of a sample list of notes
# Given an index error, return a 404 with a message

def grab_n_notes(n: int) -> List[str]:
    """Function to grab to the n (most recent?) notes

    Args:
        n (int): Number of notes to grab

    Returns:
        List[str]: A list of strings (the notes)
    """

    try:
        return SAMPLE_NOTES[:n]
    except IndexError as e:
        raise IndexError("That many notes does not exist.")
    

def add_note(note: str):
    """Adds a note

    Args:
        note (str): A note
    """

    SAMPLE_NOTES.append(note)
