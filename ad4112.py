# pylint: disable= trailing-whitespace
# pylint: disable= line-too-long
# pylint: disable= bad-whitespace
# pylint: disable= too-few-public-methods
import time
import sys
from robot.api import logger
from common import *
import spidev

SPI_PORT = 1
SPI_DEVICE = 0  # SPI1_CE0
DELIMITER = 90
DELAY1 = 0.1
DELAY2 = 0.2
DELAY3 = 1


class bcolors:
    BLUE      = '\033[94m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    RED       = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    BGREEN    = '\033[1m' + '\033[92m'
    BYELLOW   = '\033[1m' + '\033[93m'


class ad4112:
	"""
	12-bit ADC.
	According to the datasheet AD7490 requires CS as framing signal
	for every 16 bit read or write transaction.

	1) After a power-up cycle and when the power supplies are stable,
	   a device reset is required

	2) All communication begins by writing to the communications register.

	Writing to register:
	
	   8-bit command               8/16/24 bits of data             8-bit CRC
	|<--------------->|<--------------------------------------->|<------------->|
	"""

	def __init__(self):
		self.spi = spidev.SpiDev()
		self.spi.open(SPI_PORT, SPI_DEVICE)
		self.spi.max_speed_hz = SPI_SPEED
		self.spi.mode = SPI_MODE_3
		self.gp_vector = 0xc0

		self.dispatcher = {ID: self._get_id, \
		                   COMMS: self._get_id}

	def configure(self, *params):
		self.dispatcher[params[0]](params)

	def _config_ad(self):
		logger.info('Configure AD4112')
	
	def device_reset(self):
		"""
		64 serial clock cycles with DIN high => sets ADC to default state
		"""
		print('Device Reset')
		self.spi.writebytes([0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff])
		print(DELIMITER*'-')

	def _get_id(self):
		"""
		Return value should be 0x30dx. x = don't care
		"""
		command = 0x00 | RD | ID
		print('Get ID - command: 0x{:02x}'.format(command))

		rv = self.spi.xfer2([command, PADDING_BYTE, PADDING_BYTE])
		#print('0x{:02x}, 0x{:02x} 0x{:02x}'.format(rv[0], rv[1], rv[2]))
		product_id = rv[1] << 4 | (rv[2] >> 4)
		print('Product ID: 0x{:03x}'.format(product_id))
		print(DELIMITER*'-')

	def set_gpio(self, gpio, mode):
		# N.B! For the eval board ON is setting the bit to 0
		command = 0x00 | GPIOCON 
		byte1 = 0x20 # enable GPIO0 and GPIO1 as output signals

		if mode == ON:
			self.gp_vector &= ~(gpio)
		else:
			self.gp_vector |= gpio 

		byte2 = self.gp_vector

		print('Set GP - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])

	def update_offset(self, reg, val):
		command = 0x00 | reg
		print('Update OFFSET{} - command: 0x{:02x} 0x{:02x} 0x{:02x} 0x{:02x}'.format(reg-48, command, val[0], val[1], val[2]))
		self.spi.xfer2([command, val[0], val[1], val[2]])
		print(DELIMITER*'-')

	def update_gain(self, reg, val):
		command = 0x00 | reg
		print('Update GAIN{} - command: 0x{:02x} 0x{:02x} 0x{:02x} 0x{:02x}'.format(reg-56, command, val[0], val[1], val[2]))
		self.spi.xfer2([command, val[0], val[1], val[2]])
		print(DELIMITER*'-')

	def config_channel_reg(self, reg, vec):
		if reg < CH0 or reg > CH15:
			print('Invalid channel: {}'.format(reg))
		else:
			reg_masked = reg & 0x0f
			command = 0x00 | reg

			byte1 = (vec & 0xff00) >> 8
			byte2 = vec & 0x00ff

			setup_sel = vec & 0x7000
			rv = ad4112_get_setup_name(setup_sel)

			input_n = vec & 0x3ff
			rv2 = ad4112_get_input_name(input_n)

			print('Configure channel (reg: 0x{:02x}), CH{} with {}/{} - command: 0x{:02x} 0x{:02x} 0x{:02x}'.
			      format(reg, reg_masked, rv2, rv, command, byte1, byte2))

			self.spi.xfer2([command, byte1, byte2])
			print(DELIMITER*'-')

	def config_adc_mode(self, vec):
		command = 0x00 | ADCMODE 

		adc_mode = vec & 0x70
		rv = ad4112_get_adc_mode_name(adc_mode)

		# bit[13] SING_SYNC, enabled
		byte1 = (0xff00 & vec) >> 8

		# bit[6:4] Mode, 000=Cont conv, 001=Single conv
		byte2 = adc_mode

		print('Configure ADC mode (reg: 0x01) with {} - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(rv, command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])
		print(DELIMITER*'-')

	def config_interface_mode(self, vec):
		command = 0x00 | IFMODE 
		byte1 = 0x00

		# bit[6] DATA_STAT enabled
		# bit[0] WL16, 0=24-bit, 1=16-bit data
		byte2 = vec

		rv = ad4112_get_stat_name(vec)

		print('Configure Interface mode (reg: 0x02) with {} - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(rv, command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])
		print(DELIMITER*'-')

	def config_setup(self, vec):
		command = 0x00 | SETUPCON0 
		byte1 = (0xff00 & vec) >> 8
		byte2 = 0x00ff & vec

		print('Configure Setup 0 (reg: 0x20) - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])
		print(DELIMITER*'-')

	def get_data(self, sel):
		command = COMMS | RD | DATA 
		print('{}Get data (0x04) - command: 0x{:02x}'.format(bcolors.BYELLOW, command))

		rv = self.spi.xfer2([command, PADDING_BYTE, PADDING_BYTE, PADDING_BYTE, PADDING_BYTE])  # 24 bits +  DATA_STAT
		#rv = self.spi.xfer2([command, PADDING_BYTE, PADDING_BYTE])  # 16 bits

		#print('Data: {}'.format(rv))
		print('Data: 0x{:02x} 0x{:02x} 0x{:02x} 0x{:02x} 0x{:02x}'.format(rv[0], rv[1], rv[2], rv[3], rv[4]))

		sum1 = rv[1]*65536 + rv[2]*256 + rv[3]
		sum2 = sum1*10/16777215

		if sel:
			print('Out: {:.1f} V for Channel: {}'.format(sum2, rv[4]))
			print(bcolors.ENDC, DELIMITER*'-')
			return sum2
		else:
			print('Out: {:.1f} mA for Channel: {}'.format(sum2*10.5, rv[4]))
			print(bcolors.ENDC, DELIMITER*'-')
			return sum2*10.5

	def get_status(self):
		command = 0x00 | RD | STATUS
		print('Get Status - command: 0x{:02x}'.format(command))
		rv = self.spi.xfer2([command, PADDING_BYTE])
		print('0x{:02x}, 0x{:02x}'.format(rv[0], rv[1]))
		print(DELIMITER*'-')

	def get_offset_gain(self):
		command = 0x00 | RD | OFFSET0
		print('Get Offset 0 - command: 0x{:02x}'.format(command))
		rv = self.spi.xfer2([command, PADDING_BYTE, PADDING_BYTE, PADDING_BYTE])
		print('0x{:02x} 0x{:02x} 0x{:02x}'.format(rv[1], rv[2], rv[3]))

		command = 0x00 | RD | GAIN0
		print('Get Gain 0 - command: 0x{:02x}'.format(command))
		rv = self.spi.xfer2([command, PADDING_BYTE, PADDING_BYTE, PADDING_BYTE])
		print('0x{:02x} 0x{:02x} 0x{:02x}\n'.format(rv[1], rv[2], rv[3]))

		command = 0x00 | RD | OFFSET1
		print('Get Offset 1 - command: 0x{:02x}'.format(command))
		rv = self.spi.xfer2([command, PADDING_BYTE, PADDING_BYTE, PADDING_BYTE])
		print('0x{:02x} 0x{:02x} 0x{:02x}'.format(rv[1], rv[2], rv[3]))

		command = 0x00 | RD | GAIN1
		print('Get Gain 1 - command: 0x{:02x}'.format(command))
		rv = self.spi.xfer2([command, PADDING_BYTE, PADDING_BYTE, PADDING_BYTE])
		print('0x{:02x} 0x{:02x} 0x{:02x}'.format(rv[1], rv[2], rv[3]))
		print(DELIMITER*'-')

	def internal_zero_scale(self):
		# internal offset calibration, mode = 100
		command = 0x00 | ADCMODE 
		byte1 = 0x20
		byte2 = 0x40

		print('Calib, internal zero-scale (offset) - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])
		print(DELIMITER*'-')

	def internal_full_scale(self):
		# internal gain calibration, mode = 101
		command = 0x00 | ADCMODE 
		byte1 = 0x20
		byte2 = 0x50

		print('Calib, internal full-scale (gain) - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])
		print(DELIMITER*'-')

	def system_zero_scale(self):
		# system offset calibration, mode 110
		command = 0x00 | ADCMODE 
		byte1 = 0x20
		byte2 = 0x60

		print('Calib, system zero-scale calib (offset) - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])
		print(DELIMITER*'-')

	def system_full_scale(self):
		# system gain calibration, mode 111
		command = 0x00 | ADCMODE 
		byte1 = 0x20
		byte2 = 0x70

		print('Calib, system full-scale calib (gain) - command: 0x{:02x} 0x{:02x} 0x{:02x}'.format(command, byte1, byte2))
		self.spi.xfer2([command, byte1, byte2])
		print(DELIMITER*'-')


# --------------------------------------------------------------------------------
# Test purpose functions
# --------------------------------------------------------------------------------
def gpo_test(obj):
	obj.set_gpio(GP_DATA0, ON)
	time.sleep(1)

	obj.set_gpio(GP_DATA1, ON)
	time.sleep(1)

	obj.set_gpio(GP_DATA0, OFF)
	time.sleep(1)

	obj.set_gpio(GP_DATA1, OFF)
	time.sleep(1)

	print(DELIMITER*'-')

def setup_and_measure1(obj):
	vec = CH_EN | SETUP_SEL_0 | INPUT_VIN0
	obj.config_channel_reg(CH0, vec)
	time.sleep(DELAY1)

	vec = REF_BUFP | REF_BUFM | INBUF_EN
	obj.config_setup(vec)
	time.sleep(DELAY1)

	vec = REF_EN | SING_SYNC | SING_CONV
	obj.config_adc_mode(vec)
	time.sleep(DELAY1)

	vec = DATA_STAT
	obj.config_interface_mode(vec)
	time.sleep(DELAY1)

	obj.get_data(MEAS_VOLT)
	time.sleep(DELAY2)

def setup_and_measure2(obj):
	vec = CH_EN | SETUP_SEL_0 | INPUT_VIN1
	obj.config_channel_reg(CH1, vec)
	time.sleep(DELAY1)

	vec = REF_EN | SING_SYNC | SING_CONV
	obj.config_adc_mode(vec)
	time.sleep(DELAY1)

	obj.get_data(MEAS_VOLT)
	time.sleep(DELAY2)

def calibrate(obj, calib_mode):

	if calib_mode == INT_OFFSET:
		obj.internal_zero_scale()
	elif calib_mode == INT_GAIN:
		obj.internal_full_scale()
	elif calib_mode == SYSTEM_OFFSET:
		obj.system_zero_scale()
	elif calib_mode == SYSTEM_GAIN:
		obj.system_full_scale()
	else:
		print('Invalid calibration mode')
	
	time.sleep(0.6)

def main():
	myAD = ad4112()

	if len(sys.argv) > 1:
		if sys.argv[1] == 'reset':
			myAD.device_reset()
			time.sleep(DELAY3)
		elif sys.argv[1] == 'io':
			calibrate(myAD, INT_OFFSET)
		elif sys.argv[1] == 'ig':
			calibrate(myAD, INT_GAIN)
		elif sys.argv[1] == 'so':
			calibrate(myAD, SYSTEM_OFFSET)
		elif sys.argv[1] == 'sg':
			calibrate(myAD, SYSTEM_GAIN)
		else:
			print('Nope')

	myAD.update_gain(GAIN0, [0xd5, 0x97, 0xda])
	myAD.update_gain(GAIN1, [0xd5, 0x97, 0xda])

	# =========================================================
	# Below a number of test cases have been implemented.
	# To use them, comment/uncomment to select the test case
	# you want to run.
	# =========================================================


	# ---------------------------------------------------
	#myAD._get_id()
	#time.sleep(DELAY1)
	# ---------------------------------------------------


	# ---------------------------------------------------
	# Test of GPO0 and GPO1
	#gpo_test(myAD)
	#time.sleep(DELAY1)
	# ---------------------------------------------------


	# ---------------------------------------------------
	# Test of ch0 and ch1
	setup_and_measure1(myAD)
	time.sleep(DELAY2)

	setup_and_measure2(myAD)
	time.sleep(DELAY1)
	# ---------------------------------------------------


	# ---------------------------------------------------
	# Test of differential input.
	# Connect +V to VIN0 and GND to VIN1.
	# Did'nt need to send reset.
	#setup = CH_EN | SETUP_SEL_0 | INPUT_VIN0_VIN1
	#myAD.config_channel_reg(CH0, setup)
	#setup = CH_EN | SETUP_SEL_0 | INPUT_VIN0_VIN1
	#myAD.config_channel_reg(CH1, setup)

	#vec = REF_BUFP | REF_BUFM | INBUF_EN
	#myAD.config_setup(vec)

	#setup = REF_EN | SING_SYNC | SING_CONV
	#myAD.config_adc_mode(setup)

	#setup = DATA_STAT
	#myAD.config_interface_mode(setup)

	#myAD.get_data(MEAS_VOLT)
	#time.sleep(DELAY1)
	# ---------------------------------------------------


	# ---------------------------------------------------
	# Test of Current inputs.
	# Connect to II0+ and GND.
	#setup = CH_EN | SETUP_SEL_0 | IIN0
	#myAD.config_channel_reg(CH0, setup)

	#setup = REF_BUFP | REF_BUFM | INBUF_EN
	#myAD.config_setup(setup)

	#setup = REF_EN | SING_SYNC | SING_CONV
	#myAD.config_adc_mode(setup)

	#setup = DATA_STAT
	#myAD.config_interface_mode(setup)

	#myAD.get_data(MEAS_CURR)
	#time.sleep(DELAY1)
	# ---------------------------------------------------


	#myAD.get_offset_gain()
	#time.sleep(DELAY1)

	#myAD.get_status()


if __name__ == '__main__':
	main()
