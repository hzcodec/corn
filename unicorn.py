# pylint: disable=pointless-statement
# pylint: disable=protected-access

#import logging
import time

from robot.api import logger

import ad4112
import dac61408
import mcp23017
import mcp23s17

from common import *

# library used during development
from config import MCP1, MCP2, AD1

DELAY = 0.5  # 0.5 s delay
DELAY1 = 0.1
DELAY2 = 0.2
DELAY3 = 1

OFFSET_OF_BIT = 8
DELIMITER = 60
SPACE = 20

class unicorn:
	ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

	def __init__(self):
		self.io_expander_1_i2c = mcp23017.mcp23017(MCP23017_ADDR_0)
		self.io_expander_2_i2c = mcp23017.mcp23017(MCP23017_ADDR_1)
		self.io_expander_spi = mcp23s17.mcp23s17()
		self.dac = dac61408.dac61408()
		self.adc1 = ad4112.ad4112()  # cs 1
		self.adc2 = ad4112.ad4112()  # cs 2

	# ------------------------------------------------------------
	# MCP23017
	# ------------------------------------------------------------
	def init_io_expander_i2c(self):
		"""
		Port GPA0 - GPA5 are outputs
		Port GPA6 - GPA7 are inputs

		Port GPB0 - GPB2 are inputs
		Port GPB3 - GPB7 are outputs
		"""
		logger.info(DELIMITER*'-')
		logger.info('Initialize 16-bit I/O Expander, I2C - MCP23017, addr=0')

		logger.info(SPACE*' '+'--- Port A ---')
		for port in range(I2C_GPA0, I2C_GPA5+1):
			self.io_expander_1_i2c.configure(I2C_IODIRA, port, OUT)

		logger.info(SPACE*' '+'--- Port B ---')
		for port in range(I2C_GPB3, I2C_GPB7+1):
			self.io_expander_1_i2c.configure(I2C_IODIRB, port, OUT)

		""" 
		Port GPA0 - GPA7 are outputs
		Port GPB0 - GPB7 are outputs
		"""
		logger.info(DELIMITER*'-')
		logger.info('Initialize 16-bit I/O Expander, I2C - MCP23017, addr=1')
		logger.info(SPACE*' '+'--- Port A ---')
		self._config_io_port_A()
		logger.info(SPACE*' '+'--- Port B ---')
		self._config_io_port_B()

	def power_control(self, relay, mode):
		if int(mode) == ON:
			self.io_expander_1_i2c.configure(I2C_GPIOA, int(relay), HIGH)
		else:
			self.io_expander_1_i2c.configure(I2C_GPIOA, int(relay), LOW)

		logger.info('Power control: Power: {}, mode: {}'.
		             format(mcp23017_get_power_name(int(relay)), mcp23017_get_level_name(int(mode))))

		time.sleep(DELAY)

	def relay_control(self, relay, mode):
		"""
		Control the relays connected to MCP23017, addr=1
		"""
		logger.info('Relay: {} Level: {}'.format(int(relay)+1, mcp23017_get_level_name(int(mode))))

		if int(relay) < 8:
			if int(mode) == ON:
				self.io_expander_2_i2c.configure(I2C_GPIOA, int(relay), HIGH)
			else:
				self.io_expander_2_i2c.configure(I2C_GPIOA, int(relay), LOW)

		elif int(relay) < 17:
			if int(mode) == ON:
				self.io_expander_2_i2c.configure(I2C_GPIOB, int(relay)-OFFSET_OF_BIT, HIGH)
			else:
				self.io_expander_2_i2c.configure(I2C_GPIOB, int(relay)-OFFSET_OF_BIT, LOW)

		else:
			print('Invalid Relay')

		time.sleep(DELAY1)

	def _spi1_ce2(self, device, en):
		logger.info('SPI1_CE2_{} enable: {}'.format(device, en))

		bit0 = device & (1 << 0)
		bit1 = (device & (1 << 1)) >> 1
		bit2 = (device & (1 << 2)) >> 2

		if en == 1:
			logger.info('Enable device: {}'.format(mcp23017_get_device_name(device)))
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPB5, bit0)
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPB6, bit1)
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPB7, bit2)
		else:
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPB5, LOW)
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPB6, LOW)
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPB7, LOW)

	# ........................................................................
	# Handling of addr=0x21
	def _config_io_port_A(self):
		for port in range(I2C_GPA0, I2C_GPA7+1):
			self.io_expander_2_i2c.configure(I2C_IODIRA, port, OUT)

	def _config_io_port_B(self):
		for port in range(I2C_GPB0, I2C_GPB7+1):
			self.io_expander_2_i2c.configure(I2C_IODIRB, port, OUT)

	def set_io_port_A(self):
		self.io_expander_2_i2c.configure(I2C_GPIOA, I2C_GPA0, HIGH)

	def set_safe(self, mode):
		if int(mode) == ON:
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPA3, HIGH)
			logger.info('Lock lid')
		else:
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPA3, LOW)
			logger.info('Unlock lid')

	def set_reset(self, mode):
		if int(mode) == ON:
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPA4, HIGH)
			logger.info('Set Reset')
		else:
			self.io_expander_1_i2c.configure(I2C_GPIOB, I2C_GPA4, LOW)
			logger.info('Release Reset')
	# ........................................................................

	# ------------------------------------------------------------
	# MCP23S17
	# ------------------------------------------------------------
	def init_io_expander_spi(self):
		logger.info('Initialize 16-bit I/O Expander, SPI - MCP23S17')

	def config_mcp(self, item):
		#logger.info('Config mcp: {}'.format(item))

		device = int(item["Device"])
		address = int(item["SPI-addr"])
		reg = int(item["Reg"], 16)
		port = int(item["Port"])
		mode = int(item["Mode"])

		if reg == SPI_IODIRA:
			port_name = 'GPA'
			rv = mcp23017_get_mode_name(mode)
		elif reg == SPI_IODIRB:
			port_name = 'GPB'
			rv = mcp23017_get_mode_name(mode)
		elif reg == SPI_GPIOA:
			port_name = 'GPIOA'
			rv = mcp23017_get_level_name(mode)
		elif reg == SPI_GPIOB:
			port_name = 'GPIOB'
			rv = mcp23017_get_level_name(mode)

		dev_name = mcp23s17_get_device_name(device)

		logger.info('Device: {}, Addr: {}, Port: {}{}, Mode: {}'.format(dev_name, address, port_name, port, rv))

		self._spi1_ce2(device, 1)
		self.io_expander_spi.configure(device, address, reg, port, mode)
		#time.sleep(DELAY)
		self._spi1_ce2(device, 0)

	# [FIXME] this function need to be tested
	#def read_spi_portb(self, gpio_port):
		#self._spi1_ce2(1)
		#self.io_expander_spi.read_spi_gpiob(gpio_port)
		#self._spi1_ce2(0)

	# ------------------------------------------------------------
	# AD4112
	# ------------------------------------------------------------
	def init_adc(self):
		logger.info('Initialize 8 channel ADC, SPI - AD4112')

	def config_ad(self, item):
		logger.info('Item: {}'.format(item))

		device = int(item["Device"])
		address = int(item["SPI-addr"])
		print('Device: {}'.format(device))
		print('address: {}'.format(address))

	def get_adc_value(self, channel):
		self.adc1.device_reset()

		self.adc1.update_gain(GAIN0, [0xd5, 0x97, 0xda])

		vec = REF_BUFP | REF_BUFM | INBUF_EN
		self.adc1.config_setup(vec)

		if channel == CH0:
			vec = SETUP_SEL_0 | INPUT_VIN1
			self.adc1.config_channel_reg(CH1, vec)
			vec = CH_EN | SETUP_SEL_0 | INPUT_VIN0
			self.adc1.config_channel_reg(channel, vec)

		elif channel == CH1:
			# [FIXME] does not affect
			#self.adc1.update_gain(GAIN1, [0xd5, 0x97, 0xda])

			vec = SETUP_SEL_0 | INPUT_VIN0
			self.adc1.config_channel_reg(channel, vec)
			vec = CH_EN | SETUP_SEL_0 | INPUT_VIN1
			self.adc1.config_channel_reg(CH1, vec)


		vec = REF_EN | SING_SYNC | SING_CONV
		self.adc1.config_adc_mode(vec)
		vec = DATA_STAT
		self.adc1.config_interface_mode(vec)

		rv = self.adc1.get_data(MEAS_VOLT)
		return rv

	# ------------------------------------------------------------
	# DAC61416, 16 ch, 12 bit DAC
	# ------------------------------------------------------------
	def init_dac(self):
		logger.info('Initialize DAC, SPI - DAC61416')

	def config_dac(self, item):
		logger.info('Item: {}'.format(item))

		device = int(item["Device"])
		address = int(item["SPI-addr"])
		domain_range = int(item["Domain_Range"], 16)
		dac_range = int(item["Range"], 16)
		dac = int(item["Dac"], 16)

		self.dac.configure(domain_range, dac, dac_range)

