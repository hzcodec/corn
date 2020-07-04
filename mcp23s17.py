# pylint: disable= line-too-long
# pylint: disable= unused-variable
# pylint: disable= wrong-import-order
from common import *
from robot.api import logger
import spidev
import time

READ_OP_CODE = 0x41
WRITE_OP_CODE = 0x40
SHIFT_CTRL_BIT = 2
DUMMY = 0  # just to fit the parameters at function call
SECOND_BYTE = 2  # valid byte in list at read operation

# parameter index
DEVICE_IDX = 0
ADDR_IDX = 1
REG_IDX = 2
GPIO_PIN_IDX = 3
MODE_IDX = 4
LEVEL_IDX = 4


class mcp23s17():
	def __init__(self):
		"""
		create four instances since there are two sets of devices.
		Each set contains two devices of MCP23S17 with its corresponding address,
		ADDR=0 and ADDR=1.
		"""
		self.mcp_inst_0_addr_0 = mcp23s17_internal('Inst 0, Addr 0', 0)
		self.mcp_inst_0_addr_1 = mcp23s17_internal('Inst 0, Addr 1', 1)
		self.mcp_inst_1_addr_0 = mcp23s17_internal('Inst 1, Addr 0', 0)

		# Only used if an instance of the chip is mounted. See also comment below.
		#self.mcp_inst_1_addr_1 = mcp23s17_internal('Inst1, Addr 1', 1)

	def configure(self, *params):

		device = params[DEVICE_IDX]
		addr = params[ADDR_IDX]

		if device == MCP23S17_DEVICE_0:
			#logger.info('Configure Device: {}, Addr: {}'.format(device, addr))

			if addr == MCP23S17_ADDR_0:
				self.mcp_inst_0_addr_0.configure_mcp(params)
			else:
				self.mcp_inst_0_addr_1.configure_mcp(params)

		elif device == MCP23S17_DEVICE_1:
			#logger.info('Configure Device: {}, Addr: {}'.format(device, addr))

			if addr == MCP23S17_ADDR_0:
				self.mcp_inst_1_addr_0.configure_mcp(params)
			else:
				# Only used if an instance of the chip is mounted
				#self.mcp_inst_1_addr_1.configure_mcp(params)
				logger.warn('Chip does not exists!')

	def get_vector(self):
		"""
		Used for test purpose. To get track of internal vectors.
		"""
		rv1, rv2 = self.mcp_inst_0_addr_0.get_dir_vectors()
		rv3, rv4 = self.mcp_inst_0_addr_0.get_pin_vectors()
		print('MCP0, Addr 0, Direction vector A: 0x{:02x}'.format(rv1))
		print('MCP0, Addr 0, Pin vector A: 0x{:02x}'.format(rv3))
		print('MCP0, Addr 0, Direction vector B: 0x{:02x}'.format(rv2))
		print('MCP0, Addr 0, Pin vector B: 0x{:02x}'.format(rv4))


		rv1, rv2 = self.mcp_inst_0_addr_1.get_dir_vectors()
		rv3, rv4 = self.mcp_inst_0_addr_1.get_pin_vectors()
		print('MCP0, Addr 1, Direction vector A: 0x{:02x}'.format(rv1))
		print('MCP0, Addr 1, Pin vector A: 0x{:02x}'.format(rv3))
		print('MCP0, Addr 1, Direction vector B: 0x{:02x}'.format(rv2))
		print('MCP0, Addr 1, Pin vector B: 0x{:02x}'.format(rv4))

		print('----------------')
		rv1, rv2 = self.mcp_inst_1_addr_0.get_dir_vectors()
		rv3, rv4 = self.mcp_inst_1_addr_0.get_pin_vectors()
		print('MCP1, Addr 0, Direction vector A: 0x{:02x}'.format(rv1))
		print('MCP1, Addr 0, Pin vector A: 0x{:02x}'.format(rv3))
		print('MCP1, Addr 0, Direction vector B: 0x{:02x}'.format(rv2))
		print('MCP1, Addr 0, Pin vector B: 0x{:02x}'.format(rv4))


