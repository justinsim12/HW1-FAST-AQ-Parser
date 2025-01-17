# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    seq0 = 'ATCG'
    transcribed_seq0 = 'AUCG'

    assert transcribe(seq0) == transcribed_seq0

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    seq0 = 'ATCG'
    transcribed_seq0 = 'CGAU'

    assert reverse_transcribe(seq0) == transcribed_seq0


