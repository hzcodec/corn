# pylint: disable= no-else-return

# Misc defines
MCP23017_DEFAULT_ADDR = 0x20
MCP23017_ADDR_0 = 0x20
MCP23017_ADDR_1 = 0x21

# SPI defines
SPI_MCP23S17_DEVICE = 2 # SPI1_CE2
SPI_MCP23S17_PORT = 1
SPI_SPEED = 40000  # lowered the speed for test purpose

SPI_MODE_0 = 0b00
SPI_MODE_1 = 0b01
SPI_MODE_2 = 0b10
SPI_MODE_3 = 0b11

DUMMY_BYTE = 0x00
PADDING_BYTE = 0x00

# in/out mode
IN = 1
OUT = 0


# on/off mode
OFF = 0
ON = 1


# level
HIGH = 1
LOW = 0

ERROR_MSG = 'Err: Invalid input'
MEAS_CURR = 0
MEAS_VOLT = 1

# Relay index controlled by MCP23017 (addr=0)
DC_300V = 0
AC_230V = 1
PROTECTED_EARTH = 2
p_24V = 3
p_5V = 4

# port B
S1 = 0
S2 = 1
READY = 2
SAFE =  3
RESET = 4


# Relay names controlled by MCP23017 (addr=1)
RELAY1 = 0
RELAY2 = 1
RELAY3 = 2
RELAY4 = 3
RELAY5 = 4
RELAY6 = 5
RELAY7 = 6
RELAY8 = 7
RELAY9 = 8
RELAY10 =9
RELAY11 = 10
RELAY12 = 11
RELAY13 = 12
RELAY14 = 13
RELAY15 = 14
RELAY16 = 15


# -------------------------------------------------------------
# MCP23017
# -------------------------------------------------------------
# Registers port A for MCP23017 (I2C)
I2C_IODIRA = 0x00
I2C_IOPOLA = 0x02
I2C_GPIOA = 0x12

# pin numbers for MCP23017, addr=0x20
I2C_GPA0 = 0  # 24V_on
I2C_GPA1 = 1  # Ext_pwr_on
I2C_GPA2 = 2  # 5V/3V_on
I2C_GPA3 = 3  # Shut down
I2C_GPA4 = 4  # S/W_RES
I2C_GPA5 = 5  # Detect
I2C_GPA6 = 6  # Spare0
I2C_GPA7 = 7  # Spare1

# Registers port B for MCP23017 (I2C)
I2C_IODIRB = 0x01
I2C_IOPOLB = 0x03
I2C_GPIOB = 0x13
# pin numbers
I2C_GPB0 = 0  # Spare0
I2C_GPB1 = 1  # Spare1
I2C_GPB2 = 2  # Spare2
I2C_GPB3 = 3  # Spare3
I2C_GPB4 = 4  # Spare4
I2C_GPB5 = 5  # CE_A0
I2C_GPB6 = 6  # CE_A1
I2C_GPB7 = 7  # CE_A2


# -------------------------------------------------------------
# MCP23S17
# -------------------------------------------------------------
SPI_IOCON = 0x0a
# Registers port A for MCP23S17 (SPI)
SPI_IODIRA = 0x00
SPI_IOPOLA = 0x02
SPI_GPPUA = 0x0c
SPI_GPIOA = 0x12
# pin numbers
SPI_GPA0 = 0  #
SPI_GPA1 = 1  #
SPI_GPA2 = 2  #
SPI_GPA3 = 3  #
SPI_GPA4 = 4  #
SPI_GPA5 = 5  # DigOut1
SPI_GPA6 = 6  # DigOut2
SPI_GPA7 = 7  #

# Registers port B for MCP23S17 (SPI)
SPI_IODIRB = 0x01
SPI_IOPOLB = 0x03
SPI_GPPUB = 0x0d
SPI_GPIOB = 0x13
# pin numbers
SPI_GPB0 = 0  #
SPI_GPB1 = 1  #
SPI_GPB2 = 2  #
SPI_GPB3 = 3  #
SPI_GPB4 = 4  #
SPI_GPB5 = 5  #
SPI_GPB6 = 6  #
SPI_GPB7 = 7  #

SPI_MAX_GPIO_PORT = 7

# Device parameters
DAC61408_DEVICE = 0
AD4112_DEVICE_0 = 1
AD4112_DEVICE_1 = 2
MCP23S17_DEVICE_0 = 3
MCP23S17_DEVICE_1 = 4

