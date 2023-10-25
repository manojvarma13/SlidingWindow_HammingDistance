#!/usr/bin/env python3
#hello_you.py

import sys
def hello_name(name="you"):
    print("Hello, {}!".format(name))
    """ This function will return the salutation "Hello",
    followed by the name thats inputted, or will just 
    return "Hello, you!" in case no name is inputted. 
    sys module is imported to run this program just using
    arguments, this function to run correctly, needs, only
    one argument, if not given 1 argument (i.e; name),
    returns, "Hello, you!" """
if __name__=='__main__':
    arg_count = len(sys.argv) -1
    if arg_count > 0:
        hello_name(sys.argv[1])
    else:
        hello_name()