# --------------------------------------------------------------------------------
# Test functions used during development
# --------------------------------------------------------------------------------
def power_control_test(obj):
	print('power_control_test')
	obj.power_control(DC_300V, ON)
	obj.power_control(AC_230V, ON)
	obj.power_control(PROTECTED_EARTH, ON)
	obj.power_control(p_24V, ON)
	obj.power_control(p_5V, ON)

	obj.power_control(DC_300V, OFF)
	obj.power_control(AC_230V, OFF)
	obj.power_control(PROTECTED_EARTH, OFF)
	obj.power_control(p_24V, OFF)
	obj.power_control(p_5V, OFF)

def relay_control_test(obj):
	print('relay_control_test')
	obj._config_io_port_A()
	obj._config_io_port_B()
	obj.relay_control(RELAY1, ON)
	obj.relay_control(RELAY2, ON)
	obj.relay_control(RELAY3, ON)
	obj.relay_control(RELAY4, ON)
	obj.relay_control(RELAY5, ON)
	obj.relay_control(RELAY6, ON)
	obj.relay_control(RELAY7, ON)
	obj.relay_control(RELAY8, ON)
	print(60*'-')
	obj.relay_control(RELAY9, ON)
	obj.relay_control(RELAY10, ON)
	obj.relay_control(RELAY11, ON)
	obj.relay_control(RELAY12, ON)
	obj.relay_control(RELAY13, ON)
	obj.relay_control(RELAY14, ON)
	obj.relay_control(RELAY15, ON)
	obj.relay_control(RELAY16, ON)
	print(60*'-')
	obj.relay_control(RELAY1, OFF)
	obj.relay_control(RELAY2, OFF)
	obj.relay_control(RELAY3, OFF)
	obj.relay_control(RELAY4, OFF)
	obj.relay_control(RELAY5, OFF)
	obj.relay_control(RELAY6, OFF)
	obj.relay_control(RELAY7, OFF)
	obj.relay_control(RELAY8, OFF)
	print(60*'-')
	obj.relay_control(RELAY9, OFF)
	obj.relay_control(RELAY10, OFF)
	obj.relay_control(RELAY11, OFF)
	obj.relay_control(RELAY12, OFF)
	obj.relay_control(RELAY13, OFF)
	obj.relay_control(RELAY14, OFF)
	obj.relay_control(RELAY15, OFF)
	obj.relay_control(RELAY16, OFF)