MCP23S17_ADDR_0 = 0
MCP23S17_ADDR_1 = 1

SPI_ADDRESS_0 = 0
SPI_ADDRESS_1 = 1

# -------------------------------------------------------------
# DAC61408
# -------------------------------------------------------------
# Register for DAC61408
DAC0 = 0x14
DAC1 = 0x15
DAC2 = 0x16
DAC3 = 0x17
DAC4 = 0x18
DAC5 = 0x19
DAC6 = 0x1a
DAC7 = 0x1b
DAC_STATUS = 0x02
SPICONFIG = 0x03
GENCONFIG = 0x04
GPIOCON = 0x06
DACPWDWN = 0x09
DACRANGE0 = 0x0b  # DAC[7:4]
DACRANGE1 = 0x0c  # DAC[3:0]

# DAC61408 parameters
DAC_RANGE_0V_p5V = 0x0  # 0 to 5V
DAC_RANGE_0V_p10V = 0x1  # 0 to 10V
DAC_RANGE_m5V_p5V = 0x9  # -5 to +5V
DAC_RANGE_m10V_p10V = 0xa  # -10 to +10V

# -------------------------------------------------------------
# AD4112
# -------------------------------------------------------------
# Register for AD4112
COMMS = 0x00  # Communication register. All access must start here. (W)
STATUS = 0x00  # Status information (R)
ADCMODE = 0x01
IFMODE = 0x02
DATA = 0x04  # The data register contains the ADC conversion result (R)
ID = 0x07

CH0 = 0x10 # Channel control register (R/W)
CH1 = 0x11
CH2 = 0x12
CH3 = 0x13
CH4 = 0x14
CH5 = 0x15
CH6 = 0x16
CH7 = 0x17
CH8 = 0x18
CH9 = 0x19
CH10 = 0x1a
CH11 = 0x1b
CH12 = 0x1c
CH13 = 0x1d
CH14 = 0x1e
CH15 = 0x1f

SETUPCON0 = 0x20  # Setup configuration register (R/W)
SETUPCON1 = 0x21
SETUPCON2 = 0x22
SETUPCON3 = 0x23
SETUPCON4 = 0x24
SETUPCON5 = 0x25
SETUPCON6 = 0x26
SETUPCON7 = 0x27

OFFSET0 = 0x30
OFFSET1 = 0x31

GAIN0 = 0x38
GAIN1 = 0x39

# AD412 parameters
RD = 0x40 # read bit in COMMS register
VIN0 = 0
VIN1 = 1
VIN2 = 2
VIN3 = 3
VIN4 = 4
VIN5 = 5
VIN6 = 6
VIN7 = 7

VIN0_VINCOM = 0x010  # Channel register CH<n>, voltage input to voltage input common
VIN1_VINCOM = 0x030
VIN2_VINCOM = 0x050
VIN3_VINCOM = 0x070
VIN4_VINCOM = 0x090
VIN5_VINCOM = 0x0b0
VIN6_VINCOM = 0x0d0
VIN6_VINCOM = 0x0f0

GP_DATA0 = 0x80  # bit 6 in GPIOCON
GP_DATA1 = 0x40  # bit 7 in GPIOCON

INT_OFFSET = 4
INT_GAIN = 5
SYSTEM_OFFSET = 6
SYSTEM_GAIN = 7

# Channel register CH0-CH7, 0x10 - 0x1f
CH_EN = 0x8000
SETUP_SEL_0 = 0x0000
SETUP_SEL_1 = 0x1000
SETUP_SEL_2 = 0x2000
SETUP_SEL_3 = 0x3000
SETUP_SEL_4 = 0x4000
SETUP_SEL_5 = 0x5000
SETUP_SEL_6 = 0x6000
SETUP_SEL_7 = 0x7000

INPUT_VIN0 = 0x0010
INPUT_VIN1 = 0x0030
INPUT_VIN2 = 0x0050
INPUT_VIN3 = 0x0070
INPUT_VIN4 = 0x0090
INPUT_VIN5 = 0x00b0
INPUT_VIN6 = 0x00d0
INPUT_VIN7 = 0x00f0

