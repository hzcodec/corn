# pylint: disable= line-too-long
# pylint: disable= too-many-branches
# pylint: disable= singleton-comparison

from robot.api import logger
from common import *
import spidev

SPI_PORT = 1
SPI_DEVICE = 1  # SPI1_CE1


class dac61408:
	def __init__(self):
		self.spi = spidev.SpiDev()
		self.spi.open(SPI_PORT, SPI_DEVICE)
		self.spi.mode = SPI_MODE_2

		self.spi.max_speed_hz = SPI_SPEED
		print('DAC init - SPI Mode: {} at speed: {} Hz'.format(self.spi.mode, self.spi.max_speed_hz))

		self.dispatcher = {DACRANGE0: self._config_dac, \
				   DACRANGE1: self._config_dac, \
		                   DACPWDWN: self._dac_power_down}

		self.dac_range_vector_A = 0x0000
		self.dac_range_vector_B = 0x0000
		self.power_down_vector = 0xffff

		self.spi.writebytes([SPICONFIG, 0x0a, 0x84])  # Set device in Active Mode
		self.spi.writebytes([GENCONFIG, 0x00, 0x00])  # Activate internal reference
		self.spi.writebytes([DACPWDWN, 0x00, 0x00])   # Disable DAC power down mode

	def configure(self, *params):
		self.dispatcher[params[0]](params)

	def _write_configuration(self, reg, vector):
			"""
			Serial interface access cycle

			|23|22|21|20|19|18|17|16|15|14|13|12|11|10| 9| 8| 7| 6| 5| 4| 3| 2| 1| 0|
			| 0| x|     reg.addr    |             Data in                           |

			"""
			vec0 = reg
			vec1 = (vector & 0xff00) >> 8
			vec2 = vector & 0x00ff
			logger.info('Vector: 0x{:02x}{:02x}{:02x} '.format(vec0, vec1, vec2))

			self.spi.mode = SPI_MODE_2
			self.spi.writebytes([vec0, vec1, vec2])

	def _get_range_prop(self, dac, dac_range):

		dac_no = dac - 0x14

		if dac_range == DAC_RANGE_0V_p5V:
			range_str = '0V to +5V'
		elif dac_range == DAC_RANGE_0V_p10V:
			range_str = '0V to +10V'
		elif dac_range == DAC_RANGE_m5V_p5V:
			range_str = '-5V to +5V'
		elif dac_range == DAC_RANGE_m10V_p10V:
			range_str = '-10V to +10V'
		else:
			return 'None', 'None'

		return dac_no, range_str

	def _config_dac(self, params):
		reg = params[0]
		dac = params[1]
		dac_range = params[2]

		rv1, rv2 = self._get_range_prop(dac, dac_range)

		logger.info('Configuration of DAC - Register: 0x{:02x}, DAC: {}, Range: {}'.format(reg, rv1, rv2))

		# configure DAC0 - DAC3
		if reg == DACRANGE1 and dac < DAC4:
			if dac == DAC0:
				self.dac_range_vector_A |= (0x0f & dac_range)
				logger.info('DAC0 - range_vector: 0x{:04x}'.format(self.dac_range_vector_A))

			elif dac == DAC1:
				self.dac_range_vector_A |= (dac_range << 4)
				logger.info('DAC1 - range_vector: 0x{:04x}'.format(self.dac_range_vector_A))

			elif dac == DAC2:
				self.dac_range_vector_A |= (dac_range << 8)
				logger.info('DAC2 - range_vector: 0x{:04x}'.format(self.dac_range_vector_A))

			elif dac == DAC3:
				self.dac_range_vector_A |= (dac_range << 12)
				logger.info('DAC3 - range_vector: 0x{:04x}'.format(self.dac_range_vector_A))
			else:
				logger.warn('Invalid DAC for Range: {}'.format(reg))

			self._write_configuration(dac, self.dac_range_vector_A)

		# configure DAC4 - DAC7
		elif reg == DACRANGE0 and dac > DAC3:
			if dac == DAC4:
				self.dac_range_vector_B |= (0x0f & dac_range)
				logger.info('DAC0 - range_vector: 0x{:04x}'.format(self.dac_range_vector_B))

			elif dac == DAC5:
				self.dac_range_vector_B |= (dac_range << 4)
				logger.info('DAC1 - range_vector: 0x{:04x}'.format(self.dac_range_vector_B))

			elif dac == DAC6:
				self.dac_range_vector_B |= (dac_range << 8)
				logger.info('DAC2 - range_vector: 0x{:04x}'.format(self.dac_range_vector_B))

			elif dac == DAC7:
				self.dac_range_vector_B |= (dac_range << 12)
				logger.info('DAC3 - range_vector: 0x{:04x}'.format(self.dac_range_vector_B))
			else:
				logger.warn('Invalid DAC for Range: {}'.format(reg))

			self._write_configuration(dac, self.dac_range_vector_B)

		else:
			logger.warn('Invalid DAC range or combination range and DAC - Range: 0x{:02x}, DAC: 0x{:02x}'.format(reg, dac))

	def _dac_power_down(self, params):
		reg = params[0]
		dac = params[1]
		mode = params[2]
		logger.info('Reg: 0x{:02x}, DAC: 0x{:02x}, Mode: {}'.format(reg, dac, mode))

		vec_normalized = dac - 0x14
		vec = 1 << (vec_normalized+4)  # bit 4 to bit 11 in register is used

		if mode == True:
			logger.info('Power Down DACs: {}'.format(mode))
			self.power_down_vector |= vec
			logger.info('Power down vec: 0x{:02x}'.format(self.power_down_vector))
			self._write_configuration(reg, self.power_down_vector)

		elif mode == False:
			logger.info('Power Up DACs: {}'.format(mode))
			self.power_down_vector &= ~vec
			logger.info('Power down vec: 0x{:02x}'.format(self.power_down_vector))
			self._write_configuration(reg, self.power_down_vector)

		else:
			logger.warn('Invalid mode: {}'.format(mode))

	def get_status_info(self):
		rv = self.spi.xfer2([STATUS, 0x00, 0x00])
		logger.info('Status: 0x{:02x} 0x{:02x}'.format(rv[0], rv[1]))

	def close_port(self):
		logger.info('SPI port is closed')
		self.spi.close()


def main():
	myDac = dac61408()
	#myDac.configure(DACRANGE1, DAC0, DAC_RANGE_0V_p10V)
	#print('----')
	#myDac.configure(DACRANGE1, DAC3, DAC_RANGE_m10V_p10V)
	#print('----')
	##myDac.configure(DACRANGE0, DAC4, DAC_RANGE_m5V_p5V)
	##print('----')
	#myDac.configure(DACRANGE0, DAC7, DAC_RANGE_m5V_p5V)
	#print('----')

	myDac.configure(DACPWDWN, DAC0, False)
	print('----')
	#myDac.configure(DACPWDWN, DAC1, False)
	#print('----')
	#myDac.configure(DACPWDWN, DAC2, False)
	#print('----')
	myDac.configure(DACPWDWN, DAC7, False)
	print('----')
	myDac.configure(DACPWDWN, DAC0, True)
	print('----')
	#myDac.configure(DACPWDWN, DAC7, False)
	#print('----')
	myDac.configure(DACPWDWN, DAC7, True)
	print('----')
	#myDac.close_port()


if __name__ == '__main__':
	main()
