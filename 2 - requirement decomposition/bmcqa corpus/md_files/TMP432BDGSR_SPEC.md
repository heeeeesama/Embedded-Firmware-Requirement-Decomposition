# TMP431, TMP432 TMP43x ±1°C Temperature Sensor With Series-R, η-Factor, and Automatic Beta Compensation

## 1 Features

- ±1°C Remote Diode Sensor
- ±1°C Local Temperature Sensor
- Automatic Beta Compensation
- η-Factor Correction
- Programmable Threshold Limits
- Two-Wire, SMBus™ Serial Interface
- Minimum and Maximum Temperature Monitors
- Multiple Interface Addresses
- ALERT/THERM2 Pin Configuration
- Diode Fault Detection

## 2 Applications

- LCD, DLP®, LCOS Projectors
- Servers
- Industrial Controllers
- Central Office Telecom Equipment
- Desktop and Notebook Computers
- Storage Area Networks (SAN)
- Industrial And Medical Equipment
- Processor and FPGA Temperature Monitoring

## 3 Description

The TMP431 and TMP432 are remote temperature
sensor monitors with a built-in local temperature
sensor. The remote temperature sensor diodeconnected transistors are typically low-cost, NPN- or
PNP-type transistors or diodes that are an integral
part of microcontrollers, microprocessors, or FPGAs.
Remote accuracy is ±1°C for multiple device
manufacturers, with no calibration needed. The Two Wire serial interface accepts SMBus write byte, read
byte, send byte, and receive byte commands to
program the alarm thresholds and to read
temperature data.
The TMP43x include beta compensation (correction),
series resistance cancellation, programmable nonideality factor, programmable resolution,
programmable threshold limits, minimum and
maximum temperature monitors, wide remote
temperature measurement range (up to 150°C), and
diode fault detection and temperature alert function.
The TMP431 is available in a VSSOP-8 package and
the TMP432 is available in a VSSOP-10 package.

### Device Information(1)

| PART NUMBER | PACKAGE    | BODY SIZE (NOM)   |
| ----------- | ---------- | ----------------- |
| TMP431      | VSSOP (8)  | 3.00 mm × 3.00 mm |
| TMP432      | VSSOP (10) | 3.00 mm × 3.00 mm |

(1) For all available packages, see the orderable addendum at the end of the data sheet.

### Typical Application Schematics

+5V

| TMP431 | 1       | 2     | DXP | V+ | SCL   | 8 |
| ------ | ------- | ----- | --- | -- | ----- | - |
|        | 3       | DXN   | SDA | 7  | SMBus |   |
|        | 4       | THERM |     | 5  | GND   |   |
| ALERT  | THERM2/ | 6     |     |    |       |   |

One Channel Local

One Channel Remote

Two Channels Remote

## Table of Contents

1. Features .................................................................. 1
2. Applications ........................................................... 1
3. Description ............................................................. 1
4. Revision History..................................................... 2
5. Pin Configuration and Functions ......................... 4
6. Specifications......................................................... 4
7. 1. Absolute Maximum Ratings ..................................... 4
2. ESD Ratings.............................................................. 5
3. Recommended Operating Conditions....................... 5
4. Thermal Information .................................................. 5
5. Electrical Characteristics........................................... 6
6. Timing Requirements ................................................ 7
7. Typical Characteristics .............................................. 8

Parametric Measurement Information ............... 10
8. Detailed Description ............................................ 11
9. 1. Overview ................................................................. 11
2. Functional Block Diagram ....................................... 11
3. Feature Description................................................. 12

Device Functional Modes........................................ 14
10. Programming........................................................... 15
11. Register Maps ......................................................... 20
12. Application and Implementation ........................ 32
13. 1. Application Information............................................ 32
2. Typical Application ................................................. 32

Power Supply Recommendations ..................... 35
14. Layout................................................................... 35
15. 1. Layout Guidelines ................................................. 35
2. Layout Examples................................................... 36

Device and Documentation Support ................. 38

12.1 Related Links ........................................................ 38
12.2 Community Resources.......................................... 38
12.3 Trademarks ........................................................... 38
12.4 Electrostatic Discharge Caution............................ 38
12.5 Glossary ................................................................ 38
13 Mechanical, Packaging, and Orderable
Information ........................................................... 38

## 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

Changes from Revision G (December 2015) to Revision H

- Changed row 1B in Table 4 .................................................................. 22
- Changed 7th paragraph of TMP432 Status Register section ............... 26
- Changed Open Status Register section ................................................ 31
- Added last sentence to High Limit Status Register section................... 31
- Added last sentence to Low Limit Status Register section .................. 31

Changes from Revision F (August 2013) to Revision G

- Added ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information section ................... 1
- Changed the Timing Requirements table with new I²C data. Updated affected values throughout the data sheet ............. 7

Changes from Revision E (December 2012) to Revision F

- Added five new register descriptions..................................................... 31

Changes from Revision D (November 2012) to Revision E

- Changed all MSOP-10 to VSSOP-10 throughout document................... 1

Changes from Revision C (February 2011) to Revision D

- Changed all MSOP-8 to VSSOP-8 throughout document....................... 1

Changes from Revision B (April 2010) to Revision C

- Revised Figure 14 .. 16
- Updated Figure 15.. 17
- Changed Figure 16. 18
- Revised Figure 17 .. 18
- Updated Serial Bus Address section for TMP431C, TMP431D device versions ................................................................. 19
- Added footnote (3) to TMP431 Register Map........................................ 21
- Revised information about power-on reset value of THERM limit registers in Limit Registers section ............................... 24

Changes from Revision A (November 2009) to Revision B

- Corrected Equation 7............................................................................. 33

Changes from Original (September 2009) to Revision A

- Changed device status for TMP432 throughout document ..................... 1
- Corrected bit D6 value in Configuration Register 1 in TMP431 Register Map..................................................................... 21

## 5 Pin Configuration and Functions

|       | DGK Package |      |              |      |      | DGS Package  |      |
| ----- | ----------- | ---- | ------------ | ---- | ---- | ------------ | ---- |
|       | 8-Pin VSSOP |      |              |      |      | 10-Pin VSSOP |      |
| V+    | 1           | 8    | SCL          |      |      |              |      |
| DXP   | 2           |      |              |      |      | 9            | SDA  |
| DXN   | 3           | 6    | ALERT THERM2 |      |      |              |      |
| THERM | 4           | 5    | GND          |      |      |              |      |

### Pin Functions

| NAME         | TMP432 | TMP431 | I/O  | DESCRIPTION                                                  |
| ------------ | ------ | ------ | ---- | ------------------------------------------------------------ |
| ALERT/THERM2 | 8      | 6      | O    | Digital alert (reconfigurable as second thermal flag), active low, open-drain; requires pullup resistor to V+ |
| DXN          | —      | 3      | I    | Analog negative connection to remote temperature sensor      |
| DXN1         | 3      | —      | I    | Analog channel 1 negative connection to remote temperature sensor |
| DXN2         | 5      | —      | I    | Analog channel 2 negative connection to remote temperature sensor |
| DXP          | —      | 2      | I    | Analog positive connection to remote temperature sensor      |
| DXP1         | 2      | —      | I    | Analog channel 1 positive connection to remote temperature sensor |
| DXP2         | 4      | —      | I    | Analog channel 2 positive connection to remote temperature sensor |
| GND          | 6      | 5      | —    | Ground                                                       |
| SCL          | 10     | 8      | I    | Digital serial clock line for SMBus, open-drain; requires pullup resistor to V+ |
| SDA          | 9      | 7      | I/O  | Bidirectional digital, serial data line for SMBus, open-drain; requires pullup resistor to V+ |
| THERM        | 7      | 4      | O    | Digital, thermal flag, active low, open-drain; requires pullup resistor to V+ |
| V+           | 1      | 1      | —    | Power supply, positive (2.7 V to 5.5 V)                      |

## 6 Specifications

### 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted)(1)

|                           |                        | MIN  | MAX      | UNIT |
| ------------------------- | ---------------------- | ---- | -------- | ---- |
| Power supply, VS          |                        |      | 7        | V    |
| TMP431 input voltage      | Pins 2, 3, and 6       | –0.5 | V+ + 0.5 | V    |
|                           | Pins 4, 7, and 8       | –0.5 | 7        | V    |
| TMP432 input voltage      | Pins 2, 3, 4, 5, and 8 | –0.5 | V+ + 0.5 | V    |
|                           | Pins 7, 9, and 10      | –0.5 | 7        | V    |
| Input current             |                        |      | 10       | mA   |
| Operating temperature     |                        | –55  | 127      | °C   |
| Junction temperature, TJ  |                        |      | 150      | °C   |
| Storage temperature, Tstg |                        | –60  | 130      | °C   |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

### 6.2 ESD Ratings

|                                |                                                              | VALUE | UNIT |
| ------------------------------ | ------------------------------------------------------------ | ----- | ---- |
| V(ESD) Electrostatic discharge | Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1)       | ±4000 | V    |
|                                | Charged-device model (CDM), per JEDEC specification JESD22-C101(2) | ±1000 |      |
|                                | Machine model (MM)                                           | ±200  |      |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.

