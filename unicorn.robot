*** Settings ***
Library   unicorn
Library   Dialogs

Resource  common.robot
Resource  config.robot

*** Variables ***
&{MCP_port_A0}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA0}  Mode=${OUT}
&{MCP_port_A1}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA1}  Mode=${IN}
&{MCP_port_A2}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA2}  Mode=${OUT}
&{MCP_port_A3}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA3}  Mode=${IN}
&{MCP_port_A4}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA4}  Mode=${OUT}
&{MCP_port_A5}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA5}  Mode=${IN}
&{MCP_port_A6}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA6}  Mode=${OUT}
&{MCP_port_A7}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA7}  Mode=${IN}

&{MCP_port_B0}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB0}  Mode=${OUT}
&{MCP_port_B1}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB1}  Mode=${IN}
&{MCP_port_B2}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB2}  Mode=${OUT}
&{MCP_port_B3}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB3}  Mode=${IN}
&{MCP_port_B4}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB4}  Mode=${OUT}
&{MCP_port_B5}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB5}  Mode=${IN}
&{MCP_port_B6}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB6}  Mode=${OUT}
&{MCP_port_B7}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}  Port=${SPI_GPB7}  Mode=${IN}

&{MCP_A0_HI}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_GPIOA}  Port=${SPI_GPA0}  Mode=${HIGH}
&{MCP_A0_LO}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_GPIOA}  Port=${SPI_GPA0}  Mode=${LOW}
&{MCP_A1_HI}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_GPIOA}  Port=${SPI_GPA1}  Mode=${HIGH}
&{MCP_A6_HI}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_GPIOA}  Port=${SPI_GPA6}  Mode=${HIGH}
&{MCP_A7_HI}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_GPIOA}  Port=${SPI_GPA7}  Mode=${HIGH}
&{MCP_B0_LO}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_GPIOB}  Port=${SPI_GPB0}  Mode=${LOW}


*** Keywords ***
Invalid Selection
	Log To Console    *** Invalid Selection. Use 'ON' or 'OFF'

Initialize MCP ports
	log to console    *** Configure MCP23S17

	# Initialize MCP instance 0, addr 0, port A
	#:FOR  ${index}  IN RANGE  0  8
	#\	log to console  ${MCP_CONTAINTER1}[${index}]
	#\       Config MCP  ${MCP_CONTAINTER1}[${index}]

Initialize Interfaces
	log to console    *** Setup I2C and SPI interfaces
	Init IO Expander I2C
	Init IO Expander SPI
	Init DAC
	Init ADC

	Sleep   1

	#Initialize DAC ports
	#Initialize ADC ports
	Initialize MCP ports

Set 24V Power
	[Documentation]   24V LED
	[Arguments]    ${mode}

*** Settings ***
Suite Setup     Initialize Interfaces


*** Test Cases ***
#MCP_test 1
#	Log to Console    *** MCP23S17 SPI test 1
#	Config MCP   ${MCP_port_A0}  # user-defined configuration, see 'Variables'
#	Config MCP   ${MCP_port_A1}  #                 -"-
#	Config MCP   ${MCP_port_A2}  #                 -"-
#	Config MCP   ${MCP_port_A3}  #                 -"-
#	Config MCP   ${MCP_port_A4}  #                 -"-
#	Config MCP   ${MCP_port_A5}  #                 -"-
#	Config MCP   ${MCP_port_A6}  #                 -"-
#	Config MCP   ${MCP_port_A7}  #                 -"-
#
#	Config MCP   ${MCP_port_B0}  # user-defined configuration, see 'Variables'
#	Config MCP   ${MCP_port_B1}  #                 -"-
#	Config MCP   ${MCP_port_B2}  #                 -"-
#	Config MCP   ${MCP_port_B3}  #                 -"-
#	Config MCP   ${MCP_port_B4}  #                 -"-
#	Config MCP   ${MCP_port_B5}  #                 -"-
#	Config MCP   ${MCP_port_B6}  #                 -"-
#	Config MCP   ${MCP_port_B7}  #                 -"-

