class SpiDev():

	def __init__(self):
		self.max_speed_hz = 0

	def open(self, a, b):
		print('Open spidev')

	def writebytes(self, a):
		None

	def readbytes(self, a, b, c):
		print('read')
