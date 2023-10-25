#!/usr/bin/env python3
#hamming.py
import sys

def hamming(seq_1,seq_2):
    """ This function returns hamming distance between two
    strings(DNA sequences) using list loops and zip """
    start= 0
    for character_1,character_2 in zip(seq_1,seq_2):
        if character_1 != character_2:
           start +=1
    return start

if __name__ =="__main__":
    arg_count=len(sys.argv) -1
    if arg_count < 2 :
        raise Exception("This script requires two arguments (sequences) of equal length")

    a= sys.argv[1]
    b= sys.argv[2]
    if len(a) != len(b):
        raise ValueError("Make sure the sequences inputted are of same length")
    result =hamming(a,b)
    print('{}\t{}\t{}'.format(a,b,result))
