*** Settings ***

*** Variables ***

# input/output mode
${OUT} =   0
${IN} =    1

# port ON/OFF mode
${OFF} =   0
${ON} =    1

# level
${HIGH} =  1
${LOW} =  0

# Relay index controlled by MCP23017 (addr=0)
${DC_300V} =  0
${AC_230V} =  1
${PROTECTED_EARTH} =  2
${p_24V} =  3
${p_5V} =  4

${S1} =     0
${S2} =     1
${READY} =  2
${SAFE} =   3
${RESET} =  4

# Relay names controlled by MCP23017 (addr=1)
${RELAY1} =    0
${RELAY2} =    1
${RELAY3} =    2
${RELAY4} =    3
${RELAY5} =    4
${RELAY6} =    5
${RELAY7} =    6
${RELAY8} =    7
${RELAY9} =    8
${RELAY10} =   9
${RELAY11} =   10
${RELAY12} =   11
${RELAY13} =   12
${RELAY14} =   13
${RELAY15} =   14
${RELAY16} =   15

# =======}======================================================================================
# MCP23017 device
# =============================================================================================
# Port 0 and 1 are configured during initialization (used as chip enable).
# Don't use them for your own purpose.
${SPARE0} =    0  # MCP23017, GPB0
${SPARE1} =    1  # MCP23017, GPB1


# These ports are avalilable for the user
${SPARE2} =    2  # MCP23017, GPB2
${SPARE3} =    3  #    -"-  , GPB3
${SPARE4} =    4  #    -"-  , GPB4
${SPARE5} =    5  #    -"-  , GPB5
${SPARE6} =    6  #    -"-  , GPB6
${SPARE7} =    7  #    -"-  , GPB7


# =============================================================================================
# MCP23s17 device
# =============================================================================================
${SPI_IODIRA} =   0x00
${SPI_GPIOA} =   0x14
${SPI_GPA0} =    0
${SPI_GPA1} =    1
${SPI_GPA2} =    2
${SPI_GPA3} =    3
${SPI_GPA4} =    4
${SPI_GPA5} =    5
${SPI_GPA6} =    6
${SPI_GPA7} =    7

${SPI_IODIRB} =   0x01
${SPI_GPIOB} =   0x15
${SPI_GPB0} =    0
${SPI_GPB1} =    1
${SPI_GPB2} =    2
${SPI_GPB3} =    3
${SPI_GPB4} =    4
${SPI_GPB5} =    5
${SPI_GPB6} =    6
${SPI_GPB7} =    7


# =============================================================================================
# DAC61408 device
# =============================================================================================
# Registers
${DAC0} =    0x14
${DAC1} =    0x15
${DAC2} =    0x16
${DAC3} =    0x17
${DAC4} =    0x18
${DAC5} =    0x19
${DAC6} =    0x1a
${DAC7} =    0x1b

${DACRANGE0} =    0x0b  # DAC[7:4]
${DACRANGE1} =    0x0c  # DAC[3:0]

# DAC61408 parameters
${DAC_RANGE_0V_p5V} =    0x0  # 0 to 5V
${DAC_RANGE_0V_p10V} =    0x1  # 0 to 10V
${DAC_RANGE_m5V_p5V} =    0x9  # -5 to +5V
${DAC_RANGE_m10V_p10V} =    0xa  # -10 to +10V

# Output channel
${OUT_0} =   0
${OUT_1} =   1
${OUT_2} =   2
${OUT_3} =   3
${OUT_4} =   4
${OUT_5} =   5
${OUT_6} =   6
${OUT_7} =   7


# =============================================================================================
# AD4112 device
# =============================================================================================
${VIN_0} =   0
${VIN_1} =   1
${VIN_2} =   2
${VIN_3} =   3
${VIN_4} =   4
${VIN_5} =   5
${VIN_6} =   6
${VIN_7} =   7

${GP_DATA0} =   0x80  # bit 6 in GPIOCON
${GP_DATA1} =   0x40  # bit 7 in GPIOCON

${INT_OFFSET} =     4
${INT_GAIN} =       5
${SYSTEM_OFFSET} =  6
${SYSTEM_GAIN} =    7

# Channel register CH0-CH7, 0x10 - 0x1f
${CH_EN} =   0x8000
${SETUP_SEL_0} =   0x0000
${SETUP_SEL_1} =   0x1000
${SETUP_SEL_2} =   0x2000
${SETUP_SEL_3} =   0x3000
${SETUP_SEL_4} =   0x4000
${SETUP_SEL_5} =   0x5000
${SETUP_SEL_6} =   0x6000
${SETUP_SEL_7} =   0x7000

${INPUT_VIN0} =   0x0010
${INPUT_VIN1} =   0x0030
${INPUT_VIN2} =   0x0050
${INPUT_VIN3} =   0x0070
${INPUT_VIN4} =   0x0090
${INPUT_VIN5} =   0x00b0
${INPUT_VIN6} =   0x00d0
${INPUT_VIN7} =   0x00f0

${INPUT_VIN0_VIN1} =   0x0001
${INPUT_VIN1_VIN0} =   0x0020
${INPUT_VIN2_VIN3} =   0x0043
${INPUT_VIN3_VIN2} =   0x0062
${INPUT_VIN4_VIN5} =   0x0085
${INPUT_VIN5_VIN4} =   0x00a4
${INPUT_VIN6_VIN7} =   0x00c7
${INPUT_VIN7_VIN6} =   0x00e6
 
${IIN3} =   0x018b
${IIN2} =   0x01aa
${IIN2} =   0x01aa
${IIN1} =   0x01c9
${IIN0} =   0x01e8

# ADC mode register ADCMODE, 0x01
${REF_EN} =      0x8000
${SING_SYNC} =   0x2000
${CONT_CONV} =   0x0000
${SING_CONV} =   0x0010

# Channel register IFMODE, 0x02
${CONTREAD} =   0x80
${DATA_STAT} =  0x40

# Configuration register, SETUPCON0-7
${BI_POLAR} =      0x1000
${REF_BUFP} =      0x0800
${REF_BUFM} =      0x0400
${INBUF_EN} =      0x0300
${REF_SEL_INT} =   0x0020

# =============================================================================================
# Device parameters
# =============================================================================================
${DAC61408_DEVICE} =    0
${AD4112_DEVICE_0} =    1
${AD4112_DEVICE_1} =    2
${MCP23S17_DEVICE_0} =    3
${MCP23S17_DEVICE_1} =    4

${MCP23S17_ADDR_0} =    0
${MCP23S17_ADDR_1} =    1

${NA} =    99  # Not Applicable. Can be changed for future use.

${SPI_ADDRESS_0} =    0
${SPI_ADDRESS_1} =    1