(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

### 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|                                    | MIN  | NOM  | MAX  | UNIT |
| ---------------------------------- | ---- | ---- | ---- | ---- |
| Supply voltage                     | 2.7  | 3.3  | 5.5  | V    |
| Operating free-air temperature, TA | –40  |      | 125  | ºC   |

### 6.4 Thermal Information

| THERMAL METRIC(1)   |                                                        | TMP431 DGK (VSSOP) 8 PINS | TMP432 DGS (VSSOP)  10 PINS | UNIT |
| ------------------- | ------------------------------------------------------ | ------------------------- | --------------------------- | ---- |
| DGK (VSSOP) 8 PINS  | RθJA Junction-to-ambient thermal resistance            | 168.2                     | 164.6                       | °C/W |
| DGS (VSSOP) 10 PINS | RθJC(top) Junction-to-case (top) thermal resistance    | 59.7                      | 39                          | °C/W |
|                     | RθJB Junction-to-board thermal resistance              | 90.1                      | 85.9                        | °C/W |
|                     | ψJT Junction-to-top characterization parameter         | 7.7                       | 1.6                         | °C/W |
|                     | ψJB Junction-to-board characterization parameter       | 88.4                      | 84.2                        | °C/W |
|                     | RθJC(bot) Junction-to-case (bottom) thermal resistance | N/A                       | N/A                         | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report, SPRA953.

### 6.5 Electrical Characteristics

at TA = –40°C to 125°C and V+ = 2.7 V to 5.5 V (unless otherwise noted)

| PARAMETER                                             | TEST CONDITIONS                                          | MIN  | TYP      | MAX  | UNIT |
| ----------------------------------------------------- | -------------------------------------------------------- | ---- | -------- | ---- | ---- |
| TEMPERATURE ERROR                                     |                                                          |      |          |      |      |
| TELOCAL Local temperature sensor                      | TA = –40°C to 125°C                                      |      | ±1.25    | ±2.5 | °C   |
|                                                       | TA = 0°C to 100°C, V+ = 3.3 V                            |      | ±0.25    | ±1   |      |
| TEREMOTE Remote temperature sensor (1)                | TA = 0°C to 100°C, TDIODE = –40°C to 150°C, V+ = 3.3 V   |      | ±0.25    | ±1   | °C   |
|                                                       | TA = –40°C to 100°C, TDIODE = –40°C to 150°C, V+ = 3.3 V |      | ±0.5     | ±1.5 |      |
|                                                       | TA = –40°C to 125°C, TDIODE = –40°C to 150°C             |      | ±3       | ±5   |      |
| vs supply (local, remote)                             | V+ = 2.7 V to 5.5 V                                      |      | ±0.2     | ±0.5 | °C/V |
| TEMPERATURE MEASUREMENT CONVERSION TIME (PER CHANNEL) |                                                          |      |          |      |      |
| Local channel                                         |                                                          | 12   | 15       | 17   | ms   |
| Remote channel beta correction enabled (2)            | RC = 1                                                   | 97   | 126      | 137  | ms   |
|                                                       | RC = 0                                                   | 36   | 47       | 52   | ms   |
| Remote channel,beta correction disabled (3)           | RC = 1                                                   | 72   | 93       | 100  | ms   |
|                                                       | RC = 0                                                   | 33   | 44       | 47   | ms   |
| TEMPERATURE MEASUREMENT RESOLUTION                    |                                                          |      |          |      |      |
| Local channel                                         |                                                          |      | 12       |      | Bits |
| Remote channel                                        |                                                          |      | 12       |      | Bits |
| TEMPERATURE MEASUREMENT REMOTE SENSOR SOURCE CURRENTS |                                                          |      |          |      |      |
| High                                                  | Series resistance (beta correction) (4)                  |      | 120      |      | μA   |
| Medium-high                                           |                                                          |      | 60       |      | μA   |
| Medium-low                                            |                                                          |      | 12       |      | μA   |
| Low                                                   |                                                          |      | 6        |      | μA   |
| η  Remote transistor ideality factor                  | TMP43x optimized ideality factor                         |      | 1.000(2) |      |      |
|                                                       |                                                          |      | 1.008(3) |      |      |
| β  Beta correction range                              |                                                          | 0.1  |          | 27   |      |
| SMBus INTERFACE                                       |                                                          |      |          |      |      |
| VIH  Logic input high voltage  (SCL, SDA)             |                                                          | 2.1  |          |      | V    |
| VIL  Logic input low voltage (SCL, SDA)               |                                                          |      |          | 0.8  | V    |
| Hysteresis                                            |                                                          |      | 500      |      | mV   |
| SMBus output low sink current                         |                                                          | 6    |          |      | mA   |
| VOL SDA output low voltage                            | IOUT = 6 mA                                              |      | 0.15     | 0.4  | V    |
| Logic input current                                   | 0 ≤ VIN ≤ 6 V                                            | –1   |          | 1    | μA   |
| SMBus input capacitance (SCL, SDA)                    |                                                          |      | 3        |      | pF   |
| SMBus clock frequency                                 |                                                          |      |          | 3.4  | MHz  |
| SMBus timeout                                         |                                                          | 25   | 32       | 35   | ms   |
| SCL falling edge to SDA valid time                    |                                                          |      |          | 1    | μs   |
| DIGITAL OUTPUTS                                       |                                                          |      |          |      |      |
| VOL Output low voltage                                | IOUT = 6 mA                                              |      | 0.15     | 0.4  | V    |
| IOH High-level output leakage current                 | VOUT = V+                                                |      | 0.1      | 1    | μA   |
| ALERT/THERM2 output low sink current                  | ALERT/THERM2 forced to 0.4 V                             | 6    |          |      | mA   |
| THERM output low sink current                         | THERM2 forced to 0.4 V                                   | 6    |          |      | mA   |

(1) Tested with less than 5-Ω effective series resistance and 100-pF differential input capacitance. TA is the ambient temperature of the

(2) TMP43x. TDIODE is the temperature at the remote diode sensor. Beta correction configuration set to 1000 and sensor is GND collector-connected (PNP collector to ground).

(3) Beta correction configuration set to 0111 or sensor is diode-connected (base shorted to collector).

(4) If beta correction is disabled (0111), then up to 1-kΩ of series line resistance is cancelled; if beta correction is enabled (1xxx), up to 300 Ω is cancelled.

### Electrical Characteristics (continued)

at TA = –40°C to 125°C and V+ = 2.7 V to 5.5 V (unless otherwise noted)

| PARAMETER    |                             | TEST CONDITIONS                                | MIN  | TYP  | MAX  | UNIT |
| ------------ | --------------------------- | ---------------------------------------------- | ---- | ---- | ---- | ---- |
| POWER SUPPLY |                             |                                                |      |      |      |      |
| V+           | Specified voltage range     |                                                | 2.7  |      | 5.5  | V    |
| IQ           | Quiescent current           | 0.0625 conversions per second, V+ = 3.3 V      |      | 35   | 45   | μA   |
|              |                             | Eight conversions per second, V+ = 3.3 V (5)   |      | 0.7  | 1    | mA   |
|              |                             | Serial bus inactive, shutdown mode             |      | 3    | 10   | μA   |
|              |                             | Serial bus active, fS = 400 kHz, shutdown mode |      | 90   |      | μA   |
|              |                             | Serial bus active, fS = 3.4 MHz, shutdown mode |      | 350  |      |      |
| UVLO         | Undervoltage lockout        |                                                | 2.3  | 2.4  | 2.6  | V    |
| POR          | Power-on reset threshold    |                                                |      | 1.6  | 2.3  | V    |
|              | Specified temperature range |                                                | –40  |      | 125  | °C   |
|              | Storage temperature range   |                                                | –60  |      | 130  | °C   |

(5) Beta correction disabled.

### 6.6 Timing Requirements (1)

|          |                                                              | FAST MODE min | FAST MODE max | HIGH-SPEED MODE min | HIGH-SPEED MODE max | UNIT |
| -------- | ------------------------------------------------------------ | ------------- | ------------- | ------------------- | ------------------- | ---- |
| f(SCL)   | SCL operating frequency V+                                   | 0.001         | 0.4           | 0.001               | 2.5                 | MHz  |
| t(BUF)   | Bus free time between STOP and START condition               | 600           |               | 160                 |                     | ns   |
| t(HDSTA) | Hold time after repeated START condition. After this period, the first clock is generated. | 100           |               | 100                 |                     | ns   |
| t(SUSTA) | Repeated START condition setup time                          | 100           |               | 100                 |                     | ns   |
| t(SUSTO) | STOP condition setup time                                    | 100           |               | 100                 |                     | ns   |
| t(HDDAT) | Data hold time                                               | 0 (2)         | 900           | 0 (3)               | 80                  | ns   |
| t(SUDAT) | Data setup time                                              | 100           |               | 25                  |                     | ns   |
| t(LOW)   | SCL clock LOW period V+                                      | 1300          |               | 265                 |                     | ns   |
| t(HIGH)  | SCL clock HIGH period                                        | 600           |               | 60                  |                     | ns   |
| tFD      | Data fall time                                               |               | 300           |                     | 160                 | ns   |
| tRC      | Clock rise time                                              |               | 300           |                     | 40                  | ns   |
|          | Clock rise time SCLK ≤ 100 kHz                               |               | 1000          |                     |                     |      |
| tFC      | Clock fall time                                              |               | 300           |                     | 40                  | ns   |

(1) Values based on a statistical analysis of a one-time sample of devices. Minimum and maximum values are not specified and not production tested.

(2) For cases with a fall time of SCL less than 20 ns or where the rise time or fall time of SDA is less than 20 ns, the hold time must be greater than 20 ns.

(3) For cases with a fall time of SCL less than 10 ns or where the rise or fall time of SDA is less than 10 ns, the hold time must be greater than 10 ns.

### 6.7 Typical Characteristics

At TA = 25°C and V+ = 3.3 V, unless otherwise noted.

|                               | 3                           | 3                                                         |    |    |    |     |     |     |
| ----------------------------- | --------------------------- | --------------------------------------------------------- | -- | -- | -- | --- | --- | --- |
| Remote Temperature Error (°C) | 2                           | 2                                                         |    |    |    |     |     |     |
| Local Temperature Error (°C)  |                             |                                                           |    |    |    |     |     |     |
| 1                             | 1                           |                                                           |    |    |    |     |     |     |
| 0                             | 0                           |                                                           |    |    |    |     |     |     |
| -1                            | -1                          |                                                           |    |    |    |     |     |     |
| -2                            | Beta Compensation Disabled. | GND Collector-Connected Transistor with n-Factor = 1.008. |    |    |    |     |     |     |
| -3                            | -3                          |                                                           |    |    |    |     |     |     |
| -50                           | -25                         | 0                                                         | 25 | 50 | 75 | 100 | 125 |     |
|                               | -50                         | -25                                                       | 0  | 25 | 50 | 75  | 100 | 125 |

#### Figure 1. Remote Temperature Error vs Temperature

#### Figure 2. Local Temperature Error vs Temperature

|                               | 150  |                 | 700    |       |      |     |    |   |   |   |
| ----------------------------- | ---- | --------------- | ------ | ----- | ---- | --- | -- | - | - | - |
| Remote Temperature Error (°C) | 100  | RGND (Low Beta) |        |       |      |     |    |   |   |   |
|                               | 50   | RGND            | (mA)   |       |      |     |    |   |   |   |
|                               | 0    |                 | I Q    | 300   |      |     |    |   |   |   |
|                               | -50  | RVs             | 200    |       |      |     |    |   |   |   |
|                               | -100 | RVs (Low Beta)  | 100    |       |      |     |    |   |   |   |
|                               | -150 |                 | 0      |       |      |     |    |   |   |   |
|                               | 0    | 5               | 10     | 15    | 20   | 25  | 30 |   |   |   |
|                               |      |                 | 0.0625 | 0.125 | 0.25 | 0.5 | 1  | 2 | 4 | 8 |

#### Figure 3. Remote Temperature Error vs Leakage Resistance

#### Figure 4. Quiescent Current vs Conversion Rate

| 500 |      |      |     | 4.0 |     |     |     |     |     |     |
| --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| 450 |      |      |     | 3.5 |     |     |     |     |     |     |
| 400 |      |      |     | 3.0 |     |     |     |     |     |     |
| 350 |      |      |     |     |     |     |     |     |     |     |
| 300 | (mA) |      | 2.5 |     |     |     |     |     |     |     |
| 250 |      |      | m   |     |     |     |     |     |     |     |
| 200 |      | I Q  |     |     |     |     |     |     |     |     |
| 150 |      |      |     | 1.0 |     |     |     |     |     |     |
|     |      | 100  |     | 0.5 |     |     |     |     |     |     |
| 50  |      | 0    |     |     |     |     |     |     |     |     |
| 1k  | 10k  | 100k | 1M  | 10M |     |     |     |     |     |     |
|     |      |      |     | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 | 5.5 |

#### Figure 5. Shutdown Quiescent Current vs SCL Clock Frequency

#### Figure 6. Shutdown Quiescent Current vs Supply Voltage

### Typical Characteristics (continued)

At TA = 25°C and V+ = 3.3 V, unless otherwise noted.

|                               | GND Collector-Connected Transistor, 2N3906 (PNP)(1)(2) | Remote Temperature Error (°C) |     |   |   |
| ----------------------------- | ------------------------------------------------------ | ----------------------------- | --- | - | - |
| Remote Temperature Error (°C) |                                                        |                               |     |   |   |
| 3                             |                                                        | 2.5                           |     |   |   |
|                               | 2                                                      | 2.0                           |     |   |   |
|                               |                                                        | 1                             | 1.5 |   |   |
|                               |                                                        | 0                             | 1.0 |   |   |
| -1                            |                                                        | 0.5                           |     |   |   |
| -2                            | 0                                                      |                               |     |   |   |
| -3                            |                                                        | -0.5                          |     |   |   |
| -4                            |                                                        | -1.0                          |     |   |   |
| -5                            |                                                        | -1.5                          |     |   |   |
| -6                            |                                                        | -2.0                          |     |   |   |
| -7                            |                                                        | -2.5                          |     |   |   |

NOTES (1): Temperature offset is the result of h-factor being automatically set to 1.000.

Approximate h-factor of 2N3906 is 1.008.

(2) See Figure 11 for schematic configuration.

#### Figure 7. Remote Temperature Error vs Series Resistance

#### Figure 8. Remote Temperature Error vs Series Resistance (Low-Beta Transistor)

|                               | GND Collector-Connected Transistor (Auto) | Remote Temperature Error (°C) |   |   |   |   |
| ----------------------------- | ----------------------------------------- | ----------------------------- | - | - | - | - |
| Remote Temperature Error (°C) |                                           |                               |   |   |   |   |
|                               |                                           |                               |   |   | 3 | 2 |
|                               |                                           |                               |   |   | 1 | 1 |
|                               |                                           |                               |   | 0 | 0 |   |
| -1                            | -1                                        |                               |   |   |   |   |
| -2                            | -2                                        |                               |   |   |   |   |
| -3                            | -3                                        |                               |   |   |   |   |

NOTE: See Figure 12 for schematic configuration.

#### Figure 9. Remote Temperature Error vs Differential Capacitance

#### Figure 10. Remote Temperature Error vs Differential Capacitance With 45-nm CPU

## 7 Parametric Measurement Information

### Figure 11. Series Resistance Configuration

(a) GND Collector-Connected Transistor

| RS1 |   |
| --- | - |
| RS2 |   |

(b) Diode-Connected Transistor

| RS1 | DXP | DXN |
| --- | --- | --- |
| RS2 |     |     |

(1) The total series resistance RS = RS1 + RS2 must be less than 1 kΩ; see Filtering.

### Figure 12. Differential Capacitance Configuration

(a) GND Collector-Connected Transistor

| DXP | CDIFF(1) | DXN |
| --- | -------- | --- |

(b) Diode-Connected Transistor

| DXP | CDIFF(1) | DXN |
| --- | -------- | --- |

(1) CDIFF must be less than 2200 pF; see Filtering.

## 8    Detailed Description

### 8.1  Overview

The TMP431 (two-channel) and TMP432 (three-channel) are digital temperature sensors that combine a local die
temperature measurement channel and a remote junction temperature measurement channel in a single
VSSOP-8 (TMP431) or VSSOP-10 (TMP432) package. They are Two-Wire- and SMBus interface-compatible
and are specified over a temperature range of –40°C to 125°C. The TMP43x contain multiple registers for
holding configuration information, temperature measurement results, temperature comparator maximum and
minimum limits, and status information. User-programmed high and low temperature limits stored in the TMP43x
can be used to trigger an overtemperature and undertemperature alarm (ALERT) on local and remote
temperatures. Additional thermal limits can be programmed into the TMP43x and used to trigger another flag
(THERM) that can be used to initiate a system response to rising temperatures.

For proper remote temperature sensing operation, the TMP431 requires only a transistor connected between
DXP and DXN; the TMP432 requires transistors connected between DXP1 and DXN1, and between DXP2 and
DXN2. The SCL and SDA interface pins require pullup resistors as part of the communication bus; ALERT and THERM
are open-drain outputs that also need pullup resistors. ALERT and THERM can be shared with other devices if
desired for a wired-OR implementation. TI recommends a 0.1-μF power-supply bypass capacitor for good local
bypassing.

### 8.2  Functional Block Diagram

|          V+         |                  |                          |
| :-----------------: | :--------------: | ------------------------ |
|  Voltage Regulator  |   Register Bank  | Oscillator               |
|         SCL         | Serial Interface | Current Sources          |
|         SDA         |   Control Logic  |                          |
|     ALERT/THERM2    |                  | DXP                      |
| Signal Conditioning |        ADC       | DXN                      |
|        THERM        |                  | Local Temperature Sensor |
|         GND         |                  |                          |

### 8.3 Feature Description

#### 8.3.1 Temperature Measurement Data

Temperature measurement data are taken over a default range of 0°C to 127°C for both local and remote locations. However, measurements from –55°C to 150°C can be made both locally and remotely by reconfiguring the TMP43x for the extended temperature range, as described in this section. Temperature data resulting from conversions within the default measurement range are represented in binary form, as shown in Table 1, Standard Binary column. Note that any temperature below 0°C results in a data value of zero (00h). Likewise, temperatures above 127°C result in a value of 127 (7Fh). The device can be set to measure over an extended temperature range by changing bit 2 of Configuration Register 1 from low to high. The change in measurement range and data format from standard binary to extended binary occurs at the next temperature conversion. For data captured in the extended temperature range configuration, an offset of 64 (40h) is added to the standard binary value, as shown in Table 1, Extended Binary column. This configuration allows measurement of temperatures as low as –64°C, and as high as 191°C; however, most temperature-sensing diodes only measure with the range of –55°C to 150°C.

Additionally, the TMP43x are rated only for ambient local temperatures ranging from –40°C to 125°C. Parameters in Absolute Maximum Ratings must be observed.

Both local and remote temperature data use two bytes for data storage. The high byte stores the temperature with 1°C resolution. The second or low byte stores the decimal fraction value of the temperature and allows a higher measurement resolution; see Table 2. The measurement resolution for both the local and remote channels is 0.0625°C, and cannot be adjusted.

##### Table 1. Temperature Data Format (Local and Remote Temperature High Bytes)

|           | **LOCAL/REMOTE TEMPERATURE REGISTER HIGH BYTE VALUE (1°C RESOLUTION)** |         |                               |         |
| :-------- | :----------------------------------------------------------- | :------ | :---------------------------- | :------ |
| TEMP (°C) | STANDARD BINARY<sup>(1)</sup>                                |         | EXTENDED BINARY<sup>(2)</sup> |         |
|           | **Binary**                                                   | **HEX** | **Binary**                    | **HEX** |
| **-64**   | 0000 0000                                                    | 00      | 0000 0000                     | 00      |
| **-50**   | 0000 0000                                                    | 00      | 0000 1110                     | 0E      |
| **-25**   | 0000 0000                                                    | 00      | 0010 0111                     | 27      |
| **0**     | 0000 0000                                                    | 00      | 0100 0000                     | 40      |
| **1**     | 0000 0001                                                    | 01      | 0100 0001                     | 41      |
| **5**     | 0000 0101                                                    | 05      | 0100 0101                     | 45      |
| **10**    | 0000 1010                                                    | 0A      | 0100 1010                     | 4A      |
| **25**    | 0001 1001                                                    | 19      | 0101 1001                     | 59      |
| **50**    | 0011 0010                                                    | 32      | 0111 0010                     | 72      |
| **75**    | 0100 1011                                                    | 4B      | 1000 1011                     | 8B      |
| **100**   | 0110 0100                                                    | 64      | 1010 0100                     | A4      |
| **125**   | 0111 1101                                                    | 7D      | 1011 1101                     | BD      |
| **127**   | 0111 1111                                                    | 7F      | 1011 1111                     | BF      |
| **150**   | 0111 1111                                                    | 7F      | 1101 0110                     | D6      |
| **175**   | 0111 1111                                                    | 7F      | 1110 1111                     | EF      |
| **191**   | 0111 1111                                                    | 7F      | 1111 1111                     | FF      |

<sup>(1)</sup> Standard Binary  
<sup>(2)</sup> Extended Binary

(1) Resolution is 1°C per count. Negative numbers are represented in twos complement format.

(2) Resolution is 1°C per count. All values are unsigned with a –64°C offset.

##### Table 2. Decimal Fraction Temperature Data Format (Local and Remote Temperature Low Bytes)

|           | TEMPERATURE REGISTER LOW BYTE VALUE (0.0625°C RESOLUTION)(1) |      |
| --------- | ------------------------------------------------------------ | ---- |
| TEMP (°C) | STANDARD AND EXTENDED BINARY                                 | HEX  |
| 0         | 0000 0000                                                    | 00   |
| 0.0625    | 0001 0000                                                    | 10   |
| 0.1250    | 0010 0000                                                    | 20   |
| 0.1875    | 0011 0000                                                    | 30   |
| 0.2500    | 0100 0000                                                    | 40   |
| 0.3125    | 0101 0000                                                    | 50   |
| 0.3750    | 0110 0000                                                    | 60   |
| 0.4375    | 0111 0000                                                    | 70   |
| 0.5000    | 1000 0000                                                    | 80   |
| 0.5625    | 1001 0000                                                    | 90   |
| 0.6250    | 1010 0000                                                    | A0   |
| 0.6875    | 1011 0000                                                    | B0   |
| 0.7500    | 1100 0000                                                    | C0   |
| 0.8125    | 1101 0000                                                    | D0   |
| 0.8750    | 1110 0000                                                    | E0   |
| 0.9375    | 1111 0000                                                    | F0   |

(1) Resolution is 0.0625°C per count. All possible values are shown.

#### 8.3.2 Beta Compensation

Previous generations of remote junction temperature sensors were operated by controlling the emitter current of the sensing transistor. However, examination of the physics of a transistor shows that VBE is actually a function of the collector current. If beta is independent of the collector current, then VBE can be calculated from the emitter current. In earlier generations of processors that contained PNP transistors connected to these temperature sensors, controlling the emitter current provided acceptable temperature measurement results. At 90-nm process geometry and below, however, the beta factor continues to decrease and the premise that it is independent of collector current becomes less certain.

To manage this increasing temperature measurement error, the TMP43x control the collector current instead of the emitter current. The TMP43x automatically detect and choose the correct range depending on the beta factor of the external transistor. This auto-ranging is performed at the beginning of each temperature conversion in order to correct for any changes in the beta factor as a result of temperature variation. The device can operate a PNP transistor with a beta factor as low as 0.1. See Beta Compensation Configuration Register for further information.

#### 8.3.3 Series Resistance Cancellation

Series resistance in an application circuit that typically results from printed circuit-board (PCB) trace resistance and remote line length is automatically cancelled by the TMP43x, preventing what would otherwise result in a temperature offset. A total of up to 1-kΩ of series line resistance is cancelled by the TMP43x if beta correction is disabled and up to 300 Ω of series line resistance is cancelled if beta correction is enabled, eliminating the need for additional characterization and temperature offset correction. See Figure 7 and Figure 8 for details on the effects of series resistance on sensed remote temperature error.

#### 8.3.4 Differential Input Capacitance

The TMP43x can tolerate differential input capacitance of up to 2200 pF with minimal change in temperature error. The effect of capacitance on sensed remote temperature error is illustrated in Figure 9 and Figure 10. See Filtering for suggested component values where filtering unwanted coupled signals is needed.

Documentation Feedback  13

Product Folder Links: TMP431 TMP432
SBOS441H – SEPTEMBER 2009 – REVISED MARCH 2016 www.ti.com

#### 8.3.5  Filtering

Remote junction temperature sensors are usually implemented in noisy environments. Noise is frequently generated by fast digital signals and if not filtered properly can induce errors that corrupt temperature measurements. The TMP43x have a built-in 65-kHz filter on the inputs of DXP and DXN to minimize the effects of noise. However, a differential low-pass filter can help attenuate unwanted coupled signals. Exact component values are application-specific. TI also recommends that the capacitor value remains from 0 pF to 2200 pF with a series resistance less than 1 kΩ.

#### 8.3.6  Sensor Fault

The TMP43x can sense a fault at the DXP input that results from an incorrect diode connection or an open circuit. The detection circuitry consists of a voltage comparator that trips when the voltage at DXP exceeds (V+) – 0.6 V (typical). The comparator output is continuously checked during a conversion. If a fault is detected, the last valid measured temperature is used for the temperature measurement result, the OPEN bit (Status Register, bit 2) is set high, and, if the alert function is enabled, ALERT asserts low.

When not using the remote sensor with the TMP43x, the DXP and DXN inputs must be connected together to prevent meaningless fault warnings.

#### 8.3.7  THERM and ALERT/THERM2

The TMP43x have two pins dedicated to alarm functions, the THERM and ALERT/THERM2 pins. Both pins are open-drain outputs that each require a pullup resistor to V+. These pins can be wire-ORed together with other alarm pins for system monitoring of multiple sensors. The THERM pin provides a thermal interrupt that cannot be software disabled. The ALERT pin is intended for use as an earlier warning interrupt, and can be software disabled, or masked. The ALERT/THERM2 pin can also be configured for use as THERM2, a second THERM pin (Configuration Register 1: AL/TH bit = 1). The default setting configures pin 6 for the TMP431 and pin 8 for the TMP432 to function as ALERT (AL/TH = 0).

The THERM pin asserts low when either the measured local or remote temperature is outside of the temperature range programmed in the corresponding Local/Remote THERM Limit Register. The THERM temperature limit range can be programmed with a wider range than that of the limit registers, which allows ALERT to provide an earlier warning than THERM. The THERM alarm resets automatically when the measured temperature returns to within the THERM temperature limit range minus the hysteresis value stored in the THERM Hysteresis Register. The allowable values of hysteresis are listed in Table 13. The default hysteresis is 10°C. When the ALERT/THERM2 pin is configured as a second thermal alarm (Configuration Register: bit 7 = x, bit 5 = 1), it functions the same as THERM, but uses the temperatures stored in the Local/Remote Temperature High Limit Registers to set its comparison range.

When ALERT/THERM2 is configured as ALERT (Configuration Register 1: bit 7 = 0, bit 5 = 0), the pin asserts low when either the measured local or remote temperature violates the range limit set by the corresponding Local/Remote Temperature High/Low Limit Registers. This alert function can be configured to assert only if the range is violated a specified number of consecutive times (1, 2, 3, or 4). The consecutive violation limit is set in the Consecutive Alert Register. False alerts that occur as a result of environmental noise can be prevented by requiring consecutive faults. ALERT also asserts low if the remote temperature sensor is open-circuit. When the MASK function is enabled (Configuration Register 1: bit 7 = 1), ALERT is disabled (that is, masked). ALERT resets when the master reads the device address, as long as the condition that caused the alert no longer persists, and the Status Register has been reset.

### 8.4    Device Functional Modes

#### 8.4.1  Shutdown Mode (SD)

The TMP43x shutdown mode allows the user to save maximum power by shutting down all device circuitry other than the serial interface, reducing current consumption to typically less than 3 μA; see Figure 6. Shutdown mode is enabled when the SD bit of the Configuration Register 1 is high; the device shuts down immediately, aborting the current conversion. When SD is low, the device maintains a continuous conversion state.

### Device Functional Modes (continued)

#### 8.4.2 One-Shot Mode

When the TMP43x are in shutdown mode (SD = 1 in the Configuration Register 1), a single conversion on both channels is started by writing any value to the One-Shot Start Register, pointer address 0Fh. This write operation starts one conversion; the TMP43x return to shutdown mode when that conversion completes. The value of the data sent in the write command is irrelevant and is not stored by the TMP43x. When the TMP43x are in shutdown mode, an initial 200 ps is required before a one-shot command can be given. (Note: When a shutdown command is issued, the TMP43x shut down immediately, aborting the current conversion.) This wait time only applies to the 200 ps immediately following shutdown. One-shot commands can be issued without delay thereafter.

### 8.5 Programming

#### 8.5.1 Serial Interface

The TMP43x operate only as slave devices on either the Two-Wire bus or the SMBus. Connections to either bus are made via the open-drain I/O lines, SDA and SCL. The SDA and SCL pins feature integrated spike suppression filters and Schmitt triggers to minimize the effects of input spikes and bus noise. The TMP43x support the transmission protocol for fast (1 kHz to 400 kHz) and high-speed (1 kHz to 2.5 MHz) modes. All data bytes are transmitted MSB first.

#### 8.5.2 Bus Overview

The TMP43x are SMBus interface-compatible. In SMBus protocol, the device that initiates the transfer is called a master, and the devices controlled by the master are slaves. The bus must be controlled by a master device that generates the serial clock (SCL), controls the bus access, and generates the START and STOP conditions. To address a specific device, a START condition is initiated. START is indicated by pulling the data line (SDA) from a high to low logic level when SCL is high. All slaves on the bus shift in the slave address byte, with the last bit indicating whether a read or write operation is intended. During the ninth clock pulse, the slave being addressed responds to the master by generating an Acknowledge and pulling SDA low. Data transfer is then initiated and sent over eight clock pulses followed by an Acknowledge bit. During data transfer SDA must remain stable when SCL is high because any change in SDA when SCL is high is interpreted as a control signal. When all data are transferred, the master generates a STOP condition. STOP is indicated by pulling SDA from low to high when SCL is high.

#### 8.5.3 Timing Diagrams

The TMP43x are Two-Wire and SMBus-compatible. Figure 13 to Figure 17 describe the various operations on the TMP43x. Parameters for Figure 13 are defined in Figure 14. Bus definitions are given below:

- Bus Idle: Both SDA and SCL lines remain high.
- Start Data Transfer: A change in the state of the SDA line from high to low when the SCL line is high defines a START condition. Each data transfer is initiated with a START condition.
- Stop Data Transfer: A change in the state of the SDA line from low to high when the SCL line is high defines a STOP condition. Each data transfer terminates with a STOP or a repeated START condition.
- Data Transfer: The number of data bytes transferred between a START and a STOP condition is not limited and is determined by the master device. The receiver acknowledges the transfer of data.
- Acknowledge: Each receiving device, when addressed, is obliged to generate an Acknowledge bit. A device that acknowledges must pull down the SDA line during the Acknowledge clock pulse in such a way that the SDA line is stable low during the high period of the Acknowledge clock pulse. Setup and hold times must be taken into account. On a master receive, data transfer termination can be signaled by the master generating a Not-Acknowledge on the last byte that has been transmitted by the slave.

### Programming (continued)

#### Figure 13. Two-Wire Timing Diagram

|     | t(LOW)   | tR      | tF       | t(HDSTA) |          |          |
| --- | -------- | ------- | -------- | -------- | -------- | -------- |
| SCL | t(HDSTA) | t(HIGH) | t(SUSTA) | t(SUSTO) | t(HDDAT) | t(SUDAT) |
| SDA | t(BUF)   | P       | S        | S        | P        |          |

#### Figure 14. Two-Wire Timing Diagram for Write Word Format

| 1   | 9        | 1      | 9      |        |                 |   |      |     |    |    |    |    |    |    |    |    |   |
| --- | -------- | ------ | ------ | ------ | --------------- | - | ---- | --- | -- | -- | -- | -- | -- | -- | -- | -- | - |
| SCL |          |        |        |        |                 | ¼ |      |     |    |    |    |    |    |    |    |    |   |
| SDA | 1        | 0      | 0      | 1      | 1               | 0 | 0(1) | R/W | P7 | P6 | P5 | P4 | P3 | P2 | P1 | P0 | ¼ |
|     | Start By | ACK By | ACK By | Master | TMP431A/32A/31C |   |      |     |    |    |    |    |    |    |    |    |   |

Frame 1 Two-Wire Slave Address Byte

Frame 2 Pointer Register Byte

| 1           |             | 9      |    |    |    |    |    |    |         |                 |                 |
| ----------- | ----------- | ------ | -- | -- | -- | -- | -- | -- | ------- | --------------- | --------------- |
| SCL         | (Continued) |        |    |    |    |    |    |    |         |                 |                 |
| SDA         |             | D7     | D6 | D5 | D4 | D3 | D2 | D1 | D0      |                 |                 |
| (Continued) | ACK By      | ACK By |    |    |    |    |    |    | Stop By | TMP431A/32A/31C | TMP431A/32A/31C |

Frame 3 Data Byte 1

Frame 4 Data Byte 2

(1) Slave address 1001100 (TMP431A, 32A, and 31C) shown. Slave address changes for TMP431B, 32B, and 31D. See Mechanical, Packaging, and Orderable Information for more details.

### Programming (continued)

#### Figure 15. Two-Wire Timing Diagram for Single-Byte Read Format

1 9 1 9

SCL

SDA 1 0 0 1 1 0 0(1) R/W P7 P6 P5 P4 P3 P2 P1 P0

Start By ACK By ACK By

Master TMP431A/32A/31C TMP431A/32A/31C

Frame 1 Two-Wire Slave Address Byte Frame 2 Pointer Register Byte

1 9 1 9

SCL

SDA 1 0 0 1 1 0 0(1) R/W D7 D6 D5 D4 D3 D2 D1 D0

Start By ACK By From NACK By

Master TMP431A/32A/31C TMP431A/32A/31C Master(2)

Frame 3 Two-Wire Slave Address Byte Frame 4 Data Byte 1 Read Register

(1) Slave address 1001100 (TMP431A, 32A, and 31C) shown. Slave address changes for TMP431B, 32B, and 31D. See Mechanical, Packaging, and Orderable Information for more details.

(2) Master must leave SDA high to terminate a single-byte read operation.

### Programming (continued)

#### Figure 16. Two-Wire Timing Diagram for Two-Byte Read Format

| SCL                    | SDA | 1                                   | 0 | 0  | 1  | 1  | 0  | 0(1) | R/W | P7 | P6 | P5 | P4 | P3 | P2 | P1 | P0 |
| ---------------------- | --- | ----------------------------------- | - | -- | -- | -- | -- | ---- | --- | -- | -- | -- | -- | -- | -- | -- | -- |
| Start By Master        |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| ACK By TMP431A/32A/31C |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
|                        |     | Frame 1 Two-Wire Slave Address Byte |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| SCL                    | SDA | 1                                   | 0 | 0  | 1  | 1  | 0  | 0(1) | R/W | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 |
| Start By Master        |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| ACK By TMP431A/32A/31C |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| From TMP431A/32A/31C   |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| ACK By Master          |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
|                        |     | Frame 3 Two-Wire Slave Address Byte |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| SCL                    | SDA |                                     |   | D7 | D6 | D5 | D4 | D3   | D2  | D1 | D0 |    |    |    |    |    |    |
| From TMP431A/32A/31C   |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| NACK By Master(2)      |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
| Stop By Master         |     |                                     |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |
|                        |     | Frame 5 Data Byte 2 Read Register   |   |    |    |    |    |      |     |    |    |    |    |    |    |    |    |

(1) Slave address 1001100 (TMP431A, 32A, and 31C) shown. Slave address changes for TMP431B, 32B, and 31D. See Mechanical, Packaging, and Orderable Information for more details.

(2) Master must leave SDA high to terminate a two-byte read operation.

#### Figure 17. Timing Diagram for SMBus ALERT

ALERT

| SCL                    | SDA                                       | 0 | 0                          | 0 | 1 | 1 | 0 | 0 | R/W | 1 | 0 | 0 | 1 | 1 | 0 | 0(1) | Status |
| ---------------------- | ----------------------------------------- | - | -------------------------- | - | - | - | - | - | --- | - | - | - | - | - | - | ---- | ------ |
| Start By Master        |                                           |   |                            |   |   |   |   |   |     |   |   |   |   |   |   |      |        |
| ACK By TMP431A/32A/31C |                                           |   |                            |   |   |   |   |   |     |   |   |   |   |   |   |      |        |
| From TMP431A/32A/31C   |                                           |   |                            |   |   |   |   |   |     |   |   |   |   |   |   |      |        |
| NACK By Master         |                                           |   |                            |   |   |   |   |   |     |   |   |   |   |   |   |      |        |
| Stop By Master         |                                           |   |                            |   |   |   |   |   |     |   |   |   |   |   |   |      |        |
|                        | Frame 1 SMBus ALERT Response Address Byte |   |                            |   |   |   |   |   |     |   |   |   |   |   |   |      |        |
|                        |                                           |   | Frame 2 Slave Address Byte |   |   |   |   |   |     |   |   |   |   |   |   |      |        |

(1) Slave address 1001100 (TMP431A, 32A, and 31C) shown. Slave address changes for TMP431B, 32B, and 31D. See Mechanical, Packaging, and Orderable Information for more details.

### Programming (continued)

#### 8.5.4  Serial Bus Address

To communicate with the TMP43x, the master must first address slave devices via a slave address byte. The slave address byte consists of seven address bits, and a direction bit that indicates the intent of executing a read or write operation.

The address of the TMP431A, 32A, and 31C is 4Ch (1001100b). The address of the TMP431B, 32B, and 31D is 4Dh (1001101b).

#### 8.5.5  Read and Write Operations

Accessing a particular register on the TMP43x is accomplished by writing the appropriate value to the Pointer Register. The value for the Pointer Register is the first byte transferred after the slave address byte with the R/W bit low. Every write operation to the TMP43x require a value for the Pointer Register (see Figure 14).

When reading from the TMP43x, the last value stored in the Pointer Register by a write operation is used to determine which register is read by a read operation. To change the register pointer for a read operation, a new value must be written to the Pointer Register. This transaction is accomplished by issuing a slave address byte with the R/W bit low, followed by the Pointer Register byte. No additional data are required. The master can then generate a START condition and send the slave address byte with the R/W bit high to initiate the read command. See Figure 15 for details of this sequence. If repeated reads from the same register are desired, it is not necessary to continually send the Pointer Register bytes, because the TMP43x retain the Pointer Register value until it is changed by the next write operation. Note that register bytes are sent MSB first, followed by the LSB.

#### 8.5.6  Undervoltage Lockout

The TMP43x sense when the power-supply voltage has reached a minimum voltage level for the ADC to function. The detection circuitry consists of a voltage comparator that enables the ADC after the power supply (V+) exceeds 2.45 V (typical). The comparator output is continuously checked during a conversion. The TMP43x do not perform a temperature conversion if the power supply is not valid. The last valid measured temperature is used for the temperature measurement result.

#### 8.5.7  Timeout Function

The serial interface of the TMP43x resets if either SCL or SDA are held low for 32 ms (typical) between a START and STOP condition. If the TMP43x are holding the bus low, it releases the bus and waits for a START condition.

#### 8.5.8  High-Speed Mode

For the Two-Wire bus to operate at frequencies above 400 kHz, the master device must issue a High-speed mode (Hs-mode) master code (00001XXX) as the first byte after a START condition to switch the bus to high-speed operation. The TMP43x do not acknowledge this byte, but switch the input filters on SDA and SCL and the output filter on SDA to operate in Hs-mode, allowing transfers at up to 2.5 MHz. After the Hs-mode master code has been issued, the master transmits a Two-Wire slave address to initiate a data transfer operation. The bus continues to operate in Hs-mode until a STOP condition occurs on the bus. Upon receiving the STOP condition, the TMP43x switch the input and output filter back to fast-mode operation.

#### 8.5.9  General Call Reset

The TMP43x support reset through the Two-Wire General Call address 00h (0000 0000b). The TMP43x acknowledge the General Call address and respond to the second byte. If the second byte is 06h (0000 0110b), the TMP43x execute a software reset. This software reset restores the power-on reset state to all TMP43x registers, aborts any conversion in progress, and clears the ALERT and THERM pins. The TMP43x take no action in response to other values in the second byte.

Documentation FeedbackSBOS441H – SEPTEMBER 2009 – REVISED MARCH 2016

### Programming (continued)

#### 8.5.10 SMBus Alert Function

The TMP43x support the SMBus Alert function. When pin 6 (for the TMP431) or pin 8 (for the TMP432) is configured as an alert output, the ALERT pin of the TMP43x can be connected as an SMBus Alert signal. When a master detects an alert condition on the ALERT line, the master sends an SMBus Alert command (00011001) on the bus. If the ALERT pin of the TMP43x is active, the devices acknowledge the SMBus Alert command and respond by returning the slave address on the SDA line. The eighth bit (LSB) of the slave address byte indicates whether the temperature exceeding one of the temperature high limit settings or falling below one of the temperature low limit settings caused the alert condition. This bit is high if the temperature is greater than or equal to one of the temperature high limit settings; this bit is low if the temperature is less than one of the temperature low limit settings. See Figure 18 for details of this sequence.

##### Figure 18. SMBus Alert Timing Diagram

THERM Limit and ALERT High Limit

| Measured Temperature | ALERT Low Limit and THERM Limit Hysteresis |
| -------------------- | ------------------------------------------ |
| THERM                | ALERT                                      |
| SMBus ALERT          | Read                                       |
|                      | Read Time                                  |

If multiple devices on the bus respond to the SMBus Alert command, arbitration during the slave address portion of the SMBus Alert command determines which device clears its alert status. If the TMP43x win the arbitration, the ALERT pin becomes inactive at the completion of the SMBus Alert command. If the TMP43x lose the arbitration, the ALERT pin remains active.

### 8.6 Register Maps

The TMP43x contain multiple registers for holding configuration information, temperature measurement results, temperature comparator maximum, minimum, limits, and status information. These registers are described in Figure 19 and in Table 3 for the TMP431, and in Table 4 for the TMP432.

#### Figure 19. Internal Register Structure

Internal Register Structure

| Pointer Register                 |                                        |
| -------------------------------- | -------------------------------------- |
|                                  | Local and Remote Temperature Registers |
| Local and Remote Limit Registers |                                        |
| THERM Hysteresis Register        | SDA                                    |
| Status Register                  | Configuration Register                 |
| Beta Correction Register         | I/O Control                            |
| Conversion Rate Register         |                                        |
| Consecutive Alert Register       |                                        |
| Identification Registers         |                                        |

### Register Maps (continued)

#### Table 3. TMP431 Register Map

| POINTER ADDRESS (HEX) |       | POWER-ON RESET (HEX) | BIT DESCRIPTIONS |       |       |       |       |       |        |       | REGISTER DESCRIPTIONS                     |
| --------------------- | ----- | -------------------- | ---------------- | ----- | ----- | ----- | ----- | ----- | ------ | ----- | ----------------------------------------- |
| READ                  | WRITE |                      | D7               | D6    | D5    | D4    | D3    | D2    | D1     | D0    |                                           |
| 00                    | NA(1) | 00                   | LT11             | LT10  | LT9   | LT8   | LT7   | LT6   | LT5    | LT4   | Local temperature (high byte)             |
| 01                    | NA    | 00                   | RT11             | RT10  | RT9   | RT8   | RT7   | RT6   | RT5    | RT4   | Remote temperature (high byte)            |
| 02                    | NA    | 80                   | BUSY             | LHIGH | LLOW  | RHIGH | RLOW  | OPEN  | RTHRM  | LTHRM | Status register                           |
| 03                    | 09    | 00                   | MASK             | SD    | ALITH | 0     | 0     | RANGE | 0      | 0     | Configuration register 1                  |
| 04                    | 0A    | 07                   | 0                | 0     | 0     | 0     | R3    | R2    | R1     | R0    | Conversion rate register                  |
| 05                    | 0B    | 55                   | LTH11            | LTH10 | LTH9  | LTH8  | LTH7  | LTH6  | LTH5   | LTH4  | Local temperature high limit (high byte)  |
| 06                    | 0C    | 00                   | LTL11            | LTL10 | LTL9  | LTL8  | LTL7  | LTL6  | LTL5   | LTL4  | Local temperature low limit (high byte)   |
| 07                    | 0D    | 55                   | RTH11            | RTH10 | RTH9  | RTH8  | RTH7  | RTH6  | RTH5   | RTH4  | Remote temperature high limit (high byte) |
| 08                    | 0E    | 00                   | RTL11            | RTL10 | RTL9  | RTL8  | RTL7  | RTL6  | RTL5   | RTL4  | Remote temperature low limit (high byte)  |
| NA                    | 0F    | X(2)                 | X                | X     | X     | X     | X     | X     | X      | X     | One-shot start                            |
| 10                    | NA    | 00                   | RT3              | RT2   | RT1   | RT0   | 0     | 0     | 0      | 0     | Remote temperature (low byte)             |
| 13                    | 13    | 00                   | RTH3             | RTH2  | RTH1  | RTH0  | 0     | 0     | 0      | 0     | Remote temperature high limit (low byte)  |
| 14                    | 14    | 00                   | RTL3             | RTL2  | RTL1  | RTL0  | 0     | 0     | 0      | 0     | Remote temperature low limit (low byte)   |
| 15                    | NA    | 00                   | LT3              | LT2   | LT1   | LT0   | 0     | 0     | 0      | 0     | Local temperature (low byte)              |
| 16                    | 16    | 00                   | LTH3             | LTH2  | LTH1  | LTH0  | 0     | 0     | 0      | 0     | Local temperature high limit (low byte)   |
| 17                    | 17    | 00                   | LTL3             | LTL2  | LTL1  | LTL0  | 0     | 0     | 0      | 0     | Local temperature low limit (low byte)    |
| 18                    | 18    | 00                   | NC7              | NC6   | NC5   | NC4   | NC3   | NC2   | NC1    | NC0   | N-factor correction                       |
| 19                    | 19    | 55(3)                | RTHL7            | RTH6  | RTHL5 | RTHL4 | RTHL3 | RTHL2 | RTHL1  | RTHL0 | Remote THERM limit                        |
| 1A                    | 1A    | 1C                   | 0                | 0     | 0     | REN   | LEN   | RC    | 0      | 0     | Configuration register 2                  |
| 1F                    | 1F    | 00                   | 0                | 0     | 0     | 0     | 0     | 0     | RIMASK | LMASK | Channel mask                              |
| 20                    | 20    | 55(3)                | LTHL7            | LTHL6 | LTHL5 | LTHL4 | LTHL3 | LTHL2 | LTHL1  | LTHL0 | Local THERM limit                         |
| 21                    | 21    | 0A                   | TH7              | TH6   | TH5   | TH4   | TH3   | TH2   | TH1    | TH0   | THERM hysteresis                          |
| 22                    | 22    | 70                   | 0                | CTH2  | CTH1  | CTH0  | CALT2 | CALT1 | CALT0  | 0     | Consecutive alert register                |
| 25                    | 25    | 08                   | 0                | 0     | 0     | 0     | BC3   | BC2   | BC1    | BC0   | Beta range register                       |
| NA                    | FC    | 00                   | X(4)             | X     | X     | X     | X     | X     | X      | X     | Software reset                            |
| FD                    | NA    | 31                   | 0                | 0     | 1     | 1     | 0     | 0     | 0      | 1     | TMP431 device ID                          |
| FE                    | NA    | 55                   | 0                | 1     | 0     | 1     | 0     | 1     | 0      | 1     | Manufacturer ID                           |

(1) NA = Not applicable; register is write- or read-only.

(2) X = Indeterminate state.

(3) TMP431C and TMP431D versions have a power-on reset value of 69h.

(4) X = Undefined. Writing any value to this register initiates a software reset; see Software Reset

#### Table 4. TMP432 Register Map

| POINTER ADDRESS |        |                      | BIT DESCRIPTIONS |       |       |       |       |        |        |       |                                            |
| --------------- | ------ | -------------------- | ---------------- | ----- | ----- | ----- | ----- | ------ | ------ | ----- | ------------------------------------------ |
| READ            | WRITE  | POWER-ON RESET (HEX) | D7               | D6    | D5    | D4    | D3    | D2     | D1     | D0    | DESCRIPTIONS                               |
| 00              | NA (1) | 00                   | LT11             | LT10  | LT9   | LT8   | LT7   | LT6    | LT5    | LT4   | Local temperature (high byte)              |
| 01              | NA     | 00                   | RT11             | RT10  | RT9   | RT8   | RT7   | RT6    | RT5    | RT4   | Remote temperature1 (high byte)            |
| 02              | NA     | 80                   | BUSY             | 0     | 0     | HIGH  | LOW   | OPEN   | THERM  | 0     | Status register                            |
| 03              | 09     | 00                   | MASK             | SD    | AL/TH | 0     | 0     | RANGE  | 0      | 0     | Configuration register1                    |
| 04              | 0A     | 07                   | 0                | 0     | 0     | 0     | R3    | R2     | R1     | R0    | Conversion rate register                   |
| 05              | 0B     | 55                   | LTH11            | LTH10 | LTH9  | LTH8  | LTH7  | LTH6   | LTH5   | LTH4  | Local temperature high limit (high byte)   |
| 06              | 0C     | 00                   | LTL11            | LTL10 | LTL9  | LTL8  | LTL7  | LTL6   | LTL5   | LTL4  | Local temperature low limit (high byte)    |
| 07              | 0D     | 55                   | RTH11            | RTH10 | RTH9  | RTH8  | RTH7  | RTH6   | RTH5   | RTH4  | Remote temperature1 high limit (high byte) |
| 08              | 0E     | 00                   | RTL11            | RTL10 | RTL9  | RTL8  | RTL7  | RTL6   | RTL5   | RTL4  | Remote temperature1 low limit (high byte)  |
| NA              | 0F     | X (2)                | X                | X     | X     | X     | X     | X      | X      | X     | One-shot start                             |
| 10              | NA     | 00                   | RT3              | RT2   | RT1   | RT0   | 0     | 0      | 0      | 0     | Remote temperature1 (low byte)             |
| 13              | 13     | 00                   | RTH3             | RTH2  | RTH1  | RTH0  | 0     | 0      | 0      | 0     | Remote temperature1 high limit (low byte)  |
| 14              | 14     | 00                   | RTL3             | RTL2  | RTL1  | RTL0  | 0     | 0      | 0      | 0     | Remote temperature1 low limit (low byte)   |
| 15              | 15     | 55                   | RTH11            | RTH10 | RTH9  | RTH8  | RTH7  | RTH6   | RTH5   | RTH4  | Remote temperature2 high limit (high byte) |
| 16              | 16     | 00                   | RTL11            | RTL10 | RTL9  | RTL8  | RTL7  | RTL6   | RTL5   | RTL4  | Remote temperature2 low limit (high byte)  |
| 17              | 17     | 00                   | RTH3             | RTH2  | RTH1  | RTH0  | 0     | 0      | 0      | 0     | Remote temperature2 high limit (low byte)  |
| 18              | 18     | 00                   | RTL3             | RTL2  | RTL1  | RTL0  | 0     | 0      | 0      | 0     | Remote temperature2 low limit (low byte)   |
| 19              | 19     | 55                   | RTHL7            | RTHL6 | RTHL5 | RTHL4 | RTHL3 | RTHL2  | RTHL1  | RTHL0 | Remote therm limit                         |
| 1A              | 1A     | 55                   | RTHL7            | RTHL6 | RTHL5 | RTHL4 | RTHL3 | RTHL2  | RTHL1  | RTHL0 | Remote2 therm limit                        |
| 1B              | 1B     | 00                   | 0                | 0     | 0     | 0     | 0     | R2OPEN | R1OPEN | 0     | Open status                                |
| 1F              | 1F     | 00                   | 0                | 0     | 0     | 0     | 0     | R2MASK | R1MASK | LMASK | Channel mask                               |
| 20              | 20     | 55                   | LTHL7            | LTHL6 | LTHL5 | LTHL4 | LTHL3 | LTHL2  | LTHL1  | LTHL0 | Local therm limit                          |
| 21              | 21     | 0A                   | TH7              | TH6   | TH5   | TH4   | TH3   | TH2    | TH1    | TH0   | Therm limit hysteresis                     |
| 22              | 22     | 70                   | 0                | CTH2  | CTH1  | CTH0  | CALT2 | CALT1  | CALT0  | 0     | Consecutive alert register                 |
| 23              | NA     | 00                   | RT11             | RT10  | RT9   | RT8   | RT7   | RT6    | RT5    | RT4   | Remote temperature2 (high byte)            |
| 24              | NA     | 00                   | RT3              | RT2   | RT1   | RT0   | 0     | 0      | 0      | 0     | Remote temperature2 (low byte)             |
| 25              | 25     | 08                   | 0                | 0     | 0     | 0     | BC3   | BC2    | BC1    | BC0   | Ch. 1 beta range selection                 |
| 26              | 26     | 08                   | 0                | 0     | 0     | 0     | BC3   | BC2    | BC1    | BC0   | Ch. 2 beta range selection                 |
| 27              | 27     | 00                   | NC7              | NC6   | NC5   | NC4   | NC3   | NC2    | NC1    | NC0   | N-factor correction remote1                |
| 28              | 28     | 00                   | NC7              | NC6   | NC5   | NC4   | NC3   | NC2    | NC1    | NC0   | N-factor correction remote2                |

(1) NA = Not applicable; register is write- or read-only.

(2) Indeterminate state.

#### Table 4. TMP432 Register Map (continued)

| POINTER ADDRESS |       |                      | BIT DESCRIPTIONS |      |      |      |      |         |         |        |                                         |
| --------------- | ----- | -------------------- | ---------------- | ---- | ---- | ---- | ---- | ------- | ------- | ------ | --------------------------------------- |
| READ            | WRITE | POWER-ON RESET (HEX) | D7               | D6   | D5   | D4   | D3   | D2      | D1      | D0     | DESCRIPTIONS                            |
| 29              | NA    | 00                   | T3               | T2   | T1   | T0   | 0    | 0       | 0       | 0      | Local temperature (low byte)            |
| 35              | 35    | 00                   | 0                | 0    | 0    | 0    | 0    | R2HIGH  | R1HIGH  | LHIGH  | High limit status                       |
| 36              | 36    | 00                   | 0                | 0    | 0    | 0    | 0    | R2LOW   | R1LOW   | LLOW   | Low limit status                        |
| 37              | 37    | 00                   | 0                | 0    | 0    | 0    | 0    | R2THERM | R1THERM | LTHERM | Therm status                            |
| 3D              | 3D    | 00                   | LTH3             | LTH2 | LTH1 | LTH0 | 0    | 0       | 0       | 0      | Local temperature high limit (low byte) |
| 3E              | 3E    | 00                   | LTL3             | LTL2 | LTL1 | LTL0 | 0    | 0       | 0       | 0      | Local temperature low limit (low byte)  |
| 3F              | 3F    | 3C                   | 0                | 0    | REN2 | REN  | LEN  | RC      | 0       | 0      | Configuration register2                 |
| NA              | FC    | 00                   | X<sup>(a)</sup>  | X    | X    | X    | X    | X       | X       | X      | Software reset                          |
| FD              | NA    | 32                   | 0                | 0    | 1    | 1    | 0    | 0       | 1       | 0      | TMP432 device ID                        |
| FE              | NA    | 55                   | 0                | 1    | 0    | 1    | 0    | 1       | 0       | 1      | Manufacturer ID                         |

(3)  X = Undefined. Writing any value to this register initiates a software reset; see Software Reset.

#### 8.6.1 Pointer Register

Figure 19 illustrates the internal register structure of the TMP43x. The 8-bit Pointer Register is used to address a given data register. The Pointer Register identifies which of the data registers must respond to a read or write command on the Two-Wire bus. This register is set with every write command. A write command must be issued to set the proper value in the Pointer Register before executing a read command. Table 3 describes the pointer address of the registers available in the TMP431. Table 4 describes the address of the registers available in the TMP432. The power-on reset (POR) value of the Pointer Register is 00h (0000 0000b).

#### 8.6.2 Temperature Registers

The TMP431 has four 8-bit registers that hold temperature measurement results. The TMP432 has six 8-bit registers that hold temperature measurement results. Both the local channel and the remote channel have a high byte register that contains the most significant bits (MSBs) of the temperature analog-to-digital converter (ADC) result and a low byte register that contains the least significant bits (LSBs) of the temperature ADC result. The local channel high byte address for the TMP43x is 00h; the local channel low byte address is 15h for the TMP431 and 29h for the TMP432. The remote channel high byte is at address 01h; the remote channel low byte address is 10h. For the TMP432, the second remote channel high byte address is 23h; the second remote channel low byte is 24h. These registers are read-only and are updated by the ADC each time a temperature measurement is completed.

The TMP43x contain circuitry to assure that a low byte register read command returns data from the same ADC conversion as the immediately preceding high byte read command. This assurance remains valid only until another register is read. For proper operation, the high byte of a temperature register must be read first. The low byte register must be read in the next read command. The low byte register can be left unread if the LSBs are not needed. Alternatively, the temperature registers can be read as a 16-bit register by using a single two-byte read command from address 00h for the local channel result, or from address 01h for the remote channel result (23h for the second remote channel result). The high byte is output first, followed by the low byte. Both bytes of this read operation are from the same ADC conversion. The power-on reset value of both temperature registers is 00h.

#### 8.6.3 Limit Registers

The TMP43x have registers for setting comparator limits for both the local and remote measurement channels. These registers have read and write capability. The High and Low Limit Registers for both channels span two registers, as do the temperature registers. The local temperature high limit is set by writing the high byte to pointer address 0Bh and writing the low byte to pointer address 16h for the TMP431 and 3Dh for the TMP432, or by using a single two-byte write command (high byte first) to pointer address 0Bh.

The local temperature high limit is obtained by reading the high byte from pointer address 05h and the low byte from pointer address 16h for the TMP4341 and 3Dh for the TMP432, or by using a two-byte read command from pointer address 05h. The power-on reset value of the local temperature high limit is 55h, 00h (85°C in standard temperature mode; 21°C in extended temperature mode).
Similarly, the local temperature low limit is set by writing the high byte to pointer address 0Ch and writing the low byte to pointer address 17h for the TMP431 and 3Eh for the TMP432, or by using a single two-byte write command to pointer address 0Ch. The local temperature low limit is read by reading the high byte from pointer address 06h and the low byte from pointer address 17h and 3Eh for the TMP432, or by using a two-byte read from pointer address 06h. The power-on reset value of the local temperature low limit register is 00h, 00h (0°C in standard temperature mode; –64°C in extended mode).

The remote temperature high limit for the TMP431 (remote temperature1 high limit for the TMP432) is set by writing the high byte to pointer address 0Dh and writing the low byte to pointer address 13h, or by using a two-byte write command to pointer address 0Dh. The remote temperature high limit is obtained by reading the high byte from pointer address 07h and the low byte from pointer address 13h, or by using a two-byte read command from pointer address 07h. The power-on reset value of the Remote Temperature High Limit Register is 55h, 00h (85°C in standard temperature mode; 21°C in extended temperature mode).

The remote temperature low limit for the TMP431 (remote temperature1 low limit for the TMP432) is set by writing the high byte to pointer address 0Eh and writing the low byte to pointer address 14h, or by using a two-byte write to pointer address 0Eh. The remote temperature low limit is read by reading the high byte from pointer address 08h and the low byte from pointer address 14h, or by using a two-byte read from pointer address 08h. The power-on reset value of the Remote Temperature Low Limit Register is 00h, 00h (0°C in standard temperature mode; –64°C in extended mode).

The remote temperature2 high limit for the TMP432 is set by writing the high byte to pointer address 15h and writing the low byte to pointer address 17h, or by using a two-byte write command to pointer address 15h. The remote temperature high limit is obtained by reading the high byte from pointer address 15h and the low byte from pointer address 17h, or by using a two-byte read command from pointer address 15h. The power-on reset value of the Remote Temperature High Limit Register is 55h, 00h (85°C in standard temperature mode; 21°C in extended temperature mode).

The remote temperature2 low limit for the TMP432 is set by writing the high byte to pointer address 16h and writing the low byte to pointer address 18h, or by using a two-byte write to pointer address 16h. The remote temperature low limit is read by reading the high byte from pointer address 16h and the low byte from pointer address 18h, or by using a two-byte read from pointer address 16h. The power-on reset value of the Remote Temperature Low Limit Register is 00h, 00h (0°C in standard temperature mode; –64°C in extended mode).

The TMP43x also have a THERM limit register for both the local and the remote channels. These registers are eight bits and allow for THERM limits set to 1°C resolution. The local channel THERM limit is set by writing to pointer address 20h. The remote channel THERM limit is set by writing to pointer address 19h. The remote channel THERM2 limit for the TMP432 is set by writing to pointer address 1Ah.

The local channel THERM limit is obtained by reading from pointer address 20h; the remote channel THERM limit is read by reading from pointer address 19h. The remote channel THERM2 limit is read by reading from pointer address 1Ah. The power-on reset value of the THERM limit registers is 55h for the TMP431A, TMP431B, TMP432A, and TMP432B (85°C in standard temperature mode; 21°C in extended temperature mode). The power-on reset value of the THERM limit registers is 69h for the TMP431C and TMP431D (105°C in standard temperature mode; 41°C in extended temperature mode). The THERM limit comparators also have hysteresis.

The hysteresis of both comparators is set by writing to pointer address 21h. The hysteresis value is obtained by reading from pointer address 21h. The value in the Hysteresis Register is an unsigned number (always positive). The power-on reset value of this register is 0Ah (+10°C).

NOTE: Whenever changing between standard and extended temperature ranges, be aware that the temperatures stored in the temperature limit registers are not automatically reformatted to correspond to the new temperature range format. These values must be reprogrammed in the appropriate binary or extended binary format.

#### 8.6.4 Status Registers

##### 8.6.4.1 TMP431 Status Register

###### Table 5. TMP431 Status Register Format

| TMP431 STATUS REGISTER (Read = 02h, Write = NA) |       |       |      |       |      |      |       |       |
| ----------------------------------------------- | ----- | ----- | ---- | ----- | ---- | ---- | ----- | ----- |
| BIT #                                           | D7    | D6    | D5   | D4    | D3   | D2   | D1    | D0    |
| BIT NAME                                        | BUSY  | LHIGH | LLOW | RHIGH | RLOW | OPEN | RTHRM | LTHRM |
| POR VALUE                                       | 0 (1) | 0     | 0    | 0     | 0    | 0    | 0     | 0     |

(1) The BUSY bit changes to 1 almost immediately (&#x3C;&#x3C; 100 μs) following power-up, as the TMP431 begins the first temperature conversion. It is high whenever the TMP431 is converting a temperature reading.

The TMP431 has a Status Register to report the state of the temperature comparators. Table 5 shows the Status Register bits. The Status Register is read-only and is read by reading from pointer address 02h.

The BUSY bit reads as 1 if the ADC is making a conversion. This bit reads as 0 if the ADC is not converting. The OPEN bit reads as 1 if the remote transistor is detected as open from the last read of the Status Register. The OPEN status is only detected when the ADC is attempting to convert a remote temperature.

The RTHRM bit reads as 1 if the remote temperature exceeds the remote THERM limit and remains greater than the remote THERM limit less the value in the shared Hysteresis Register; see Figure 18. The LTHRM bit reads as 1 if the local temperature exceeds the local THERM limit and remains greater than the local THERM limit less the value in the shared Hysteresis Register; see Figure 18.

The LHIGH and RHIGH bit values depend on the state of the AL/TH bit in the Configuration Register 1. If the AL/TH bit is ‘0’, the LHIGH bit reads as 1 if the local high limit was exceeded from the last clearing of the Status Register. The RHIGH bit reads as 1 if the remote high limit was exceeded from the last clearing of the Status Register. If the AL/TH bit is 1, the remote high limit and the local high limit are used to implement a THERM2 function. LHIGH reads as 1 if the local temperature exceeds the local high limit and remains greater than the local high limit less the value in the Hysteresis Register. The RHIGH bit reads as 1 if the remote temperature has exceeded the remote high limit and remains greater than the remote high limit less the value in the Hysteresis Register.

The LLOW and RLOW bits are not affected by the AL/TH bit. The LLOW bit reads as 1 if the local low limit was exceeded from the last clearing of the Status Register. The RLOW bit reads as 1 if the remote low limit was exceeded from the last clearing of the Status Register.

The values of the LLOW, RLOW, and OPEN (as well as LHIGH and RHIGH when AL/TH is 0) are latched and read as 1 until the Status Register is read or a device reset occurs. These bits are cleared by reading the Status Register, provided that the condition causing the flag to be set no longer exists. The values of BUSY, LTHRM, and RTHRM (as well as LHIGH and RHIGH when ALERT/THERM2 is 1) are not latched and are not cleared by reading the Status Register. They always indicate the current state, and are updated appropriately at the end of the corresponding ADC conversion. Clearing the Status Register bits does not clear the state of the ALERT pin; an SMBus alert response address command must be used to clear the ALERT pin.

The TMP431 NORs LHIGH, LLOW, RHIGH, RLOW, and OPEN, so a status change for any of these flags from 0 to 1 automatically causes the ALERT pin to go low (only applies when the ALERT/THERM2 pin is configured for ALERT mode).

##### 8.6.4.2 TMP432 Status Register

###### Table 6. TMP432 Status Register Format

| **TMP432 STATUS REGISTER (Read = 02h, Write = NA)** |       |      |      |      |      |      |       |      |
| --------------------------------------------------- | ----- | ---- | ---- | ---- | ---- | ---- | ----- | ---- |
| BIT #                                               | D7    | D6   | D5   | D4   | D3   | D2   | D1    | D0   |
| BIT NAME                                            | BUSY  | 0    | 0    | HIGH | LOW  | OPEN | THERM | 0    |
| POR VALUE                                           | 0 (1) | 0    | 0    | 0    | 0    | 0    | 0     | 0    |

(1) The BUSY bit changes to 1 almost immediately (&#x3C;&#x3C; 100 μs) following power-up, as the TMP432 begins the first temperature conversion. It is high whenever the TMP432 is converting a temperature reading.
The TMP432 has a Status Register to report the state of the temperature comparators. Table 6 lists the Status Register bits. The Status Register is read-only and is read by reading from pointer address 02h.

The BUSY bit reads as 1 if the ADC is making a conversion. It reads as 0 if the ADC is not converting. The OPEN bit reads as 1 if the remote transistor was detected as open from the last read of the Status Register. The OPEN status is only detected when the ADC is attempting to convert a remote temperature.

The THERM bit reads as 1 if the temperature from any channel (remote or local) has exceeded the THERM limit and remains greater than the THERM limit less the value in the shared Hysteresis Register; see Figure 18.

The HIGH bit value depends on the state of the AL/TH bit in the Configuration Register 1. If the AL/TH bit is 0, the HIGH bit reads 1 if any of the temperature channels go beyond the programmed high limit from the last clearing of the Status Register. If the AL/TH bit is 1, the HIGH limit is used to implement THERM2 function. The HIGH bit reads as 1 if the temperature exceeds the high limit less the value in the Hysteresis Register.

The AL/TH bit does not affect the Status Register LOW bit. The LOW bit reads as 1 if any of the temperature channels go beyond the programmed low limit from the last clearing of the Status Register.

The values of the LOW and OPEN bits (as well as HIGH when AL/TH is 0) are latched and read as 1 until the corresponding Status Register is read or a device reset occurs. These bits are cleared by reading the Low Limit Status, High Limit Status, and Open Status registers if the condition causing the flag to be set no longer exists.

The values of BUSY and THERM (as well as HIGH when AL/TH is 1) are not latched and are not cleared by reading the Status Register. They always indicate the current state, and are updated appropriately at the end of the corresponding ADC conversion. Clearing the Status Register bits does not clear the state of the ALERT pin; an SMBus alert response address command must be used to clear the ALERT pin.

The TMP432 NORs HIGH, LOW, and OPEN, so a status change for any of these flags from 0 to 1 automatically causes the ALERT pin to go low (only applies when the ALERT/THERM2 pin is configured for ALERT mode).

#### 8.6.5  Configuration Register 1

The Configuration Register 1 sets the temperature range, controls shutdown mode, and determines how the ALERT/THERM2 pin functions. The Configuration Register is set by writing to pointer address 09h and read by reading from pointer address 03h.

The MASK bit (bit 7) enables or disables the ALERT pin output if ALERT/THERM = 0. If ALERT/THERM = 1 then the MASK bit has no effect. If MASK is set to ‘0’, the ALERT pin goes low when one of the temperature measurement channels exceeds its high or low limits for the chosen number of consecutive conversions. If the MASK bit is set to 1, the TMP43x retain the ALERT pin status, but the ALERT pin does not go low.

The shutdown (SD) bit (bit 6) enables or disables the temperature measurement circuitry. If SD = 0, the TMP43x convert continuously at the rate set in the conversion rate register. When SD is set to 1, the TMP43x immediately stop converting and enter a shutdown mode. When SD is set to 0 again, the TMP43x resume continuous conversions. A single conversion can be started when SD = 1 by writing to the One-Shot Register.

The AL/TH bit (bit 5) controls whether the ALERT pin functions in ALERT mode or THERM2 mode. If AL/TH = 0, the ALERT pin operates as an interrupt pin. In this mode, the ALERT pin goes low after the set number of consecutive out-of-limit temperature measurements occur.

If AL/TH = 1, the ALERT/THERM2 pin implements a THERM function (THERM2). In this mode, THERM2 functions similar to the THERM pin except that the local high limit and remote high limit registers are used for the thresholds. THERM2 goes low when either RHIGH or LHIGH is set.

The temperature range is set by configuring bit 2 of the Configuration Register 1. Setting this bit low configures the TMP43x for the standard measurement range (0°C to 127°C); temperature conversions will be stored in the standard binary format. Setting bit 2 high configures the TMP43x for the extended measurement range (–55°C to 150°C); temperature conversions are stored in the extended binary format (see Table 1).

The remaining bits of the Configuration Register 1 are reserved and must always be set to 0. The power-on reset value for this register is 00h. Table 7 summarizes the bits of the Configuration Register 1.

##### Table 7. Configuration Register 1 Bit Descriptions

| CONFIGURATION REGISTER 1<br/><br/>(Read = 03h, Write = 09h, POR = 00h) |                   |                                     |                      |
| ------------------------------------------------------------ | ----------------- | ----------------------------------- | -------------------- |
| BIT                                                          | NAME              | FUNCTION                            | POWER-ON RESET VALUE |
| 7                                                            | MASK              | 0 = ALERT enabled 1 = ALERT masked  | 0                    |
| 6                                                            | SD                | 0 = Run 1 = Shut down               | 0                    |
| 5                                                            | AL/TH             | 0 = ALERT mode 1 = THERM mode       | 0                    |
| 4, 3                                                         | Reserved          | —                                   | 0                    |
| 2                                                            | Temperature range | 0 = 0°C to 127°C 1 = −55°C to 150°C | 0                    |
| 1, 0                                                         | Reserved          | —                                   | 0                    |

#### 8.6.6 Configuration Register 2

Configuration Register 2 (pointer address 1Ah for the TMP431 and 3Fh for the TMP432) controls which temperature measurement channels are enabled and whether the external channels have the resistance correction feature enabled or not.

The RC bit enables the resistance correction feature for the external temperature channels. If RC = 1, series resistance correction is enabled; if RC = 0, resistance correction is disabled. Resistance correction must be enabled for most applications. However, disabling the resistance correction can yield slightly improved temperature measurement noise performance, and reduce conversion time by about 50%, which could lower power consumption when conversion rates of two per second or less are selected.

The LEN bit enables the local temperature measurement channel. If LEN = 1, the local channel is enabled; if LEN = 0, the local channel is disabled.

The REN bit enables external temperature measurement channel 1 (connected to pins 2 and 3). If REN = 1, the external channel is enabled; if REN = 0, the external channel is disabled.

For the TMP432 only, the REN2 bit enables the second external measurement channel (connected to pins 4 and 5). If REN2 = 1, the second external channel is enabled; if REN2 = 0, the second external channel is disabled.

The temperature measurement sequence is local channel, external channel 1, external channel 2, shutdown, and delay (to set conversion rate, if necessary). The sequence starts over with the local channel. If any of the channels are disabled, they are skipped in the sequence.

##### Table 8. Configuration Register 2 Bit Descriptions

| CONFIGURATION REGISTER 2<br/><br/>(Read, Write = 1 A for TMP431 3F for TMP432; POR = 1Ch for TMP431; 3Ch for TMP432) |          |                                                              |                      |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------------------- |
| BIT                                                          | NAME     | FUNCTION                                                     | POWER-ON RESET VALUE |
| 7, 6                                                         | Reserved | —                                                            | 0                    |
| 5                                                            | REN2     | 0 = External channel 2 disabled 1 = External channel 2 enabled | 0 (TMP431)           |
| 4                                                            | REN      | 0 = External channel 1 disabled 1 = External channel 1 enabled | 1                    |
| 3                                                            | LEN      | 0 = Local channel disabled 1 = Local channel enabled         | 1                    |
| 2                                                            | RC       | 0 = Resistance correction disabled 1 = Resistance correction enabled | 1                    |
| 1, 0                                                         | Reserved | —                                                            | 0                    |

#### 8.6.7  Conversion Rate Register

The Conversion Rate Register (pointer address 0Ah) controls the rate at which temperature conversions are performed. This register adjusts the idle time between conversions but not the conversion timing itself, thereby allowing the TMP43x power dissipation to be balanced with the temperature register update rate. Table 9 shows the conversion rate options and corresponding current consumption.

##### Table 9. Conversion Rate Register

| CONVERSION RATE REGISTER (Read = 04h, Write = 0Ah, POR = 07h) |      |      |      |      |      |      |      |                       |                                |            |
| :----------------------------------------------------------: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :-------------------: | ------------------------------ | ---------- |
|                              R7                              |  R6  |  R5  |  R4  |  R3  |  R2  |  R1  |  R0  | CONVERSION<br>PER SEC | AVERAGE I<sub>Q</sub>(TYP)(μA) |            |
|                                                              |      |      |      |      |      |      |      |                       | V+ = 2.7V                      | V+ = 5.5 V |
|                              0                               |  0   |  0   |  0   |  0   |  0   |  0   |  0   |        0.0625         | 11                             | 32         |
|                              0                               |  0   |  0   |  0   |  0   |  0   |  0   |  1   |         0.125         | 17                             | 38         |
|                              0                               |  0   |  0   |  0   |  0   |  0   |  1   |  0   |         0.25          | 28                             | 49         |
|                              0                               |  0   |  0   |  0   |  0   |  0   |  1   |  1   |          0.5          | 47                             | 69         |
|                              0                               |  0   |  0   |  0   |  0   |  1   |  0   |  0   |           1           | 80                             | 103        |
|                              0                               |  0   |  0   |  0   |  0   |  1   |  0   |  1   |           2           | 128                            | 155        |
|                              0                               |  0   |  0   |  0   |  0   |  1   |  1   |  0   |           4           | 190                            | 220        |
|                           (to 0Fh)                           |      |      |      |      |      |      |      |           8           | 373                            | 413        |

#### 8.6.8  Beta Compensation Configuration Register

If the Beta Compensation Configuration Register is set to 1xxx (beta correction enabled) for a given remote channel at the beginning of each temperature conversion, the TMP43x automatically detects if the sensor is diode-connected or GND collector-connected, selects the proper beta range, and measures the sensor temperature appropriately.

If the Beta Compensation Configuration Register is set to 0111 (beta correction disabled) for a given channel, the automatic detection is bypassed and the temperature is measured assuming a diode-connected sensor. A PNP transistor can continue to be GND collector-connected in this mode, but no beta compensation factor is applied.

When the beta correction is set to 0111 or the sensor is diode-connected (base shorted to collector), the η-factor used by the TMP43x is 1.008. When the beta correction configuration is set to 1xxx (beta correction enabled) and the sensor is GND collector-connected (PNP collector to ground), the η-factor used by the TMP43x is 1.000. Table 10 shows the read value for the selected beta ranges and the appropriate η-factor used for each conversion.

##### Table 10. Beta Compensation Configuration Register

| BCx3-BCx0 | BETA RANGE DESCRIPTION                              | η-FACTOR | TIME   |
| --------- | --------------------------------------------------- | -------- | ------ |
| 1000      | Automatically selected range 0 (0.10 < beta < 0.18) | 1        | 126 ms |
| 1001      | Automatically selected range 1 (0.16 < beta < 0.26) | 1        | 126 ms |
| 1010      | Automatically selected range 2 (0.24 < beta < 0.43) | 1        | 126 ms |
| 1011      | Automatically selected range 3 (0.35 < beta < 0.78) | 1        | 126 ms |
| 1100      | Automatically selected range 4 (0.64 < beta < 1.8)  | 1        | 126 ms |
| 1101      | Automatically selected range 5 (1.4 < beta < 9)     | 1        | 126 ms |
| 1110      | Automatically selected range 6 (6.7 < beta < 40)    | 1        | 126 ms |
| 1111      | Automatically selected range 7 (beta > 27)          | 1        | 126 ms |
| 1111      | Automatically detected diode connected sensor       | 1.008    | 93 ms  |
| 0000      | Manually selected range 0 (0.10 < beta < 0.5)       | 1        | 93 ms  |
| 0001      | Manually selected range 1 (0.13 < beta < 1)         | 1        | 93 ms  |
| 0010      | Manually selected range 2 (0.18 < beta < 2)         | 1        | 93 ms  |
| 0011      | Manually selected range 3 (0.3 < beta < 25)         | 1        | 93 ms  |
| 0100      | Manually selected range 4 (0.5 < beta < 50)         | 1        | 93 ms  |
| 0101      | Manually selected range 5 (1.1 < beta < 100)        | 1        | 93 ms  |
| 0110      | Manually selected range 6 (2.4 < beta < 150)        | 1        | 93 ms  |
| 0111      | Manually disabled beta correction                   | 1.008    | 93 ms  |

#### 8.6.9  η-Factor Correction Register

The TMP43x allow for a different η-factor value to be used for converting remote channel measurements to temperature. The remote channel uses sequential current excitation to extract a differential VBE voltage measurement to determine the temperature of the remote transistor. Equation 1 relates this voltage and temperature.

VBE2 - VBE1 = hkT/q(ln I2 / I1)                                                                     (1)

The value η in Equation 1 is a characteristic of the particular transistor used for the remote channel. When the beta compensation configuration is set to 0111 (beta compensation disabled) or the sensor is diode-connected (base shorted to collector), the η-factor used by the TMP43x is 1.008. When the beta compensation configuration is set to 1000 (beta compensation enabled) and the sensor is GND collector-connected (PNP collector to ground), the η-factor used by the TMP43x is 1. If the η-factor used for the temperature conversion does not match the characteristic of the sensor, then temperature offset is observed. The value in the η-Factor Correction Register can be used to adjust the effective η-factor according to Equation 2 and Equation 3 for disabled beta compensation or a diode-connected sensor. Equation 4 and Equation 5 can be used for enabled beta compensation and a GND collector-connected sensor.

heff =  1.008 × 300 / (300 - NADJUST)                                                                                        (2)

NADJUST = 300 - (300 × 1.008 / heff)                                                                                (3)

heff =  1.000 × 300 / (300 - NADJUST)                                                                                        (4)

NADJUST = 300 - (300 × 1.000 / heff)                                                                                (5)

The η-correction value must be stored in twos-complement format, yielding an effective data range from –128 to 127. Table 11 shows the η-factor range for both 1.008 and 1. For the TMP431, the η-correction value can be written to and read from pointer address 18h. For the TMP432, the η-correction value can be written to and read from pointer address 27h. The η-correction value for the second remote channel is read to and written from pointer address 28h. The register power-on reset value is 00h, thus having no effect unless written to.

##### Table 11. η-Factor Range

| NADJUST  |      |         |          |
| -------- | ---- | ------- | -------- |
| BINARY   | HEX  | DECIMAL | η        |
| 01111111 | 7F   | 127     | 1.747977 |
| 00001010 | 0A   | 10      | 1.042759 |
| 00001000 | 08   | 8       | 1.035616 |
| 00000110 | 06   | 6       | 1.028571 |
| 00000100 | 04   | 4       | 1.021622 |
| 00000010 | 02   | 2       | 1.014765 |
| 00000001 | 01   | 1       | 1.011371 |
| 00000000 | 00   | 0       | 1.008    |
| 11111111 | FF   | –1      | 1.004651 |
| 11111110 | FE   | –2      | 1.001325 |
| 11111100 | FC   | –4      | 0.994737 |
| 11111010 | FA   | –6      | 0.988235 |
| 11111000 | F8   | –8      | 0.981818 |
| 11110110 | F6   | –10     | 0.975484 |
| 10000000 | 80   | –128    | 0.706542 |

#### 8.6.10 Software Reset

The TMP43x can be reset by writing any value to Pointer Register FCh. This action restores the power-on reset state to all of the TMP43x registers as well as abort any conversion in process and clear the ALERT and THERM pins.

The TMP43x also support reset via the two-wire general call address (00000000). The TMP43x acknowledge the general call address and respond to the second byte. If the second byte is 00000110, the TMP43x execute a software reset. The TMP43x do not respond to other values in the second byte.

#### 8.6.11 Consecutive Alert Register

The value in the Consecutive Alert Register (address 22h) determines how many consecutive out-of-limit measurements must occur on a measurement channel before the ALERT or the THERM signal is activated. The value in this register does not affect bits in the Status Register. Values of one, two, three, or four consecutive conversions can be selected; one conversion is the default. This function allows additional filtering for the ALERT or the THERM pin. Table 14 shows the consecutive alert bits. For bit descriptions, see Table 12.

##### Table 12. Consecutive Alert Register Bit Descriptions

| BIT NAME   |            |            |                                                              |
| ---------- | ---------- | ---------- | ------------------------------------------------------------ |
| CALT2/CTH2 | CALT1/CTH1 | CALT0/CTH0 | NUMBER OF CONSECUTIVE OUT-OF-LIMIT MEASUREMENTS (ALERT/THERM) |
| 0          | 0          | 0          | 1                                                            |
| 0          | 0          | 1          | 2                                                            |
| 0          | 1          | 1          | 3                                                            |
| 1          | 1          | 1          | 4                                                            |

#### 8.6.12 Therm Hysteresis Register

The THERM Hysteresis Register (see Table 15) stores the hysteresis value used for the THERM pin alarm function. This register must be programmed with a value that is less than the Local Temperature High Limit Register value, Remote Temperature High Limit Register value, Local THERM Limit Register value, or Remote THERM Limit Register value; otherwise, the respective temperature comparator does not trip on the measured temperature falling edges. Allowable hysteresis values are in Table 13. The default hysteresis value is 10°C, whether the device is operating in the standard or extended mode setting.

##### Table 13. Allowable THERM Hysteresis Values

|                  | THERM HYSTERESIS VALUE     |       |
| ---------------- | -------------------------- | ----- |
| TEMPERATURE (°C) | TH\[7:0] (STANDARD BINARY) | (HEX) |
| 0                | 0000 0000                  | 00    |
| 1                | 0000 0001                  | 01    |
| 5                | 0000 0101                  | 05    |
| 10               | 0000 1010                  | 0A    |
| 25               | 0001 1001                  | 19    |
| 50               | 0011 0010                  | 32    |
| 75               | 0100 1011                  | 4B    |
| 100              | 0110 0100                  | 64    |
| 125              | 0111 1101                  | 7D    |
| 127              | 0111 1111                  | 7F    |
| 150              | 1001 0110                  | 96    |
| 175              | 1010 1111                  | AF    |
| 200              | 1100 1000                  | C8    |
| 225              | 1110 0001                  | E1    |
| 255              | 1111 1111                  | FF    |

#### 8.6.13 Identification Registers

The TMP43x allow for the Two-Wire bus controller to query the device for manufacturer and device IDs to enable the device for software identification of the device at the particular Two-Wire bus address. The manufacturer ID is obtained by reading from pointer address FEh. The TMP43x both return 55h for the manufacturer code. The device ID is obtained by reading from pointer address FDh. The TMP431 returns 31h for the device ID and the TMP432 returns 32h for the device ID (see Table 3 and Table 4). These registers are read-only.

##### Table 14. Consecutive Alert Register Format

| CONSECUTIVE ALERT REGISTER<br/>(READ = 22h, WRITE = 22h, POR = 70h) |      |      |      |      |       |       |       |      |
| ------------------------------------------------------------ | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ---- |
| BIT #                                                        | D7   | D6   | D5   | D4   | D3    | D2    | D1    | D0   |
| BIT NAME                                                     | 0    | CTH2 | CTH1 | CTH0 | CALT2 | CALT1 | CALT0 | 0    |
| POR VALUE                                                    | 0    | 1    | 1    | 1    | 0     | 0     | 0     | 0    |

##### Table 15. THERM Hysteresis Register Format

| THERM HYSTERESIS REGISTER<br/>(Read = 21h, Write = 21h, POR = 0Ah) |      |      |      |      |      |      |      |      |
| ------------------------------------------------------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| BIT #                                                        | D7   | D6   | D5   | D4   | D3   | D2   | D1   | D0   |
| BIT NAME                                                     | TH7  | TH6  | TH5  | TH4  | TH3  | TH2  | TH1  | TH0  |
| POR VALUE                                                    | 0    | 0    | 0    | 0    | 1    | 0    | 1    | 0    |

#### 8.6.14 Open Status Register

The Open Status Register indicates if there is a fault on the remote channel diode. Bit 2 is set if remote channel 2 is open or faultily connected. Similarly, bit 1 corresponds to remote channel 1. These bits are cleared by reading this register if the condition causing the flag to be set no longer exists.

#### 8.6.15 Channel Mask Register

The Channel Mask Register controls individual channel masking. When a channel is masked, the ALERT pin is asserted when the masked channel reads a diode fault or out-of-limit error.

#### 8.6.16 High Limit Status Register

The High Limit Status Register contains the status bits that are set when a temperature channel high limit is exceeded. If any of these bits are set, then the HIGH status bit in the Status Register is set. These bits are cleared by reading this register if the condition causing the flag to be set no longer exists.

#### 8.6.17 Low Limit Status Register

The Low Limit Status Register contains the status bits that are set when a temperature channel low limit is exceeded. If any of these bits are set, then the LOW status bit in the Status Register is set. These bits are cleared by reading this register if the condition causing the flag to be set no longer exists.

#### 8.6.18 THERM Limit Status Register

The THERM Limit Status Register contains the status bits that are set when a temperature channel THERM limit is exceeded. If any of these bits are set, then the THERM status bit in the Status Register is set.

Documentation Feedback  31 Product Folder Links: TMP431 TMP432SBOS441H – SEPTEMBER 2009 – REVISED MARCH 2016

## 9 Application and Implementation</h9>

NOTE Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

### 9.1 Application Information</h9>
The TMP43x devices require only a transistor connected between the DXP and DXN pins for remote temperature measurement. Tie the DXP pin to GND if the remote channel is not used and only the local temperature is measured. The SDA, ALERT, and THERM pins (and SCL, if driven by an open-drain output) require pullup resistors as part of the communication bus. TI recommends a 0.1-μF power-supply decoupling capacitor for local bypassing. Figure 20 shows a typical configuration of the TMP431; see Figure 21 for a typical configuration of the TMP432.

### 9.2 Typical Application</h9>

#### Figure 20. TMP431 Basic Connections

+5V

| GND collector-connected transistor configuration(1): |          |     |        |       | (typ)            |
| ---------------------------------------------------- | -------- | --- | ------ | ----- | ---------------- |
| Series Resistance                                    | V+       | 8   | 10kΩ   | 10kΩ  | 10kΩ             |
| RS1(2)                                               | 2        | DXP | TMP431 | SCL   |                  |
| RS2(2)                                               | CDIFF(3) | 3   | SDA    | 7     | SMBus Controller |
| ALERT                                                | THERM2   | 6   |        | THERM | 4                |
| GND                                                  | 5        |     |        |       | Fan Controller   |

Diode-connected configuration(1):

| RS1(2) |          |   |   |   |
| ------ | -------- | - | - | - |
| RS2(2) | CDIFF(3) |   |   |   |

NOTES:

- (1) Diode-connected configuration provides better settling time.
- GND collector-connected transistor configuration provides better series resistance cancellation.
- (2) The total series resistance (RS1 + RS2) should be &#x3C; 1 kΩ. This resistance is optional.
- (3) CDIFF should be &#x3C; 2200pF. Selection of CDIFF depends on specific application; see Filtering section and Figure 9, Remote Temperature Error vs Differential Capacitance.

### Typical Application (continued)

#### Figure 21. TMP432 Basic Connections

+5V

| GND collector-connected transistor configuration(1): |                   |          | 0.1mF | 10kΩ   | 10kΩ   | 10kΩ  | 10kΩ  |       |   |
| ---------------------------------------------------- | ----------------- | -------- | ----- | ------ | ------ | ----- | ----- | ----- | - |
|                                                      | Series Resistance |          | 1     |        | (typ)  | (typ) | (typ) | (typ) |   |
|                                                      | RS1(2)            | 2        | DXP1  | V+     | SCL    | 10    |       |       |   |
|                                                      | RS2(2)            | CDIFF(3) | 3     | DXN1   | TMP432 | SDA   | 9     |       |   |
|                                                      |                   |          | ALERT | THERM2 | 8      |       |       |       |   |
|                                                      | RS1               | 4        | DXP2  | /      |        |       |       |       |   |
|                                                      | RS2(2)            | CDIFF(3) | 5     | DXN2   | THERM  | 7     |       |       |   |
|                                                      | GND               |          |       |        |        |       |       |       | 6 |

Diode-connected configuration(1):

|   | RS1(2) |      |   |     |
| - | ------ | ---- | - | --- |
|   | R      | (2)  | C | (3) |
|   | S2     | DIFF |   |     |

NOTES:

- (1) Diode-connected configuration provides better settling time.
- GND collector-connected transistor configuration provides better series resistance cancellation.
- (2) The total series resistance (RS1 + RS2) should be &#x3C; 1 kΩ. This resistance is optional.
- (3) CDIFF should be &#x3C; 2200pF. Selection of CDIFF depends on specific application; see Filtering section and Figure 9, Remote Temperature Error vs Differential Capacitance.

#### 9.2.1 Design Requirements

The TMP43x are designed to be used with either discrete transistors or substrate transistors built into processor chips and ASICs. Either NPN- or PNP-type transistors can be used, as long as the base-emitter junction is used as the remote temperature sense. NPN transistors must be diode-connected. PNP transistors can either be transistor- or diode- connected (see Figure 20).

Errors in remote temperature sensor readings are typically the consequence of the ideality factor and current excitation used by the TMP43x versus the manufacturer-specified operating current for a given transistor. Some manufacturers specify a high-level and low-level current for the temperature-sensing substrate transistors. The TMP43x use 6 μA for ILOW and 120 μA for IHIGH. The TMP43x allow for different η-factor values; see η-Factor Correction Register.

The ideality factor (η) is a measured characteristic of a remote temperature sensor diode as compared to an ideal diode. The ideality factor for the TMP43x is trimmed to be 1.008. For transistors whose ideality factor does not match the TMP43x, Equation 6 can be used to calculate the temperature error. Note that for the equation to be used correctly, actual temperature (°C) must be converted to Kelvin (K).

TERR = (η - 1.008/1.008) × [273.15 + T(°C)]

Where:

- η = Ideality factor of remote temperature sensor
- T(°C) = actual temperature
- TERR = Error in TMP43x reading due to η ≠ 1.008
- Degree delta is the same for °C and K

For η = 1.004 and T(°C) = 100°C:

TERR = (1.004 - 1.008) × (273.15 + 100)

TERR = 1.48 °C

### Typical Application (continued)

If a discrete transistor is used as the remote temperature sensor with the TMP43x, the best accuracy can be achieved by selecting the transistor according to the following criteria:

1. Base-emitter voltage > 0.25 V at 6 μA, at the highest sensed temperature
2. Base-emitter voltage &#x3C; 0.95 V at 120 μA, at the lowest sensed temperature
3. Base resistance &#x3C; 100 Ω
4. Tight control of VBE characteristics indicated by small variations in hFE (that is, 50 to 150)

Based on these criteria, two recommended small-signal transistors are the 2N3904 (NPN) or 2N3906 (PNP).

#### 9.2.2 Detailed Design Procedure

The temperature measurement accuracy of the TMP43x depends on the remote and local temperature sensor being at the same temperature as the system point being monitored. Clearly, if the temperature sensor is not in good thermal contact with the part of the system being monitored, then there will be a delay in the response of the sensor to a temperature change in the system. For remote temperature sensing applications that use a substrate transistor (or a small, SOT23 transistor) placed close to the device being monitored, this delay is usually not a concern.

The local temperature sensor inside the TMP43x monitors the ambient air around the device. The thermal time constant for the TMP43x is approximately 2 s. This constant implies that if the ambient air changes quickly by 100°C, it would take the TMP43x about 10 seconds (that is, five thermal time constants) to settle to within 1°C of the final value. In most applications, the TMP43x package is in thermal contact with the printed circuit board (PCB), as well as subjected to forced airflow. The accuracy of the measured temperature directly depends on how accurately the PCB and forced airflow temperatures represent the temperature that the TMP43x is measuring. Additionally, the internal power dissipation of the TMP43x can cause the temperature to rise above the ambient or PCB temperature. The internal power dissipated as a result of exciting the remote temperature sensor is negligible because of the small currents used. For a 5.5-V supply and maximum conversion rate of eight conversions per second, the TMP43x dissipate 1.82 mW (PDIQ = 5.5 V × 330 μA). If both the ALERT/THERM2 and THERM pins are each sinking 1 mA, an additional 0.8 mW is dissipated (PDOUT = 1 mA × 0.4 V + 1 mA × 0.4 V = 0.8 mW). Total power dissipation is then 2.62 mW (PDIQ + PDOUT) and, with an θJA of 150°C/W, causes the junction temperature to rise approximately 0.393°C above the ambient.

#### 9.2.3 Application Curve

Figure 22 shows the typical step response to a submerging of a sensor in an oil bath with temperature of 100ºC.

##### Figure 22. Temperature Step Response

| 100                                                     | 95 | 90 | 85 | 80 | 75 | 70 | 65 | 60 | 55 | 50 | 45 | 40 | 35 | 30 | 25 |
| ------------------------------------------------------- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Temperature (°C)                                        |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| ±1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
| Time (s)                                                |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |

## 10   Power Supply Recommendations

The TMP43x devices operates with a power supply range of 2.7 V to 5.5 V. The device is optimized for operation at 3.3-V supply but can measure temperature accurately in the full supply range.

TI recommends placing a power-supply bypass capacitor as close as possible to the supply and ground pins of the device. A typical value for this supply bypass capacitor is 0.1 μF. Applications with noisy or high-impedance power supplies can require additional decoupling capacitors to reject power-supply noise.

## 11   Layout

### 11.1 Layout Guidelines

Remote temperature sensing on the TMP43x measures very small voltages using very low currents; therefore, noise at the IC inputs must be minimized. Most applications using the TMP43x have high digital content, with several clocks and logic level transitions creating a noisy environment. Layout must conform to the following guidelines:

1. Place the TMP43x as close to the remote junction sensor as possible.
2. Route the DXP and DXN traces next to each other and shield them from adjacent signals through the use of ground guard traces; see Figure 24. If a multilayer PCB is used, bury these traces between ground or VDD planes to shield them from extrinsic noise sources. TI recommends 5 mil (0.127 mm) PCB traces.
3. Minimize additional thermocouple junctions caused by copper-to-solder connections. If these junctions are used, make the same number and approximate locations of copper-to-solder connections in both the DXP and DXN connections to cancel any thermocouple effects.
4. Use a 0.1-μF local bypass capacitor directly between the V+ and GND of the TMP43x. Figure 25 illustrates the suggested bypass capacitor placement for the TMP43x. This capacitance includes any cable capacitance between the remote temperature sensor and TMP43x.
5. If the connection between the remote temperature sensor and the TMP43x is less than 8 inches (20.32 cm), use a twisted-wire pair connection. Beyond 8 inches, use a twisted, shielded pair with the shield grounded as close to the TMP43x as possible. Leave the remote sensor connection end of the shield wire open to avoid ground loops and 60-Hz pickup.
6. Thoroughly clean and remove all flux residue in and around the pins of the TMP43x to avoid temperature offset readings as a result of leakage paths between DXP or DXN and GND, or between DXP or DXN and V+.

### 11.2 Layout Examples

#### Figure 23. TMP431 Layout Example

VIA to Power or Ground Plane

VIA to Internal Layer

Ground Plane Pull-Up Resistors Supply Voltage

Supply Bypass Capacitor

| 1  | V+    | SCL     | 8       |          |   |
| -- | ----- | ------- | ------- | -------- | - |
| 2  | DXP   | SDA     | 7       |          |   |
| 3  | DXN   | ALERT / | 6       |          |   |
| RS | THERM | GND     | 5       |          |   |
|    |       |         | Thermal | Shutdown |   |

Serial Bus Traces

#### Figure 24. Example Signal Traces

V+

DXP

Ground or V+ layer on bottom and/or top, if possible.

DXN

GND

Note: Use 5 mil (0.005 in, or 0.127 mm) traces with 5 mil (0.005 in, or 0.127 mm) spacing.

### Layout Examples (continued)

#### Figure 25. Suggested Bypass Capacitor Placement

| 0.1 mF Capacitor | V+ | GND |         |
| ---------------- | -- | --- | ------- |
| PCB Via          | 1  | 8   | PCB Via |
| DXP              | 2  | 7   |         |
| DXN              | 3  | 6   |         |
| 4                | 5  |     |         |

| 0.1 mF Capacitor | V+ | GND |         |
| ---------------- | -- | --- | ------- |
| PCB Via          | 1  | 10  | PCB Via |
| DXP1             | 2  | 9   |         |
| DXN1             | 3  | 8   |         |
| DXP2             | 4  | 7   |         |
| DXN2             | 5  | 6   |         |

## 12 Device and Documentation Support

### 12.1 Related Links

The table below lists quick access links. Categories include technical documents, support and community resources, tools and software, and quick access to sample or buy.

#### Table 16. Related Links

| PARTS  | PRODUCT FOLDER | SAMPLE & BUY | TECHNICAL DOCUMENTS | TOOLS & SOFTWARE | SUPPORT & COMMUNITY |
| ------ | -------------- | ------------ | ------------------- | ---------------- | ------------------- |
| TMP431 | Click here     | Click here   | Click here          | Click here       | Click here          |
| TMP432 | Click here     | Click here   | Click here          | Click here       | Click here          |

### 12.2 Community Resources

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

- TI E2E™ Online Community: TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers.
- Design Support: TI's Design Support Quickly find helpful E2E forums along with design support tools and contact information for technical support.

### 12.3 Trademarks

E2E is a trademark of Texas Instruments.

DLP is a registered trademark of Texas Instruments.

SMBus is a trademark of Intel Corporation.

All other trademarks are the property of their respective owners.

### 12.4 Electrostatic Discharge Caution

These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam during storage or handling to prevent electrostatic damage to the MOS gates.

### 12.5 Glossary

SLYZ022 — TI Glossary. This glossary lists and explains terms, acronyms, and definitions.

## 13 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

## PACKAGE OPTION ADDENDUM

PACKAGING INFORMATION

| Orderable Device | Status(1) | Package Type | Package Drawing | Pins | Package Qty | Eco Plan                | Lead/Ball Finish | MSL Peak Temp       | Op Temp (°C) | Device Marking | Samples |
| ---------------- | --------- | ------------ | --------------- | ---- | ----------- | ----------------------- | ---------------- | ------------------- | ------------ | -------------- | ------- |
| TMP431ADGKR      | ACTIVE    | VSSOP        | DGK             | 8    | 2500        | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DRTI           | Samples |
| TMP431ADGKT      | ACTIVE    | VSSOP        | DGK             | 8    | 250         | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DRTI           | Samples |
| TMP431BDGKR      | ACTIVE    | VSSOP        | DGK             | 8    | 2500        | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DRUI           | Samples |
| TMP431BDGKT      | ACTIVE    | VSSOP        | DGK             | 8    | 250         | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DRUI           | Samples |
| TMP431CDGKR      | ACTIVE    | VSSOP        | DGK             | 8    | 2500        | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DUEC           | Samples |
| TMP431CDGKT      | ACTIVE    | VSSOP        | DGK             | 8    | 250         | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DUEC           | Samples |
| TMP431DDGKR      | ACTIVE    | VSSOP        | DGK             | 8    | 2500        | Green (RoHS & no Sb/Br) | CU NIPDAU        | Level-2-260C-1 YEAR | -40 to 125   | DUFC           | Samples |
| TMP431DDGKT      | ACTIVE    | VSSOP        | DGK             | 8    | 250         | Green (RoHS & no Sb/Br) | CU NIPDAU        | Level-2-260C-1 YEAR | -40 to 125   | DUFC           | Samples |
| TMP432ADGSR      | ACTIVE    | VSSOP        | DGS             | 10   | 2500        | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DSCI           | Samples |
| TMP432ADGST      | ACTIVE    | VSSOP        | DGS             | 10   | 250         | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DSCI           | Samples |
| TMP432BDGSR      | ACTIVE    | VSSOP        | DGS             | 10   | 2500        | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DSDI           | Samples |
| TMP432BDGST      | ACTIVE    | VSSOP        | DGS             | 10   | 250         | Green (RoHS & no Sb/Br) | CU NIPDAUAG      | Level-2-260C-1 YEAR | -40 to 125   | DSDI           | Samples |

Footnotes

(1) The marketing status values are defined as follows:

- ACTIVE: Product device recommended for new designs.
- LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
- NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
- PREVIEW: Device has been announced but is not in production. Samples may or may not be available.
- OBSOLETE: TI has discontinued the production of the device.

(2) Eco Plan - The planned eco-friendly classification: Pb-Free (RoHS), Pb-Free (RoHS Exempt), or Green (RoHS &#x26; no Sb/Br) - please check http://www.ti.com/productcontent for the latest availability information and additional product content details.

Pb-Free (RoHS): TI's terms "Lead-Free" or "Pb-Free" mean semiconductor products that are compatible with the current RoHS requirements for all 6 substances, including the requirement that lead not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, TI Pb-Free products are suitable for use in specified lead-free processes.

Pb-Free (RoHS Exempt): This component has a RoHS exemption for either 1) lead-based flip-chip solder bumps used between the die and package, or 2) lead-based die adhesive used between the die and leadframe. The component is otherwise considered Pb-Free (RoHS compatible) as defined above.

Green (RoHS &#x26; no Sb/Br): TI defines "Green" to mean Pb-Free (RoHS compatible), and free of Bromine (Br) and Antimony (Sb) based flame retardants (Br or Sb do not exceed 0.1% by weight in homogeneous material).

(3) MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

(4) There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

(5) Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a continuation of the previous line and the two combined represent the entire Device Marking for that device.

(6) Lead/Ball Finish - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead/Ball Finish values may wrap to two lines if the finish value exceeds the maximum column width.

Important Information and Disclaimer: The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

## PACKAGE MATERIALS INFORMATION

TAPE AND REEL INFORMATION

REEL DIMENSIONS

TAPE DIMENSIONS

| Reel Diameter | Cavity                                                    | A0 |
| ------------- | --------------------------------------------------------- | -- |
| A0            | Dimension designed to accommodate the component width     |    |
| B0            | Dimension designed to accommodate the component length    |    |
| K0            | Dimension designed to accommodate the component thickness |    |
| W             | Overall width of the carrier tape                         |    |
| P1            | Pitch between successive cavity centers                   |    |

QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

|    | Q1 | Q2 | Q1 | Q2                     |
| -- | -- | -- | -- | ---------------------- |
| Q3 | Q4 | Q3 | Q4 | User Direction of Feed |

Pocket Quadrants

*All dimensions are nominal

| Device      | Package Type | Package Drawing | Pins | SPQ  | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| ----------- | ------------ | --------------- | ---- | ---- | ------------------ | ------------------ | ------- | ------- | ------- | ------- | ------ | ------------- |
| TMP431ADGKR | VSSOP        | DGK             | 8    | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431ADGKT | VSSOP        | DGK             | 8    | 250  | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431BDGKR | VSSOP        | DGK             | 8    | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431BDGKT | VSSOP        | DGK             | 8    | 250  | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431CDGKR | VSSOP        | DGK             | 8    | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431CDGKR | VSSOP        | DGK             | 8    | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431CDGKT | VSSOP        | DGK             | 8    | 250  | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431CDGKT | VSSOP        | DGK             | 8    | 250  | 177.8              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431DDGKR | VSSOP        | DGK             | 8    | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP431DDGKT | VSSOP        | DGK             | 8    | 250  | 177.8              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432ADGSR | VSSOP        | DGS             | 10   | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432ADGSR | VSSOP        | DGS             | 10   | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432ADGST | VSSOP        | DGS             | 10   | 250  | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432ADGST | VSSOP        | DGS             | 10   | 250  | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432BDGSR | VSSOP        | DGS             | 10   | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432BDGSR | VSSOP        | DGS             | 10   | 2500 | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432BDGST | VSSOP        | DGS             | 10   | 250  | 330.0              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |
| TMP432BDGST | VSSOP        | DGS             | 10   | 250  | 177.8              | 12.4               | 5.3     | 3.4     | 1.4     | 8.0     | 12.0   | Q1            |

## PACKAGE MATERIALS INFORMATION

TAPE AND REEL BOX DIMENSIONS

| Device      | Package Type | Package Drawing | Pins | SPQ  | Length (mm) | Width (mm) | Height (mm) |
| ----------- | ------------ | --------------- | ---- | ---- | ----------- | ---------- | ----------- |
| TMP431ADGKR | VSSOP        | DGK             | 8    | 2500 | 366.0       | 364.0      | 50.0        |
| TMP431ADGKT | VSSOP        | DGK             | 8    | 250  | 366.0       | 364.0      | 50.0        |
| TMP431BDGKR | VSSOP        | DGK             | 8    | 2500 | 366.0       | 364.0      | 50.0        |
| TMP431BDGKT | VSSOP        | DGK             | 8    | 250  | 366.0       | 364.0      | 50.0        |
| TMP431CDGKR | VSSOP        | DGK             | 8    | 2500 | 346.0       | 346.0      | 41.0        |
| TMP431CDGKR | VSSOP        | DGK             | 8    | 2500 | 366.0       | 364.0      | 50.0        |
| TMP431CDGKT | VSSOP        | DGK             | 8    | 250  | 366.0       | 364.0      | 50.0        |
| TMP431CDGKT | VSSOP        | DGK             | 8    | 250  | 223.0       | 270.0      | 35.0        |
| TMP431DDGKR | VSSOP        | DGK             | 8    | 2500 | 346.0       | 346.0      | 29.0        |
| TMP431DDGKT | VSSOP        | DGK             | 8    | 250  | 223.0       | 270.0      | 35.0        |
| TMP432ADGSR | VSSOP        | DGS             | 10   | 2500 | 346.0       | 346.0      | 41.0        |
| TMP432ADGSR | VSSOP        | DGS             | 10   | 2500 | 366.0       | 364.0      | 50.0        |
| TMP432ADGST | VSSOP        | DGS             | 10   | 250  | 358.0       | 335.0      | 35.0        |
| TMP432ADGST | VSSOP        | DGS             | 10   | 250  | 366.0       | 364.0      | 50.0        |
| TMP432BDGSR | VSSOP        | DGS             | 10   | 2500 | 346.0       | 346.0      | 41.0        |
| TMP432BDGSR | VSSOP        | DGS             | 10   | 2500 | 366.0       | 364.0      | 50.0        |
| TMP432BDGST | VSSOP        | DGS             | 10   | 250  | 366.0       | 364.0      | 50.0        |
| TMP432BDGST | VSSOP        | DGS             | 10   | 250  | 223.0       | 270.0      | 35.0        |

## PACKAGE OUTLINE

DGS0010A VSSOP - 1.1 mm max height

SMALL OUTLINE PACKAGE

|        | 5.05 TYP   | SEATING PLANE | 4.75     |   |
| ------ | ---------- | ------------- | -------- | - |
| A      | PIN 1 ID   | 0.1 C         | AREA     |   |
| 8X 0.5 | 1          | 10            |          |   |
| 3.1    | 2X         | 2.9           | 2        |   |
| NOTE 3 | 5          | 6             | 10X 0.27 |   |
| 0.17   | B          | 3.1           | 0.1 C    |   |
| A      | B          | 1.1 MAX       | 2.9      |   |
|        | 0.23 TYP   | SEE DETAIL A  | 0.13     |   |
| 0.25   | GAGE PLANE |               |          |   |

| 0 - 8             | 0.7  | 0.15     |
| ----------------- | ---- | -------- |
| 0.4               | 0.05 | DETAIL A |
| TYPICAL           |      |          |
| 4221984/A 05/2015 |      |          |

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-187, variation BA.

## EXAMPLE BOARD LAYOUT

| 10X (1.45) |     | 10X (0.3) |   | SYMM  | (R0.05) |
| ---------- | --- | --------- | - | ----- | ------- |
| 1          | TYP | 10        |   | SYMM  |         |
| 8X (0.5)   | 5   | 6         |   | (4.4) |         |

LAND PATTERN EXAMPLE

SCALE: 10X

| SOLDER MASK OPENING     | METAL               | METAL UNDER SOLDER MASK OPENING | SOLDER MASK |
| ----------------------- | ------------------- | ------------------------------- | ----------- |
| 0.05 MAX                | 0.05 MIN            | ALL AROUND                      | ALL AROUND  |
| NON SOLDER MASK DEFINED | SOLDER MASK DEFINED |                                 |             |

SOLDER MASK DETAILS

NOT TO SCALE

4221984/A 05/2015

NOTES: (continued)

1. Publication IPC-7351 may have alternate designs.
2. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

## EXAMPLE STENCIL DESIGN

| 10X (0.3) | 10X (1.45) | SYMM  | (R0.05) TYP |
| --------- | ---------- | ----- | ----------- |
| 1         |            | 10    |             |
| SYMM      | 8X (0.5)   |       |             |
| 5         | 6          |       |             |
|           |            | (4.4) |             |

SOLDER PASTE EXAMPLE

BASED ON 0.125 mm THICK STENCIL

SCALE: 10X

4221984/A 05/2015

NOTES: (continued)

1. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
2. Board assembly site may have different recommendations for stencil design.

## MECHANICAL DATA

DGK (S-PDSO-68) PLASTIC SMALL-OUTLINE PACKAGE

| 0,25 | 0,13 |
| ---- | ---- |
| 3,10 | 5,05 |
| 2,90 | 4,75 |

Gauge Plane

|      | 0,70 |
| ---- | ---- |
|      | 0,40 |
| 2,90 |      |

Seating Plane

| 1,10 MAX | 0,15 | 0,10 |
| -------- | ---- | ---- |
|          | 0,05 |      |

4073329 /E 05/06

NOTES:

All linear dimensions are in millimeters.

This drawing is subject to change without notice.

Body length does not include mold flash, protrusions, gate burrs; Mold flash, protrusions; gate burrs shall not exceed 0.15 per end:

Body width does not include interlead flash; Interlead flash shall not exceed 0.50 per side:

Falls within JEDEC MO-187 variation AA, except interlead flash.

## LAND PATTERN DATA

DGK (S-PDSO-68) PLASTIC SMALL OUTLINE PACKAGE

Example Board Layout

Example Stencil Openings

Based stencil thickness 1127mm OOSinch): See Note D)

HHo,65)TYP. 8X(0,45) H+o,65)TYP.

8X(1,45)

PKG PKG

Example Non Soldermask Defined Pad

(0,45) Solder Mask Opening (See Note E)

(1,45) Pad Geometry (0,05) (See Note C)

All Around

4221236/A 11/13

NOTES:

All linear dimensions are in millimeters.

This drawing is subject to change without notice:

Publication IPC-7351 recommended for alternate designs.

Laser cutting apertures with trapezoidal walls and also rounding corners will offer better paste release. Customers should contact their board assembly site for stencil design recommendations. Refer to IPC-7525 for other stencil recommendations.

Customers should contact their board fabrication site for solder mask tolerances between and around signal pads.

TEXAS INSTRUMENTS

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS” AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, or other requirements. These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI’s products are provided subject to TI’s Terms of Sale (www.ti.com/legal/termsofsale.html) or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable warranties or warranty disclaimers for TI products.

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2019, Texas Instruments Incorporated

