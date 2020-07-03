# pylint: disable=import-error
# pylint: disable=invalid-name
# pylint: disable=mixed-indentation
# pylint: disable=too-many-locals
# pylint: disable=unused-wildcard-import
# pylint: disable=wrong-import-order

from common import *
from robot.api import logger
import smbus
import time

MCP23017_ADDR = 0x27
DELAY = 0.1  # 0.1 s delay


class mcp23017:
	"""
	16-bit I/O Expander with I2C interface.
	"""

	def __init__(self, addr=MCP23017_DEFAULT_ADDR):
		self.hardware_address = addr
		self.bus = smbus.SMBus(1)

		print('MCP23017 configured hardware address: 0x{:02x}'.format(self.hardware_address))

		self.dispatcher = {I2C_IODIRA: self._set_bit_for_iodira, \
		                   I2C_IODIRB: self._set_bit_for_iodirb, \
		                   I2C_GPIOA: self._set_bit_for_gpioa, \
		                   I2C_GPIOB: self._set_bit_for_gpiob}

		self.port_A_dir_vector = 0xff  # direction is default set to input according to data sheet
		self.port_B_dir_vector = 0xff  # -"-
		self.port_A_pin_vector = 0x00
		self.port_B_pin_vector = 0x00

	def configure(self, *params):
		self.dispatcher[params[0]](params)

	def _set_bit_for_iodira(self, param):
		#print('*** MCP i2c IODIRA {}'.format(param))
		gpio_pin = param[1]
		mode = param[2]

		if mode == IN:
			self.port_A_dir_vector |= (1 << gpio_pin)
		elif mode == OUT:
			self.port_A_dir_vector &= ~(1 << gpio_pin)
		else:
			# [FIXME] this should be a log warning
			print('Invalid configuration of port A')

		logger.info('(i2c) Direction PortA - Pin: {}, mode: {}, Dir Vector: 0x{:02x}'.
		      format(gpio_pin, mcp23017_get_mode_name(mode), self.port_A_dir_vector))

		self.bus.write_byte_data(self.hardware_address, I2C_IODIRA, self.port_A_dir_vector)

	def _set_bit_for_iodirb(self, param):
		#print('MCP i2c IODIRB')
		gpio_pin = param[1]
		mode = param[2]

		if mode == IN:
			self.port_B_dir_vector |= (1 << gpio_pin)
		elif mode == OUT:
			self.port_B_dir_vector &= ~(1 << gpio_pin)
		else:
			# [FIXME] this should be a log warning
			print('Invalid configuration of port B')

		logger.info('(i2c) Direction PortB - Pin: {}, mode: {}, Dir Vector: 0x{:02x}'.
		      format(gpio_pin, mcp23017_get_mode_name(mode), self.port_B_dir_vector))

		self.bus.write_byte_data(self.hardware_address, I2C_IODIRB, self.port_B_dir_vector)

	def _set_bit_for_gpioa(self, param):
		#print('MCP i2c GPIOA')
		gpio_pin = param[1]
		level = param[2]

		if self.port_A_dir_vector & (1 << gpio_pin):
			# [FIXME] this should be a log warning
			print('(i2c) PortA, pin: {} is configured as input'.format(gpio_pin))
		else:
			if level == HIGH:
				self.port_A_pin_vector |= (1 << gpio_pin)
			elif level == LOW:
				self.port_A_pin_vector &= ~(1 << gpio_pin)
			else:
				print('(i2c) Invalid config, Use either LOW or HIGH for pin: {} at Port A'.
				      format(gpio_pin))

		print('(i2c) Output PortA - Pin: {}, Level: {}, Pin Vector: 0x{:02x}'.
		      format(gpio_pin, level, self.port_A_pin_vector))

		self.bus.write_byte_data(self.hardware_address, I2C_GPIOA, self.port_A_pin_vector)

	def _set_bit_for_gpiob(self, param):
		#print('MCP i2c GPIOB')
		gpio_pin = param[1]
		level = param[2]

		if self.port_B_dir_vector & (1 << gpio_pin):
			# [FIXME] this should be a log warning
			print('(i2c) PortB, pin: {} is configured as input'.format(gpio_pin))
		else:
			if level == HIGH:
				self.port_B_pin_vector |= (1 << gpio_pin)
			elif level == LOW:
				self.port_B_pin_vector &= ~(1 << gpio_pin)
			else:
				print('(i2c) Invalid config, Use either LOW or HIGH for pin: {} at Port B'.
				      format(gpio_pin))

		print('(i2c) Output PortB - Pin: {}, mode: {}, Pin Vector: 0x{:02x}'
		      .format(gpio_pin, level, self.port_B_pin_vector))

		self.bus.write_byte_data(self.hardware_address, I2C_GPIOB, self.port_B_pin_vector)

	def read_port(self, reg):
		rv = self.bus.read_byte_data(self.hardware_address, reg)
		print('Read from MCP23017 - Reg: 0x{:02x}, Data: 0x{:02x}'.format(reg, rv))
		return rv


# --------------------------------------------------------------------------------
# Test purpose functions
# --------------------------------------------------------------------------------
def set_port_A_hi(obj):
	obj.configure(I2C_IODIRA, I2C_GPA0, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA1, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA2, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA3, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA4, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA5, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA6, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA7, OUT)

	for port in range(8):
		obj.configure(I2C_GPIOA, port, HIGH)
		time.sleep(DELAY)

def set_port_B_hi(obj):
	obj.configure(I2C_IODIRB, I2C_GPB0, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB1, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB2, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB3, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB4, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB5, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB6, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB7, OUT)

	for port in range(8):
		obj.configure(I2C_GPIOB, port, HIGH)
		time.sleep(DELAY)

def running_port_A(obj):
	obj.configure(I2C_IODIRA, I2C_GPA0, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA1, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA2, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA3, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA4, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA5, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA6, OUT)
	obj.configure(I2C_IODIRA, I2C_GPA7, OUT)

	for port in range(8):
		obj.configure(I2C_GPIOA, port, ON)
		time.sleep(DELAY)
		obj.configure(I2C_GPIOA, port, OFF)
		time.sleep(DELAY)

def running_port_B(obj):
	obj.configure(I2C_IODIRB, I2C_GPB0, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB1, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB2, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB3, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB4, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB5, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB6, OUT)
	obj.configure(I2C_IODIRB, I2C_GPB7, OUT)

	for port in range(8):
		obj.configure(I2C_GPIOB, port, ON)
		time.sleep(DELAY)
		obj.configure(I2C_GPIOB, port, OFF)
		time.sleep(DELAY)


def main():
	myMCP = mcp23017()

	set_port_A_hi(myMCP)
	print(60*'-')
	set_port_B_hi(myMCP)
	print(60*'-')

	running_port_A(myMCP)
	print(60*'-')
	running_port_B(myMCP)


if __name__ == '__main__':
	main()
