#!/usr/bin/python
from os import system, name, linesep
from sys import argv
from lmc_instruction import *
from lmc_fetcher import *
from lmc_compiler import *

system('cls' if name == 'nt' else 'clear')

i = lmc_instruction()
f = lmc_fetcher(i)
c = lmc_compiler(f)

print """
  _      __  __  _____   _____       _                                 
 | |    |  \/  |/ ____| |  __ \     | |                                
 | |    | \  / | |      | |  | | ___| |__  _   _  __ _  __ _  ___ _ __ 
 | |    | |\/| | |      | |  | |/ _ | '_ \| | | |/ _` |/ _` |/ _ | '__|
 | |____| |  | | |____  | |__| |  __| |_) | |_| | (_| | (_| |  __| |   
 |______|_|  |_|\_____| |_____/ \___|_.__/ \__,_|\__, |\__, |\___|_|   
                                                  __/ | __/ |          
                                                 |___/ |___/           

"""
SIZE = 200 # Default value for data segment of memory
args = {"-c" : "compile", "-d" : "disass"}

def compile(filename):
    c.lmc_compile(filename, "app.lmc", linesep)
    print "[+] Code at %s is compiled and saved to app.lmc" % (filename)
    
def disass(filename):
    c.lmc_disass(filename, "source.lmcs", linesep)
    print "[+] Code at %s is disassembled and saved to source.lmcs" % (filename)

if len(argv) > 1 and len(argv) < 5:

    if len(argv) == 2:
	print "[+] Code debugging started."
	i.memset(SIZE, i.mailBox_dat)
	c.lmc_execute(argv[1])
	exit()

    for arg in argv:
	if "-" not in arg:
	    filename = arg

    for arg in args:
	if arg in argv:
	    locals()[args[arg]](filename)


else:
    print "Usage: lmcdbg.py <filename> [options (-c, -d)]"
    exit()