def ce_test(obj):
	#obj._spi1_ce2(DAC61408_DEVICE, 1)

	obj._spi1_ce2(AD4112_DEVICE_0, 1)
	obj._spi1_ce2(AD4112_DEVICE_0, 0)

	#obj._spi1_ce2(AD4112_DEVICE_1, 1)
	#obj._spi1_ce2(MCP23S17_DEVICE_0, 1)

	obj._spi1_ce2(MCP23S17_DEVICE_1, 1)
	obj._spi1_ce2(MCP23S17_DEVICE_1, 0)

def spi_mcp_test(obj):
	obj.config_mcp(MCP1)
	obj.config_mcp(MCP2)

def main():
	myUnicorn = unicorn()

	# ---------------------------------------------------
	# Test of power control (MCP23017, addr=0 and addr=1)
	#myUnicorn.init_io_expander_i2c()
	#power_control_test(myUnicorn)
	#relay_control_test(myUnicorn)
	# ---------------------------------------------------


	#myUnicorn.init_io_expander_spi()
	# ---------------------------------------------------

	# ---------------------------------------------------
	# Test of realys
	#relay_test(myUnicorn)
	# ---------------------------------------------------


	# ---------------------------------------------------
	# Test of AD4112
	#rv = myUnicorn.get_adc_value(CH1)
	#print('rv: {:.1f} V'.format(rv))

	#rv = myUnicorn.get_adc_value(CH0)
	#print('rv: {:.1f} V'.format(rv))
	# ---------------------------------------------------


	# ---------------------------------------------------
	# Test of AD4112
	#spi_mcp_test(myUnicorn)
	# ---------------------------------------------------


	#ce_test(myUnicorn)


if __name__ == '__main__':
	main()
