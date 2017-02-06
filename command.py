#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft
import sys
import os
# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
# Get the arguments list 
cmdargs = str(sys.argv)
 
# Print it
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)


#os.system('ls')
os.system("sudo ssh -i '/home/toobler/sanoop/projects/lugza/doc/Lugza.pem' ubuntu@ec2-52-39-30-17.us-west-2.compute.amazonaws.com")