class mcp23s17_internal:
	def __init__(self, par, addr):
		self.spi = spidev.SpiDev()
		# [FIXME ] removed just for test purpose - self.spi.open(SPI_MCP23S17_PORT, SPI_MCP23S17_DEVICE)
		self.spi.open(1, 0)

		self.spi.max_speed_hz = SPI_SPEED

		self.dispatcher = {SPI_IODIRA: self._set_bit_for_iodira,
		                   SPI_IODIRB: self._set_bit_for_iodirb,
		                   SPI_GPIOA: self._set_bit_for_gpioa,
		                   SPI_GPIOB: self._set_bit_for_gpiob}

		self.port_A_dir_vector = 0xff  # direction is default set to input according to data sheet (1 = IN, 0 = OUT)
		self.port_B_dir_vector = 0xff  # -"-
		self.port_A_pin_vector = 0x00
		self.port_B_pin_vector = 0x00

		# Enable HAEN, i.e hardware address (A2, A1, A0) is used
		control_byte = WRITE_OP_CODE | addr
		print('Enable HAEN for "{}", control_byte: 0x{:01x}'.format(par, control_byte))
		self.spi.writebytes([control_byte, SPI_IOCON, 0x08])
		time.sleep(0.1)

	def configure_mcp(self, params):
		logger.info('Internal mcp config: {}'.format(params))
		#self.dispatcher[params[REG_IDX]](params)

	def _get_instance_prop(self, device, mode=IN, level=LOW):
		if device == MCP23S17_DEVICE_0:
			rv1 = 'MCP23S17_DEVICE_0'
		elif device == MCP23S17_DEVICE_1:
			rv1 = 'MCP23S17_DEVICE_1'
		else:
			rv1 = 'None'

		if mode == IN:
			rv2 = 'IN'
		elif mode == OUT:
			rv2 = 'OUT'
		else:
			rv2 = 'None'

		if level == LOW:
			rv3 = 'LOW'
		elif level == HIGH:
			rv3 = 'HIGH'
		else:
			rv3 = 'None'

		return rv1, rv2, rv3

	def _set_bit_for_iodira(self, param):
		device = param[DEVICE_IDX]
		addr = param[ADDR_IDX]
		gpio_pin = param[GPIO_PIN_IDX]
		mode = param[MODE_IDX]

		# SPI control byte format
		# bit no:  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
		# value:   | 0 | 1 | 0 | 0 | a | b | c | 0 |
		#                          |<--------->|
		#                              addr
		#                                        WR

		# Device is either 0x011 or 0x100. so bit 2 is used to set up the slave addres
		control_byte = WRITE_OP_CODE | (addr >> SHIFT_CTRL_BIT)
		#print('control_byte for IODIRA: 0x{:02x}'.format(control_byte))

		if mode == IN:
			self.port_A_dir_vector |= (1 << gpio_pin)
		elif mode == OUT:
			self.port_A_dir_vector &= ~(1 << gpio_pin)
		else:
			logger.warn('Invalid config of IODIRA')

		rv1, rv2, rv3 = self._get_instance_prop(device, mode, DUMMY)
		print('(spi) Device: {},  Addr {} - Pin: {}, mode: {}, Dir Vector A: 0x{:02x}'
		      .format(rv1, addr, gpio_pin, rv2, self.port_A_dir_vector))

		self.spi.writebytes([control_byte, SPI_IODIRA, self.port_A_dir_vector])

	def _set_bit_for_iodirb(self, param):
		device = param[DEVICE_IDX]
		addr = param[ADDR_IDX]
		gpio_pin = param[GPIO_PIN_IDX]
		mode = param[MODE_IDX]

		# SPI control byte format
		# bit no:  | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
		# value:   | 0 | 1 | 0 | 0 | a | b | c | 0 |
		#                          |<--------->|
		#                              addr
		#                                        WR

		# Device is either 0x011 or 0x100. so bit 2 is used to set up the slave addres
		control_byte = WRITE_OP_CODE | (addr << SHIFT_CTRL_BIT)
		#print('control_byte for IODIRB: 0x{:02x}'.format(control_byte))

		if mode == IN:
			self.port_B_dir_vector |= (1 << gpio_pin)
		elif mode == OUT:
			self.port_B_dir_vector &= ~(1 << gpio_pin)
		else:
			logger.warn('Invalid config of IODIRB')

		rv1, rv2, rv3 = self._get_instance_prop(device, mode, DUMMY)
		print('(spi) Device: {},  Addr {} - Pin: {}, mode: {}, Dir Vector B: 0x{:02x}'
		            .format(rv1, addr, gpio_pin, rv2, self.port_B_dir_vector))

		self.spi.writebytes([control_byte, SPI_IODIRB, self.port_B_dir_vector])

	def _set_bit_for_gpioa(self, param):
		print('Param: ', param)
		#device = param[DEVICE_IDX]
		#addr = param[ADDR_IDX]
		#gpio_pin = param[GPIO_PIN_IDX]
		#level = param[LEVEL_IDX]

		#control_byte = WRITE_OP_CODE | (addr >> SHIFT_CTRL_BIT)

		#if self.port_A_dir_vector & (1 << gpio_pin):
		#	logger.warn('PortA {} is configured as input'.format(gpio_pin))
		#else:
		#	if level == HIGH:
		#		self.port_A_pin_vector |= (1 << gpio_pin)
		#	elif level == LOW:
		#		self.port_A_pin_vector &= ~(1 << gpio_pin)
		#	else:
		#		logger.warn('(spi) Invalid config, Use either LOW or HIGH for pin: {} at Port A'.format(gpio_pin))

		#rv1, rv2, rv3 = self._get_instance_prop(device, DUMMY, level)
		#print('(spi) Device: {},  Addr {} - Pin: {}, Level: {}, Pin Vector A: 0x{:02x}'
		#            .format(rv1, addr, gpio_pin, rv3, self.port_A_pin_vector))

		#self.spi.writebytes([control_byte, SPI_GPIOA, self.port_A_pin_vector])

	def _set_bit_for_gpiob(self, param):
		device = param[DEVICE_IDX]
		addr = param[ADDR_IDX]
		gpio_pin = param[GPIO_PIN_IDX]
		level = param[LEVEL_IDX]

		control_byte = WRITE_OP_CODE | (addr >> SHIFT_CTRL_BIT)
		#print('control_byte for GPIOB: 0x{:02x}'.format(control_byte))

		if self.port_B_dir_vector & (1 << gpio_pin):
			# [FIXME] this should be a log warning
			print('(spi) PortB {} is configured as input'.format(gpio_pin))
		else:
			if level == HIGH:
				self.port_B_pin_vector |= (1 << gpio_pin)
			elif level == LOW:
				self.port_B_pin_vector &= ~(1 << gpio_pin)
			else:
				print('(spi) Invalid config, Use either LOW or HIGH for pin: {} at Port B'.format(gpio_pin))

		rv1, rv2, rv3 = self._get_instance_prop(device, DUMMY, level)
		print('(spi) Device: {},  Addr {} - Pin: {}, Level: {}, Pin Vector B: 0x{:02x}'
		            .format(rv1, addr, gpio_pin, rv3, self.port_B_pin_vector))

		self.spi.writebytes([control_byte, SPI_GPIOB, self.port_B_pin_vector])

	def read_spi_gpiob(self, gpio_pin):
		"""
		All ports on GPIO B are set to pullup.
		"""
		self.spi.writebytes([WRITE_OP_CODE, SPI_GPPUB, 0xff])  # pullup

		rv = self.spi.xfer2([READ_OP_CODE, SPI_GPIOB, DUMMY_BYTE])
		logger.info('Read SPI port B[{}] - op: 0x{:02x}, reg: 0x{:02x} rv: 0x{:02x}'
		            .format(gpio_pin, READ_OP_CODE, SPI_GPIOB, rv[SECOND_BYTE]))

		bit = rv[2] & (1 << int(gpio_pin))
		logger.info('bit = {} for port: {}'.format(bit, gpio_pin))

	def get_dir_vectors(self):
		return self.port_A_dir_vector, self.port_B_dir_vector

	def get_pin_vectors(self):
		return self.port_A_pin_vector, self.port_B_pin_vector


