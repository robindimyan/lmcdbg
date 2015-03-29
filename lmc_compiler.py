class lmc_compiler:

    def __init__(self, fetcher_class):
        self.fetch = fetcher_class

    ops = {"add" : "1", "sub" : "2", "sto" : "3", "cob" : "444", "lda" : "5", "br" : "6", "brz" : "7", "brp" : "8", "in" : "901", "out" : "902"}
    inst = {"1" : "ADD ", "2" : "SUB ", "3" : "STO ", "444" : "COB", "5" : "LDA ", "6" : "BR ", "7" : "BRZ ", "8" : "BRP ", "901" : "IN", "902" : "OUT"}

    def lmc_compile(self, source, destination, newline):
	opcode = ""
        src = open(source, 'r')
        dst = open(destination, 'w+')
        sourceCode = src.read().split(newline)
        
	for line in sourceCode:
		ins = line.split(" ")
		if ins[0].lower() in self.ops.keys():
		    opcode += line.replace(ins[0], self.ops[ins[0].lower()])
		else:
		    print "[-] Instruction not found : '%s'" % (ins[0])
	opcode = opcode.replace(" ", "")
        dst.write(opcode)
        src.close()
        dst.close()

    def lmc_disass(self, source, destination, newline):
	sourceCode = ""
	src = open(source, 'r')
	dst = open(destination, 'w+')
	opcode = src.read()

	for i in range(0, len(opcode), 3):
	    ins = opcode[i]
	    addr = opcode[i+1:i+3]

	    if ins == "9" or ins == "4":
		sourceCode += self.inst[opcode[i:i+3]] + newline
	    else:
		if ins in self.inst.keys():
		    sourceCode += self.inst[ins] + addr + newline
		else:
		    print "[-] Invalid opcode: '%s'" % (ins)
	print "<Source code of %s>:" % (source)
	print sourceCode

	dst.write(sourceCode)
	src.close()
	dst.close()

    def lmc_execute(self, source):
        src = open(source, 'r')
        sourceCode = src.read()
        src.close()
        self.fetch.load_ins(sourceCode)
        self.fetch.exec_ins()
