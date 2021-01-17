# @name:    DorkScanner
# @repo:    https://github.com/adimas999/G-Dork
# @author:  MrDevils


import argparse
from os import system, name 
import os 
import sys
def clear(): 
    return os.system('cls' if os.name == 'nt' else 'clear')

print ("")
A = """             
    
       ______      ____             __  
      / ____/     / __ \____  _____/ /__
     / / ________/ / / / __ \/ ___/ //_/
    / /_/ /_____/ /_/ / /_/ / /  / ,<   
    \____/     /_____/\____/_/  /_/|_|  
                                    

    Dork Scanner coded by Mr-Devils
    please use -h to see help
    """
print ("")
print(A)

parser = argparse.ArgumentParser("dork.py",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-g","--google", help="google mode", action='store_true' )
parser.add_argument("-s","--scada", help="scada mode ", action='store_true' )
parser.add_argument("-t","--tor", help="Tor mode ", action='store_true' )
parser.add_argument("-p","--proxy", help="Proxy mode ", action='store_true' )


args = parser.parse_args()

if args.google :
 clear() 
 from Modes import Gmode
 
if args.scada :
 clear ()
 from Modes import Scada
 
if args.tor :
 clear ()
 from Modes import Tor
  
if args.proxy :
 clear ()
 from Modes import Proxy