INPUT_VIN0_VIN1 = 0x0001
INPUT_VIN1_VIN0 = 0x0020
INPUT_VIN2_VIN3 = 0x0043
INPUT_VIN3_VIN2 = 0x0062
INPUT_VIN4_VIN5 = 0x0085
INPUT_VIN5_VIN4 = 0x00a4
INPUT_VIN6_VIN7 = 0x00c7
INPUT_VIN7_VIN6 = 0x00e6

IIN3 = 0x018b
IIN2 = 0x01aa
IIN2 = 0x01aa
IIN1 = 0x01c9
IIN0 = 0x01e8

# ADC mode register ADCMODE, 0x01
REF_EN = 0x8000
SING_SYNC = 0x2000
CONT_CONV = 0x0000
SING_CONV = 0x0010

# Channel register IFMODE, 0x02
CONTREAD = 0x80
DATA_STAT = 0x40

# Configuration register, SETUPCON0-7
BI_POLAR = 0x1000
REF_BUFP = 0x0800
REF_BUFM = 0x0400
INBUF_EN = 0x0300
REF_SEL_INT = 0x0020

# ------------------------------------------------------------------
# help functions
# ------------------------------------------------------------------
def ad4112_get_adc_mode_name(inp):
	if inp == CONT_CONV:
		return 'CONT_CONV'
	elif inp == SING_CONV:
		return 'SING_CONV'
	else:
		return ERROR_MSG

setup_name = {
    SETUP_SEL_0: lambda: "SETUP_SEL_0",
    SETUP_SEL_1: lambda: "SETUP_SEL_1",
    SETUP_SEL_2: lambda: "SETUP_SEL_2",
    SETUP_SEL_3: lambda: "SETUP_SEL_3",
    SETUP_SEL_4: lambda: "SETUP_SEL_4",
    SETUP_SEL_5: lambda: "SETUP_SEL_5",
    SETUP_SEL_6: lambda: "SETUP_SEL_6",
    SETUP_SEL_7: lambda: "SETUP_SEL_7",
}

def ad4112_get_setup_name(inp):
	return setup_name[inp]()

input_name = {
    INPUT_VIN0: lambda: "INPUT_VIN0",
    INPUT_VIN1: lambda: "INPUT_VIN1",
    INPUT_VIN2: lambda: "INPUT_VIN2",
    INPUT_VIN3: lambda: "INPUT_VIN3",
    INPUT_VIN4: lambda: "INPUT_VIN4",
    INPUT_VIN5: lambda: "INPUT_VIN5",
    INPUT_VIN6: lambda: "INPUT_VIN6",
    INPUT_VIN7: lambda: "INPUT_VIN7",
    INPUT_VIN0_VIN1: lambda: "INPUT_VIN0_VIN1",
    INPUT_VIN1_VIN0: lambda: "INPUT_VIN1_VIN0",
    INPUT_VIN2_VIN3: lambda: "INPUT_VIN2_VIN3",
    INPUT_VIN3_VIN2: lambda: "INPUT_VIN3_VIN2",
    INPUT_VIN4_VIN5: lambda: "INPUT_VIN4_VIN5",
    INPUT_VIN5_VIN4: lambda: "INPUT_VIN5_VIN4",
    INPUT_VIN6_VIN7: lambda: "INPUT_VIN6_VIN7",
    INPUT_VIN7_VIN6: lambda: "INPUT_VIN7_VIN6",
    IIN0: lambda: "IIN0+,IIN0-",
    IIN1: lambda: "III1+,IIN1-",
    IIN2: lambda: "III2+,IIN2-",
    IIN3: lambda: "III3+,IIN3-",
}

def ad4112_get_input_name(inp):
	return input_name[inp]()

def ad4112_get_stat_name(inp):
	if inp == DATA_STAT:
		return 'DATA_STAT'
	else:
		return ERROR_MSG

def mcp23017_get_mode_name(inp):
	if inp == OUT:
		return 'OUT'
	else:
		return 'IN'

def mcp23017_get_level_name(inp):
	if inp == ON:
		return 'ON'
	else:
		return 'OFF'

def mcp23017_get_device_name(inp):
	if inp == 0:
		return 'AD4112 device 1'
	elif inp == 1:
		return 'AD4112 device 2'
	elif inp == 2:
		return 'DAC61408'
	elif inp == 3:
		return 'MCP23S17 device 0'
	elif inp == 4:
		return 'MCP23S17 device 1'
	else:
		return ERROR_MSG