# ------------------------------------------------------------------------------------------------------
# Test functions
# ------------------------------------------------------------------------------------------------------
def inst_0_addr_0_port_A_test(obj):
	"""
	Set Port A to output and set all ports to HIGH wait 2 sec and set all ports to LOW
	"""
	print('Configure Port A output')
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_0, SPI_IODIRA, port, OUT)

	print('*** Set Port A high')
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_0, SPI_GPIOA, port, HIGH)
	time.sleep(2)

	print('*** Set Port A low')
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_0, SPI_GPIOA, port, LOW)
	time.sleep(2)

def inst_0_addr_0_port_B_test(obj):
	"""
	Set Port B to output and set all ports to HIGH
	"""
	print('Configure Port B output')
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_0, SPI_IODIRB, port, OUT)

	print('*** Set Port B high')
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_0, SPI_GPIOB, port, HIGH)
	time.sleep(2)

	print('*** Set Port B low')
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_0, SPI_GPIOB, port, LOW)
	time.sleep(2)

def inst_0_addr_1_port_A_test(obj):
	"""
	Set Port A to output and set all ports to HIGH
	"""
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_1, SPI_IODIRA, port, OUT)

	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_1, SPI_GPIOA, port, HIGH)

def inst_0_addr_1_port_B_test(obj):
	"""
	Set Port B to output and set all ports to HIGH
	"""
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_1, SPI_IODIRB, port, OUT)

	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_0, MCP23S17_ADDR_1, SPI_GPIOB, port, HIGH)


