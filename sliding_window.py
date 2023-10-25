#!/usr/bin/env python3
# sliding_window.py


import sys


def sliding_window(k, dna):
    """ This function will take two arguments, size of the k-mer &
    the string of the DNA, and will return all the possible k-mers
    of size specified. """
    kmers = []
    end = len(dna) - int(k) + 1
    for start in range(0, end):
        kmers.append(dna[start:start + int(k)])

    return kmers
  
def gc_content(dna):
    """ This function will take 1 argumen, a string of DNA, will 
    convert it into lower case and will calculate the GC content
    in it. """
    dna=dna.lower()
    gc = 0
    for nucleotide in dna:
        if nucleotide in ['g' , 'c']:
            gc += 1
    return float(gc/len(dna))

if __name__ == "__main__":
  # To check if number of arguments are less than 2, if less, raise exception and notify the user the input 2 arguments. 
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
       raise Exception("This script requires 2 arguments: a kmer size and then a string")

    k = int(sys.argv[1])
    dna = sys.argv[2]
    kmers = sliding_window(k,dna)
    kmer_gc={}
   # Calculate the GC content
    #result = gc_content(dna)
    for i in kmers:
        kmer_gc[i] = gc_content(i)

    for key,value in kmer_gc.items():
        # Print the result, rounding GC content to 2 decimal places
       # print(key + '\t' +str(round(value,2)))#".format(kmers[i],gc_content(kmers[i])))
       print("{0}\t{1:.2f}".format(key,value))
       #print ("This site is {0:f}% securely {1}!!". 
                                  # format(100, "encrypted"))

    for i in range(len(kmer_gc)):
        print("{}\t{:.2f}".format(i,gc_content()))
