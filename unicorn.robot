*** Settings ***
Library   unicorn
Library   Dialogs

Resource  common.robot
Resource  config.robot

*** Variables ***

*** Keywords ***
Invalid Selection
	Log To Console    *** Invalid Selection. Use 'ON' or 'OFF'

Initialize DAC ports
	log to console    *** Configure DAC61408
	Config DAC   ${DAC_NO_0}
	Config DAC   ${DAC_NO_1}
	Config DAC   ${DAC_NO_2}
	Config DAC   ${DAC_NO_3}
	Config DAC   ${DAC_NO_4}
	Config DAC   ${DAC_NO_5}
	Config DAC   ${DAC_NO_6}
	Config DAC   ${DAC_NO_7}

Initialize ADC ports
	log to console    *** Configure AD4112 device 0
	Config AD   ${AD_NO_0}
	Config AD   ${AD_NO_1}
	Config AD   ${AD_NO_2}
	Config AD   ${AD_NO_3}
	Config AD   ${AD_NO_4}
	Config AD   ${AD_NO_5}
	Config AD   ${AD_NO_6}
	Config AD   ${AD_NO_7}

Initialize MCP ports
	log to console    *** Configure MCP23S17

	# Initialize MCP instance 0, addr 0, port A
	:FOR  ${index}  IN RANGE  0  8
	#\	log to console  ${MCP_CONTAINTER1}[${index}]
	\       Config MCP  ${MCP_CONTAINTER1}[${index}]

	## Initialize MCP instance 0, addr 0, port B
	#:FOR  ${index}  IN RANGE  0  8
	##\	log to console  ${MCP_CONTAINTER2}[${index}]
	#\       Config MCP  ${MCP_CONTAINTER2}[${index}]

	## Initialize MCP instance 0, addr 1, port A
	#:FOR  ${index}  IN RANGE  0  8
	##\	log to console  ${MCP_CONTAINTER3}[${index}]
	#\       Config MCP  ${MCP_CONTAINTER3}[${index}]

	## Initialize MCP instance 0, addr 1, port B
	#:FOR  ${index}  IN RANGE  0  8
	##\	log to console  ${MCP_CONTAINTER4}[${index}]
	#\       Config MCP  ${MCP_CONTAINTER4}[${index}]

	## Initialize MCP instance 1, addr 0, port A
	#:FOR  ${index}  IN RANGE  0  8
	##\	log to console  ${MCP_CONTAINTER5}[${index}]
	#\       Config MCP  ${MCP_CONTAINTER5}[${index}]

	## Initialize MCP instance 1, addr 0, port B
	#:FOR  ${index}  IN RANGE  0  8
	##\	log to console  ${MCP_CONTAINTER6}[${index}]
	#\       Config MCP  ${MCP_CONTAINTER6}[${index}]

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
	[Documentation]   24V LED (on Halfbaked board) light comes on/off
	[Arguments]    ${mode}


*** Settings ***
Suite Setup     Initialize Interfaces
#Suite Teardown    Teardown The Suite


*** Test Cases ***
#Main Test
#	Dummy
#	Sleep    2
#
##Chip Enable Test
##	User Test 1

DAC Port test
	Log to Console    *** DAC port test

#AD 0 Port Test
#    log to console    *** ADC 0 test

#IO 0 Port Test
#    Define an object for MCP23S17 device 0 port A, GPA0 high 
#    ${MCP_A0_Hi} =    Create Dictionary  Device=${MCP23S17_DEVICE_0}  
#        ...                          	 SPI-addr=${SPI_ADDRESS_0}
#	...    				 Reg=${SPI_GPIOA}
#	...			    	 Port=${SPI_GPA0}
#	...			    	 Mode=${HIGH}
#
#    Set output port high
#    Config MCP   ${MCP_A0_Hi}
#
#
#    Define an object for MCP23S17 device 0 port A, GPA7 high 
#    ${MCP_A1_Hi} =    Create Dictionary  Device=${MCP23S17_DEVICE_0}  
#        ...                          	 SPI-addr=${SPI_ADDRESS_0}
#	...    				 Reg=${SPI_GPIOA}
#	...			    	 Port=${SPI_GPA7}
#	...			    	 Mode=${HIGH}
#
#    Config MCP   ${MCP_A1_Hi}

AD test
	Log to Console    *** AD test
