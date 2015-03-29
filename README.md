# lmcdbg
An Assembler/Disassembler for Little Man Computer.

This debugger is made to assemble and execute programs made with 'Little Man Computer' model.
Basic instruction set as the following:

 1xx - ADD   
 2xx - SUB      
 3xx - STO (Store)    
 444 - COB (Coffee break, a.k.a terminate) 
 5xx - LDA (Load)           
 6xx - BR (Branch)          
 7xx - BRZ (Branch if zero)     
 8xx - BRP (Branch if positive)  
 901 - IN (Input)             
 902 - OUT (Output)                         

You can find the source code of a simple program which is a basic implementation of a for loop.

Usage of the program:

"lmcdbg.py <filename> [options (-c, -s)]"


More information about LMC:
http://en.wikipedia.org/wiki/Little_man_computer
