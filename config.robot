Resource  common.robot

*** Variables ***

# Define DAC properties
&{DAC_NO_0}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE1}  Range=${DAC_RANGE_m5V_p5V}  Dac=${DAC0}
&{DAC_NO_1}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE1}  Range=${DAC_RANGE_m5V_p5V}  Dac=${DAC1}
&{DAC_NO_2}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE1}  Range=${DAC_RANGE_0V_p10V}  Dac=${DAC2}
&{DAC_NO_3}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE1}  Range=${DAC_RANGE_m10V_p10V}  Dac=${DAC3}
&{DAC_NO_4}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE0}  Range=${DAC_RANGE_m10V_p10V}  Dac=${DAC4}
&{DAC_NO_5}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE0}  Range=${DAC_RANGE_m10V_p10V}  Dac=${DAC5}
&{DAC_NO_6}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE0}  Range=${DAC_RANGE_m10V_p10V}  Dac=${DAC6}
&{DAC_NO_7}    Device=${DAC61408_DEVICE}  SPI-addr=${NA}  Domain_Range=${DACRANGE0}  Range=${DAC_RANGE_m10V_p10V}  Dac=${DAC7}

# ----------------------------------------------------------------------------------------------------------------------------------

# Define ADC properties
&{AD_NO_0}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_0}
&{AD_NO_1}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_1}
&{AD_NO_2}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_2}
&{AD_NO_3}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_3}
&{AD_NO_4}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_4}
&{AD_NO_5}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_5}
&{AD_NO_6}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_6}
&{AD_NO_7}    Device=${AD4112_DEVICE_0}  SPI-addr=${NA}   Adc=${VIN_7}


# ----------------------------------------------------------------------------------------------------------------------------------

# Define MCP23S17 instance 0, addr 0, port A properties, OUT
&{MCP_00A0}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA0}  Mode=${OUT}
&{MCP_00A1}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA1}  Mode=${OUT}
&{MCP_00A2}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA2}  Mode=${OUT}
&{MCP_00A3}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA3}  Mode=${OUT}
&{MCP_00A4}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA4}  Mode=${OUT}
&{MCP_00A5}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA5}  Mode=${OUT}
&{MCP_00A6}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA6}  Mode=${OUT}
&{MCP_00A7}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA7}  Mode=${OUT}

@{MCP_CONTAINTER1}  &{MCP_00A0}  &{MCP_00A1}  &{MCP_00A2}  &{MCP_00A3}  &{MCP_00A4}  &{MCP_00A5}  &{MCP_00A6}  &{MCP_00A7}


# Define MCP23S17 instance 0, addr 0, port B properties, OUT
&{MCP_00B0}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB0}  Mode=${OUT}
&{MCP_00B1}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB1}  Mode=${OUT}
&{MCP_00B2}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB2}  Mode=${OUT}
&{MCP_00B3}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB3}  Mode=${OUT}
&{MCP_00B4}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB4}  Mode=${OUT}
&{MCP_00B5}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB5}  Mode=${OUT}
&{MCP_00B6}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB6}  Mode=${OUT}
&{MCP_00B7}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB7}  Mode=${OUT}

@{MCP_CONTAINTER2}  &{MCP_00B0}  &{MCP_00B1}  &{MCP_00B2}  &{MCP_00B3}  &{MCP_00B4}  &{MCP_00B5}  &{MCP_00B6}  &{MCP_00B7}


# Define MCP23S17 instance 0, addr 1, port A properties, OUT
&{MCP_01A0}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA0}  Mode=${OUT}
&{MCP_01A1}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA1}  Mode=${OUT}
&{MCP_01A2}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA2}  Mode=${OUT}
&{MCP_01A3}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA3}  Mode=${OUT}
&{MCP_01A4}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA4}  Mode=${OUT}
&{MCP_01A5}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA5}  Mode=${OUT}
&{MCP_01A6}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA6}  Mode=${OUT}
&{MCP_01A7}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRA}   Port=${SPI_GPA7}  Mode=${OUT}

@{MCP_CONTAINTER3}  &{MCP_01A0}  &{MCP_01A1}  &{MCP_01A2}  &{MCP_01A3}  &{MCP_01A4}  &{MCP_01A5}  &{MCP_01A6}  &{MCP_01A7}


# Define MCP23S17 instance 0, addr 1, port B properties, OUT
&{MCP_01B0}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB0}  Mode=${OUT}
&{MCP_01B1}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB1}  Mode=${OUT}
&{MCP_01B2}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB2}  Mode=${OUT}
&{MCP_01B3}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB3}  Mode=${OUT}
&{MCP_01B4}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB4}  Mode=${OUT}
&{MCP_01B5}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB5}  Mode=${OUT}
&{MCP_01B6}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB6}  Mode=${OUT}
&{MCP_01B7}    Device=${MCP23S17_DEVICE_0}  SPI-addr=${MCP23S17_ADDR_1}  Reg=${SPI_IODIRB}   Port=${SPI_GPB7}  Mode=${OUT}

@{MCP_CONTAINTER4}  &{MCP_01B0}  &{MCP_01B1}  &{MCP_01B2}  &{MCP_01B3}  &{MCP_01B4}  &{MCP_01B5}  &{MCP_01B6}  &{MCP_01B7}


# Define MCP23S17 instance 1, addr 0, port A properties, OUT
&{MCP_10A0}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA0}  Mode=${OUT}
&{MCP_10A1}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA1}  Mode=${OUT}
&{MCP_10A2}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA2}  Mode=${OUT}
&{MCP_10A3}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA3}  Mode=${OUT}
&{MCP_10A4}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA4}  Mode=${OUT}
&{MCP_10A5}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA5}  Mode=${OUT}
&{MCP_10A6}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA6}  Mode=${OUT}
&{MCP_10A7}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRA}   Port=${SPI_GPA7}  Mode=${OUT}

@{MCP_CONTAINTER5}  &{MCP_10A0}  &{MCP_10A1}  &{MCP_10A2}  &{MCP_10A3}  &{MCP_10A4}  &{MCP_10A5}  &{MCP_10A6}  &{MCP_10A7}


# Define MCP23S17 instance 1, addr 0, port B properties, OUT
&{MCP_10B0}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB0}  Mode=${OUT}
&{MCP_10B1}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB1}  Mode=${OUT}
&{MCP_10B2}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB2}  Mode=${OUT}
&{MCP_10B3}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB3}  Mode=${OUT}
&{MCP_10B4}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB4}  Mode=${OUT}
&{MCP_10B5}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB5}  Mode=${OUT}
&{MCP_10B6}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB6}  Mode=${OUT}
&{MCP_10B7}    Device=${MCP23S17_DEVICE_1}  SPI-addr=${MCP23S17_ADDR_0}  Reg=${SPI_IODIRB}   Port=${SPI_GPB7}  Mode=${OUT}

@{MCP_CONTAINTER6}  &{MCP_10B0}  &{MCP_10B1}  &{MCP_10B2}  &{MCP_10B3}  &{MCP_10B4}  &{MCP_10B5}  &{MCP_10B6}  &{MCP_10B7}

