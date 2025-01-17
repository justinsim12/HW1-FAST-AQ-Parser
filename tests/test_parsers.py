# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Read in fasta file
    fasta_file = 'data/test.fq' # if this was a fastq file, an AssertionError is raised
    parser_obj = FastaParser(fasta_file)
    file_lines = [record for record in parser_obj]

    assert file_lines[0][0] != None, "Ensure file is a FastA file."
    assert file_lines[0][1] != None, "Ensure file is a FastA file."

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
     # Read in fasta file
    fasta_file = 'data/test.fa' # if this was a fastq file, an AssertionError is raised
    parser_obj = FastaParser(fasta_file)
    file_lines = [record for record in parser_obj]

    assert file_lines[0][0] != None, "Ensure file is a FastA file."


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # Read in fastq file
    fastq_file = 'data/test.fq'
    parser_obj = FastqParser(fastq_file)
    file_lines = [record for record in parser_obj]

    # Known seq0 of fastq file
    seq0 = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    # Known quality of seq0
    qual0 = '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='

    # Check both sequence and quality
    check_val = False
    if ((file_lines[0][1] == seq0) and (file_lines[0][2] == qual0)):
        check_val = True
    
    assert check_val, "FastQ parser error"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Read in fastq file
    fastq_file = 'data/test.fq'
    parser_obj = FastqParser(fastq_file)
    file_lines = [record for record in parser_obj]

    # Known seq0 of fastq file
    seq0 = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    # Known quality of seq0
    qual0 = '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='

    # Check both sequence and quality
    check_val = False
    if ((file_lines[0][1] == seq0) and (file_lines[0][2] == qual0)):
        check_val = True

    assert check_val, "FastQ format error"
