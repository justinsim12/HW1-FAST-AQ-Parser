# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    return seq.upper().replace('T','U')


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # I AM ASSUMING YOU WOULD LIKE THIS FUNCTION TO RETURN THE _REVERSE COMPLEMENT_ STRAND, NOT THE REVERSE TRANSCRIBED (RNA->DNA)
    # D:
    # Used chat
    new_seq = ''.join(TRANSCRIPTION_MAPPING[nucleotide] for nucleotide in seq.upper())

    return new_seq[::-1]