def inst_1_addr_0_port_A_test(obj):
	"""
	Set Port A to output and set all ports to HIGH
	"""
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_0, SPI_IODIRA, port, OUT)

	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_0, SPI_GPIOA, port, HIGH)

def inst_1_addr_0_port_B_test(obj):
	"""
	Set Port B to output and set all ports to HIGH
	"""
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_0, SPI_IODIRB, port, OUT)

	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_0, SPI_GPIOB, port, HIGH)

def inst_1_addr_1_port_A_test(obj):
	"""
	Set Port A to output and set all ports to HIGH
	"""
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_1, SPI_IODIRA, port, OUT)

	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_1, SPI_GPIOA, port, HIGH)

def inst_1_addr_1_port_B_test(obj):
	"""
	Set Port B to output and set all ports to HIGH
	"""
	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_1, SPI_IODIRB, port, OUT)

	for port in range(0, 8):
		obj.configure(MCP23S17_DEVICE_1, MCP23S17_ADDR_1, SPI_GPIOB, port, HIGH)


def main():
	myMCP = mcp23s17()

	inst_0_addr_0_port_A_test(myMCP)
	print(' ')

	#inst_0_addr_0_port_B_test(myMCP)
	#print(' ')

	#inst_0_addr_1_port_A_test(myMCP)
	#print(' ')

	#inst_0_addr_1_port_B_test(myMCP)
	#print('-------')

	#inst_1_addr_0_port_A_test(myMCP)
	#print(' ')

	#inst_1_addr_0_port_B_test(myMCP)
	#print(' ')

	#inst_1_addr_1_port_A_test(myMCP)
	#print(' ')

	#inst_1_addr_1_port_B_test(myMCP)
	#print(' ')

	print(30*'-')
	print('Internal vectors:')
	# [FIXME] removed during test - myMCP.get_vector()
	print(30*'-')

if __name__ == '__main__':
	main()
