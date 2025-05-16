"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time

from happy import Happy
from sad import Sad
#from smiley import Smiley
from angry import Angry

def main():
   
    #Happy blinking smiley 
    smiley = Happy()
    smiley.show()
    time.sleep(1)
    smiley.blink()
    
    #Sad blinking smiley
    smiley = Sad()
    smiley.show()
    time.sleep(1)
    smiley.blink()
    
    #Angry smiley
    angry = Angry()
    angry.show()
    
    
    # smiley = Smiley()
    # smiley.show()
    
    # Default yellow smiley
    # smiley1 = Smiley()
    # smiley1.show()
    # time.sleep(2)

    # # Green smiley
    # smiley2 = Smiley(complexion=Smiley.GREEN)
    # smiley2.show()

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

