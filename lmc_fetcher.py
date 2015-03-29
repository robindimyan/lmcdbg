class lmc_fetcher:

    def __init__(self, instruction_class):
        self.ins = instruction_class

    def load_ins(self, opcode):
        if len(opcode) % 3 != 0:
            self.ins.error('Invalid opcode.')
        else:
            for i in range(0, len(opcode), 3):
                self.ins.mailBox_in.append(opcode[i:i + 3])

    # ops = {"1" : "", "2" : "", "3" : "", "5" : "", "6" : "", "7" : "", "8" : "", "901" : "", "902" : ""}

    def exec_ins(self):
        trio = self.ins.mailBox_in[self.ins.counter]
        while trio[0] != '4':
            op = trio[0]
            addr = int(trio[1:3])
            if op == '1':
                self.ins.add(addr)
                trio = self.ins.mailBox_in[self.ins.counter]
            elif op == '2':
                self.ins.substract(addr)
                trio = self.ins.mailBox_in[self.ins.counter]
            elif op == '3':
                self.ins.store(addr)
                trio = self.ins.mailBox_in[self.ins.counter]
            elif op == '5':
                self.ins.load(addr)
                trio = self.ins.mailBox_in[self.ins.counter]
            elif op == '6':
                self.ins.branch(addr)
                trio = self.ins.mailBox_in[self.ins.counter]
            elif op == '7':
                self.ins.branchzero(addr)
                trio = self.ins.mailBox_in[self.ins.counter]
            elif op == '8':
                self.ins.branchpositive(addr)
                trio = self.ins.mailBox_in[self.ins.counter]
            elif op == '9':
                if addr == 1:
                    self.ins.inp()
                    trio = self.ins.mailBox_in[self.ins.counter]
                elif addr == 2:
                    self.ins.out()
                    trio = self.ins.mailBox_in[self.ins.counter]
                else:
                    self.ins.error('Invalid I/O option.')
            else:
                self.ins.error('Invalid operation.')

        self.ins.coffee()
