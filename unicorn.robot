*** Settings ***
Library   unicorn
Library   Dialogs

Resource  common.robot
Resource  config.robot

*** Variables ***
&{MCP_port_A0}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA0}  Mode=${OUT}
&{MCP_port_A1}  Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}  Port=${SPI_GPA1}  Mode=${OUT}
&{MCP_A0_HI}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_GPIOA}  Port=${SPI_GPA0}  Mode=${HIGH}

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
MCP_test
	Log to Console    *** MCP23S17 SPI test
	Config MCP   ${MCP_port_A0}
	Config MCP   ${MCP_port_A1}

Relay Test
	Relay Control  ${RELAY1}  ${ON}
	Relay Control  ${RELAY8}  ${ON}
	Relay Control  ${RELAY1}  ${OFF}
	Relay Control  ${RELAY8}  ${OFF}

	Relay Control  ${RELAY9}  ${ON}
	Relay Control  ${RELAY16}  ${ON}
	Relay Control  ${RELAY9}  ${OFF}
	Relay Control  ${RELAY16}  ${OFF}

#IO 0 Port Test
#    #Define an object for MCP23S17 device 0 port A, GPA0 high 
#    ${MCP_A0_Hi} =    Create Dictionary  Device=${MCP23S17_DEVICE_0}  
#        ...                          	 SPI-addr=${SPI_ADDRESS_0}
#	...    				 Reg=${SPI_GPIOA}
#	...			    	 Port=${SPI_GPA0}
#	...			    	 Mode=${HIGH}
#
##   Set output port high
#    Config MCP   ${MCP_A0_Hi}