#MCP_test 2
#	Log to Console    *** MCP23S17 SPI test 2
#	Config MCP   ${MCP_00A0}  # pre-defined configuration, see config.robot
#	Config MCP   ${MCP_00A1}  #                    -"-
#	Config MCP   ${MCP_00A2}  #                    -"-
#	Config MCP   ${MCP_00A3}  #                    -"-
#	Config MCP   ${MCP_00A4}  #                    -"-
#	Config MCP   ${MCP_00A5}  #                    -"-
#	Config MCP   ${MCP_00A6}  #                    -"-
#	Config MCP   ${MCP_00A7}  #                    -"-
#
#	Config MCP   ${MCP_00B0}  # pre-defined configuration, see config.robot
#	Config MCP   ${MCP_00B1}  #                    -"-
#	Config MCP   ${MCP_00B2}  #                    -"-
#	Config MCP   ${MCP_00B3}  #                    -"-
#	Config MCP   ${MCP_00B4}  #                    -"-
#	Config MCP   ${MCP_00B5}  #                    -"-
#	Config MCP   ${MCP_00B6}  #                    -"-
#	Config MCP   ${MCP_00B7}  #                    -"-
#
#	Log to Console    *** MCP23S17 device 0, addr 1
#	Config MCP   ${MCP_01A0}  # pre-defined configuration, see config.robot
#	Config MCP   ${MCP_01A1}  #                    -"-
#	Config MCP   ${MCP_01A2}  #                    -"-
#	Config MCP   ${MCP_01A3}  #                    -"-
#	Config MCP   ${MCP_01A4}  #                    -"-
#	Config MCP   ${MCP_01A5}  #                    -"-
#	Config MCP   ${MCP_01A6}  #                    -"-
#	Config MCP   ${MCP_01A7}  #                    -"-
#
#	Config MCP   ${MCP_01B0}  # pre-defined configuration, see config.robot
#	Config MCP   ${MCP_01B1}  #                    -"-
#	Config MCP   ${MCP_01B2}  #                    -"-
#	Config MCP   ${MCP_01B3}  #                    -"-
#	Config MCP   ${MCP_01B4}  #                    -"-
#	Config MCP   ${MCP_01B5}  #                    -"-
#	Config MCP   ${MCP_01B6}  #                    -"-
#	Config MCP   ${MCP_01A7}  #                    -"-
#
#	Log to Console    *** MCP23S17 device 1, addr 0
#	Config MCP   ${MCP_10A0}  # pre-defined configuration, see config.robot
#	Config MCP   ${MCP_10A1}  #                    -"-
#	Config MCP   ${MCP_10A2}  #                    -"-
#	Config MCP   ${MCP_10A3}  #                    -"-
#	Config MCP   ${MCP_10A4}  #                    -"-
#	Config MCP   ${MCP_10A5}  #                    -"-
#	Config MCP   ${MCP_10A6}  #                    -"-
#	Config MCP   ${MCP_10A7}  #                    -"-
#
#	Config MCP   ${MCP_10B0}  # pre-defined configuration, see config.robot
#	Config MCP   ${MCP_10B1}  #                    -"-
#	Config MCP   ${MCP_10B2}  #                    -"-
#	Config MCP   ${MCP_10B3}  #                    -"-
#	Config MCP   ${MCP_10B4}  #                    -"-
#	Config MCP   ${MCP_10B5}  #                    -"-
#	Config MCP   ${MCP_10B6}  #                    -"-
#	Config MCP   ${MCP_10A7}  #                    -"-

#MCP_test 3
#	Log to Console    *** MCP23S17 SPI test 3
#
#	#Initialize MCP instance 0, addr 0, port A
#	:FOR  ${index}  IN RANGE  0  8
#	\       Config MCP  ${MCP_CONTAINTER1}[${index}]
#
#	#Initialize MCP instance 0, addr 0, port B
#	:FOR  ${index}  IN RANGE  0  8
#	\       Config MCP  ${MCP_CONTAINTER2}[${index}]
#
#	#Initialize MCP instance 1, addr 0, port B
#	:FOR  ${index}  IN RANGE  0  8
#	\       Config MCP  ${MCP_CONTAINTER6}[${index}]

MCP_test 4
	Log to Console    *** MCP23S17 SPI test 4
	Config MCP   ${MCP_port_A0}  # user-defined configuration, see 'Variables'
	Config MCP   ${MCP_port_A6}  #                 -"-

	Config MCP   ${MCP_A0_HI}    #                 -"-
	Config MCP   ${MCP_A0_LO}    #                 -"-
	Config MCP   ${MCP_A1_HI}    # this will give a warning since port is input
	Config MCP   ${MCP_A7_HI}    # this will give a warning since port is input
	Config MCP   ${MCP_A6_HI}

	Config MCP   ${MCP_port_B0}
	Config MCP   ${MCP_B0_LO}


#Power Test
#	Log to Console    *** Power Control test
#	Power Control  ${DC_300V}  ${ON}
#	Power Control  ${AC_230V}  ${ON}
#	Power Control  ${PROTECTED_EARTH}  ${ON}
#	Power Control  ${p_24V}  ${ON}
#	Power Control  ${p_5V}  ${ON}
#
#	Power Control  ${DC_300V}  ${OFF}
#	Power Control  ${AC_230V}  ${OFF}
#	Power Control  ${PROTECTED_EARTH}  ${OFF}
#	Power Control  ${p_24V}  ${OFF}
#	Power Control  ${p_5V}  ${OFF}

#Relay Test
#	Log to Console    *** Relay test
#	Relay Control  ${RELAY1}  ${ON}
#	Relay Control  ${RELAY8}  ${ON}
#	Relay Control  ${RELAY1}  ${OFF}
#	Relay Control  ${RELAY8}  ${OFF}
#
#	Relay Control  ${RELAY9}  ${ON}
#	Relay Control  ${RELAY16}  ${ON}
#	Relay Control  ${RELAY9}  ${OFF}
#	Relay Control  ${RELAY16}  ${OFF}

#IO 0 Port Test
#    #Define an object for MCP23S17 device 0 port A, GPA0 high 
#    ${MCP_A0_HI} =    Create Dictionary  Device=${MCP23S17_DEVICE_0}  
#        ...                          	 SPI-addr=${SPI_ADDRESS_0}
#	...    				 Reg=${SPI_GPIOA}
#	...			    	 Port=${SPI_GPA0}
#	...			    	 Mode=${HIGH}
#
#
#    Config MCP   ${MCP_A0_HI}
#
#   Set output port high
#    Config MCP   ${MCP_A0_HI}

