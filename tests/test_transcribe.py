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
    # Known seq0 of fastq file
    seq0 = 'TGTGGTCGTAT'
    # 
    transcribed_seq0 = 'TGTGGTCGTAT'
    print(transcribe(seq0))

    # Check
    check_val = False
    if (transcribe(seq0) == transcribed_seq0):
        check_val = True
    
    assert check_val, "FastQ parser error"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    pass

test_transcribe()
