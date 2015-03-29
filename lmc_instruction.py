class lmc_instruction:

	def __init__(self):
		self.calc = 0
		self.counter = 0

		self.mailBox_in = [] #Mailbox to store instructions
		self.mailBox_dat = [] #Mailbox to store data


	def memset(self, size, memory):
		for i in range(size):
			memory.append(0)

	def error(self, msg):
		print "Error: " + msg
		exit()

	def count(self, value):
		self.counter = value

	def add(self, addr):
		if addr >= len(self.mailBox_dat):
			self.error("Address doesn't exist.")
		else:
			self.calc += self.mailBox_dat[addr]
			self.count(self.counter+1)

	def substract(self, addr):
		if addr >= len(self.mailBox_dat):
			self.error("Address doesn't exist.")
		else:
			self.calc -= self.mailBox_dat[addr]
			self.count(self.counter+1)

	def store(self, addr):
		if addr >= len(self.mailBox_dat):
			self.error("Address doesn't exist.")
		else:
			self.mailBox_dat[addr] = self.calc
			self.count(self.counter+1)

	def load(self, addr):
		if addr >= len(self.mailBox_dat):
			error("Address doesn't exist.")
		else:
			self.calc = self.mailBox_dat[addr]
			self.count(self.counter+1)

	def branch(self, addr):
		if addr >= len(self.mailBox_in):
			self.error("Address doesn't exist.")
		else:
			self.count(self.addr)

	def branchzero(self, addr):
		if addr >= len(self.mailBox_in):
			self.error("Address doesn't exist.")
		else:
			if self.calc == 0:
				self.count(addr)
			else:
				self.count(self.counter+1)

	def branchpositive(self, addr):
		if addr >= len(self.mailBox_in):
			self.error("Address doesn't exist.")
		else:
			if self.calc >= 0:
				self.count(addr)
			else:
				self.count(self.counter+1)

	def inp(self):
		user_inp = raw_input()
		self.calc = int(user_inp)
		self.count(self.counter+1)

	def out(self):
		print self.calc
		self.count(self.counter+1)

	def coffee(self):
		exit()
