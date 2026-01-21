
# TPS546C23 4.5-V to 18-V, 35-A Stackable Synchronous Buck Converters With PMBus

## 1 Features

- PMBus™ 1.3 Compliant Converters: 35 A
- 2-Device Stackable for up to 70 A With Current Sharing
- Input Voltage Range: 4.5 V to 18 V
- Output Voltage Range: 0.35 V to 5.5 V
- 5 mm × 7 mm LQFN Package
- Single Thermal Pad
- Integrated 3.2-mΩ and 1.4-mΩ Stacked NexFET™ Power Stage
- 350-mV to 1650-mV Reference for Adaptive Voltage Scaling (AVS) Function and Margining through PMBus
- 0.5% Reference Accuracy at 600 mV and Above
- Lossless Low-Side MOSFET Current Sensing
- Voltage Mode Control With Input Feed-Forward
- Differential Remote Sensing
- Monotonic Start-Up into Pre-Biased Output
- Output Voltage and Output Current Reporting
- Internal Die Temperature Monitoring
- 64 Programmable PMBus Addresses via ADDR0 and ADDR1 Pins
- Programmable via the PMBus Interface
- - VOUT_COMMAND and AVS VOUT Transition Rate
- Overcurrent Protection With Thermal Compensation
- UVLO, Soft-Start and Soft-Stop
- PGOOD, OV, UV, OT Levels
- Fault Responses
- Turn-On and Turn-Off Delays

Thermal Shutdown
- Pin Strapping for Switching Frequency: 200 kHz to 1 MHz
- Frequency Synchronization to an External Clock
  or Output Clock to Sync Out

## 2 Applications

- Test and Instrumentation
- Ethernet Switches, Optical Switches, Routers, Base Stations
- Servers
- Enterprise Storage SSD
- High-Density Power Solutions

## 3 Description

The TPS546C23 devices are PMBus 1.3 Compliant, non-isolated DC-DC converters with integrated FETs, capable of high-frequency operation and 35-A current output from a 5-mm × 7-mm package. Two TPS546C23 devices can be paralleled together to provide up to 70-A load. Current sensing is realized by sampling a small portion of the power stage current and independent on the device temperature. High-frequency, low-loss switching, provided by an integrated NexFET power stage and optimized drivers, allows for very high-density power solutions. The PMBus interface enables the AVS functions through VOUT_COMMAND, flexible converter configuration, as well as key parameters monitoring including output voltage, current, and internal die temperature. Response to fault conditions can be set to either restart, latch-off or ignore depending on system requirements.

### Device Information(1)

| DEVICE NAME | PACKAGE   | BODY SIZE         |
| ----------- | --------- | ----------------- |
| TPS546C23   | LQFN (40) | 5.00 mm × 7.00 mm |

(1) For all available packages, see the orderable addendum at the end of the data sheet.

### Simplified Application

BP3

VIN

VOUT

DIFFO RESET/PGD AVIN PVIN RSP

FB

COMP

BOOT

RT TPS546C23 SW +

ADDR0 BP6 LOAD

ADDR1 SMB_ALERT t

PMB_DATA

VSHARE PMB_CLK

BP3 ISHARE SYNC PGND

CNTL

AGND DRGND

## Table of Contents

1. Features .................................................................. 1
2. Applications ........................................................... 1
3. Description ............................................................. 1
4. Revision History..................................................... 2
5. Pin Configuration and Functions ......................... 3
6. Specifications......................................................... 5
7. Detailed Description ............................................ 14
8. Register Maps ......................................................... 34
9. Applications and Implementation ...................... 78
10. Power Supply Recommendations ...................... 87
11. Layout................................................................... 87
12. Device and Documentation Support ................. 90
13. Mechanical, Packaging, and Orderable Information ........................................................... 90

## 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

Changes from Revision A (August 2016) to Revision B

- Changed Simplified Application schematic – showing the ADDR0 and ADDR1 pins ........................................................... 1
- Changed "VSEL" to "ADDR1", and "SS" to "ADDR0" in the Absolute Maximum Ratings table ............................................ 5
- Deleted "FB" from the Input voltage VSEL, SS row of the Absolute Maximum Ratings table, and added "FB" to the SYNC, RESET/PGD row ........................................................................................................................................................ 5
- Added MIOUT(acc) spec for ambient temp ................................................................................................................................. 9
- Changed Figure 23 by adding bus-sharing connections ...................................................................................................... 15
- Deleted "Read only " from the Default Behavior column of Table 4 for CMD Codes 78h through 80h ............................... 33

Changes from Original (July 2016) to Revision A

- Changed the product status from Product Preview to Production Data ................................................................................ 1

## 5 Pin Configuration and Functions

RVF Package

40-Pin LQFN With Exposed Thermal Pad

Top View

|      |       |       |       |           |              |           |      |    |    |    |    |
| ---- | ----- | ----- | ----- | --------- | ------------ | --------- | ---- | -- | -- | -- | -- |
| COMP | DIFFO | AGND  | SYNC  | CNTL      | FB           | RSNRSP    |      |    |    |    |    |
|      |       | 40    | 39    | 38        | 37           | 36        | 35   | 34 | 33 |    |    |
|      | RT    | ADDR1 | ADDR0 | PMB\_DATA | PMB\_CLK     | SMB\_ALRT | BOOT | SW |    |    |    |
|      |       | 1     |       | 2         | 3            | 4         | 5    | 6  | 7  | 8  |    |
|      | SW    | SW    | SW    | SW        | SW           | SW        | SW   | SW |    |    |    |
|      |       |       |       | 9         | 10           | 11        | 12   | 13 | 14 | 15 | 16 |
|      |       | PGND  |       |           |              |           |      |    |    |    |    |
|      |       |       |       |           | Not to scale |           |      |    |    |    |    |

### Pin Functions

| NAME  | PIN NO. | I/O | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                             |
| ----- | ------- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ADDR0 | 3       | I   | Sets low-order 3-bits of the PMBus address. Connect a resistor between this pin and AGND.                                                                                                                                                                                                                                                                               |
| ADDR1 | 2       | I   | Sets high-order 3-bits of the PMBus address. Connect a resistor between this pin and AGND.                                                                                                                                                                                                                                                                              |
| AGND  | 38      | —   | Analog ground return for controller device. Connect this pin to PGND and DRGND at the thermal pad.                                                                                                                                                                                                                                                                      |
| AVIN  | 29      | I   | Input power to the controller. Connect a low-impedance bypass with a minimum of 1 μF to PGND. The AVIN voltage is also used for input feed-forward. PVIN and AVIN must be the same potential for accurate short circuit protection.                                                                                                                                     |
| BP3   | 27      | O   | Output of the 3.3-V onboard regulator. This regulator powers the controller and should be bypassed with a minimum of 2.2 μF to AGND. The BP3 pin is not designed to power external circuit.                                                                                                                                                                             |
| BP6   | 28      | O   | Output of the 6.5-V onboard regulator. This regulator powers the driver stage of the controller and should be bypassed with a minimum of 2.2 μF to the thermal pad (power-stage ground, essentially PGND). TI recommends using an additional 100-nF (typical) bypass capacitor for reducing ripple on BP6. The low-impedance bypassing of this pin to PGND is critical. |
| BOOT  | 7       | I/O | Bootstrap pin for the internal flying high-side driver. Connect a 100-nF (typical) capacitor from this pin to the SW pin. To reduce the voltage spike at SW, a BOOT resistor with a value between 1 Ω to 15 Ω can be placed in series with the BOOT capacitor to slow down turnon of the high-side FET.                                                                 |
| CNTL  | 40      | I   | PMBus CNTL pin. See the Supported PMBus Commands section. The CNTL pin has an internal pullup and floats high when left floating.                                                                                                                                                                                                                                       |
| COMP  | 37      | O   | Output of the error amplifier. Connect compensator network from this pin to the FB pin.                                                                                                                                                                                                                                                                                 |
| DIFFO | 35      | O   | Output of the differential remote sense amplifier. This provides remote sensing for output voltage reporting and the voltage control loop. For the loop slave device in a 2-phase configuration, the DIFFO pin can be left floating.                                                                                                                                    |
| DRGND | 26      | —   | Power ground return for controller device. This pin should be directly connected to the thermal pad on the PCB board.                                                                                                                                                                                                                                                   |

### Pin Functions (continued)

| NAME        | PIN NO. | I/O  | DESCRIPTION                                                  |
| ----------- | ------- | ---- | ------------------------------------------------------------ |
| FB          | 36      | I    | Feedback pin for the control loop. Negative input of the error amplifier. In 2-phase configuration, the FB pin of the loop slave device should be tied to the BP3 pin. |
| ISHARE      | 31      | I/O  | Current sharing signal for 2-phase operation. For a stand-alone device, the ISHARE pin can be left floating. |
| PGND        | 13-20   | —    | Power stage ground return. These pins are internally connected to the thermal pad. |
| PMB\_CLK    | 5       | I    | PMBus CLK pin. See the Supported PMBus Commands section.     |
| PMB\_DATA   | 4       | I/O  | PMBus DATA pin. See the Supported PMBus Commands section.    |
| PVIN        | 21-25   | I    | Input power to the power stage. Low-impedance bypassing of these pins to PGND is critical. |
| RESET/PGD   | 30      | I/O  | This pin is for the output voltage reset or the power-good output. The function of this pin is determined by the user-accessible bit, EN\_RESET\_B, in the MFR\_SPECIFIC\_21 (E4h) register. The default of this pin is for the power-good indicator. For output voltage reset, this pin is a logic-low input. An internal pulldown of 750 kΩ is present so this pin requires a pullup resistor to enable the programming of VOUT. As the power-good indicator, this pin is an open-drain output which floats up to external pullup when the device is operation and in regulation. During any fault or warn conditions, this pin is pulled low. For details see Table 2. The PGD pin can be left floating when not used. |
| RSP         | 33      | I    | The positive input of the remote sense amplifier. For a stand-alone device or the loop master device in a 2-phase configuration, connect the RSP pin to the output voltage at the load. For the loop slave device in a 2-phase configuration, the remote sense amplifier is not required for output voltage sensing or regulation. |
| RSN         | 34      | I    | The negative input of the remote sense amplifier. For a stand-alone device or the loop master device in a 2-phase configuration, connect the RSN pin to the ground at the load. For the loop slave device in a 2-phase configuration, the remote sense amplifier is not required for output-voltage sensing or regulation. |
| RT          | 1       | I    | Frequency-setting resistor. Connect a resistor from this pin to AGND to program the switching frequency. Do not leave this pin floating. |
| SMB\_ALRT   | 6       | O    | SMBus™ alert pin. See the Supported PMBus Commands section.  |
| SW          | 8-12    | I/O  | Switched power output of the device. Connect the output averaging filter and bootstrap capacitor to this group of pins. |
| SYNC        | 39      | I/O  | For frequency synchronization. For the stand-alone device or the loop master device in a 2-phase configuration, with external pullup to the BP6 pin, the SYNC pin will be configured as SYNC-IN pin, and will be synchronized to the rising edge of the external clock applied to this pin. Otherwise, the SYNC pin will be configured as SYNC-OUT pin. For the loop slave device in a 2-phase configuration, the SYNC pin will always be SYNC-IN, and will be synchronized to the falling edge of the incoming clock on SYNC pin. Only 50% duty cycle external clock can be applied to the 2-phase stack to realize the interleaving of 2 phases. Applying an external clock to both the loop master and the loop slave device to synchronize the stack is optional. Without the external clock, the loop master device will output a 50% duty-cycle clock to the loop slave device and the slave device will be synchronized to the falling edge of the clock. The SYNC pin can be left floating when not used. |
| VSHARE      | 32      | I/O  | Voltage sharing signal for 2-phase operation. For stand-alone device, the VSHARE pin can be left floating. |
| Thermal pad |         | —    | Package thermal pad, internally connected to PGND. The thermal pad must have adequate solder coverage for proper operation. |

## 6 Specifications

### 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted) (1)

|                |                                                              | MIN  | MAX  | UNIT |
| -------------- | ------------------------------------------------------------ | ---- | ---- | ---- |
| Input voltage  | PVIN, AVIN                                                   | –0.3 | 18   | V    |
|                | PVIN, AVIN< 2 ms transient                                   | –0.3 | 19   |      |
|                | PVIN - SW (PVIN to SW differential)                          | –0.3 | 25   |      |
|                | PVIN - SW (PVIN to SW differential, < 10-ns transient because of SW ringing) | –5   | 25   |      |
|                | BOOT                                                         | –0.3 | 37   |      |
|                | BOOT – SW (BOOT to SW differential)                          | –0.3 | 7    |      |
|                | PMB\_CLK, PMB\_DATA                                          | –0.3 | 5.5  |      |
|                | ADDR1, ADDR0                                                 | –0.3 | 3.6  |      |
|                | SYNC, RESET/PGD, CNTL, RSP, RSN, RT, ISHARE, FB              | –0.3 | 7    |      |
| Output voltage | SW                                                           | –1   | 25   | V    |
|                | SW < 100 ns transient                                        | –5   | 25   |      |
|                | BP6, COMP, DIFFO, VSHARE                                     | –0.3 | 7    |      |
|                | SMB\_ALRT                                                    | –0.3 | 5.5  |      |
|                | BP3                                                          | –0.3 | 3.6  |      |
|                | Operating junction temperature, TJ                           | –40  | 150  | °C   |
|                | Storage temperature, Tstg                                    | –55  | 150  | °C   |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

### 6.2 ESD Ratings

|                                |                                                              | VALUE | UNIT |
| ------------------------------ | ------------------------------------------------------------ | ----- | ---- |
| V(ESD) Electrostatic discharge | Human-body model (HBM), per ANSI/ESDA/JEDEC JS–001(1) (2)    | ±2000 | V    |
|                                | Charged-device model (CDM), per JEDEC specification JESD22-C101 | ±1500 |      |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.

(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

### 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|       |                           | MIN  | NOM  | MAX  | UNIT |
| ----- | ------------------------- | ---- | ---- | ---- | ---- |
| VAVIN | Controller input voltage  | 4.5  | 12   | 18   | V    |
| VPVIN | Power stage input voltage | 4.5  | 12   | 18   | V    |
| TJ    | Junction temperature      | –40  |      | 125  | °C   |

### 6.4 Thermal Information

|           | THERMAL METRIC(1)                            | TPS546C23<br/>RVF (PQFN)<br/>40 PINS | UNIT |
| --------- | -------------------------------------------- | ------------------------------------ | ---- |
| RθJA      | Junction-to-ambient thermal resistance       | 28.5                                 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance    | 18                                   | °C/W |
| RθJB      | Junction-to-board thermal resistance         | 3.8                                  | °C/W |
| ψJT       | Junction-to-top characterization parameter   | 1                                    | °C/W |
| ψJB       | Junction-to-board characterization parameter | 3.8                                  | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | 0.7                                  | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report (SPRA953).

### 6.5 Electrical Characteristics

TJ = –40°C to 125°C, VPVIN = VAVIN= 12 V, RRT = 40.2 kΩ; zero power dissipation (unless otherwise noted)

| PARAMETER                            |                                | TEST CONDITIONS                           |      | MIN   | TYP       | MAX  | UNIT |      |
| ------------------------------------ | ------------------------------ | ----------------------------------------- | ---- | ----- | --------- | ---- | ---- | ---- |
| INPUT SUPPLY                         |                                |                                           |      |       |           |      |      |      |
| VAVIN                                | Input supply voltage range     |                                           |      | 4.5   |           | 18   | V    |      |
| VPVIN                                | Power stage voltage range      |                                           |      | 4.5   |           | 18   |      |      |
| IAVIN                                | Input Operating Current        | Not switching                             |      |       | 7.7       | 12   | mA   |      |
| UVLO                                 |                                |                                           |      |       |           |      |      |      |
| VIN\_ON                              | Input turnon voltage           | Factory default setting                   |      |       | 4.5       |      | V    |      |
|                                      |                                | Programmable range, 15 different settings |      | 4.25  |           | 7.75 |      |      |
|                                      |                                | Accuracy                                  |      | –5%   |           | 5%   |      |      |
| VIN\_OFF                             | Input turnoff voltage          | Factory default setting                   |      |       | 4         |      | V    |      |
|                                      |                                | Programmable range, 15 different settings |      | 4     |           | 7.5  |      |      |
|                                      |                                | Accuracy                                  |      | –5%   |           | 5%   |      |      |
| ERROR AMPLIFIER AND FEEDBACK VOLTAGE |                                |                                           |      |       |           |      |      |      |
| VFB                                  | Feedback pin voltage           | Default setting                           |      |       | 600       |      | mV   |      |
|                                      |                                | Setpoint range(1)                         |      | 0.35  |           | 1.65 | V    |      |
|                                      |                                | Setpoint resolution(1)                    |      |       | 2-9       |      | V    |      |
| VFB(ACC)                             | Feedback pin voltage accuracy  | VFB = 600 mV, 0°C ≤ TJ ≤ 85°C(2)          |      | –0.5% |           | 0.5% | %    |      |
|                                      |                                | VFB = 600 mV, -40°C ≤ TJ ≤ 125°C(2)       |      | –1%   |           | 1%   |      |      |
|                                      |                                | VFB = 1650 mV, -40°C ≤ TJ ≤ 125°C(2)      |      | –1%   |           | 1%   |      |      |
|                                      |                                | VFB = 350 mV, -40°C ≤ TJ ≤ 125°C(2)       |      | –1.5% |           | 1.5% |      |      |
| AOL                                  | Open-loop gain(1)              |                                           |      | 80    |           |      | dB   |      |
| GBWP                                 | Gain bandwidth product(1)      |                                           |      | 15    |           |      | MHz  |      |
| IFB                                  | FB pin input bias current      | VFB = 0.6 V                               |      | –75   |           | 75   | nA   |      |
| ICOMP                                | Sourcing                       | VFB = 0 V                                 |      | 1     |           |      | mA   |      |
|                                      | Sinking                        | VFB = 1.2 V                               |      | 1     |           |      | mA   |      |
| OSCILLATOR                           |                                |                                           |      |       |           |      |      |      |
| fSW                                  | Adjustment range(2)            |                                           |      | 200   |           | 1000 | kHz  |      |
|                                      | Switching frequency(2)         | RRT = 40.2 kΩ                             |      | 450   | 500       | 550  | kHz  |      |
| VRMP                                 | Ramp peak-to-peak(1)           |                                           |      |       | VAVIN/6.5 |      | V    |      |
| VVLY                                 | Valley voltage(1)              |                                           |      |       | 1.23      |      | V    |      |
| SYNCHRONIZATION                      |                                |                                           |      |       |           |      |      |      |
| VIH(sync)                            | High-level input voltage       |                                           |      | 2.2   |           |      | V    |      |
| VIL(sync)                            | Low-level input voltage        |                                           |      |       |           | 0.80 | V    |      |
| Tpw(sync)                            | Sync input minimum pulse width | Fsw = 160kHz to 1.2MHz                    |      |       |           | 200  | ns   |      |

(1) Specified by design. Not production tested.

(2) The parameter covers 4.5 V to 18 V of AVIN.

### Electrical Characteristics (continued)

TJ = –40°C to 125°C, VPVIN = VAVIN= 12 V, RRT = 40.2 kΩ; zero power dissipation (unless otherwise noted)

| PARAMETER              |                                                              | TEST CONDITIONS                                              | MIN  | TYP  | MAX  | UNIT |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ---- | ---- | ---- |
| TMdelay(sync)          | Delay from the rising edge of SYNC input to the SW rising edge of the loop master device |                                                              |      | 515  |      | ns   |
| TS delay(sync)         | Delay from the falling edge of SYNC input to the SW rising edge of the loop slave device |                                                              |      | 515  |      | ns   |
| fSYNC                  | Synchronization frequency                                    |                                                              | 160  |      | 1200 | kHz  |
| ΔfSYNC                 | SYNC pin frequency range from free running frequency(1)      |                                                              | –20% |      | 20%  |      |
| RESET                  |                                                              |                                                              |      |      |      |      |
| VIH(reset)             | High-level input voltage(1)                                  |                                                              | 1.35 |      |      | V    |
| VIL(reset)             | Low-level input voltage                                      |                                                              |      |      | 0.8  |      |
| Tpw(reset)             | Minimum RESET\_B pulse width                                 |                                                              | 200  |      |      | ns   |
| BP6 REGULATOR          |                                                              |                                                              |      |      |      |      |
| VBP6                   | Regulator output voltage                                     | IBP6 = 10 mA                                                 | 5.85 | 6.4  | 6.95 | V    |
| VBP6(do)               | Regulator dropout voltage                                    | VAVIN – VBP6, VAVIN = 4.5 V, IBP6 = 25 mA                    | 100  | 200  | 400  | mV   |
| IBP6SC                 | Regulator short-circuit current(1)                           | VAVIN = 12 V                                                 |      | 150  |      | mA   |
| VBP6UV                 | Regulator UVLO voltage(1)                                    |                                                              |      | 3.73 |      | V    |
| VBP6UV(hyst)           | Regulator UVLO voltage hysteresis (1)                        |                                                              |      | 270  |      | mV   |
| BOOTSTRAP              |                                                              |                                                              |      |      |      |      |
| VBOOT(drop)            | Bootstrap voltage drop                                       | IBOOT = 5 mA                                                 |      |      | 150  | mV   |
| BP3 REGULATOR          |                                                              |                                                              |      |      |      |      |
| VBP3                   | 3-V regulator output voltage                                 | VAVIN ≥ 4.5 V, IBP3 = 5 mA                                   | 3    | 3.2  | 3.4  | V    |
| IBP3SC                 | 3-V regulator short-circuit current(1)                       |                                                              | 18   | 35   |      | mA   |
| PWM                    |                                                              |                                                              |      |      |      |      |
| TON(min)               | Minimum controllable pulse width(1)                          |                                                              |      |      | 100  | ns   |
| TOFF(min)              | Minimum off-time(1)                                          |                                                              |      | 515  | 550  | ns   |
| SOFT START             |                                                              |                                                              |      |      |      |      |
| TON\_RISE              | Soft-start time                                              | Factory default setting                                      |      | 3    |      | ms   |
|                        |                                                              | Programmable range, 16 discrete settings(1) (3)              | 0    |      | 100  |      |
|                        |                                                              | Accuracy, TON\_RISE = 3 ms, VOUT\_COMMAND = 0.95 V           | –10% |      | 10%  |      |
| TON\_MAX\_FAULT\_LIMIT | Upper limit on the time to power up the output               | Factory default setting(4)                                   |      | 0    |      | ms   |
|                        |                                                              | Programmable range, 16 discrete settings(1) (4)              | 0    |      | 100  |      |
|                        |                                                              | Accuracy(1)                                                  | –10% |      | 10%  |      |
| TON\_DELAY             | Turn-on delay                                                | Factory default setting                                      |      | 0    |      | ms   |
|                        |                                                              | Programmable range, 16 discrete settings (1)                 | 0    |      | 100  |      |
|                        |                                                              | Accuracy(1)                                                  | –10% |      | 10%  |      |
| SOFT STOP              |                                                              |                                                              |      |      |      |      |
| TOFF\_FALL             | Factory default setting(5)                                   | Factory default setting(5)                                   |      | 0    |      | ms   |
|                        |                                                              | Soft-stop time Programmable range, 16 discrete settings(1)(5) | 0    |      | 100  |      |
|                        |                                                              | Accuracy, TOFF\_FALL = 1 ms, VOUT\_COMMAND = 0.95V           | –10% |      | 10%  |      |
| TOFF\_DELAY            | Turn-off delay  (1)                                          | Factory default setting                                      |      | 0    |      | ms   |
|                        |                                                              | Programmable range, 16 discrete settings(1)                  | 0    |      | 100  |      |
|                        |                                                              | Accuracy(1)                                                  | –10% |      | 10%  |      |
| REMOTE SENSE AMPLIFIER |                                                              |                                                              |      |      |      |      |

(3) The setting of TON_RISE of 0 ms means the unit to bring its output voltage to the programmed regulation value as quickly as possible, which results in an effective TON_RISE time of 1 ms (fastest time supported).

(4) The setting of TON_MAX_FAULT_LIMIT of 0 means disabling TON_MAX_FAULT response and reporting completely.

(5) The setting of TOFF_FALL of 0 ms means the unit to bring its output voltage down to 0 as quickly as possible, which results in an effective TOFF_FALL time of 1 ms (fastest time supported).

### Electrical Characteristics (continued)

TJ = –40°C to 125°C, VPVIN = VAVIN= 12 V, RRT = 40.2 kΩ; zero power dissipation (unless otherwise noted)

| PARAMETER      |                                             | TEST CONDITIONS       | MIN  | TYP  | MAX      | UNIT |
| -------------- | ------------------------------------------- | --------------------- | ---- | ---- | -------- | ---- |
| V DIFFO(ERROR) | Error Voltage from DIFFO to (RSP –<br/>RSN) | (VRSP – VRSN) = 0.6 V | –4   |      | 4        | mV   |
|                |                                             | (VRSP – VRSN) = 1.2 V | –5   |      | 5        | mV   |
|                |                                             | (VRSP – VRSN) = 3 V   | –15  |      | 15       | mV   |
| BW             | Closed-loop bandwidth(1)                    |                       | 2    |      |          | MHz  |
| VDIFFO(max)    | Maximum DIFFO output voltage                |                       |      |      | VBP6–0.2 | V    |
| IDIFFO         | DIFFO sourcing current                      |                       | 1    |      |          | mA   |
|                | DIFFO sinking current                       |                       | 1    |      |          | mA   |

POWER STAGE

| RHS         | High-side power device on-resistance                         | VBOOT - VSW = 4.5 V, TJ = 25°C |      | 3.5  |      | mΩ   |
| ----------- | ------------------------------------------------------------ | ------------------------------ | ---- | ---- | ---- | ---- |
|             |                                                              | VBOOT - VSW = 6.3V, TJ = 25°C  |      | 3.2  |      | mΩ   |
| RLS         | Low-side power device on-resistance                          | VAVIN = 4.5 V, TJ = 25°C       |      | 1.5  |      | mΩ   |
|             |                                                              | VAVIN ≥ 12 V, TJ = 25°C        |      | 1.4  |      | mΩ   |
| TDEAD(LtoH) | Power stage driver dead-time from Low-side off to High-side on | VAVIN ≥ 12 V, TJ = 25°C(1)     |      | 15   |      | ns   |
| TDEAD(HtoL) | Power stage driver dead-time from High-side off to Low-side on | VAVIN ≥ 12 V, TJ = 25°C(1)     |      | 15   |      | ns   |

CURRENT SHARING

| ISHARE(acc) | Output current sharing accuracy of two devices defined as the ratio of the current difference between two devices | IOUT ≥ 20 A per device | –15% |      | 15%  |      |
| ----------- | ------------------------------------------------------------ | ---------------------- | ---- | ---- | ---- | ---- |
|             | Output current sharing accuracy of two devices defined as the current difference between each device and the half of total current | IOUT < 20 A per device | –3   |      | 3    | A    |

LOW-SIDE CURRENT LIMIT PROTECTION

| tOFF(OC)                | Off time between restart attempts(1)                     |                         |      | 7 × TON\_RI SE |      | ms   |
| ----------------------- | -------------------------------------------------------- | ----------------------- | ---- | -------------- | ---- | ---- |
| IOUT\_OC\_FAUL T\_LIMIT | Output current overcurrent fault threshold               | Factory default setting |      | 42             |      | A    |
|                         |                                                          | Programmable range      | 5    |                | 52   |      |
| INEGOC                  | Negative output current overcurrent protection threshold |                         | –60  | –40            | –20  | A    |
| IOUT\_OC\_WAR           | Output current overcurrent warning threshold             | Factory default setting |      | 37             |      | A    |
| N\_LIMIT                | threshold                                                | Programmable range      | 4    |                | 50   |      |
| IOC(acc)                | Output current overcurrent fault accuracy                | IOUT ≥ 20 A             | –15% |                | 15%  |      |

HIGH-SIDE SHORT CIRCUIT PROTECTION

| IHSOC | High-side short-circuit protection fault threshold | (VBOOT-VSW) = 6.3V, TJ = 25°C |      | 65   |      | A    |
| ----- | -------------------------------------------------- | ----------------------------- | ---- | ---- | ---- | ---- |

POWER GOOD (PGOOD) AND OVERVOLTAGE/UNDERVOLTAGE WARNING

| RPGD       | PGD pulldown resistance                                      | VDIFFO = 0, IPGD = 5 mA           |      | 45   | 60   | Ω      |
| ---------- | ------------------------------------------------------------ | --------------------------------- | ---- | ---- | ---- | ------ |
| IPGD(OH)   | Output high open drain leakage current into PGD pin          | VPGD = 5 V                        |      |      | 15   | μA     |
| VPGD(OL)   | PGD pin output low level voltage at no supply voltage        | VAVIN=0, IPGD = 80 μA             |      |      | 0.8  | V      |
| VFBOVW     | Overvoltage warning threshold at FB pin (PGD fault threshold on rising) | Factory default, at VREF = 600 mV | 108  | 112  | 116  | % VREF |
| VFBUVW     | Undervoltage warning threshold at FB pin (PGD fault threshold on falling) | Factory default, at VREF = 600 mV | 84   | 88   | 92   | % VREF |
| VPGD(rise) | Undervotlage warning threshold de-assertation threshold at FB pin | VREF = 600 mV                     |      | 95   |      | % VREF |
| VPGD(fall) | Overvotlage warning threshold de-assertation threshold at FB pin | VREF = 600 mV                     |      | 105  |      | % VREF |

OUTPUT OVERVOLTAGE AND UNDERVOLTAGE FAULT PROTECTION

### Electrical Characteristics (continued)

TJ = –40°C to 125°C, VPVIN = VAVIN= 12 V, RRT = 40.2 kΩ; zero power dissipation (unless otherwise noted)

| PARAMETER               |                                                              | TEST CONDITIONS                                 | MIN   | TYP  | MAX  | UNIT   |
| ----------------------- | ------------------------------------------------------------ | ----------------------------------------------- | ----- | ---- | ---- | ------ |
| VFBOVF                  | Overvoltage fault threshold at FB pin                        | Factory default, at VREF = 600 mV               | 113   | 117  | 121  | % VREF |
| VFBUVF                  | Undervoltage fault threshold at FB pin                       | Factory default, at VREF = 600mV                | 79    | 83   | 87   | % VREF |
| OUTPUT VOLTAGE TRIMMIN8 |                                                              |                                                 |       |      |      |        |
| VFBRES                  | Resolution of FB steps with VOUT\_COMMAND, Trim and Margin   |                                                 |       | 2 -9 |      | V      |
| VOUT\_TRANSITION\_RATE  | Output voltage transition rate                               | Factory default setting                         |       | 1    |      | mV/μs  |
|                         |                                                              | Programmable range, 8 discrete settings         | 0.067 |      | 1.5  |        |
|                         |                                                              | Accuracy                                        | –10%  |      | 10%  |        |
| VOUT\_SCALE\_LOOP       | Feedback loop scaling factor                                 | Factory default setting                         |       | 1    |      |        |
|                         |                                                              | Programmable range, 3 discrete settings         | 0.25  |      | 1    |        |
| VOUT\_COMMA ND          | Output voltage programmable register value, multiply by 2-9 to get output voltage | Factor default setting                          |       | 307  |      |        |
|                         |                                                              | Programmable<br/>range/VOUT\_SCALE\_LOOP = 1(1) | 179   |      | 845  |        |
|                         |                                                              | VOUT\_SCALE\_LOOP = 0.5(1)                      | 358   |      | 1690 |        |
|                         |                                                              | VOUT\_SCALE\_LOOP = 0.25(1)                     | 716   |      | 2816 |        |

TEMPERATURE SENSE AND THERMAL SHUTDOWN

| Tsd               | Junction thermal shutdown temperature(1)               |                         | 135  | 145  | 160  | °C   |
| ----------------- | ------------------------------------------------------ | ----------------------- | ---- | ---- | ---- | ---- |
| THYST             | Junction thermal shutdown hysteresis (1)               |                         |      | 25   |      | °C   |
| OT\_FAULT\_LIMI T | Internal overtemperature fault limit (1)               | Factory default setting |      | 145  |      | °C   |
|                   |                                                        | Programmable range      | 120  |      | 165  | °C   |
| OT\_WARN\_LIMI T  | Internal overtemperature warning limit (1)             | Factory default setting |      | 120  |      | °C   |
|                   |                                                        | Programmable range      | 100  |      | 140  | °C   |
| TOT(hys)          | Internal overtemperature fault, warning hysteresis (1) |                         | 15   | 20   | 25   | °C   |

MEASUREMENT SYSTEM

| MVOUT(rng)  | Output voltage measurement range(1)          |                     | 0    |      | 5.8  | V    |
| ----------- | -------------------------------------------- | ------------------- | ---- | ---- | ---- | ---- |
| MVOUT(acc)  | Output voltage measurement accuracy          | DIFFO = 1.2 V       | –2%  |      | 2%   | %    |
| MVOUT(lsb） | Output voltage measurement bit resolution(1) |                     |      | 2-9  |      | V    |
| MIOUT(rng)  | Output current measurement range(1)          |                     | 0    |      | 52   | A    |
| MIOUT(acc)  | Output current measurement accuracy          | IOUT 20 A, TJ= 25°C | –10% | 0    | 10%  |      |
|             |                                              | IOUT ≥ 20 A         | –15% |      | 15%  |      |
|             |                                              | 3A ≤ IOUT <20 A     | –3   |      | 3    | A    |
| MIOUT(lsb)  | Output current measurement bit resolution(1) |                     |      | 62.5 |      | mA   |
| MTSNS(rng)  | Internal temperature sense range(1)          |                     | –40  |      | 165  | °C   |
| MTSNS(acc)  | Internal temperature sense accuracy(1)       | –40°C ≤ TJ ≤ 165°C  | –5   |      | 5    |      |
| MTSNS(lsb)  | Internal temperature sense bit resolution(1) |                     |      | 1    |      |      |

PMBUS INTERFACE

| VIH(PMBUS) | High-level input voltage on PMB\_CLK, PMB\_DATA, CNTL        |                                                             | 1.35 |      |      | V    |
| ---------- | ------------------------------------------------------------ | ----------------------------------------------------------- | ---- | ---- | ---- | ---- |
| VIL(PMBUS) | Low-level input voltage on PMB\_CLK, PMB\_DATA, CNTL         |                                                             |      |      | 0.8  | V    |
| VhysCNTL   | Hysteresis on CNTL                                           |                                                             |      | 170  |      | mV   |
| IIH(PMBUS) | Input high level current into PMB\_CLK, PMB\_DATA            |                                                             | –10  |      | 10   | μA   |
| IIL(PMBUS) | Input low level current into PMB\_CLK, PMB\_DATA             |                                                             | –10  |      | 10   | μA   |
| ICNTL      | CNTL pin pullup current                                      |                                                             | 5    |      | 10   | μA   |
| VOL(PMBUS) | Output low level voltage on PMB\_DATA, SMB\_ALRT             | VAVIN > 4.5 V, input current to PMB\_DATA, SMB\_ALRT = 4 mA |      |      | 0.4  | V    |
| IOH(PMBUS) | Output high level open drain leakage current into PMB\_DATA, SMB\_ALRT | Voltage on PMB\_DATA, SMB\_ALRT = 5.5 V                     |      |      | 10   | μA   |

### Electrical Characteristics (continued)

TJ = –40°C to 125°C, VPVIN = VAVIN= 12 V, RRT = 40.2 kΩ; zero power dissipation (unless otherwise noted)

| PARAMETER  |                                                              | TEST CONDITIONS                       | MIN  | TYP  | MAX  | UNIT |
| ---------- | ------------------------------------------------------------ | ------------------------------------- | ---- | ---- | ---- | ---- |
| IOL(PMBUS) | Output low level open drain leakage current into PMB\_DATA, SMB\_ALRT | Voltage on PMB_DATA, SMB_ALRT < 0.4 V | 4    |      |      | mA   |
| FPMBUS     | PMBus operating frequency range                              | Slave mode                            | 10   |      | 400  | kHz  |

### 6.6 Typical Characteristics

VPIN = VAVIN = 12 V, TA = 25 ºC, RRT = 40.2 kΩ (unless otherwise specified). Safe operating area curves were measured using a Texas Instruments evaluation module (EVM).

#### Figure 1. Efficiency vs Output Current

| 100 | 100 |
| --- | --- |
| 95  | 95  |
| 90  | 90  |
| (%) | (%) |
| 85  | 85  |
| 80  | 80  |
| 75  | 75  |
| 70  | 70  |
| 65  | 65  |
| 60  | 60  |

VOUT = 0.8 V

~~V~~OUT~~= 1 V~~

Load Current (A)

VIN = 5 V

L = 300 nH

Snubber = 1 nF + 1Ω

fSW = 300 kHz

RDCR = 0.2 mΩ

RBOOT = 0 Ω

#### Figure 2. Efficiency vs Output Current

| 100 | 100 |
| --- | --- |
| 95  | 95  |
| 90  | 90  |
| (%) | (%) |
| 85  | 85  |
| 80  | 80  |
| 75  | 75  |
| 70  | 70  |
| 65  | 65  |
| 60  | 60  |

VOUT = 0.8 V

~~V~~OUT~~= 1 V~~

Load Current (A)

VIN = 12 V

L = 300 nH

Snubber = 1 nF + 1Ω

fSW = 300 kHz

RDCR = 0.2 mΩ

RBOOT = 0 Ω

#### Figure 3. Efficiency vs Output Current

#### Figure 4. Efficiency vs Output Current

### Typical Characteristics (continued)

VPIN = VAVIN = 12 V, TA = 25 ºC, RRT = 40.2 kΩ (unless otherwise specified). Safe operating area curves were measured using a Texas Instruments evaluation module (EVM).

|     |     | VAVIN = 4.5 V | VAVIN = 12 V | VAVIN = 18 V |
| --- | --- | ------------- | ------------ | ------------ |
| 1.9 | 1.8 | 4.8           | 4.6          | 4.4          |
| 1.7 | 1.6 | 3.8           | 3.6          | 3.4          |
| 1.5 | 1.4 | 3.2           | 3.0          | 2.8          |
| 1.1 | 1.0 | 2.6           | 2.4          | 2.2          |

-40  -25  -10  5  20  35  50  65  80  95 110  125

Junction Temperature (°C)  D001

#### Figure 5. Low-Side MOSFET On-Resistance (RDS(on)) vs Junction Temperature

#### Figure 6. High-Side MOSFET On-Resistance (RDS(on)) vs Junction Temperature

| Frequency | Voltage | Switching | Feedback |
| --------- | ------- | --------- | -------- |
| 601       | 600.5   | 1.02      | 1.015    |
| 600       | 599.5   | 1.01      | 0.995    |
| 598.5     | 598     | 0.985     | 0.98     |
| 597.5     | 597     | 0.975     | 0.97     |

-40  -25  -10  5  20  35  50  65  80  95 110  125

Junction Temperature (°C)  D001

VFB = 600 mV

#### Figure 7. Feedback Voltage vs Junction Temperature

#### Figure 8. Normalized Switching Frequency vs Junction Temperature

| Current | Quiescent Voltage |
| ------- | ----------------- |
| 10      | 6.9               |
| 9.5     | 6.8               |
| 9       | 6.7               |
| 8.5     | 6.6               |
| 8       | 6.5               |
| 7.5     | 6.4               |
| 7       | 6.3               |

-40  -25  -10  5  20  35  50  65  80  95 110  125

Junction Temperature (°C)  D001

IBP6 = 10 mA  VPVIN = VAVIN= 12 V

#### Figure 9. Non-Switching Input Current (IAVIN) vs Junction Temperature

#### Figure 10. BP6 Voltage vs Junction Temperature

### Typical Characteristics (continued)

VPIN = VAVIN = 12 V, TA = 25 ºC, RRT = 40.2 kΩ (unless otherwise specified). Safe operating area curves were measured using a Texas Instruments evaluation module (EVM).

| (V)  | Voltage    |           |   |
| ---- | ---------- | --------- | - |
|      | Resistance | Pull-Down |   |
| 3.4  | 100        |           |   |
| 3.35 | 90         |           |   |
| 3.3  | 80         |           |   |
| 3.25 | 70         |           |   |
| 3.2  | 60         |           |   |
| 3.15 | 50         |           |   |
| 3.1  | 40         |           |   |
| 3.05 | 30         |           |   |
| 3    | 20         |           |   |
|      | 10         |           |   |
|      | 0          |           |   |

Junction Temperature (°C)

IBP3 = 5 mA VPVIN = VAVIN= 12 V

Figure 11. BP3 Voltage vs Junction Temperature

#### Figure 12. PGOOD Pulldown Resistance vs Junction Temperature

| (V)     | Voltage |   |          |   |   |
| ------- | ------- | - | -------- | - | - |
| Turn-On |         |   | Turn-Off |   |   |
| 4.6     |         |   | 4.2      |   |   |
| 4.55    |         |   | 4.15     |   |   |
| 4.5     |         |   | 4.1      |   |   |
|         |         |   | 4.05     |   |   |
| 4.45    | 4       |   |          |   |   |
| 4.4     |         |   | 3.95     |   |   |
| 4.35    |         |   | 3.9      |   |   |
| 4.3     |         |   | 3.85     |   |   |
|         |         |   | 3.8      |   |   |

Junction Temperature (°C)

VIN_ON = 4.5 V

#### Figure 13. Turnon Voltage vs Junction Temperature

#### Figure 14. Turnoff Voltage vs Junction Temperature

| %       | Accuracy |                |       |   |
| ------- | -------- | -------------- | ----- | - |
| Current |          | Output-Voltage |       |   |
| 2       |          | 0.25           |       |   |
| 1       |          |                |       |   |
|         |          | 0              | -0.25 |   |
|         | -1       | -0.5           |       |   |
| -2      | -0.75    |                |       |   |
| -3      | -1       |                |       |   |
| -4      |          |                |       |   |

Junction Temperature (°C)

IOUT = 20 A VPVIN = VAVIN= 12 V

#### Figure 15. READ_IOUT Accuracy vs Junction Temperature

#### Figure 16. READ_VOUT Accuracy vs Junction Temperature

### Typical Characteristics (continued)

VPIN = VAVIN = 12 V, TA = 25 ºC, RRT = 40.2 kΩ (unless otherwise specified). Safe operating area curves were measured using a Texas Instruments evaluation module (EVM).

|           |       | Threshold (%) |             |       |
| --------- | ----- | ------------- | ----------- | ----- |
| 1.15      | 4     | 3             | 1.1         |       |
| 1.05      | 2     | 1             | 1           | (OCP) |
| High-Side | 1     | (OCF)         | Protection  | 0     |
| 0.95      | Fault | Normalized    | Overcurrent |       |
| 0.9       | -2    |               |             |       |
| 0.85      | -3    |               |             |       |
| 0.8       | -4    |               |             |       |

-40  -25  -10   5  20  35  50  65  80  95 110 125  -40  -25   -10  5  20  35  50  65  80  95 110 125

Junction Temperature (°C)  D001  Junction Temperature (°C)  D001

BOOT – SW = 6.5 V  VPVIN = VAVIN= 12 V  OCF = 20 A  VPVIN = VAVIN= 12 V

#### Figure 17. High-Side Overcurrent Protection vs Junction Temperature

#### Figure 18. Overcurrent Fault Protection (OCF) Accuracy vs Junction Temperature

| -50 | 110      |         |     |                    |
| --- | -------- | ------- | --- | ------------------ |
| -45 | (A)      | C)      | 100 |                    |
| -40 | q        | Limit   | (   | Temperature        |
| -35 | Current  | 90      |     |                    |
| -30 | Negative | Ambient | 80  | Natural Convection |
| -25 | 100 LFM  |         |     |                    |
| -20 | 200 LFM  |         |     |                    |
| -15 | 300 LFM  |         |     |                    |
| -40 | -25      | -10     | 5   | 20                 |
| 35  | 50       | 65      | 80  | 95                 |
| 110 | 125      | 0       | 4   | 8                  |
| 12  | 16       | 20      | 24  | 28                 |
| 32  | 36       |         |     |                    |

#### Figure 19. Negative Overcurrent Limit vs Junction Temperature

#### Figure 20. Safe Operating Area

|         | 110     | 110         |                    |    |
| ------- | ------- | ----------- | ------------------ | -- |
| C)      | 100     | C)          | 100                |    |
| q       | (       | Temperature | Temperature        |    |
| 90      | 90      |             |                    |    |
| Ambient | Ambient | 80          | Natural Convection |    |
| 100 LFM | 100 LFM |             |                    |    |
| 200 LFM | 200 LFM |             |                    |    |
| 300 LFM | 300 LFM |             |                    |    |
| 400 LFM | 400 LFM |             |                    |    |
| 70      | 70      |             |                    |    |
| 0       | 4       | 8           | 12                 | 16 |
| 20      | 24      | 28          | 32                 | 36 |

#### Figure 21. Safe Operating Area

#### Figure 22. Safe Operating Area

## 7 Detailed Description

### 7.1 Overview

The devices are PMBus 1.3 compliant 35-A, high-performance, synchronous buck converters with two integrated
N-channel NexFET™ power MOSFETs, enabling high-power density and minimal PCB area. These devices
implement the industry-standard fixed switching frequency, voltage-mode control with input feed-forward topology
that responds instantly to input voltage change. These devices can be synchronized to the external clock to
eliminate beat noise and reduce EMI and EMC. Monotonic prebias capability eliminates concerns about
damaging sensitive loads. Two devices can be paralleled together to provide up to 70-A load. Current sensing for
overcurrent protection, current reporting and current sharing between two devices are implemented by sampling
a small portion of the power stage current which provides accurate information independent on the device
temperature. The integrated PMBus interface capability provides precise current, voltage, and internal die-
temperature monitoring, as well as many user-programmable configuration options including Adaptive Voltage
Scaling (AVS) function through standard VOUT_COMMAND on the PMBus.

### 7.2 Functional Block Diagram

| AVIN                                   | BP6                   | BOOT          |
| -------------------------------------- | --------------------- | ------------- |
| BP6                                    | Linear Regulators     | PVIN          |
| BP3                                    | RT                    | High-Side FET |
| SYNC                                   | COMP                  | SW            |
| R                                      | Anti-Cross-Conduction | BP6           |
| Level Shifter                          | +                     | +             |
| VREF                                   | +                     | VSHARE        |
| ISHARE                                 | Current Sharing       | OC event      |
| Overcurrent detection, current sensing | Average IOUT          | PGND          |
| DRGND                                  | AGND                  | PMB\_CLK      |
| Analog Inputs and ADC                  | Fault                 | RSN           |
| PMBus 1.3 Interface                    | SMB\_ALRT             | Commands      |
| EEPROM                                 | Remote Sense          | RSP           |
| CNTL                                   | Sense Amplifier       |               |
| ADDR0                                  | ADDR1                 | RESET/PGD     |
| DIFFO                                  |                       |               |

### 7.3 Feature Description

#### 7.3.1 2-Phase Application

Figure 23 shows the setup for a 2-phase application using two devices.

##### Figure 23. 2-Phase Application

| Vin       | BP3       | BP3       |          |           |           |      |      |           |       |
| --------- | --------- | --------- | -------- | --------- | --------- | ---- | ---- | --------- | ----- |
| DIFFO     | PGD       | AVIN      | PVIN     | RSP       | RSP       | PVIN | AVIN | ~~RESET~~ | DIFFO |
| FB        | RESET     | BOOT      | BOOT     | PGD       | COMP      |      |      |           |       |
| VOUT      | RT        | TPS546C23 | SW       | SW        | TPS546C23 | RT   |      |           |       |
| ADDR1     | BP6       | BP6       | ADDR1    | BP3       | BP3       |      |      |           |       |
|           | PMB\_DATA | PGND      | PGND     | PMB\_DATA |           |      |      |           |       |
| SMB\_ALRT | VSHARE    | PMB\_CLK  | PMB\_CLK | VSHARE    |           |      |      |           |       |
| ISHARE    | SYNC      | DRGND     | DRGND    | CNTL      | AGND      |      |      |           |       |
| VSHARE    | ISHARE    | SYNC      | DRGND    | DRGND     | CNTL      | AGND |      |           |       |

#### 7.3.2 Linear Regulators BP3 and BP6

The devices have two onboard linear regulators to provide suitable power for the internal circuitry of the device. Bypass the BP3 and BP6 pins externally for the converter to function properly. The BP3 pin requires a minimum of 2.2 μF of capacitance connected to AGND. The BP6 pin requires a minimum 2.2 μF of capacitance connected to PGND. TI recommends using a 4.7-μF capacitor and an additional 100-nF capacitor to reduce the ripple on the BP6 pin.

NOTE

Place bypass capacitors as close as possible to the device pins, with a minimum return loop back to ground and the return loop should be kept away from fast switching voltage and main current path. For more information, see the Layout section. Poor bypassing can degrade the performance of the regulator.

The use of the internal regulators to power other circuits is not recommended because the loads placed on the regulators might adversely affect operation of the controller.

#### 7.3.3 Input Undervoltage Lockout (UVLO)

The devices provide flexible user adjustment of the undervoltage lockout (UVLO) threshold and hysteresis. Two PMBus commands, VIN_ON (35h) and VIN_OFF (36h), allow the user to independently set turnon and turnoff thresholds of these input voltages, with a minimum of 4-V turnoff to a maximum 7.75-V turnon. For more information, see Table 4.

#### 7.3.4 Turnon and Turnoff Delay and Sequencing

The devices provide many sequencing options. Using the ON_OFF_CONFIG command, the device can be configured to start up whenever the input voltage is above the UVLO threshold, to require an additional signal on the CNTL pin, to receive an update to the OPERATION command through the PMBus interface, or a combination of these configurations. When the gating signal as specified by the ON_OFF_CONFIG command is asserted, a programmable turnon delay can be set with the TON_DELAY command to delay the start of regulation. Similarly, a programmable turnoff delay can be set with the TOFF_DELAY command to delay the stop of regulation once the gating signal is deasserted. Delay times are specified in milliseconds (ms), from 0 to 100 ms.

### Feature Description (continued)

Figure 24 shows control of the start-up and shutdown operations of the device when the device is configured to respond to both the CNTL signal and the OPERATION command. The device can also be configured to independently use either the CNTL signal or the OPERATION command, or to convert power when a sufficient input voltage is available.

#### Figure 24. Turnon Controlled by Both Operation(1) and Control (1)

| TON\_DELAY    |      | TOFF\_DELAY   |                |     |   |   |   |
| ------------- | ---- | ------------- | -------------- | --- | - | - | - |
|               |      | ~~TON\_RISE~~ | ~~TOFF\_FALL~~ | VIN |   |   |   |
| OPERATION\[7] | OFF  | ON            | OFF            |     |   |   |   |
| CNTL          | VOUT |               |                |     |   |   |   |
| Time          |      |               |                |     |   |   |   |

#### 7.3.5  Voltage Reference

A reference digital-to-analog converter (DAC) with a 350-mV to 1650-mV range and 2–9-V (1.953 mV) resolution connects to the noninverting input of the error amplifier. The tight tolerance on the reference voltage allows the user to design power supply with very-high DC accuracy.

#### 7.3.6  Differential Remote Sense and Compensation

The devices implement a differential remote-sense amplifier to provide excellent load regulation by cancelling IR-drop in high-current applications. The RSP and RSN pins should be kelvin-connected to the output capacitor bank directly at the load, and routed back to the device as a tightly coupled differential pair. Ensure that these traces are isolated from fast switching signals and high current paths on the final PCB layout, as these can add differential-mode noise. Optionally, use a small coupling capacitor (1-nF typical) between the RSP and RSN pins to improve noise immunity. The output of the differential remote sense amplifier (DIFFO) is used for output voltage setting and error amplifier frequency compensation local to the device as shown in Figure 25.

The devices use voltage mode control with input feedforward. Frequency compensation can be accomplished using standard Type III techniques as shown in Figure 25.

In 2-phase configuration, the FB pin of the loop slave device should be tied to BP3 and the typical application circuit is shown in Figure 23. The loop master passes the internal COMP voltage through VSHARE pin to the loop slave device. For more information, see the Current Sharing section.

Additionally, the voltage at the DIFFO pin is digitized, averaged to reduce measurement noise and continually stored in the READ_VOUT command, enabling output voltage telemetry.

(1)  Bit 7 of OPERATION is used to control power conversion.

### Feature Description (continued)

#### 7.3.7 Set Output Voltage and Adaptive Voltage Scaling (AVS)

A voltage divider from the DIFFO pin to the FB pin is typically required to set the nominal output voltage like the one formed by R1 and RBIAS resistors shown in Figure 25 and the resulted output voltage is shown in Equation 1.

VOUT = EA_REF × (RBIAS + R1) / RBIAS                                                                                  (1)

##### 7.3.7.1 VOUT_COMMAND

To allow PMBus devices to map between the nominal commanded voltage and the voltage at the control circuit input FB (VOUT divided down to match the reference voltage EA_REF), the device uses the VOUT_SCALE_LOOP command.

VOUT_SCALE_LOOP = RBIAS / (RBIAS + R1)                                                                                (2)

Table 1 lists the range of valid VOUT_COMMAND values which are dependent upon the configured
VOUT_SCALE_LOOP (29h) command

###### Table 1. FB Resistor Divider Ratio and VOUT_COMMAND Data Valid Range

| VOUT\_SCALE\_LOOP | RESISTOR DIVIDER (IN Figure 25) | OUTPUT VOLTAGE RANGE (V) min | max  | VOUT\_COMMAND DATA VALID RANGE min | max  |
| ----------------- | ------------------------------- | ---------------------------- | ---- | ---------------------------------- | ---- |
| 1                 | Unnecessary                     | 0.35                         | 1.65 | 179                                | 845  |
| 0.5               | 1:1                             | 0.7                          | 3.3  | 358                                | 1690 |
| 0.25              | 1:3                             | 1.4                          | 5.5  | 716                                | 2816 |

If the value programmed to VOUT_COMMAND exceeds the value stored in either VOUT_MIN or VOUT_MAX. In this case, VOUT_COMMAND will be set to the appropriate VOUT_MIN or VOUT_MAX value (whichever was violated). For the specific status bits set in either case, see the command descriptions for the VOUT_MIN (28h) or VOUT_MAX (24h) command.

##### 7.3.7.2 VREF_TRIM

The nominal output voltage of the converter can also be adjusted by changing the feedback voltage, VFB, using the VREF_TRIM command. The adjustment range is from –64 × 1.953 mV to +63 × 1.953 mV from the nominal FB voltage. This command adjusts the final output voltage of the converter to a high degree of accuracy without relying on high-precision feedback resistors. The resolution of the adjustment is approximately 1.953 mV.

##### 7.3.7.3 MARGIN

The devices also allow simple testing of the output-voltage margin, by applying a either a positive or negative offset to the feedback voltage. The STEP_VREF_MARGIN_HIGH (MFR_SPECIFIC_05) (D5h) and STEP_VREF_MARGIN_LOW (MFR_SPECIFIC_06) (D6h) commands control the size of the applied high offset or low offset (respectively). The adjustment range is from –64 × 1.953 mV to 31 × 1.953 mV from the nominal feedback voltage. The OPERATION command toggles the converter between the following three states:

- Margin none (no output margining)
- Margin high
- Margin low

Use Equation 3 to calculate the resulted internal-reference voltage.

EA_REF = [(VOUT_COMMAND × VOUT_SCALE_LOOP) + (VREF_TRIM + STEP_VREF_MARGIN_HIGH × OPERATION[5] + STEP_VREF_MARGIN_LOW × OPERATION[4])] × 1.953 mV                               (3)

The total adjustable range of the output voltage, including VOUT_COMMAND, MARGIN, and VREF_TRIM, is limited by the internal reference DAC of 0.35 V – 1.65 V. For more information on the implementation, see the Supported PMBus Commands section.

NOTE

- The VOUT_SCALE_LOOP is limited to only 3 possible options: 1 (default, no bottom resistor required for the divider), 0.5, and 0.25.
- When VOUT_SCALE_LOOP is set to 1 (default), no bottom RBIAS resistor is required. The reference voltage is equal to the output voltage, which allows tighter system DC accuracy by removing the resistor divider tolerance.
- If the divider ratio, RBIAS / (RBIAS + R1), does not match the programmed VOUT_SCALE_LOOP, the user should be aware that the actual output voltage determined by Equation 1 and Equation 3 may not match the programmed VOUT_COMMAND.

#### 7.3.8 Reset VOUT

Without power cycling, the VOUT_COMMAND value and the corresponding output voltage can be reset to the default value which is latched when the devices are powered up from AVIN. When the RESET/PGD pin is pulled low, the digital core sets the VOUT_COMMAND value to the default value. Figure 26 shows the timing diagram for resetting the output voltage. When the RESET/PGD pin is asserted low, after a short delay (less than 2 μs), the output voltage begins to transition from the current value to the default VOUT_COMMAND value according to the slew-rate set in the VOUT_TRANSITION_RATE command. The VOUT_COMMAND value does not change to any values programmed in the VOUT_COMMAND register while the RESET/PGD pin is held low. The reset_vout status bit in the STATUS_MFR_SPECIFIC (80h) register is set for indication.

In the case of fault restart, the user has access to allow the VOUT_COMMAND value to be reset to the initial boot-up voltage by setting the RST_VOUT_oSD Bit in the OPTIONS (MFR_SPECIFIC_21) (E5h) register.

##### Figure 26. Output Voltage Reset

SLUSCC7B – JULY 2016 – REVISED NOVEMBER 2016

VRESET_B

| VOUT | ~~Pre-AVS V~~OUT | Default Output Voltage |
| ---- | ---------------- | ---------------------- |
| (A)  | (B)              | Response Delay Time    |

A. VOUT_COMMAND adjustment occurs through the PMBus interface.

B. Reset to the default VOUT_COMMAND value which is latched when the devices are powered up from AVIN. The slew rate is defined by the VOUT_TRANSITION_RATE command.

#### 7.3.9   Switching Frequency and Synchronization

A resistor from the RT pin (RRT) to AGND sets the switching frequency. Use Equation 4 to calculate the RRT resistor value.

RRT = 2.01 * 1010 / fSW

where

- RRT is the timing resistor in Ohms
- fSW is the switching frequency in Hertz

(4)

The devices are designed to operate from 200 kHz to 1 MHz.

##### 7.3.9.1      Synchronization

The devices can synchronize to an external clock that is ±20% of the free-running frequency.

###### 7.3.9.1.1     Stand-Alone Device

The device supports auto detection on the SYNC pin of the stand-alone device or the PWM-loop master device in a 2-phase configuration. With the external clock applied to the SYNC pin before AVIN power-up or pulling up the SYNC pin to the BP3 or BP6 pin, the SYNC pin is configured as SYNC-IN, and is synchronized to the rising edge of the external clock applied to this pin, with a minimum pulse width of 200 ns (maximum). If no external clock edges occur or logic-high voltage is applied to the SYNC pin at AVIN power-up, the SYNC pin is configured as SYNC-OUT, and the internal free-running frequency set by the RT resistor is output on the SYNC pin. A sudden change in synchronization clock frequency causes an associated control-loop response, resulting in an overshoot or undershoot on the output voltage.

###### 7.3.9.1.2     Master-Slave Configuration

Without the requirement of an external clock, the SYNC pin of the PWM-loop master device can be configured as SYNC-OUT and output a 50% duty-cycle clock to the slave device. The slave device is then synchronized to the falling edge of the clock applied to the SYNC pin. Both the loop master and slave devices require an RT resistor to set the free-running frequency. Figure 27 shows the simplified schematic for this configuration. For the loop slave device in a 2-phase configuration, the SYNC pin is always configured as SYNC-IN, and is synchronized to the falling edge of the incoming clock on the SYNC pin. Figure 28 shows the timing for phase interleaving.

###### Figure 27. Master-Slave Synchronization and Phase Interleaving Setting

Master    Slave

RT

SYNC

SYNC

RT

###### Figure 28. Phase Interleaving Timing

SYNC (50% duty cycle)

Voltage

Master PWM

515 ns

515 ns

Slave PWM

t0

t1

Time

An external clock can optionally be applied to both the PWM-loop master and the slave device to synchronize the stack. Only 50% duty cycle of the external clock can be applied to the 2-phase stack to realize the interleaving of two phases. The loop master automatically (auto) detects if an external clock is available for synchronisation. One clock master can also sync another stack as shown in Figure 29. When the auto detection determines the clock master and clock slave, the configuration cannot change until AVIN power cycling.

The EEPROM setup (FORCE_SYNC_IN Bit and FORCE_SYNC_OUT Bit) overrides auto detection of the SYNC pin. Therefore, if the FORCE_SYNC_OUT Bit is set to 1, the user should not apply the external clock to SYNC pin, which may cause catastrophic damage to the device. The FORCE_SYNC_IN Bit has higher priority than the FORCE_SYNC_OUT Bit. Neither the FORCE_SYNC_IN Bit nor the FORCE_SYNC_OUT Bit are set as a factory-default setting.

###### Figure 29. Phase Interleaving Timing

BP3 or BP6

Clock Slave

Clock Slave

RT

SYNC

SYNC

RT

Master

Slave

###### 7.3.9.1.3 SYNC Fault

The converter is allowed to stop switching after detecting the SYNC signal is expected, but not present or has been lost. The device also reports a live (essentially unlatched) sync_flt bit in the STATUS_MFR_SPECIFIC (80h) register. The SMBALERT is not triggered if the SYNC_FAULT bit goes high. The default SYNC fault response is as follows.

- For the case of a clock that is lost after it was previously present, the SYNC-loss detection latency is approximately 10 μs. During this delay time (between when the clock is lost to when the controller detects it), the clock slave (loop slave or loop master set as clock slave) continues to operate at a frequency that is approximately 40% less than the free-running frequency. The frequencies of two devices are most likely not identical during this 10-μs duration. The clock master continues to operate at the free-running frequency during the 10-μs duration.
- For the case of a clock signal that is never present, both phases (for 2-phase) or the standalone PWM-loop master (1-phase) remain off (never switch) while waiting for the external clock to arrive. After the external clock is restored, seven clock cycles are counted and then the rail performs a new soft-start. No further user intervention (for example, power-cycle, CNTL toggle, CLEAR_FAULTS, or others) is required for the rail to start up after clock restoration.

NOTE

The SYNC fault response can be disabled by setting the SYNC_FAULT_DIS Bit in the MISC_CONFIG_OPTIONS (MFR_SPECIFIC_32) (F0h) register. The SYNC_FAULT_DIS Bit, when set, disables the sync_flt reporting status, and the devices that lost the SYNC clock input (loop slave or loop master set clock slave) continue to operate at a frequency approximately 40% less than the free-running frequency for approximately 10 μs, then back to the free-running frequency without shutting down. But the frequencies of two devices are most likely not identical because the clock master continues to operate at its own free-running frequency.

#### 7.3.10 Current Sharing

For two devices to operate in a 2-phase application, the SYNC, VSHARE, and ISHARE pins of both devices should be connected respectively, as shown in Figure 30. The loop master device shares the same VSHARE voltage. Essentially the internal COMP voltage is shared with the loop slave by connecting the VSHARE pin of each device together. The sensed current in each phase is compared first by connecting the ISHARE pin of each device, then the error current is added into the internal COMP. The resulting voltage is compared with the PWM ramp to generate the PWM pulse. This current sharing loop maintains the current balance between devices. An additional resistor connected between the ISHARE pins of both devices can be used to lower the current-sharing loop gain for better stability margin. Use to calculate the current sharing gain (GISHARE).

GISHARE = 19.5 × 10 kΩ / (10 kΩ + RSHARE) mV/A

##### Figure 30. Current Sharing

Loop Master  Loop Slave

| SYNC              | SYNC   |
| ----------------- | ------ |
| VSHARE            | VSHARE |
| RSHARE (optional) |        |
| ISHARE            | ISHARE |

In addition to sharing the same internal COMP voltage, the VSHARE pin is also used for fault communication between the loop master and slave devices. The VSHARE pin voltage is pulled low if any device encounters any fault conditions so that the other device sharing VSHARE pin is alerted and stops switching accordingly.

An optional high-frequency capacitor can be added between the VSHARE pin and ground in noisy systems, but the capacitance should not exceed 10 pF.

#### 7.3.11 Soft-Start Time and TON_RISE Command

To control the inrush current required to charge the output capacitor bank during start up, the devices implement a soft-start time. When the device is enabled, the feedback reference voltage, VREF, ramps from 0 V to the final level defined by Equation 3 at a slew rate defined by the TON_RISE command. The specified rise times are defined by the slew rate required to ramp the reference voltage from 0 V to the final value at each given rise time.

The actual rise time of the converter output is slightly less than the rise time defined by the TON_RISE command. This difference occurs because switching does not occur until the error-amplifier output reaches the valley of the PWM ramp. During the soft-start time, the error-amplifier output voltage starts at 0 V and then begins switching again only when the VSHARE voltage reaches the valley of the PWM ramp which is 1.23 V (typical). When the VSHARE voltage reaches the valley of the PWM ramp, the converter output voltage rises quickly until the feedback voltage, VFB, reaches the VREF level, at which point they track through the end of the soft-start period.

##### Figure 31. Soft-Start Timing

The devices support several soft-start times from 1 ms to 100 ms which are selected by the TON_RISE command.

#### 7.3.12 Prebiased Output Start-Up

The devices prevent current from being discharged from the output during start-up, when a prebiased output condition exists. If the output is prebiased, no SW pulses occur until the internal soft-start voltage rises above the error-amplifier input voltage (FB pin). As soon as the soft-start voltage exceeds the error-amplifier input, SW pulses start and the device limits synchronous rectification after each SW pulse with a narrow on-time. The on-time of the low-side MOSFET slowly increases on a cycle-by-cycle basis until 128 pulses have been generated and the synchronous rectifier runs fully complementary to the high-side MOSFET. This approach prevents the sinking of current from a prebiased output, and ensures the output-voltage start-up and ramp-to-regulation sequences are smooth and monotonic.

For prebias that is higher than regulation, the PWM-loop master device is forced to go through the 128 cycles of prebias operation at the end of TON_RISE time.

The output overvoltage warn is tripped when the FB pin is prebiased to higher than 5% about the regulation level. These devices respond to a prebiased output overvoltage condition immediately upon AVIN powered up and when the BP6 regulator voltage is above the BP6 UVLO of 3.73 V (typical).

#### 7.3.13 Soft-Stop time and TOFF_FALL Command

The devices implement the TOFF_FALL command to define the time for the output voltage to drop from regulation to 0 as shown in Figure 24. Negative current in the devices can occur during the TOFF_FALL time to discharge the output voltage. The setting of the TOFF_FALL command to 0 ms causes the unit to bring the output voltage down to 0 as quickly as possible, which results in an effective TOFF_FALL time of 1 ms (fastest time supported). This feature can be disabled in the ON_OFF_CONFIG command for the turnoff controlled by the CNTL pin or bit 6 of the OPERATION register if the regulator is turned off by the OPERATION command. If the regulator is turned off by the OPERATION command, both the high-side and low-side FET drivers are turned off immediately and the output voltage is discharged by the load.

#### 7.3.14 Output Current Telemetry and Low-Side MOSFET Overcurrent Protection

##### 7.3.14.1 Output Current Telemetry

The devices sense the average output current using an internal sense FET as shown in Figure 32. A sense FET conducts a scaled-down version of the power-stage current. Sampling this current in the middle of the low-side drive signal determines the average output current. This architecture achieves excellent current monitoring and better overcurrent threshold accuracy than the current sensing of a DC-resistance (DCR) inductor with minimal temperature variation and no dependence on power loss in a higher DCR inductor. Use the IOUT_CAL_OFFSET command to improve current sensing and overcurrent accuracy by removing systematic errors related to board layout after assembly. The devices continually digitize the sensed output current, and average it to reduce measurement noise. The devices then store the current value in the read-only register, READ_IOUT, which enables output-current telemetry.

###### Figure 32. SenseFET Average Current Sensing and Overcurrent Protection

AVIN    PVIN

Terminate PWM    PWM Pulse               +       HFET

Peak Current                        HDRV

Three          HSOC                   Comparator                                SW

Consecutive                                                    Current Sense

Cycle                                                       Amplifier

Counter                    LSOC                                       +    SenseFET      LFET

OCF/OCW                       Average

Current Sensing

Hiccup/                    FAULT_RESPONSE                                            LDRV

Latch-off                                          OCF/OCW

OCF   OCW Thresholds     IOUT_CAL_OFFSET

READ_IOUT

STATUS_IOUT                          PMBus Engine

SMBALERT

AGND  DRGND  PGND

##### 7.3.14.2 Low-Side MOSFET Overcurrent Protection

The devices implement low-side MOSFET overcurrent protection with programmable fault and warning thresholds. The IOUT_OC_FAULT_LIMIT and IOUT_OC_WARN_LIMIT commands set the low-side overcurrent thresholds.

If an overcurrent event is detected in a given switching cycle, the device increments an overcurrent counter as shown in Figure 32. When the device detects three consecutive overcurrent events (either high-side or low-side), the converter responds by flagging the appropriate status registers, triggering the SMBALERT signal if it is not masked, and entering either continuous-restart-hiccup mode or latches off according to the IOUT_OC_FAULT_RESPONSE command. In continuous-restart-hiccup mode, the devices implement a seven TON_RISE time, followed by a normal soft-start attempt. When the overcurrent fault clears, normal operation resumes, otherwise, the device detects overcurrent and the process repeats. The IOUT_OC_FAULT_RESPONSE command can also be set to ignore the OC fault for debugging purposes.

##### 7.3.14.3 Negative Overcurrent Protection

The devices also implement low-side MOSFET Rds,on based negative overcurrent protection. After detecting negative current (sinking from SW to PGND) beyond the negative OC limit, the low-side MOSFET gate drive will be turned off immediately. The low-side gate drive signal will always be turned on for the duration of the minimum off-time in Specifications to re-detect negative OC condition. If negative OC condition persists, the next low-side gate drive pulse will be skipped, except at the end of the clock period, where the low-side gate drive still being turned on for the minimum off-time. This is a cycle-by-cycle clamp. Set the DIS_NEGILIM bit in OPTIONS (MFR_SPECIFIC_21) can disable negative OC protection. The output Overvoltage protection has higher priority than negative OC protection, in other words, in case of output Overvoltage condition persists, the low-side FET will be turned on with the negative OC protection being ignored in order to discharge the output voltage and protect the load equipment.

#### 7.3.15 High-Side MOSFET Short-Circuit Protection

The devices also implement a fixed high-side MOSFET overcurrent (HSOC) protection to limit peak current, and prevent inductor saturation in the event of a short circuit. The devices detect an overcurrent event by sensing the voltage drop across the high-side MOSFET when it is on. If the peak current reaches the IHOSC level on any given cycle, the cycle terminates to prevent the current from increasing any further. High-side MOSFET overcurrent events are counted using the method shown in Figure 32. If the devices detect three consecutive overcurrent events (high-side or low-side), the converter responds by flagging the appropriate status registers, triggering the SMBALERT signal if it is not masked, and entering either continuous-restart-hiccup mode or latches off according to the IOUT_OC_FAULT_RESPONSE command. For accurate overcurrent protection for the high-side MOSFET, the PVIN and AVIN pins must have the same potential because split-rail operation is not supported. The IOUT_OC_FAULT_RESPONSE command can also be set to ignore the OC fault for debugging purposes. When the IOUT_OC_FAULT_RESPONSE command is set to ignore, the device continues to have cycle-by-cycle HSOC protection.

#### 7.3.16 Die Temperature Telemetry and Overtemperature Protection

An internal temperature sensor based off the bandgap reference protects the devices from thermal runaway. The internal thermal shutdown threshold, TSD, is fixed at 145°C (typical). When the devices sense a temperature above TSD, an otf_bg bit in the STATUS_MFR_SPECIFIC command is flagged, and power conversion stops until the sensed junction temperature decreases by the amount of the thermal shutdown hysteresis, THYST (20°C typical). The SMBALERT signal is triggered if it is not masked.

The devices also provide temperature telemetry and programmable internal overtemperature fault or warning thresholds using measurements from an internal temperature sensor as shown in Figure 33. The temperature-sensor circuit applies two bias currents to an internal diode-connected NPN transistor, and measures ΔVBE to infer the junction temperature of the sensor. The devices then digitize the result and compare it to the user-configured overtemperature fault and warning thresholds. When an internal overtemperature fault (OTF) is detected, power conversion stops until the sensed temperature decreases by 20°C. The READ_TEMPERATURE_1 (8Dh) register is continually updated with the digitized temperature measurement, enabling temperature telemetry. The OT_FAULT_LIMIT (4Fh) and OT_WARN_LIMIT (51h) commands set the overtemperature fault and warning thresholds through the PMBus interface. When an overtemperature event is detected, the device sets the appropriate flags in STATUS_TEMPERATURE (7Dh) command and triggers the SMBALERT signal if it is not masked.

The device response upon internal overtemperature fault can be set to Latch-off, Restart and Ignore in OT_FAULT_RESPONSE. The default response to an over temperature fault is to ignore. Fixed band gap-detected overtemperature (OT) faults are never ignored. The band gap OT faults always respond in a shutdown and attempted restart once the part cools.

Table 2 summarizes the fault-response scheme.

##### Figure 33. Overtemperature Protection

Bandgap-Based

Bandgap OT Fault + Internal Temperature

Thermal Shutdown

145° C

OT_FAULT_RESPONSE

Internal OT Fault

OT_FAULT_LIMIT

OT_WARN_LIMIT

READ_TEMPERATURE_1

STATUS_TEMPERATURE

STATUS_MFR_SPECIFIC

PMBus Engine

Temperature Conversion

SMBALERT

QT

#### 7.3.17 Output Voltage Telemetry and Over-/Under-voltage Protection

##### 7.3.17.1 Output Voltage Telemetry

The output voltage is sensed at the remote sense amplifier output pin, and the device continually digitizes the sensed output voltage, and average it to reduce measurement noise. The devices then store the current value in the read-only register, READ_VOUT, which enables output voltage telemetry. Please refer to OPTIONS (MFR_SPECIFIC_21) for details of programming output voltage telemetry signal range, averaging and update rate.

##### 7.3.17.2 Output Overvoltage and Undervoltage Protection

The devices include both output overvoltage protection and output undervoltage protection capability by comparing the FB pin voltage to internal selectable pre-set voltages, as defined by the PCT_OV_UV_WRN_FLT_LIMITS (MFR_SPECIFIC_07) (D7h) command.

If the FB pin voltage rises above the output overvoltage protection threshold, the device terminates normal switching and turns on the low-side MOSFET to discharge the output capacitor and prevent further increases in the output voltage. The device also declares an OV fault, flagging the appropriate status registers, triggering SMBALERT if it is not masked. Then the device enters continuous-restart-hiccup mode or latches off according to the VOUT_OV_FAULT_RESPONSE command. The devices respond to the output Overvoltage condition immediately upon AVIN powered up and BP6 regulator voltage above its own UVLO of 3.73 V (typical). The VOUT_OV_FAULT_RESPONSE can also be set to ignore the output overvoltage fault and continue without interruption. Under this configuration, the control loop continues to respond and adjust PWM duty cycle to keep output voltage within regulation.

If the FB pin voltage falls below the Undervoltage protection level after soft-start has completed, the device terminates normal switching and forces both the high-side and low-side MOSFETs off, and awaits an external reset or begins a hiccup time-out delay prior to restart, depending on the value of the VOUT_UV_FAULT_RESPONSE command. The device also declares a UV fault by flagging the appropriate status registers and triggering SMBALERT if it is not masked. The VOUT_UV_FAULT_RESPONSE can also be set to ignore the output undervoltage fault and continue without interruption for debug purpose.

The devices also provide FB referred fixed threshold (2.2 V typical) output overvoltage protection.

Table 2 summarizes the fault-response scheme.

#### 7.3.18 TON_MAX Fault

The TON_MAX_FAULT_LIMIT command sets an upper limit, in milliseconds, on how long the unit can attempt to power up the output without reaching the output undervoltage fault limit. The devices differentiate a startup UV fault and a regulation UV fault by implementing the TON_MAX_FAULT_LIMIT command. The TON_MAX_FAULT_LIMIT command can allow the devices more time than the soft-start time defined by TON_RISE to come into regulation and the UV detection is essentially delayed up to the TON_MAX_FAULT_LIMIT time. For more details, see the TON_MAX_FAULT_LIMIT (62h) section.

#### 7.3.19 Power Good (PGOOD) Indicator

When the output voltage remains within the PGOOD window after the start-up period, PGOOD as an open-drain output is released, and rises to an externally supplied logic level. The PGOOD window is defined by OV warning limit and UV warning limit in PCT_OV_UV_WRN_FLT_LIMITS (MFR_SPECIFIC_07) (D7h), which can be programmed through the PMBus interface, as shown in Figure 34. The PGOOD pin pulls low upon any fault condition on default. Please refer to Table 2 for the possible sources to pull down the PGOOD pin.

The PGOOD signal can be connected to the CNTL pin of another device to provide additional controlled turn-on and turn-off sequencing.

The OVW or PGOOD signal trips when the FB pin is prebiased to higher than 5% about the regulation level. This level of prebias is unusual and it is beneficial to flag a warning in this situation.

##### Figure 34. PGOOD Threshold and Hysteresis

| OV Fault      | OV Warn | OVW         | Hysteresis |            |
| ------------- | ------- | ----------- | ---------- | ---------- |
| VOUT\_COMMAND | UV Warn | UVW         | FB         | Hysteresis |
| UV Fault      | PGOOD   | (non-latch) | Time       |            |

NOTE: Pulling PGOOD pin high before the devices gets input power could cause PGOOD pin going high due to the limited pulldown capability in un-powered condition. If this is not desired, increase the pullup resistance or reduce the external pullup supply voltage.

#### 7.3.20 Fault Protection Responses

Table 2 summarizes the various fault protections and associated responses.

##### Table 2. Fault Protection Summary

Internal Over Temp Fault (OT_FAULT_LIMIT - 4Fh)

| FAULT RESPONSE | FET BEHAVIOR                                            | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| -------------- | ------------------------------------------------------- | --------------- | --------------- | -------- | ----- |
| Latch-off      | Both FETs off                                           | Yes             | Yes             | Yes      | Low   |
| Restart        | Both FETs off, restart after cooling down<sup>(1)</sup> | Yes             | Yes             | Yes      | Low   |
| Ignore         | FETs controlled by PWM                                  | Yes             | Yes             | Yes      | High  |

Internal Over Temp Warn (OT_WARN_LIMIT - 51h)

| FAULT RESPONSE    | FET BEHAVIOR | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| ----------------- | ------------ | --------------- | --------------- | -------- | ----- |
| Latch-off/Restart | PWM control  | Yes             | Yes             | Yes      | Low   |
| Ignore Fault      | PWM control  | Yes             | Yes             | Yes      | High  |

Bandgap Over Temp Fault (Internal Threshold)

| FAULT RESPONSE | FET BEHAVIOR                                            | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| -------------- | ------------------------------------------------------- | --------------- | --------------- | -------- | ----- |
| Latch-off      | Both FETs off                                           | Yes             | Yes             | Yes      | Low   |
| Restart        | Both FETs off, restart after cooling down<sup>(1)</sup> | Yes             | Yes             | Yes      | Low   |
| Ignore         | Both FETs off, restart after cooling down<sup>(2)</sup> | Yes             | Yes             | Yes      | Low   |

Low-Side OC Fault (IOUT_OC_FAULT_LIMIT - 46h)

| FAULT RESPONSE | FET BEHAVIOR                                 | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| -------------- | -------------------------------------------- | --------------- | --------------- | -------- | ----- |
| Latch-off      | 3 PWM→Both FETs off                          | Yes             | Yes             | Yes      | Low   |
| Restart        | 3 PWM→Both FETs off→restart after 7×TON_RISE | Yes             | Yes             | Yes      | Low   |
| Ignore         | PWM control                                  | Yes             | Yes             | Yes      | High  |

Low-Side OC Warn (IOUT_OC_WARN_LIMIT)

| FAULT RESPONSE    | FET BEHAVIOR | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| ----------------- | ------------ | --------------- | --------------- | -------- | ----- |
| Latch-off/Restart | PWM control  | Yes             | Yes             | Yes      | Low   |
| Ignore Fault      | PWM control  | Yes             | Yes             | Yes      | High  |

High-Side OC Fault 

| FAULT RESPONSE | FET BEHAVIOR                                 | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| -------------- | -------------------------------------------- | --------------- | --------------- | -------- | ----- |
| Latch-off      | 3 PWM→Both FETs off→restart after 7×TON_RISE | Yes             | Yes             | Yes      | Low   |
| Restart        | 3 PWM→Both FETs off→restart after 7×TON_RISE | Yes             | Yes             | Yes      | Low   |
| Ignore         | Cycle-by-cycle current limit                 | Yes             | Yes             | Yes      | High  |

VOUTOV Fault (PCT_OV_UV_WRN_FLT_LIMIT S (MFR_SPECIFIC_07) (D7h) ）

| FAULT RESPONSE | FET BEHAVIOR                                       | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| -------------- | -------------------------------------------------- | --------------- | --------------- | -------- | ----- |
| Latch-off      | HS off, LS by OV_RESP_SEL (latch/till FB<0.2V)     | Yes             | Yes             | Yes      | Low   |
| Restart        | HS off, LS by OV_RESP_SEL→restart after 7×TON_RISE | Yes             | Yes             | Yes      | Low   |
| Ignore         | PWM control                                        | Yes             | Yes             | Yes      | Low   |

VOUTOV Warn (PCT_OV_UV_WRN_FLT_LIMIT - D7h)

| FAULT RESPONSE    | FET BEHAVIOR | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| ----------------- | ------------ | --------------- | --------------- | -------- | ----- |
| Latch-off/Restart | PWM control  | Yes             | Yes             | Yes      | Low   |
| Ignore Fault      | PWM control  | Yes             | Yes             | Yes      | Low   |

VOUTUV Fault (PCT_OV_UV_WRN_FLT_LIMIT - D7h)

| FAULT RESPONSE | FET BEHAVIOR                           | ACTIVE TON_RISE | SMBALERT SOURCE | MASKABLE | PGOOD |
| -------------- | -------------------------------------- | --------------- | --------------- | -------- | ----- |
| Latch-off      | Both FETs off                          | **No**          | Yes             | Yes      | Low   |
| Restart        | Both FETs off→restart after 7×TON_RISE | **No**          | Yes             | Yes      | Low   |
| Ignore         | PWM control                            | **No**          | Yes             | Yes      | Low   |

(1) When the overtemperature fault is tripped, the device shuts off both FETs and restarts until the sensed temperature decreases 20°C from the tripping threshold.

(2) The bandgap overtemperature Fault cannot be ignored, the device shuts off both FETs and restarts after the internal die temperature drops below the threshold.

##### Table 2. Fault Protection Summary (continued)

| FAULT or WARN     | PROGRAMMING                                         | FAULT RESPONSE SETTING        | FET BEHAVIOR                                 | ACTIVE DURING TON_RISE | SOURCE OF SMBALERT | SMBALERT MASKABLE | PGOOD |
| ----------------- | --------------------------------------------------- | ----------------------------- | -------------------------------------------- | ---------------------- | ------------------ | ----------------- | ----- |
| **V OUT UV Warn** | PCT_OV_UV_WRN_FLT_LIMIT<br>S(MFR_SPECIFIC_07) (D7h) | Latch-off or Restart on Fault | PWM maintains control of FETs                | No                     | Yes                | Yes               | Low   |
|                   |                                                     | Ignore Fault                  | PWM maintains control of FETs                | No                     | Yes                | Yes               | Low   |
| **TON Max Fault** | TON_MAX_FAULT_LIMIT                                 | Latch-off                     | Both FETs off                                | No                     | Yes                | Yes               | Low   |
|                   |                                                     | Restart                       | Both FETs off, then restart after 7×TON_RISE | No                     | Yes                | Yes               | Low   |
|                   |                                                     | Ignore                        | PWM maintains control of FETs                | No                     | Yes                | Yes               | Low   |
| **VIN UVLO**      | VIN_ON, VIN_OFF                                     | Shut down                     | Both FETs off                                | Yes                    | Yes                | Yes               | Low   |

NOTE

The best practice is to have the fault response of the loop master and slave device set as the same to avoid unexpected behavior.

#### 7.3.21 Switching Node

The SW pin connects to the switching node of the power-conversion stage and acts as the return path for the high-side gate driver. When configured as a synchronous buck stage, the voltage swing on SW normally traverses from below ground to well above the input voltage. Parasitic inductance in the high-side FET and the output capacitance (COSS) of both power FETs form a resonant circuit that can produce high frequency ( > 100 MHz) ringing on this node. The voltage peak of this ringing, if not controlled, can be significantly higher than the input voltage. Ensure that the peak ringing amplitude does not exceed the absolute maximum rating limit for the pin.

In many cases, a series resistor and capacitor snubber network connected from the switching node to PGND can be helpful in damping the ringing and decreasing the peak amplitude. Provide provisions for snubber network components in the layout of the printed circuit board. If testing reveals that the ringing amplitude at the SW pin exceeds the limit, then include snubber components. For more information about snubber circuits design, refer to Snubber Circuits: Theory, Design and Application (SLUP100).

Placing a BOOT resistor in series with the BOOT capacitor slows down the turnon of the high-side FET and can help to reduce the peak ringing at the switching node as well.

#### 7.3.22 PMBus General Description

Timing and electrical characteristics of the PMBus interface specification can be found in the PMB Power Management Protocol Specification, Part 1, revision 1.3 available at http://pmbus.org. The devices support both the 100-kHz and 400-kHz bus timing requirements. The devices do not stretch pulses when communicating with the master device.

Communication over the PMBus interface can support the Packet Error Checking (PEC) scheme if desired. If the master supplies clock (CLK pin) pulses for the PEC byte, PEC is used. If the CLK pulses are not present before a STOP, the PEC is not used.

The devices support a subset of the commands in the PMBus 1.3 Power Management Protocol Specification. See Supported PMBus Commands for more information.

The devices also support the SMBALERT response protocol. The SMBALERT response protocol is a mechanism by which a slave device (such as the devices) can alert the bus master that it is available for communication. The master processes this event and simultaneously accesses all slaves on the bus (that support the protocol) through the alert response address (ARA). Only the slave that caused the alert acknowledges this request. The host performs a modified receive byte operation to ascertain the slave address. At this point, the master can use the PMBus status commands to query the slave that caused the alert. By default these devices implement the auto alert response, a manufacturer specific improvement to the SMBALERT response protocol, intended to mitigate the issue of bus hogging. For more information, see the Auto ARA Response section. For more information on the SMBus alert response protocol, refer to the System Management Bus (SMBus) specification.

The devices contain nonvolatile memory that stores configuration settings and scale factors. However, the device does not save the settings programmed into this nonvolatile memory. The STORE_DEFAULT_ALL (11h) or STORE_USER_ALL (11h) command must be used to commit the current settings to nonvolatile memory as device defaults. The settings that are capable of being stored in nonvolatile memory are noted in the detailed command descriptions.

#### 7.3.23 PMBus Address

The PMBus specification requires that each device connected to the PMBus have a unique address on the bus. The devices each have 64 possible addresses (0 through 63 in decimal) that can be assigned by connecting resistors from the ADDR0 and ADDR1 pins to AGND. The address is set in the form of two octal (0 to 7) digits, one digit for each pin. ADDR1 is the high order digit and ADDR0 is the low-order digit. These address selection resistors must be 1% tolerance or better. Using resistors other than the recommended values can result in devices responding to adjacent addresses.

The E48 series resistors with no worse than 1% tolerance suggested for each digit value are shown in Table 3.

##### Table 3. Required Address Resistors

| DIGIT | RESISTOR VALUE (kΩ) |
| ----- | ------------------- |
| 0     | 7.15                |
| 1     | 14                  |
| 2     | 22.6                |
| 3     | 34.8                |
| 4     | 51.1                |
| 5     | 78.7                |
| 6     | 121                 |
| 7     | 187                 |

The devices also detect values that are out of range on the ADDR0 and ADDR1 pins. If the device detects that either pin has an out-of-range resistance connected to it, the device continues to respond to PMBus interface commands, but does so at address 127 decimal, which is outside of the possible programmed addresses. It is possible but not recommended to use the device in this condition, especially if other devices are present on the bus or if another device could possibly occupy the 127 decimal address.

Certain addresses in the I2C address space are reserved for special functions and it is possible to set the address of the devices to respond to these addresses. The user is responsible for knowing which of these reserved addresses are in use in a system and for setting the address of the devices accordingly so as not to interfere with other system operations. The devices can be set to respond to the global call address or 0. It is recommended not to set the devices to this address unless the user is certain that no other devices respond to this address and that the overall bus is not affected by having such an address present.

#### 7.3.24 PMBus Connections

The devices support both the 100-kHz and 400-kHz bus speeds, 1.8-V or 3.3-V and 5-V PMBus-interface logic level. For more information, see the PMBus Interface section of the Specifications.

#### 7.3.25 Auto ARA (Alert Response Address) Response

By default, the devices implement the auto alert response, a manufacturer specific improvement to the standard SMBALERT response protocol defined in the SMBus specification. The auto alert response is designed to prevent SMBALERT monopolizing in the case of a persistent fault condition on the bus. The user can choose to disable the auto ARA response, and use the standard SMBALERT response as defined in the SMBus specification, by using the EN_AUTO_ARA Bit of the OPTIONS (MFR_SPECIFIC_21) register.

In the case of a fault condition, the slave device experiencing the fault pulls down the shared SMBALERT line, to alert the host that a fault condition has occurred. To establish which slave device has experienced the fault, the host issues a modified receive byte operation to the alert response address (ARA), to which only the slave pulling down on SMBALERT should respond. The SMBus protocol provides a method for address arbitration in the case that multiple slaves on the same bus are experiencing fault conditions. When the host has established the address of the offending device, it must take any necessary action to release the SMBALERT line. For more information on the standard SMBus alert response protocol, refer to the SMBus specification.

In the case of a non-persistent fault (a single-time event, such as an invalid command or data byte), the host can ascertain the address of the slave experiencing a fault using the standard ARA response, and simply issue CLEAR_FAULTS to release the SMBALERT line, and resume normal operation. However, in the case of a persistent fault (one which remains active for some time, such as a short-circuit, or thermal shutdown), once the device issues a CLEAR_FAULTS command, the fault immediately re-triggers, and SMBALERT continues to be pulled low. In this case, the device holds low the SMBALERT line until the host masks the SMBALERT line using SMBALERT_MASK and then issues the CLEAR_FAULTS command. Because the SMBALERT line remains low, the host cannot be alerted to other fault conditions on the bus until it clears SMBALERT.Figure 35 and Figure 36
show this response. 

##### Figure 35. Example Standard ARA Response to Nonpersistent Fault

SMBALERT is not released until CLEAR_FAULTS is issued by the host

| STATUS\_CML | No Faults | Invalid Command | No Faults     |              |
| ----------- | --------- | --------------- | ------------- | ------------ |
| DATA        | PAGE      | ARA             | Slave Address | CLEAR\_FAULT |
| HOST        | HOST      | SLAVE           |               | HOST         |

##### Figure 36. Example Standard ARA Response to a Persistent Fault

SMBALERT is low until host masks fault, and issues CLEAR_FAULTS if the fault condition persists

STATUS_IOUT No Faults OC FAULT

| DATA | ARA   | Slave Address | MASK\_SMBALERT | CLEAR\_FAULTS |
| ---- | ----- | ------------- | -------------- | ------------- |
| HOST | SLAVE | HOST          |                | HOST          |

Short Circuit

To mitigate the problem of SMBALERT bus hogging described previously, the devices implement the Auto ARA response. When Auto ARA is enabled, the devices releases SMBALERT automatically after successfully responding to access from the host at the alert response address. In this case, even when the device is experiencing a persistent fault, it does not hold the SMBALERT line low following successful notification of the host, and the host can be alerted to other faults on the bus in the normal manner. Examples of the auto ARA response are shown in Figure 37 and Figure 38.

##### Figure 37. Example Auto ARA Response to Nonpersistent Fault

SMBALERT is released when slave successfully responds to ARA

| STATUS\_CML | No Faults | Invalid Command | No Faults     |              |
| ----------- | --------- | --------------- | ------------- | ------------ |
| DATA        | PAGE      | ARA             | Slave Address | CLEAR\_FAULT |
| HOST        | HOST      | SLAVE           |               | HOST         |

##### Figure 38. Example Auto ARA Response to Persistent Fault

SMBALERT is released when slave successfully responds to ARA

STATUS_IOUT No Faults OC FAULT

| DATA | ARA   | Slave Address | MASK\_SMBALERT | CLEAR\_FAULTS |
| ---- | ----- | ------------- | -------------- | ------------- |
| HOST | SLAVE | HOST          |                | HOST          |

Short Circuit

### 7.4 Device Functional Modes

#### 7.4.1 Continuous Conduction Mode

The devices operate in continuous conduction mode (CCM) at a fixed frequency, regardless of the output current. For the first 128 switching cycles, the low-side MOSFET on-time is slowly increased to prevent excessive current sinking in the event the device is started with a prebiased output. Following the first 128 clock cycles, the low-side MOSFET and the high-side MOSFET on-times are fully complementary.

#### 7.4.2 Operation with CNTL Signal Control

According to the value in the ON_OFF_CONFIG register, the devices can be commanded to use the CNTL pin to enable or disable regulation, regardless of the state of the OPERATION command. The CNTL pin can be configured as either active high or active low (inverted) logic.

#### 7.4.3 Operation with OPERATION Control

According to the value in the ON_OFF_CONFIG register, the devices can be commanded to use the OPERATION command to enable or disable regulation, regardless of the state of the CNTL signal.

#### 7.4.4 Operation with CNTL and OPERATION Control

According to the value in the ON_OFF_CONFIG register, the devices can be commanded to require both a signal on the CNTL pin, and the OPERATION command to enable or disable regulation.

### 7.5 Programming

#### 7.5.1 Supported PMBus Commands

The commands listed in Table 4 are implemented as described to conform to the PMBus 1.3 specification. Table 4 also lists the default for the bit behavior and register values.

##### Table 4. Supported PMBus Commands and Default Values

| CMD  CODE | PMBus 1.3 COMMAND NAME | PMBus COMMAND DESCRIPTION                                    | DEFAULT BEHAVIOR                                             | DEFAULT REGISTER VALUE | NVM  |
| --------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------- | ---- |
| 01h       | OPERATION              | Can be configured through ON\_OFF\_CONFIG to be used to turn the output on and off with or without input from the CTRL pin. | OPERATION is not used to enable regulation                   | 00h                    | No   |
| 02h       | ON\_OFF\_CONFIG        | Configures the combination of CNTL pin input and OPERATION command for turning output on and off. | CNTL only. Active High                                       | 16h                    | Yes  |
| 03h       | CLEAR\_FAULTS          | Clears all fault status registers to 0x00 and releases SMBALERT. | Write-only                                                   | n/a                    | No   |
| 10h       | WRITE\_PROTECT         | Used to control writing to the volatile operating memory (PMBus and restore from EEPROM). | Allow writes to all registers                                | 00h                    | Yes  |
| 11h       | STORE\_DEFAULT\_ALL    | Stores all current storable register settings into EEPROM as new defaults. | Write-only                                                   | n/a                    | No   |
| 12h       | RESTORE\_DEFAULT\_ALL  | Restores all storable register settings from EEPROM.         | Write-only                                                   | n/a                    | No   |
| 15h       | RESTORE\_USER\_ALL     | Stores all current storable register settings into EEPROM as new defaults. | Write-only                                                   | n/a                    | No   |
| 16h       | RESTORE\_USER\_ALL     | Restores all storable register settings from EEPROM.         | Write-only                                                   | n/a                    | No   |
| 19h       | CAPABILITY             | Provides a way for a host system to determine key PMBus capabilities of the device. | Read only. PMBus v1.3, 400 kHz, PEC and SMBus Alert Response Protocol supported. | B0h                    | No   |
| 1Bh       | SMBALERT\_MASK         | Mask Warn or Fault status bits                               | Mask PGOODz only                                             | n/a                    | Yes  |
| 20h       | VOUT\_MODE             | Read-only output mode indicator.                             | Linear, exponent = –9                                        | 17h                    | No   |
| 21h       | VOUT\_COMMAND          | Default Regulation Setpoint                                  | 600mV                                                        | 0133h                  | Yes  |

### Programming (continued)

#### Table 4. Supported PMBus Commands and Default Values (continued)

| CMD CODE | PMBus 1.3<br/>COMMAND NAME | PMBus COMMAND DESCRIPTION                                    | DEFAULT BEHAVIOR                                             | DEFAULT<br/>REGISTER<br/>VALUE | NVM  |
| -------- | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------ | ---- |
| 24h      | VOUT\_MAX                  | Sets the maximum output voltage.<br/>VOUT_MAX imposes a higher bound to any<br/>attempted VOUT setting. | If VOUT\_SCALE\_LOOP = 1: VOUT\_MAX will restore to 1.65 V.  | 034Dh                          | No   |
|          |                            |                                                              | If VOUT\_SCALE\_LOOP = 0.5: VOUT\_MAX will restore to 3.3 V. | 069Ah                          |      |
|          |                            |                                                              | If VOUT\_SCALE\_LOOP = 0.25: VOUT\_MAX will restore to 6 V.  | 0C00h                          |      |
| 27h      | VOUT\_TRANSITION\_RATE     | Sets the rate at which the output should change voltage.     | 1 mV/us                                                      | D03Ch                          | No   |
| 29h      | VOUT\_SCALE\_LOOP          | Sets output sense scaling ratio for main control loop.       | 1                                                            | F004h                          | Yes  |
| 2Bh      | VOUT\_MIN                  | Sets the minimum output voltage. VOUT_MIN imposes a lower bound to any<br/>attempted VOUT setting. | If VOUT\_SCALE\_LOOP = 1: VOUT\_MIN will restore to 0.35 V.  | 0166h                          | No   |
|          |                            |                                                              | If VOUT\_SCALE\_LOOP = 0.5: VOUT\_MIN will restore to 0.7 V. | 0166h                          |      |
|          |                            |                                                              | If VOUT\_SCALE\_LOOP = 0.25: VOUT\_MIN will restore to 1.4 V. | 02CCh                          |      |
| 35h      | VIN\_ON                    | Sets value of input voltage at which the device should start power conversion. | 4.5 V                                                        | F012h                          | Yes  |
| 36h      | VIN\_OFF                   | Sets value of input voltage at which the device should stop power conversion. | 4 V                                                          | F010h                          | Yes  |
| 39h      | IOUT\_CAL\_OFFSET          | Can be set to null out offsets in the current sensing circuit. | 0.0000 A                                                     | E000h                          | Yes  |
| 41h      | VOUT\_OV\_FAULT\_RESPONSE  | Sets output overvoltage fault response.                      | Restart                                                      | BFh                            | Yes  |
| 45h      | VOUT\_UV\_FAULT\_RESPONSE  | Sets output undervoltage fault response.                     | Restart                                                      | BFh                            | Yes  |
| 46h      | IOUT\_OC\_FAULT\_LIMIT     | Sets the value of the output current that causes an overcurrent fault condition. | 42 A                                                         | F854h                          | Yes  |
| 47h      | IOUT\_OC\_FAULT\_RESPONSE  | Sets response to output overcurrent faults to latch-off, hiccup mode or ignore. | Restart                                                      | FFh                            | Yes  |
| 4Ah      | IOUT\_OC\_WARN\_LIMIT      | Sets the value of the output current that causes an overcurrent warning condition. | 37 A                                                         | F84Ah                          | No   |
| 4Fh      | OT\_FAULT\_LIMIT           | Sets the value of the sensed temperature that causes an overtemperature fault condition. | 145°C                                                        | 0091h                          | Yes  |
| 50h      | OT\_FAULT\_RESPONSE        | Sets response to over temperature faults to latch-off, hiccup mode or ignore. | Ignore                                                       | 3Fh                            | Yes  |
| 51h      | OT\_WARN\_LIMIT            | Sets the value of the sensed temperature that causes an overtemperature warning condition. | 120°C                                                        | 0078h                          | No   |
| 60h      | TON\_DELAY                 | Sets the turnon delay.                                       | 0 ms                                                         | 0000h                          | Yes  |
| 61h      | TON\_RISE                  | Sets the time from when the output starts to rise until the voltage has entered the regulation band. | 3 ms                                                         | 0003h                          | Yes  |
| 62h      | TON\_MAX\_FAULT\_LIMIT     | Sets an UPPER limit in milliseconds, on how long the unit can attempt to power up the output without reaching the output undervoltage fault limit. The time begins counting as the device enters the soft-start period. | Disabled                                                     | 0000h                          | No   |
| 63h      | TON\_MAX\_FAULT\_RESPONSE  | Sets the soft start timeout fault response.                  | Restart                                                      | BFh                            | Yes  |
| 64h      | TOFF\_DELAY                | Sets the turnoff delay.                                      | 0 ms                                                         | 0000h                          | Yes  |
| 65h      | TOFF\_FALL                 | Sets the soft stop fall time.                                | 0 ms                                                         | 0000h                          | Yes  |
| 78h      | STATUS\_BYTE               | Returns one byte summarizing the most critical faults.       |                                                              | Current status                 | No   |
| 79h      | STATUS\_WORD               | Returns two bytes summarizing fault and warning conditions.  |                                                              | Current status                 | No   |
| 7Ah      | STATUS\_VOUT               | Returns one byte detailing if an output fault or warning has occurred. |                                                              | Current status                 | No   |

### Programming (continued)

#### Table 4. Supported PMBus Commands and Default Values (continued)

| CMD CODE | PMBus 1.3 COMMAND NAME                            | PMBus COMMAND DESCRIPTION                                    | DEFAULT BEHAVIOR                                             | DEFAULT REGISTER VALUE      | NVM  |
| -------- | ------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------- | ---- |
| 7Bh      | STATUS\_IOUT                                      | Returns one byte detailing if an overcurrent fault or warning has occurred |                                                              | Current status              | No   |
| 7Ch      | STATUS\_INPUT                                     | Returns one byte of information relating to the status of the converter's input related faults. |                                                              | Current status              | No   |
| 7Dh      | STATUS\_TEMPERATURE                               | Returns one byte detailing if a sensed temperature fault or warning has occurred. |                                                              | Current status              | No   |
| 7Eh      | STATUS\_CML                                       | Returns one byte containing PMBus serial communication faults. |                                                              | Current status              | No   |
| 80h      | STATUS\_MFR\_SPECIFIC                             | Returns one byte detailing if internal overtemperature or address detection fault has occurred. |                                                              | Current status              | No   |
| 8Bh      | READ\_VOUT                                        | Returns the output voltage in volts.                         | Read only                                                    | Current status              | No   |
| 8Ch      | READ\_IOUT                                        | Returns the output current in amps.                          | Read only                                                    | Current status              | No   |
| 8Dh      | READ\_TEMPERATURE\_1                              | Returns the sensed die temperature in degrees Celsius.       | Read-only                                                    | Current status              | No   |
| 98h      | PMBUS\_REVISION                                   | Returns PMBus revision to which the device is compliant.     | PMBus 1.3                                                    | 33h                         | No   |
| ADh      | IC\_DEVICE\_ID                                    | This Read-only Block Read command<br/>returns a single word (16 bits) with the<br/>unique Device Code identifier for each<br/>device for which this device can be<br/>configured. The BYTE_COUNT field in the<br/>Block Read command is 2 (indicating 2<br/>bytes follow): Low Byte first, then High Byte | TPS546C23                                                    | 4623h                       | No   |
| AEh      | IC\_DEVICE\_REV                                   | This Read-only Block Read command<br/>returns a single word (16 bits) with the<br/>unique Device revision identifier. The<br/>BYTE_COUNT field in the Block Read<br/>command is 2 (indicating 2 bytes follow):<br/>Low Byte first, then High Byte. | Read only                                                    | 0001h                       | No   |
| D0h      | MFR\_SPECIFIC\_00                                 | User scratch pad.                                            |                                                              | 0000h                       | Yes  |
| D4h      | VREF\_TRIM (MFR\_SPECIFIC\_04)                    | Applies a fixed offset voltage to the Error Amplifier Reference voltage (EA\_REF). | Fixed offset of 0 mV                                         | 0000h                       | Yes  |
| D5h      | STEP\_VREF\_MARGIN\_HIGH (MFR\_SPECIFIC\_05)      | Increases the value of the reference voltage by shifting the reference higher. | If RSMHI_VAL = 0:<br/>STEP_VREF_MARGIN_HIGH will<br/>restore to 17.6 mV | If RSMHI_VAL<br/>= 0: 0009h | No   |
|          |                                                   |                                                              | If RSMHI_VAL = 1:<br/>STEP_VREF_MARGIN_HIGH will<br/>restore to 29.3 mV | If RSMHI_VAL<br/>= 1: 000fh |      |
| D6h      | STEP\_VREF\_MARGIN\_LOW (MFR\_SPECIFIC\_06)       | Decreases the value of the reference voltage by shifting the reference lower. | If RSMLO_VAL = 0:<br/>STEP_VREF_MARGIN_LOW will<br/>restore to –17.6 mV | If RSMLO_VAL<br/>= 0: fff7h | No   |
|          |                                                   |                                                              | If RSMLO_VAL = 1:<br/>STEP_VREF_MARGIN_LOW will<br/>restore to –29.3 mV | If RSMLO_VAL<br/>= 1: fff1h |      |
| D7h      | PCT\_OV\_UV\_WRN\_FLT\_LIMITS (MFR\_SPECIFIC\_07) | Sets the PGOOD, VOUT\_UNDER\_VOLTAGE (UV) and VOUT\_OVER\_VOLTAGE (OV) Limits as a percentage of nominal. | –17% for UV Fault, –12% for UV Warning, +12% for OV Warning, +17% for OV Fault. | 00h                         | Yes  |
| E5h      | OPTIONS (MFR\_SPECIFIC\_21)                       | Sets user selectable options.                                | See detailed command description                             | 1184h                       | Yes  |
| F0h      | MISC\_CONFIG\_OPTIONS (MFR\_SPECIFIC\_32)         | Sets miscellaneous user selectable options.                  | See detailed command description                             | 0013h                       | Yes  |

### 7.6 Register Maps

This family of devices supports the following commands from the PMBus 1.3 specification.

#### Table 5. Legend for Register Access Type

| Access Type         | Code | Description                              |
| ------------------- | ---- | ---------------------------------------- |
| Read Type           |      |                                          |
| R                   | r    | Read                                     |
| Write Type          |      |                                          |
| W                   | w    | Write                                    |
| Other               |      |                                          |
| superscript E  r/wE | E    | Bit is backed up with nonvolatile EEPROM |

#### 7.6.1 OPERATION (01h)

The OPERATION command turns the device output on or off in conjunction with input from the CNTL signal. It is
also used to set the output voltage to the upper or lower margin voltages. The unit stays in the commanded
operating mode until a subsequent OPERATION command or a change in the state of the CNTL pin instructs the
device to change to another mode.

For PWM loop slave device, which is recognized during power-up calibration, this command cannot be accessed.
Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d
command, the reporting of an IVC fault, and triggering of SMB_ALERT.

| COMMAND       | OPERATION       |      |        |      |      |      |      |      |
| ------------- | --------------- | ---- | ------ | ---- | ---- | ---- | ---- | ---- |
| Format        | Unsigned binary |      |        |      |      |      |      |      |
| Bit Position  | 7               | 6    | 5      | 4    | 3    | 2    | 1    | 0    |
| Access        | r/w             | r/w  | r/w    | r/w  | r/w  | r/w  | r    | r    |
| Function      | ON              | OFF  | MARGIN |      |      |      | X    | X    |
| Default Value | 0               | 0    | 0      | 0    | 0    | 0    | X    | X    |

##### 7.6.1.1 On Bit

This bit is an enable command to the converter.

- 0: output switching is disabled. Both drivers placed in an off or low state.
- 1: output switching is enabled if the input voltage is above undervoltage lockout, OPERATION is configured
as a gating signal in ON_OFF_CONFIG, and no fault conditions exist.

##### 7.6.1.2 Off Bit

This bit sets the turnoff behavior when commanding the unit to turn off through OPERATION[7] (the On bit).

- 0: Immediately turn off the output (not honoring the programmed turnoff delay (TOFF_DELAY) and ramp
down (TOFF_FALL)) when commanded off through OPERATION[7] (the On bit).
- 1: Use the programmed turnoff delay (TOFF_DELAY) and ramp down (TOFF_FALL) when commanded off
through OPERATION[7] (also called soft off).

NOTE

The device ignores any values written to read-only bits. Additionally, both the on and off bits being set at the
same time is not allowed and considered invalid data per section 12.1 of the PMBus Specification Part II; any
attempt to do so causes the device to set the cml bit in the STATUS_BYTE and the ivd bit in the STATUS_CML
registers, and triggers SMBALERT signal.

##### 7.6.1.3 Margin Bit

If Margin Low is enabled, load the value from the STEP_VREF_MARGIN_LOW command. If Margin High is enabled,
load the value from the STEP_VREF_MARGIN_HIGH command.

- 0001: Margin Off. Output voltage source is VOUT_COMMAND. OV and UV faults are ignored.
- 0000, 0010, 0011: Margin Off. Output voltage source is VOUT_COMMAND. OV/UV faults behave normally as
programmed in their respective fault response registers.

• 0101: Margin Low (Ignore Fault). Output voltage defined directly below.

• 0110: Margin Low (Act On Fault). Output voltage defined directly below.

• 1001: Margin High (Ignore Fault). Output voltage defined directly below.

• 1010: Margin High (Act On Fault). Output voltage defined directly below.

• 11XX, 0100, 0111, 1000, 1011: Shall be invalid and shall declare an Invalid Data Fault (Part II Rev 1.3 Section 10.9.3, Page 52)

VOUT_MARGIN_LOW data shall be equal to:

VOUT_COMMAND + (VREF_TRIM – STEP_VREF_MARGIN_LOW) / VOUT_SCALE_LOOP

VOUT_MARGIN_HIGH data shall be equal to:

VOUT_COMMAND + (VREF_TRIM + STEP_VREF_MARGIN_HIGH) / VOUT_SCALE_LOOP

For the Margin Low, Ignore Fault configuration (essentially [5:2] = 4’b0101), any incoming UV faults shall trigger the normal UVF status, and trigger SMB_ALERT (albeit the state machine response will be to ignore and not respond). If the desired response is to have the device to not trigger SMB_ALERT for UVF events when margining, they must set the UVF SMBALERT_MASK bit. For the Margin High, Ignore Fault configuration (essentially [5:2] = 4’b1001), any incoming OV faults shall trigger the normal OVF status, and trigger SMB_ALERT (albeit the state machine response will be to ignore and not respond). If the desired response is to have the device to not trigger SMB_ALERT for UVF events when margining, they must set the UVF SMBALERT_MASK bit. OVF and UVF can also be ignored when VOUT_COMMAND is the VOUT source by programming [5:2] to a value of 4’b0001. OVF and UVF events will still set status and trigger SMB_ALERT.

#### 7.6.2 ON_OFF_CONFIG (02h)

The ON_OFF_CONFIG command configures the combination of CNTL pin input and serial bus commands needed to turn the unit on and off. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL (11h) command. The default value in ON_OFF_CONFIG register is to have the device power up by CNTL pin only with the active high polarity and use the programmed turnoff delay (TOFF_DELAY) and ramp down (TOFF_FALL) for powering off the converter.

For PWM loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

| COMMAND       | ON\_OFF\_CONFIG |      |      |      |      |      |      |      |
| ------------- | --------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Unsigned binary |      |      |      |      |      |      |      |
| Bit Position  | 7               | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r               | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      | X               | X    | X    | pu   | cmd  | cpr  | pol  | cpa  |
| Default Value | X               | X    | X    | 1    | 0    | 1    | 1    | 0    |

##### 7.6.2.1 pu Bit

The pu bit sets the default to either operate any time power is present or for power conversion to be controlled by CNTL pin and PMBus OPERATION command. This bit is used in conjunction with the cpr, cmd, and on bits to determine start up.

| BIT VALUE | ACTION                                                                                                                                          |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 0         | Device powers up any time power is present regardless of state of the CNTL pin.                                                                 |
| 1         | Device does not power up until commanded by the CNTL pin and/or OPERATION command as programmed in bits \[3:0] of the ON\_OFF\_CONFIG register. |

##### 7.6.2.2 cmd Bit

The cmd bit controls how the device responds to the OPERATION command. This bit is used in conjunction with the cpr, pu, and on bits to determine start up.

| BIT VALUE | ACTION                                                    |
| --------- | --------------------------------------------------------- |
| 0         | Device ignores the “on” bit in the OPERATION command.     |
| 1         | Device responds to the “on” bit in the OPERATION command. |

##### 7.6.2.3  cpr Bit

The cpr bit sets the CNTL pin response. This bit is used in conjunction with the cmd, pu, and on bits to determine start up.

| BIT VALUE | ACTION                                                       |
| --------- | ------------------------------------------------------------ |
| 0         | Device ignores the CNTL pin. Power conversion is controlled only by the OPERATION command. |
| 1         | Device requires the CNTL pin to be asserted to start the unit. |

##### 7.6.2.4  pol Bit

The pol bit controls the polarity of the CNTL pin. For a change to become effective, the contents of the ON_OFF_CONFIG register must be stored to nonvolatile memory using the STORE_DEFAULT_ALL command and the device power cycled. Simply writing a new value to this bit does not change the polarity of the CNTL pin.

| BIT VALUE | ACTION                   |
| --------- | ------------------------ |
| 0         | CNTL pin is active low.  |
| 1         | CNTL pin is active high. |

##### 7.6.2.5  cpa Bit

The cpa bit sets the CNTL pin action when turning the converter off.

| BIT VALUE | ACTION                                                       |
| --------- | ------------------------------------------------------------ |
| 0         | Use the programmed turnoff delay (TOFF_DELAY) and ramp down (TOFF_FALL). |
| 1         | Immediately turn off the output (not honoring the programmed turnoff delay (TOFF_DELAY) and ramp down (TOFF_FALL)). |

#### 7.6.3   CLEAR_FAULTS (03h)

The CLEAR_FAULTS command is used to clear any fault bits that have been set. This command clears all bits in all status registers simultaneously. At the same time, the device negates (clears, releases) its SMBALERT signal output if the device is asserting the SMBALERT signal. The CLEAR_FAULTS command does not cause a unit that has latched off for a fault condition to restart. If the fault is still present when the bit is cleared, the fault bit is immediately reset and the host notified by the usual means.

NOTE

•     To get a reliable clear fault result, the clear_fault command should be issued (8 × TON_RISE + TON_DELAY) after the switcher shuts down.

•     In the case of OV fault with a latch off response, the LS FET latches on when the fault is detected. If the OV_RESP_SEL Bit in (F0h) MFR_SPECIFIC_32 is set to 1, then the LS FET releases when the FB pin voltage falls below 0.2 V. Otherwise, it remains on until the CLEAR_FAULTS command is issued. The CLEAR FAULTS command causes the LS FET to turn off.

•     CNTL pin toggling can also clear fault, but the logic low duration should be higher than 100 ns for the internal circuit to recognize.

#### 7.6.4   WRITE_PROTECT (10h)

The WRITE_PROTECT command is used to control writing to the PMBus device. The intent of this command is to provide protection against accidental changes. This command is not intended to provide protection against deliberate or malicious changes to the device configuration or operation. All supported command parameters may have their parameters read, regardless of the WRITE_PROTECT settings. Write protection also prevents protected registers from being updated in the event of a RESTORE_DEFAULT_ALL. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

| COMMAND       | WRITE_PROTECT   |      |      |      |      |      |      |      |
| ------------- | --------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Unsigned binary |      |      |      |      |      |      |      |
| Bit Position  | 7               | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r/wE            | r/wE | r/wE | X    | X    | X    | X    | X    |
| Function      | bit7            | bit6 | bit5 | X    | X    | X    | X    | X    |
| Default Value | 0               | 0    | 0    | X    | X    | X    | X    | X    |

##### 7.6.4.1 bit5

| BIT VALUE | ACTION                                                                                                                                  |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 0         | Enable all writes as permitted in bit6 or bit7                                                                                          |
| 1         | Disable all writes except the WRITE\_PROTECT, OPERATION, ON\_OFF\_CONFIG, and VOUT\_COMMAND. (bit6 and bit7 must be 0 to be valid data) |

##### 7.6.4.2 bit6

| BIT VALUE | ACTION                                                                                                               |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| 0         | Enable all writes as permitted in bit5 or bit7                                                                       |
| 1         | Disable all writes except for the WRITE\_PROTECT, and OPERATION commands. (bit5 and bit7 must be 0 to be valid data) |

##### 7.6.4.3 bit7

| BIT VALUE | ACTION                                                                                               |
| --------- | ---------------------------------------------------------------------------------------------------- |
| 0         | Enable all writes as permitted in bit5 or bit6                                                       |
| 1         | Disable all writes except for the WRITE\_PROTECT command. (bit5 and bit6 must be 0 to be valid data) |

In any case, only one of the three bits may be set at any one time. Attempting to set more than one bit results in an alert being generated and the cml bit is STATUS_WORD being set. An invalid setting of the WRITE_PROTECT command results in no write protection.

| Data Byte Value | ACTION                                                       |
| --------------- | ------------------------------------------------------------ |
| 1000 0000       | Disables all WRITES except to the WRITE\_PROTECT command.    |
| 0100 0000       | Disables all WRITES except to the WRITE\_PROTECT, and OPERATION commands. |
| 0010 0000       | Disables all WRITES except to the WRITE\_PROTECT, OPERATION, ON\_OFF\_CONFIG, and VOUT\_COMMAND commands. |

#### 7.6.5 STORE_DEFAULT_ALL (11h)

The STORE_DEFAULT_ALL command stores all of the current storable register settings in the EEPROM memory as the new defaults on power up. It is permissible to use this command while the device is switching. Note however that the device continues to switch but ignores all fault conditions until the internal store process has completed. Issuing STORE_DEFAULT_ALL also causes the device to be unresponsive through PMBus for a period of approximately 100 ms. EEPROM programming faults cause the device to NACK and set the cml bit in the STATUS_BYTE and the mem bit in the STATUS_CML registers.

#### 7.6.6 RESTORE_DEFAULT_ALL (12h)

The RESTORE_DEFAULT_ALL command restores all of the storable register settings from EEPROM memory to those registers which are unprotected according to current setting of WRITE_PROTECT. Issuing STORE_DEFAULT_ALL also causes the device to be unresponsive through PMBus for a period of approximately 100 ms.

NOTE

Do not use this command while the device is actively switching, this causes the device to stop switching and the output voltage to fall during the restore event. Depending on loading conditions, the output voltage could reach an undervoltage level and trigger an undervoltage fault response if programmed to do so. The command can be used while the device is switching, but this usage is not recommended as it results in a restart that could disrupt power sequencing requirements in more complex systems. TI strongly recommends stopping the device before issuing this command.

#### 7.6.7 STORE_USER_ALL (11h)

The STORE_USER_ALL command stores all of the current storable register settings in the EEPROM memory as the new defaults on power up. It is permissible to use this command while the device is switching. Note however that the device continues to switch but ignores all fault conditions until the internal store process has completed. Issuing STORE_USER_ALL also causes the device to be unresponsive through PMBus for a period of approximately 100 ms. EEPROM programming faults cause the device to NACK and set the cml bit in the STATUS_BYTE and the mem bit in the STATUS_CML registers. This command shares the same hardware implementation as STORE_DEFAULT_ALL.

#### 7.6.8 RESTORE_USER_ALL (12h)

The RESTORE_USER_ALL command restores all of the storable register settings from EEPROM memory to those registers which are unprotected according to current setting of WRITE_PROTECT. Issuing STORE_USER_ALL also causes the device to be unresponsive through PMBus for a period of approximately 100 ms. This command shares the same hardware implementation as RESTORE_DEFAULT_ALL.

NOTE

Do not use this command while the device is actively switching, this causes the device to stop switching and the output voltage to fall during the restore event. Depending on loading conditions, the output voltage could reach an undervoltage level and trigger an undervoltage fault response if programmed to do so. The command can be used while the device is switching, but this usage is not recommended as it results in a restart that could disrupt power sequencing requirements in more complex systems. TI strongly recommends stopping the device before issuing this command.

#### 7.6.9 CAPABILITY (19h)

The CAPABILITY command provides a way for a host system to determine some key capabilities of this PMBus device.

| COMMAND       | CAPABILITY      |      |      |      |      |      |          |      |
| ------------- | --------------- | ---- | ---- | ---- | ---- | ---- | -------- | ---- |
| Format        | Unsigned binary |      |      |      |      |      |          |      |
| Bit Position  | 7               | 6    | 5    | 4    | 3    | 2    | 1        | 0    |
| Access        | r               | r    | r    | r    | r    | r    | r        | r    |
| Function      | PEC             |      | SPD  | ALRT |      |      | Reserved |      |
| Default Value | 1               | 0    | 1    | 1    | 0    | 0    | 0        | 0    |

#### 7.6.10 SMBALERT_MASK (1Bh)

The SMBALERT_MASK command can be used to prevent a warning or fault condition from asserting the SMBALERT signal.

NOTE

The command uses the SMBus Write Word command protocol to overlay a “mask byte” with an associated/designated status register. It uses the SMBus Block Write/Block Read protocol – with a block size = 1, to read the mask settings for any given status register. If the host in the Block_Count field of the Block Write portion sends a block size unequal to 1 the device returns a NACK. The device always returns a Block Count of 1 upon reads of SMBALERT_MASK.

The bits in the mask byte align with the bits in the corresponding status register. For example, if the STATUS_TEMPERATURE command were sent with the mask byte 01000000b, then an Overtemperature Warning condition would be blocked from asserting SMBALERT. Please refer to the PMBus v1.3 specification - section 15.38 (SMBALERT_MASK Command) and the SMBus specification Block Write/Block Read protocol for further details.

There are 19 maskable SMBALERT sources in the TPS546C23. Each of these 19 status conditions has an associated EEPROM backed mask bit. These sources are represented and identified in the status register command descriptions by a particular status bit denoted as having EEPROM backup (for example a bit access of r/wE). Writes and reads to SMBALERT_MASK command code accepts only the following as valid STATUS_x command codes:

- STATUS_WORD
- STATUS_VOUT
- STATUS_IOUT
- STATUS_INPUT
- STATUS_TEMPERATURE
- STATUS_CML
- STATUS_MFR_SPECIFIC

Attempting to write a mask byte for any STATUS_X command code other than this list causes the device to set the cml bit in the STATUS_BYTE and the ivd bit in the STATUS_CML registers, and triggers SMBALERT. Attempting to read a mask byte for any STATUS_x command code other than this list returns 00h for the mask byte. Refer to these individual command descriptions for further details on their specific SMBALERT masking capabilities.

There is 1 unique status bit in the TPS546C23 that warrants special clarification: PGOOD_Z (STATUS_WORD[10]) is maskable as an SMBALERT source through SMBALERT_MASK commands to STATUS_WORD. If the user wants to write, or read, the mask bit for PGOOD_Z, the user must put 79h in the STATUS_x COMMAND_CODE field of the SMBALERT_MASK command. PGOOD_Z SMBALERT_MASK bit default to 1.

#### 7.6.11 VOUT_MODE (20h)

The PMBus specification dictates that the data word for the VOUT_MODE command is one byte that consists of a 3-bit mode and 5-bit exponent parameter, as shown below. The 3-bit mode sets whether the device uses the Linear or Direct modes for output voltage related commands. The 5-bit parameter sets the exponent value for the linear data mode. The mode and exponent parameters are fixed and do not permit the user to change the values.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

| COMMAND       | VOUT\_MODE |      |      |          |      |      |      |      |      |
| ------------- | ---------- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- |
| Bit Position  | 7          | 6    | 5    | 4        |      | 3    | 2    | 1    | 0    |
| Access        | r          | r    | r    | r        | r    | r    | r    | r    |      |
| Function      | Mode       |      |      | Exponent |      |      |      |      |      |
| Default Value | 0          | 0    | 0    | 1        | 0    | 1    | 1    | 1    |      |

##### 7.6.11.1 Mode Bit

Value fixed at 000, linear mode.

##### 7.6.11.2 Exponent Bit

Value fixed at 10111, Exponent for Linear mode values is –9 (equivalent of 1.95mV/count).

#### 7.6.12 VOUT_COMMAND (21h)

The VOUT_COMMAND command sets the output voltage in volts. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command. The exponent is set be VOUT_MODE at –9 (equivalent of 1.953 mV/count). The programmed internal reference voltage is computed as:

EA_REF = [(VOUT_COMMAND × VOUT_SCALE_LOOP) + (VREF_TRIM + STEP_VREF_MARGIN_HIGH × OPERATION[5] + STEP_VREF_MARGIN_LOW × OPERATION[4] )] × 2–9 (V)                                                 (5)

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The range of valid VOUT_COMMAND values is dependent upon the configured VOUT_SCALE_LOOP (29h) as follows:

| VOUT\_SCALE\_LOOP | Vout Range (volts) | VOUT\_COMMAND data valid range |
| ----------------- | ------------------ | ------------------------------ |
| 1                 | 0.35 to 1.65       | 179 to 845                     |
| 0.5               | 0.7 to 3.3         | 358 to 1690                    |
| 0.25              | 1.4 to 5.5         | 716 to 2816                    |

Any VOUT_COMMAND > 2816 (5.5-V maximum VOUT equivalent) is treated as invalid data:

- NACK the data byte
- Do not update VOUT_COMMAND
- Set CML bit in STATUS_BYTE
- Set IVD bit in STATUS_CML

If the value programmed to VOUT_COMMAND exceeds the value stored in either VOUT_MIN or VOUT_MAX. In this case, VOUT_COMMAND will be set to the appropriate VOUT_MIN or VOUT_MAX value (whichever was violated). See the command descriptions for (28h) VOUT_MIN or (24h) VOUT_MAX for the specific status bits set in either case.

| COMMAND       | VOUT_COMMAND            |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| ------------- | ----------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Linear, unsigned binary |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7                       | 6    | 5    | 4    | 3    | 2    | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r                       | r    | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      | Mantissa                |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0                       | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 1    | 0    | 0    | 1    | 1    | 0    | 0    | 1    |

##### 7.6.12.1 Exponent

Value fixed at 10111, Exponent for Linear mode values is –9 (equivalent of 1.95mV/count, specified in VOUT_MODE command).

##### 7.6.12.2 Mantissa

This is the Mantissa for the linear format. The default for this bit value is: 0000 0001 0011 0011 (binary) 486 (decimal) (equivalent Vout default = 0.6 V).

#### 7.6.13 VOUT_MAX (24h)

The VOUT_MAX command sets the maximum output voltage. The purpose is to protect the devices on the output rail supplied by this device from a higher than acceptable output voltage. VOUT_MAX imposes an upper bound to any attempt to program the output voltage to a VOUT_EQUIV setting by changing any of the following registers:

VOUT_COMMAND

VOUT_MAX

VOUT_MIN

OPERATION[5]

OPERATION[4]

VREF_TRIM

STEP_VREF_MARGIN_HIGH

STEP_VREF_MARGIN_LOW

VOUT_SCALE_LOOP

The exponent is set be VOUT_MODE at –9 (equivalent of 1.953 mV/count). Use Equation 6 to calculate the programmed output voltage.

MAXIMUM VOUT allowed = VOUT_MAX × VOUT_MODE (V) = VOUT_MAX × 2–9 (V)                    (6)

The range of valid VOUT_MAX values is dependent upon the configured (29h) VOUT_SCALE_LOOP as shown in Equation 7.

MAXIMUM VOUT Reference allowed = VOUT_MAX × VOUT_SCALE_LOOP x VOUT_MODE (V) = VOUT_MAX × VOUT_SCALE_LOOP × 2–9 (V)                                                               (7)

If, while the output voltage is turned on, any attempt is made to program: (1) VOUT_EQUIV to be greater than VOUT_MAX; (2) VOUT_MAX to be less than, or equal to, VOUT_MIN, or; (3) VOUT_MIN to be greater than, or equal to, VOUT_MAX – the device will:

- Clamp the internal reference voltage to VOUT_MAX × VOUT_SCALE_LOOP × VOUT_MODE value. In the event VOUT_MAX &#x3C; VOUT_MIN, VOUT_MAX shall dominate.
- Sets the OTH (other) bit in the STATUS_BYTE
- Sets the VFW bit in the STATUS_WORD
- Sets the VOUT_MAX_MIN_Warning bit in the STATUS_VOUT register
- Notifies the host through the SMBALERT pin

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

| COMMAND      | VOUT_MAX                |          |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| ------------ | ----------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format       | Linear, unsigned binary |          |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| Bit Position | 7                       | 6        | 5    | 4    | 3    | 2    | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access       | r                       | r        | r    | r    | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  |
| Function     |                         | Mantissa |      |      |      |      |      |      |      |      |      |      |      |      |      |      |

##### 7.6.13.1 Exponent

Value fixed at 10111, Exponent for Linear mode values is –9 (equivalent of 1.95 mV/count, specified in VOUT_MODE command).

##### 7.6.13.2 Mantissa

The range of valid VOUT_MAX values is dependent upon the configured (29h) VOUT_SCALE_LOOP as follows.

If VOUT_SCALE_LOOP = 1:

- default: 0000 0011 0100 1101 (binary) 845 (decimal) (equivalent VOUT_MAX = 1.65 V)
- Minimum: 0000 0001 0001 1010 (binary) 282 (decimal) (equivalent VOUT_MAX = 0.55 V)
- Maximum: 0000 0011 0100 1101 (binary) 845 (decimal) (equivalent VOUT_MAX = 1.65 V)

If VOUT_SCALE_LOOP = 0.5:

- default: 0000 0110 1001 1010 (binary) 1690 (decimal) (equivalent VOUT_MAX = 3.3 V)
- Minimum: 0000 0010 0011 0100 (binary) 564 (decimal) (equivalent VOUT_MAX = 1.1 V)
- Maximum: 0000 0110 1001 0000 (binary) 1690 (decimal) (equivalent VOUT_MAX = 3.3 V)

If VOUT_SCALE_LOOP = 0.25:

- default: 0000 1100 0000 0000 (binary) 3072 (decimal) (equivalent VOUT_MAX = 6 V)
- Minimum: 0000 0100 0110 1000 (binary) 1128 (decimal) (equivalent VOUT_MAX = 2.2 V)
- Maximum: 0000 1100 0000 0000 (binary) 3072 (decimal) (equivalent VOUT_MAX = 6 V)

#### 7.6.14 VOUT_TRANSITION_RATE (27h)

The VOUT_TRANSITION_RATE command sets the rate of change in mV/μs of any output voltage change during normal operation (also includes vout changes in TOFF_DELAY state. In contrast the soft-start transition rate is controlled by TON_RISE and the TOFF_FALL transition rate is controlled by TOFF_FALL command).

For PWM loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

Only 8 fixed output voltage transition rates are available in the device. As such, the range of programmed VOUT-transition rates are sub-divided into 8 buckets that then selects one of the 8 fixed VOUT-transition rates. Programmed values are rounded to the nearest bucket/transition rate as outlined below:

| COMMAND       | VOUT_TRANSITION_RATE            |      |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | ------------------------------- | ---- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Linear, two’s complement binary |      |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7                               | 6    | 5    | 4    | 3    | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r                               | r    | r    | r    | r    | r        | r    | r    | r    | r/w  | r/w  | r/w  | r/w  | r/w  |      | r/w  |
| Function      | Exponent                        |      |      |      |      | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value | 1                               | 1    | 1    | 0    | 1    | 0        | 0    | 0    | 0    | 0    | 1    | 1    | 1    | 1    | 0    | 0    |

##### 7.6.14.1 Exponent

default: 11010 (binary) –6 (decimal) (0.015625) These default settings are not programmable.

##### 7.6.14.2 Mantissa

default: 000 0011 1100 (binary) 60 (decimal) (equivalent VOUT_TRANSITION_RATE = 1 mV/μs)

NOTE

Using VOUT_TRANSITION_RATE to slew Vref faster than the voltage loop can track is possible. This usage causes a control related overshoot/undershoot response on the output voltage.

|                                  | VOUT_TRANSITION Mantissa (d) |                       |
| -------------------------------- | ---------------------------- | --------------------- |
| VOUT\_TRANSITION ON rate (mV/μs) | Greater than                 | Less than or equal to |
| 0.067                            | —                            | 5                     |
| 0.1                              | 5                            | 7                     |
| 0.143                            | 7                            | 12                    |
| 0.222                            | 12                           | 17                    |
| 0.333                            | 17                           | 25                    |
| 0.5                              | 25                           | 47                    |
| 1                                | 47                           | 79                    |
| 1.5                              | 79                           | —                     |

#### 7.6.15 VOUT_SCALE_LOOP (29h)

The VOUT_SCALE_LOOP command is equal to the feedback resistor ratio (RBIAS / (RBIAS + R1) in the configuration shown in Figure 25). This command is limited to only 3 possible options/ratios: 1 (default, no RBIAS needed), 0.5, and 0.25. Attempting to write a value unequal to one of these three options cause the device to set the cml bit in the STATUS_BYTE, and the ivd bit in the STATUS_CML registers. Additionally, SMBALERT is asserted and the value of VOUT_SCALE_LOOP remains unchanged. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

NOTE

Construct the feedback resistor ratio appropriately (see Table 1). If the VOUT_SCALE_LOOP does not match the external feedback resistor ratio, the converter will regulate the output with the reference voltage as outlined in Equation 1 and Equation 2. Program the VOUT_SCALE_LOOP setting before the output is turned on.

For the range checking to work properly and to avoid invalid data scenarios:

- VOUT_SCALE_LOOP should be changed first, if needed.
- VOUT_MIN and VOUT_MAX should be changed after VOUT_SCALE_LOOP, if needed.
- Additionally, it is assumed that VOUT_SCALE_LOOP will be programmed before the output is turned on; but, the hardware will not do anything to prohibit changing VOUT_SCALE_LOOP in any state.

| COMMAND       | VOUT_SCALE_LOOP                 |          |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| ------------- | ------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Linear, two’s complement binary |          |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7                               | 6        | 5    | 4    | 3    | 2    | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r                               | r        | r    | r    | r    | r    | r    | r    | r    | r    | r    | r    | r    | r/wE | r/wE | r/wE |
| Function      |                                 | Mantissa |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| Default Value | 1                               | 1        | 1    | 1    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 1    | 0    | 0    |

##### 7.6.15.1 Exponent

default: 11110 (binary) –2 (decimal) (equivalent LSB = 0.25)

These default settings are not programmable.

##### 7.6.15.2 Mantissa

default: 000 0000 0100 (binary) 4 (decimal) (equivalent VOUT_SCALE_LOOP voltage = 1)

- For VOUT_SCALE_LOOP = 1, mantissa = 004h. (4 × 2–2 = 1)
- For VOUT_SCALE_LOOP = 0.5, mantissa = 002h. (2 × 2–2 = 0.5)
- For VOUT_SCALE_LOOP = 0.25, mantissa = 001h. (1 × 2–2 = 0.25)

#### 7.6.16 VOUT_MIN (2Bh)

The VOUT_MIN command sets the minimum output voltage. The purpose is to protect the devices on the output rail supplied by this device from a lower than acceptable output voltage. VOUT_MIN imposes a lower bound to any attempt to program the output voltage to a VOUT_EQUIV setting by changing any of the following registers:

- VOUT_COMMAND
- VOUT_MAX
- VOUT_MIN
- OPERATION[5]
- OPERATION[4]
- VREF_TRIM
- STEP_VREF_MARGIN_HIGH
- STEP_VREF_MARGIN_LOW
- VOUT_SCALE_LOOP

The exponent is set be VOUT_MODE at –9 (equivalent of 1.953 mV/count). Use Equation 8 to calculate the programmed output voltage.

MINIMUM VOUT allowed = VOUT_MIN × VOUT_MODE (V) = VOUT_MIN × 2–9 (V) (8)

The range of valid VOUT_MIN values is dependent upon the configured (29h) VOUT_SCALE_LOOP as shown in Equation 9.

MINIMUM VOUT allowed = VOUT_MIN × VOUT_SCALE_LOOP × VOUT_MODE (V) = VOUT_MIN × VOUT_SCALE_LOOP × 2–9 (V) (9)

If, while the output voltage is turned on, any attempt is made to program: (1) VOUT_EQUIV to be less than VOUT_MIN, the device will:

- Clamp the internal reference voltage to VOUT_MIN × VOUT_SCALE_LOOP × VOUT_MODE value. In the event VOUT_MAX &#x3C; VOUT_MIN, VOUT_MAX shall dominate.
- Sets the OTH (other) bit in the STATUS_BYTE
- Sets the VFW bit in the STATUS_WORD
- Sets the VOUT_MAX_MIN_Warning bit in the STATUS_VOUT register
- Notifies the host through the SMBALERT pin

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

| COMMAND      | VOUT_MIN |                         |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| ------------ | -------- | ----------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format       |          | Linear, unsigned binary |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| Bit Position | 7        | 6                       | 5    | 4    | 3    | 2    | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access       | r        | r                       | r    | r    | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  |
| Function     |          | Mantissa                |      |      |      |      |      |      |      |      |      |      |      |      |      |      |

##### 7.6.16.1 Exponent

Value fixed at 10111, Exponent for Linear mode values is –9 (equivalent of 1.95 mV/count, specified in VOUT_MODE command).

##### 7.6.16.2 Mantissa

The range of valid VOUT_MIN values is dependent upon the configured (29h) VOUT_SCALE_LOOP as follows.

- If VOUT_SCALE_LOOP = 1:
- - default: 0000 0000 1011 0011 (binary) 179 (decimal) (equivalent VOUT_MIN = 0.35 V)
- Minimum: 0000 0000 1011 0011 (binary) 179 (decimal) (equivalent VOUT_MIN = 0.35 V)
- Maximum: 0000 0011 0000 0000 (binary) 768 (decimal) (equivalent VOUT_MIN = 1.5 V)

If VOUT_SCALE_LOOP = 0.5:
- - default: 0000 0001 0110 0110 (binary) 358 (decimal) (equivalent VOUT_MIN = 0.7 V)
- Minimum: 0000 0001 0110 0110 (binary) 358 (decimal) (equivalent VOUT_MIN = 0.7 V)
- Maximum: 0000 0110 0000 0000 (binary) 1536 (decimal) (equivalent VOUT_MIN = 3 V)

If VOUT_SCALE_LOOP = 0.25:

#### 7.6.17 VIN_ON (35h)

The VIN_ON command sets the value of the input voltage at which the unit should start operation assuming all other required startup conditions are met. Values are mapped to the nearest supported increment. Values outside the supported range are treated as invalid data and cause the device to set the CML bit in the STATUS_BYTE and the invalid data (ivd) bit in the STATUS_CML registers, and trigger SMBALERT signal. The value of VIN_ON remains unchanged on an out-of-range write attempt. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

The supported VIN_ON values are shown in Table 6:

##### Table 6. Supported VIN_ON Values

| VIN\_ON Values (V) |               |      |      |      |
| ------------------ | ------------- | ---- | ---- | ---- |
| 4.25               | 4.5 (default) | 4.75 | 5    | 5.25 |
| 5.5                | 5.75          | 6    | 6.25 | 6.5  |
| 6.75               | 7             | 7.25 | 7.5  | 7.75 |

VIN_ON must be set higher than VIN_OFF. Attempting to write either VIN_ON lower than VIN_OFF or VIN_OFF higher than VIN_ON results in the new value being rejected, SMBALERT signal being asserted along with the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML.

The data word that accompanies this command is divided into a fixed 5-bit exponent and an 11-bit mantissa. The four most significant bits of the mantissa are fixed, while the lower 4 bits may be altered.

| COMMAND       | VIN_ON |      |          |      |      |          |      |                                 |      |      |      |      |      |      |      |      |
| ------------- | ------ | ---- | -------- | ---- | ---- | -------- | ---- | ------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |        |      |          |      |      |          |      | Linear, two's complement binary |      |      |      |      |      |      |      |      |
| Bit Position  | 7      | 6    | 5        | 4    | 3    | 2        | 1    | 0                               | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r      | r    | r        | r    | r    | r        | r    | r                               | r    | r    | r    | r    | r/wE | r/wE | r/wE | r/wE |
| Function      |        |      | Exponent |      |      | Mantissa |      |                                 |      |      |      |      |      |      |      |      |
| Default Value | 1      | 1    | 1        | 1    | 0    | 0        | 0    | 0                               | 0    | 0    | 0    | 1    | 0    | 0    | 1    | 0    |

##### 7.6.17.1 Exponent

default: 11110 (binary) –2 (decimal) (equivalent LSB = 0.25 V)

These default settings are not programmable.

##### 7.6.17.2 Mantissa

default: 000 0001 0010 (binary) 18 (decimal) (equivalent VIN_ON voltage = 4.5 V)

Minimum: 000 0001 0001 (binary) 17 (decimal) (equivalent VIN_ON voltage = 4.25 V)

Maximum: 000 0001 1111 (binary) 31 (decimal) (equivalent VIN_ON voltage = 7.75 V)

#### 7.6.18 VIN_OFF (36h)

The VIN_OFF command sets the value of the input voltage at which the unit should stop operation. Values are mapped to the nearest supported increment. Values outside the supported range is treated as invalid data and causes the device to set the CML bit in the STATUS_BYTE and the invalid data (ivd) bit in the STATUS_CML registers, and trigger SMBALERT signal. The value of VIN_OFF remains unchanged during an out-of-range write attempt. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

The supported VIN_OFF values are shown in Table 7:

##### Table 7. Supported VIN_OFF Values

| VIN\_OFF Values (V) |      |      |      |      |
| ------------------- | ---- | ---- | ---- | ---- |
| 4 (default)         | 4.25 | 4.5  | 4.75 | 5    |
| 5.25                | 5.5  | 5.75 | 6    | 6.25 |
| 6.5                 | 6.75 | 7    | 7.25 | 7.5  |

VIN_ON must be set higher than VIN_OFF. Attempting to write either VIN_ON lower than VIN_OFF or VIN_OFF higher than VIN_ON results in the new value being rejected, SMBALERT being asserted along with the cml bit in STATUS_BYTE and the invalid data bit in STATUS_CML.

The data word that accompanies this command is divided into a fixed 5 bit exponent and an 11 bit mantissa. The 4 most significant bits of the mantissa are fixed, while the lower 7 bits may be altered.

| COMMAND       |      | VIN_OFF |          |      |      |      |                                 |      |      |      |      |      |      |      |      |      |
| ------------- | ---- | ------- | -------- | ---- | ---- | ---- | ------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |      |         |          |      |      |      | Linear, two's complement binary |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7    | 6       | 5        | 4    | 3    | 2    | 1                               | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r    | r       | r        | r    | r    | r    | r                               | r    | r    | r    | r    | r    | r/wE | r/wE | r/wE | r/wE |
| Function      |      |         | Exponent |      |      |      | Mantissa                        |      |      |      |      |      |      |      |      |      |
| Default Value | 1    | 1       | 1        | 1    | 0    | 0    | 0                               | 0    | 0    | 0    | 0    | 1    | 0    | 0    | 0    | 0    |

##### 7.6.18.1 Exponent

default: 11110 (binary) –2 (decimal) (equivalent LSB = 0.25 V)

These default settings are not programmable.

##### 7.6.18.2 Mantissa

default: 000 0001 0000 (binary) 16 (decimal) (equivalent VIN_OFF voltage = 4 V)

Minimum: 000 0001 0000 (binary) 16 (decimal) (equivalent VIN_OFF voltage = 4 V)

Maximum: 000 0001 1110 (binary) 30 (decimal) (equivalent VIN_OFF voltage = 7.5 V)

#### 7.6.19 IOUT_CAL_OFFSET (39h)

The IOUT_CAL_OFFSET command is used to compensate for offset errors in the READ_IOUT results and the IOUT_OC_FAULT_LIMIT and IOUT_OC_WARN_LIMIT thresholds. The units are amperes. The default setting is 0 A. The resolution of the argument for this command is 62.5 mA and the range is +3.9375 A to –4 A. Values written outside of this range alias into the supported range. This occurs because the read-only bits are fixed. The exponent is always –4 and the 5 MSB bits of the Mantissa are always equal to the sign bit. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

| COMMAND       | IOUT_CAL_OFFSET |      |          |      |      |      |                                 |      |      |      |      |      |      |      |      |      |
| ------------- | --------------- | ---- | -------- | ---- | ---- | ---- | ------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |                 |      |          |      |      |      | Linear, two's complement binary |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7               | 6    | 5        | 4    | 3    | 2    | 1                               | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r               | r    | r        | r    | r    | r/wE | r                               | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |                 |      | Exponent |      |      |      | Mantissa                        |      |      |      |      |      |      |      |      |      |
| Default Value | 1               | 1    | 1        | 0    | 0    | 0    | 0                               | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

##### 7.6.19.1 Exponent

default: 11100 (binary) –4 (decimal) (LSB = 62.5 mA)

These default settings are not programmable.

##### 7.6.19.2 Mantissa

MSB is programmable with sign, next 4 bits are sign extend only. Lower six bits are programmable with a default value of 0 (decimal).

#### 7.6.20 VOUT_OV_FAULT_RESPONSE (41h)

The VOUT_OV_FAULT_RESPONSE command instructs the device on what action to take in response to an Output Over Voltage Fault based on MFR_SPECIFIC_07 (PCT_OV_UV_WRN_FLT_LIMITS). The device also:

- Sets the OVF bit in the STATUS_BYTE
- Sets the VFW bit in the STATUS_WORD
- Sets the OVF bit in the STATUS_VOUT register, and
- Notifies the host by asserting SMBALERT

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

The default response to a output overvoltage fault is to shut down and restart with 7 × TON_RISE time delay.

| COMMAND       |         | VOUT\_OV\_FAULT\_RESPONSE |        |        |        |        |        |        |
| ------------- | ------- | ------------------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| Format        |         | Unsigned binary           |        |        |        |        |        |        |
| Bit Position  | 7       | 6                         | 5      | 4      | 3      | 2      | 1      | 0      |
| Access        | r/wE    | r                         | r/wE   | r/w    | r/w    | r      | r      | r      |
| Function      | RSP\[1] | 0                         | RS\[2] | RS\[1] | RS\[0] | TD\[2] | TD\[1] | TD\[0] |
| Default Value | 1       | 0                         | 1      | 1      | 1      | 1      | 1      | 1      |

##### 7.6.20.1 RSP[1] Bit

This bit sets the output voltage overvoltage response to either ignore or not. The default for this bit is 1.

| BIT VALUE | ACTION                                                                                                                                                                                                      |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0         | The PMBus device continues operation without interruption. Note: In this ignore fault response mode, the associated fault status bits is set. Additionally, SMBALERT remains triggered if it is not masked. |
| 1         | The PMBus device shuts down and restarts according to RS\[2:0].                                                                                                                                             |

##### 7.6.20.2 RS[2:0] Bits

These bits are output voltage overvoltage retry setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                                                                                                                                                                                                        |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 000       | A zero value for the retry setting means that the unit does not attempt to restart. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification).                                                |
| 111       | A one value for the retry setting means that the unit goes through a normal startup (Soft start) continuously, without limitation, until it is commanded off or bias power is removed or another fault condition causes the unit to shutdown. |

Any value other than 000 or 111 is not accepted. Attempting to write any other value is rejected, causing the device to assert SMBALERT along with the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML. Note: because all 3 bits must be the same, only one (bit 5) is stored in EEPROM.

##### 7.6.20.3 TD[2:0] Bits

These bits are output voltage overvoltage retry time delay setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                                                                                                                                                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 000       | A zero value for the retry time delay setting means that the unit does not attempt to delay a restart. This is only supported when Restart is disabled by RS\[2:0] = 000. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification). |
| 111       | A one value for the retry time delay setting means that the unit waits 7 TON\_RISE times before it goes through a normal startup (Soft start). This is only supported when Restart is enabled by RS\[2:0] = 111.                                                                     |

These bits are direct reflections of the RS[2] (bit 5) value in this register.

#### 7.6.21 VOUT_UV_FAULT_RESPONSE (45h)

The VOUT_UV_FAULT_RESPONSE command instructs the device on what action to take in response to an Output Under Voltage Fault based on MFR_SPECIFIC_07 (PCT_OV_UV_WRN_FLT_LIMITS). The device also:

- Sets the oth bit in the STATUS_BYTE
- Sets the VFW bit in the STATUS_WORD
- Sets the UVF bit in the STATUS_VOUT register, and
- Notifies the host by asserting SMBALERT

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command. The default response to a output undervoltage fault is to shut down and restart with 7 × TON_RISE time delay.

| COMMAND       |         |      |        |        | VOUT\_UV\_FAULT\_RESPONSE |                 |        |        |
| ------------- | ------- | ---- | ------ | ------ | ------------------------- | --------------- | ------ | ------ |
| Format        |         |      |        |        |                           | Unsigned binary |        |        |
| Bit Position  | 7       | 6    | 5      | 4      | 3                         | 2               | 1      | 0      |
| Access        | r/wE    | r    | r/wE   | r/w    | r/w                       | r               | r      | r      |
| Function      | RSP\[1] | 0    | RS\[2] | RS\[1] | RS\[0]                    | TD\[2]          | TD\[1] | TD\[0] |
| Default Value | 1       | 0    | 1      | 1      | 1                         | 1               | 1      | 1      |

##### 7.6.21.1 RSP[1] Bit

This bit sets the output voltage undervoltage response to either ignore or not. The default for this bit is 1.

| BIT VALUE | ACTION                                                                                                                                                                                                               |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0         | The PMBus device continues operation without interruption. Note: In this ignore fault response mode, the associated fault status bits are set. Additionally, SMBALERT continues to be triggered if it is not masked. |
| 1         | The PMBus device shuts down and restarts according to RS\[2:0].                                                                                                                                                      |

##### 7.6.21.2 RS[2:0] Bits

These bits are output voltage undervoltage retry setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                                                                                                                                                                                                        |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 000       | A zero value for the retry setting means that the unit does not attempt to restart. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification)                                                 |
| 111       | A one value for the retry setting means that the unit goes through a normal startup (soft start) continuously, without limitation, until it is commanded off or bias power is removed or another fault condition causes the unit to shutdown. |

Any value other than 000 or 111 is not accepted. Attempting to write any other value is rejected, causing the device to assert SMBALERT along with the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML. Because all 3 bits must be the same, only one (bit 5) is stored in EEPROM.

##### 7.6.21.3 TD[2:0] Bits

These bits are output voltage undervoltage retry time delay setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                                                                                                                                                                                                                                              |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 000       | A zero value for the retry time delay setting means that the unit does not attempt to delay a restart. This is only supported when Restart is disabled by RS\[2:0] = 000. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification) |
| 111       | A one value for the retry time delay setting means that the unit waits 7 TON\_RISE times before it goes through a normal startup (Soft start). This is only supported when Restart is enabled by RS\[2:0] = 111.                                                                    |

These bits are direct reflections of the RS[2] (bit 5) value in this register.

#### 7.6.22 IOUT_OC_FAULT_LIMIT (46h)

The IOUT_OC_FAULT_LIMIT command sets the value of the output current, in amperes, that causes the overcurrent detector to indicate an overcurrent fault condition. The IOUT_OC_FAULT_LIMIT should be set equal to or greater than the IOUT_OC_WARN_LIMIT. Writing a value to IOUT_OC_FAULT_LIMIT less than IOUT_OC_WARN_LIMIT causes the device to set the CML bit in the STATUS_BYTE and the invalid data (ivd) bit in the STATUS_CML registers as well as assert the SMBALERT signal. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command. Since 2-LSBs are not stored in EEPROM, on STORE, always round up. If IOUT_OC_FAULT_LIMIT [1:0] > 0, add 1 to IOUT_OC_FAULT_LIMIT [6:2]

The IOUT_OC_FAULT_LIMIT takes a two-byte data word formatted as shown below:

| COMMAND       | IOUT\_OC\_FAULT\_LIMIT |                                 |      |      |           |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | ---------------------- | ------------------------------- | ---- | ---- | --------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |                        | Linear, two's complement binary |      |      |           |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7                      | 6                               | 5    | 4    | 3         | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r                      | r                               | r    | r    | r         | r        | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/w  | r/w  |
| Function      |                        | Exponent                        |      |      |           | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value |                        |                                 |      |      | See Below |          |      |      |      |      |      |      |      |      |      |      |

##### 7.6.22.1 Exponent

default: 11111 (binary) –1 (decimal) (0.5 A)

These default settings are not programmable.

##### 7.6.22.2 Mantissa

The upper four bits are fixed at 0.

The lower seven bits are programmable.

Use Equation 10 to calculate the actual output current for a given mantissa and exponent.

IOUT(oc) = Mantissa × 2Exponent = Mantissa/2 (10)

The default values and allowable ranges for each device are summarized below:

| DEVICE    | MIN OC\_FAULT\_LIMIT min | DEFAULT | MAX  | UNIT |
| --------- | ------------------------ | ------- | ---- | ---- |
| TPS546C23 | 5                        | 42      | 52   | A    |

#### 7.6.23 IOUT_OC_FAULT_RESPONSE (47h)

The IOUT_OC_FAULT_RESPONSE command instructs the device on what action to take in response to an IOUT_OC_FAULT_LIMIT. The device also:

- Sets the OCF bit in the STATUS_BYTE
- Sets the OCFW bit in the STATUS_WORD
- Sets the OCF bit in the STATUS_IOUT register, and
- Notifies the host by asserting SMBALERT

The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

The default response to an overcurrent fault is to shut down and restart with 7 × TON_RISE time delay.

| COMMAND       |         | IOUT\_OC\_FAULT\_RESPONSE |        |        |        |        |        |        |
| ------------- | ------- | ------------------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| Format        |         | Unsigned binary           |        |        |        |        |        |        |
| Bit Position  | 7       | 6                         | 5      | 4      | 3      | 2      | 1      | 0      |
| Access        | r/wE    | r/w                       | r/wE   | r/w    | r/w    | r      | r      | r      |
| Function      | RSP\[1] | RSP\[0]                   | RS\[2] | RS\[1] | RS\[0] | TD\[2] | TD\[1] | TD\[0] |
| Default Value | 1       | 1                         | 1      | 1      | 1      | 1      | 1      | 1      |

##### 7.6.23.1 RSP[1:0] Bits

These bits set the overcurrent fault response to either ignore or not. The default for this bit is 11b. Any value other than 00b or 11b will not be accepted, such an attempt will cause the ’cml’ bit in the STATUS_BYTE register and the ivd bit in the STATUS_CML register to be set, and assert SMBALERT. Because both bits must be the same, only one (bit 7) is stored in EEPROM. The default for this bit is 11b.

| BIT VALUE | ACTION                                                       |
| --------- | ------------------------------------------------------------ |
| 00        | The PMBus device continues operation without interruption. Note: In this “ignore” fault response mode, the associated fault status bits are set. Additionally, SMBALERT continues to be triggered if it is not masked. |
| 11        | The PMBus device shuts down and restarts according to RS[2:0]. |

##### 7.6.23.2 RS[2:0] Bits

These bits are overcurrent fault retry setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                       |
| --------- | ------------------------------------------------------------ |
| 000       | A zero value for the retry setting means that the unit does not attempt to restart. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification) |
| 111       | A one value for the retry setting means that the unit goes through a normal startup (soft-start) continuously, without limitation, until it is commanded off or bias power is removed or another fault condition causes the unit to shutdown. |

Any value other than 000 or 111 is not accepted. Attempting to write any other value is rejected, causing the device to assert SMBALERT along with the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML. Because all 3 bits must be the same, only one (bit 5) is stored in EEPROM.

##### 7.6.23.3 TD[2:0] Bits

These bits are over current retry time delay setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                       |
| --------- | ------------------------------------------------------------ |
| 000       | A zero value for the retry time delay setting means that the unit does not attempt to delay a restart. This is only supported when Restart is disabled by RS[2:0] = 000. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification) |
| 111       | A one value for the retry time delay setting means that the unit waits 7 TON_RISE times before it goes through a normal startup (Soft start). This is only supported when Restart is enabled by RS[2:0] = 111. |

These bits are direct reflections of the RS[2] (bit 5) value in this register.

#### 7.6.24 IOUT_OC_WARN_LIMIT (4Ah)

The IOUT_OC_WARN_LIMIT command sets the value of the output current, in amperes, that causes the overcurrent detector to indicate an overcurrent warning. When this current level is exceeded the device:

- Sets the oth bit in the STATUS_BYTE
- Sets the OCFW bit in the STATUS_WORD
- Sets the OCW bit in the STATUS_IOUT register, and
- Notifies the host by asserting SMBALERT

The IOUT_OC_WARN_LIMIT threshold should always be set to less than or equal to the IOUT_OC_FAULT_LIMIT. Writing a value to IOUT_OC_WARN_LIMIT greater than IOUT_OC_FAULT_LIMIT causes the device to set the CML bit in the STATUS_BYTE and the invalid data (ivd) bit in the STATUS_CML registers as well as assert the SMBALERT signal. In such case, the register content will remain unchanged. This behavior can be overridden by the user setting Data Limit Override (DLO) in MFR_SPECIFIC_21[4].

The default IOUT_OC_WARN_LIMIT is always set to relative to 87.5% of the OCF value. Because the IOUT_OC_WARN_LIMIT is not stored in EEPROM, the IOUT_OC_WARN_LIMIT register is set to 12.5% less than the stored OCF threshold upon any RESTORE from EEPROM (reset_restore, or RESTORE_DEFAULT_ALL command). The digital math to achieve this is: OCW_default = (OCF – OCF/8).

The IOUT_OC_WARN_LIMIT takes a two byte data word formatted as shown below:

| COMMAND       | IOUT_OC_WARN_LIMIT |                                 |      |      |           |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | ------------------ | ------------------------------- | ---- | ---- | --------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |                    | Linear, two's complement binary |      |      |           |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7                  | 6                               | 5    | 4    | 3         | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r                  | r                               | r    | r    | r         | r        | r    | r    | r    | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  |
| Function      |                    | Exponent                        |      |      |           | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value |                    |                                 |      |      | See Below |          |      |      |      |      |      |      |      |      |      |      |

##### 7.6.24.1 Exponent

default: 11111 (binary) –1 (decimal) (0.5 A)

These default settings are not programmable.

##### 7.6.24.2 Mantissa

The upper four bits are fixed at 0. Lower seven bits are programmable. The actual output warning current level for a given mantissa and exponent is:

IOUT (OCW ) = Mantissa* 2Exponent = Mantissa/2

The default values and allowable ranges for each device are summarized below:

| DEVICE    | OC\_WARN\_LIMIT MIN | DEFAULT | MAX  | UNIT |
| --------- | ------------------- | ------- | ---- | ---- |
| TPS546C23 | 4                   | 37      | 50   | A    |

#### 7.6.25 OT_FAULT_LIMIT (4Fh)

The OT_FAULT_LIMIT command sets the value of the temperature, in degrees Celsius, that causes an overtemperature fault condition, when the sensed temperature from the external sensor exceeds this limit. The OT_FAULT_LIMIT must always be greater than the OT_WARN_LIMIT. Writing a value to OT_FAULT_LIMIT less than or equal to OT_WARN_LIMIT causes the device to set the CML bit in the STATUS_BYTE and the invalid data (ivd) bit in the STATUS_CML registers as well as asserts the SMBALERT signal. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

The OT_FAULT_LIMIT takes a two byte data word formatted as shown below.

| COMMAND       | OT_FAULT_LIMIT |                                 |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | -------------- | ------------------------------- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |                | Linear, two's complement binary |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7              | 6                               | 5    | 4    | 3    | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r              | r                               | r    | r    | r    | r        | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |                | Exponent                        |      |      |      | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0              | 0                               | 0    | 0    | 0    | 0        | 0    | 0    | 1    | 0    | 0    | 1    | 0    | 0    | 0    | 1    |

##### 7.6.25.1 Exponent

default: 00000 (binary) 0 (decimal) (represents mantissa with steps of 1 degree Celsius)

These default settings are not programmable.

##### 7.6.25.2 Mantissa

default: 000 1001 0001 (binary) 145 (decimal) (145°C)

Minimum: 000 0111 1000 (binary) (equivalent OTF = 120°C)

Maximum: 000 1010 0101 (binary) (equivalent OTF = 165°C)

#### 7.6.26 OT_FAULT_RESPONSE (50h)

The OT_FAULT_RESPONSE command instructs the device on what action to take in response to an OT_FAULT_LIMIT. The device also:

- Sets the OTFW bit in the STATUS_BYTE
- Sets the OTF bit in the STATUS_TEMPERATURE
- Notifies the host by asserting SMBALERT

When the overtemperature fault is tripped, the fault flag is latched until the external sensed temperature decreases 20°C from the OT_FAULT_LIMIT.

The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command. The default response to an over temperature fault is to ignore. Fixed Bandgap Detected Overtemperature faults are never ignored. The Bandgap OT faults always respond in a shutdown and attempted restart once the part cools.

|               | COMMAND | OT\_FAULT\_RESPONSE |        |        |        |        |        |        |
| ------------- | ------- | ------------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| Format        |         | Unsigned binary     |        |        |        |        |        |        |
| Bit Position  | 7       | 6                   | 5      | 4      | 3      | 2      | 1      | 0      |
| Access        | r/wE    | r                   | r/wE   | r/w    | r/w    | r      | r      | r      |
| Function      | RSP\[1] | 0                   | RS\[2] | RS\[1] | RS\[0] | TD\[2] | TD\[1] | TD\[0] |
| Default Value | 0       | 0                   | 1      | 1      | 1      | 1      | 1      | 1      |

##### 7.6.26.1 RSP[1] Bit

This bit sets the over temperature fault response to either ignore or not. The default for this bit is 0.

| BIT VALUE | ACTION                                                                                                                                                                                                                 |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0         | The PMBus device continues operation without interruption. Note: In this “ignore” fault response mode, the associated fault status bits are set. Additionally, SMBALERT continues to be triggered if it is not masked. |
| 1         | The PMBus device shuts down and restarts according to RS\[2:0].                                                                                                                                                        |

##### 7.6.26.2 RS[2:0] Bits

These bits are over temperature fault retry setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                                                                                                                                                                                                        |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 000       | A zero value for the Retry Setting means that the unit does not attempt to restart. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification).                                                |
| 111       | A one value for the Retry Setting means that the unit goes through a normal startup (Soft start) continuously, without limitation, until it is commanded off or bias power is removed or another fault condition causes the unit to shutdown. |

Any value other than 000 or 111 is not accepted. Attempting to write any other value is rejected, causing the device to assert SMBALERT along with the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML. Because all 3 bits must be the same, only one (bit 5) is stored in EEPROM.

NOTE

The programmed response here is also applied to the bandgap-detected overtemperature (OT) faults with the one exception of the ignore response. The fixed Bandgap-detected overtemperature faults are never ignored. The bandgap OT faults always respond in a shutdown and attempted restart when the part cools.

##### 7.6.26.3 TD[2:0] Bits

These bits are overtemperature fault retry time delay setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                                                                                                                                                                                                                                              |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 000       | A zero value for the retry time delay setting means that the unit does not attempt to delay a restart. This is only supported when restart is disabled by RS\[2:0] = 000. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification) |
| 111       | A one value for the retry time delay setting means that the unit waits 7 TON\_RISE times before it goes through a normal startup (soft start). This is only supported when restart is enabled by RS\[2:0] = 111.                                                                    |

These bits are direct reflections of the RS[2] (bit 5) value in this register.

#### 7.6.27 OT_WARN_LIMIT (51h)

The OT_WARN_LIMIT command sets the value of the temperature, in degrees Celsius, that causes an overtemperature warning condition, when the sensed temperature from the external sensor exceeds this limit. Upon triggering the overtemperature warning, the device takes the following actions:

- Sets the TEMPERATURE bit in the STATUS_BYTE
- Sets the OT Warning bit in the STATUS_TEMPERATURE
- Notifies the host by asserting SMBALERT

Once the overtemperature warning is tripped, the warning flag is latched until the external sensed temperature decreases 20°C from the OT_WARN_LIMIT. The OT_WARN_LIMIT must always be less than the OT_FAULT_LIMIT. Writing a value to OT_WARN_LIMIT greater than or equal to OT_FAULT_LIMIT causes the device to set the CML bit in the STATUS_BYTE and the invalid data (ivd) bit in the STATUS_CML registers as well as assert the SMBALERT signal. In such case, the register content will remain unchanged. This behavior can be overridden by the user setting Data Limit Override (DLO) in MFR_SPECIFIC_21[4].

The default OT_WARN_LIMIT is mathematically derived from the EEPROM backed OTF limit by subtracting 25 from (4Fh) OT_FAULT_LIMIT to reach the default OT_WARN_LIMIT. If the calculated OTW is less than 100°C, then the default value is set to 100°C. OTW=max(OTF-25, 100)

The OT_WARN_LIMIT takes a two byte data word formatted as shown below:

| COMMAND       | OT_WARN_LIMIT |                 |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | ------------- | --------------- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |               | Unsigned binary |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7             | 6               | 5    | 4    | 3    | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r             | r               | r    | r    | r    | r        | r    | r    | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  |
| Function      |               | Exponent        |      |      |      | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0             | 0               | 0    | 0    | 0    | 0        | 0    | 0    | 0    | 1    | 1    | 1    | 1    | 0    | 0    | 0    |

##### 7.6.27.1 Exponent

default: 00000 (binary) 0 (decimal) (represents mantissa with steps of 1 degree Celsius) These default settings are not programmable.

##### 7.6.27.2 Mantissa

default: 000 0111 1000 (binary) 120 (decimal) (120°C) 25°C less than default OTF

Minimum: 000 0110 0100 (binary) (equivalent OTF = 100°C)

Maximum: 000 1000 1100 (binary) (equivalent OTF = 140°C)

#### 7.6.28 TON_DELAY (60h)

The TON_DELAY command sets the time in milliseconds, from when a start condition is received to when the output voltage starts to rise. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command. For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The TON_DELAY command is formatted as a linear mode two’s complement binary integer.

| COMMAND       | TON_DELAY |                                 |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | --------- | ------------------------------- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |           | Linear, two's complement binary |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7         | 6                               | 5    | 4    | 3    | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r         | r                               | r    | r    | r    | r        | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |           | Exponent                        |      |      |      | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0         | 0                               | 0    | 0    | 0    | 0        | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

##### 7.6.28.1 Exponent

default: 00000 (binary) 0 (decimal) (1 millisecond)

These default settings are not programmable.

##### 7.6.28.2 Mantissa

The upper four bits are fixed at 0. The lower seven bits are programmable with a default value of 000 0000 0000 (binary) (0 ms).

Only 16 fixed TON_DELAY times are available in the device. As such, the range of programmed TON_DELAY settings are sub-divided into 16 buckets that then selects one of the 16 supported times. Programmed values are rounded to the nearest bucket/transition rate as outlined in the table Supported TON_DELAY Values:

###### Table 8. Supported TON_DELAY Values

| EFFECTIVE TON\_DELAY (ms) | PROGRAMMED TON\_DELAY MANTISSA (decimal) **Greater than** | Less than or equal to |
| ------------------------- | --------------------------------------------------------- | --------------------- |
| 0 (50 us)                 | —                                                         | 0                     |
| 1                         | 0                                                         | 1                     |
| 2                         | 1                                                         | 2                     |
| 3                         | 2                                                         | 3                     |
| 4                         | 3                                                         | 4                     |
| 5                         | 4                                                         | 5                     |
| 6                         | 5                                                         | 6                     |
| 7                         | 6                                                         | 9                     |
| 10                        | 9                                                         | 12                    |
| 14                        | 12                                                        | 17                    |
| 19                        | 17                                                        | 22                    |
| 27                        | 22                                                        | 32                    |
| 37                        | 32                                                        | 44                    |
| 52                        | 44                                                        | 62                    |
| 72                        | 62                                                        | 86                    |
| 100                       | 86                                                        | -                     |

#### 7.6.29 TON_RISE (61h)

The TON_RISE command sets the time in milliseconds, from when the reference starts to rise until the voltage has entered the regulation band. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

Programming a value of 0 instructs the unit to bring its output voltage to the programmed regulation value as quickly as possible. For the TPS546C23 device, this results in an effective TON_RISE time of 1ms (fastest time supported).

The TON_RISE command is formatted as a linear mode two’s complement binary integer.

| COMMAND       | TON_RISE |                                 |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | -------- | ------------------------------- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |          | Linear, two's complement binary |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7        | 6                               | 5    | 4    | 3    | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r        | r                               | r    | r    | r    | r        | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |          | Exponent                        |      |      |      | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0        | 0                               | 0    | 0    | 0    | 0        | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 1    | 1    |

##### 7.6.29.1 Exponent

default: 00000 (binary) 0 (decimal) (1 millisecond)

These default settings are not programmable.

##### 7.6.29.2 Mantissa

The upper four bits are fixed at 0. The lower seven bits are programmable with a default value of 000 0000 0011 (binary) (3 ms). For PWM loop slave device, the effective TON_RISE time is locked at 100 ms.

The supported TON_RISE times over PMBus are shown in Table 9:

| Effective TON\_RISE (ms) | Programmed TON\_RISE Mantissa (d) Greater than | Less than or equal to |
| ------------------------ | ---------------------------------------------- | --------------------- |
| 1                        | —                                              | 1                     |
| 2                        | 1                                              | 2                     |
| 3                        | 2                                              | 3                     |
| 4                        | 3                                              | 4                     |
| 5                        | 4                                              | 5                     |
| 6                        | 5                                              | 6                     |
| 7                        | 6                                              | 9                     |
| 10                       | 9                                              | 12                    |
| 14                       | 12                                             | 17                    |
| 19                       | 17                                             | 22                    |
| 27                       | 22                                             | 32                    |
| 37                       | 32                                             | 44                    |
| 52                       | 44                                             | 62                    |
| 72                       | 62                                             | 86                    |
| 100                      | 86                                             | —                     |

#### 7.6.30 TON_MAX_FAULT_LIMIT (62h)

The TON_MAX_FAULT_LIMIT command sets an UPPER limit in milliseconds, on how long the unit can attempt to power up the output without reaching the output undervoltage fault limit. The time begins counting as soon as the device enters the soft-start state begins to ramp the output. In other words, the TON_MAX_FAULT_LIMIT timer starts at the beginning of the TON_RISE state.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

When TON_MAX_FAULT_LIMIT is set to 0, the TON_MAX_FAULT timer is disabled, which means that there is no limit and that the unit can attempt to bring up the output voltage indefinitely.

The device does not prohibit setting TON_MAX_FAULT_LIMIT &#x3C; TON_RISE, however, in this configuration, the device will trigger a TON_MAX_FAULT if the VOUT has not risen above the UVF threshold by 4 seconds after the TON_DELAY and TON_RISE times expire.

The TON_MAX_FAULT_LIMIT command is formatted as a linear mode two’s complement binary integer.

| COMMAND       | TON_MAX_FAULT_LIMIT |                                 |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | ------------------- | ------------------------------- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |                     | Linear, two's complement binary |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7                   | 6                               | 5    | 4    | 3    | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r                   | r                               | r    | r    | r    | r        | r    | r    | r    | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  |
| Function      |                     | Exponent                        |      |      |      | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0                   | 0                               | 0    | 0    | 0    | 0        | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

##### 7.6.30.1 Exponent

default: 00000 (binary) 0 (decimal) (Disable)

These default settings are not programmable.

##### 7.6.30.2 Mantissa

The upper four bits are fixed at 0.

This register is not EEPROM backed, a RESTORE_DEFAULT_ALL command causes the TON_MAX_FAULT_LIMIT to restore to the default 0 ms value.

The supported TON_MAX_FAULT_LIMIT times over PMBus are shown in Supported TON_MAX_FAULT_LIMIT Values:

###### Table 10. Supported TON_MAX_FAULT_LIMIT Values

| Effective TON\_MAX\_FAULT\_LIMIT (ms) | Programmed TON\_MAX\_FAULT\_LIMIT Mantissa (d) Greater than | Less than or equal to |
| ------------------------------------- | ----------------------------------------------------------- | --------------------- |
| No Limit (timer disabled)             | —                                                           | 0                     |
| 1                                     | 0                                                           | 1                     |
| 2                                     | 1                                                           | 2                     |
| 3                                     | 2                                                           | 3                     |
| 4                                     | 3                                                           | 4                     |
| 5                                     | 4                                                           | 5                     |
| 6                                     | 5                                                           | 6                     |
| 7                                     | 6                                                           | 9                     |
| 10                                    | 9                                                           | 12                    |
| 14                                    | 12                                                          | 17                    |
| 19                                    | 17                                                          | 22                    |
| 27                                    | 22                                                          | 32                    |
| 37                                    | 32                                                          | 44                    |
| 52                                    | 44                                                          | 62                    |
| 72                                    | 62                                                          | 86                    |
| 100                                   | 86                                                          | —                     |

#### 7.6.31 TON_MAX_FAULT_RESPONSE (63h)

The TON_MAX_FAULT_RESPONSE command instructs the device on what action to take in response to an TON_MAX_FAULT_LIMIT. The device also:

- Sets the oth bit in the STATUS_BYTE
- Sets the VFW bit in the STATUS_WORD
- Sets the TONMAXF bit in the STATUS_VOUT register, and
- Notifies the host by asserting SMBALERT

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command. The default response to a TON_MAX_FAULT is to shut down and restart with 7 × TON_RISE time delay.

| COMMAND       | TON\_MAX\_FAULT\_RESPONSE |                 |        |        |        |        |        |        |
| ------------- | ------------------------- | --------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| Format        |                           | Unsigned binary |        |        |        |        |        |        |
| Bit Position  | 7                         | 6               | 5      | 4      | 3      | 2      | 1      | 0      |
| Access        | r/wE                      | r               | r/wE   | r/w    | r/w    | r      | r      | r      |
| Function      | RSP\[1]                   | 0               | RS\[2] | RS\[1] | RS\[0] | TD\[2] | TD\[1] | TD\[0] |
| Default Value | 1                         | 0               | 1      | 1      | 1      | 1      | 1      | 1      |

##### 7.6.31.1 RSP[1] Bit

This bit sets the TON_MAX_FAULT response to either ignore or not. The default for this bit is 1.

| BIT VALUE | ACTION                                                                                                                                                                                                               |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0         | The PMBus device continues operation without interruption. Note: In this ignore fault response mode, the associated fault status bits are set. Additionally, SMBALERT continues to be triggered if it is not masked. |
| 1         | The PMBus device shuts down and restarts according to RS\[2:0].                                                                                                                                                      |

##### 7.6.31.2 RS[2:0] Bits

These bits are TON_MAX_FAULT retry setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                                                                                                                                                                                                        |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 000       | A zero value for the retry setting means that the unit does not attempt to restart. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification).                                                |
| 111       | A one value for the retry setting means that the unit goes through a normal startup (soft start) continuously, without limitation, until it is commanded off or bias power is removed or another fault condition causes the unit to shutdown. |

Any value other than 000 or 111 is not accepted. Attempting to write any other value is rejected, causing the device to assert SMBALERT along with the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML. Because all 3 bits must be the same, only one (bit 5) is stored in EEPROM.

##### 7.6.31.3 TD[2:0] Bits

These bits are TON_MAX_FAULT retry time delay setting. The default for this bit is 111b.

| BIT VALUE | ACTION                                                       |
| --------- | ------------------------------------------------------------ |
| 000       | A zero value for the retry time delay setting means that the unit does not attempt to delay a restart. This is only supported when restart is disabled by RS\[2:0] = 000. The output remains disabled until the fault is cleared (Refer to section 10.7 of the PMBus specification). |
| 111       | A one value for the retry time delay setting means that the unit waits 7 TON_RISE times before it goes through a normal startup (soft start). This is only supported when restart is enabled by RS[2:0] = 111 |

These bits are direct reflections of the RS[2] (bit 5) value in this register.

#### 7.6.32 TOFF_DELAY (64h)

The TOFF_DELAY command sets the time in milliseconds, from when a stop condition is received and when the output voltage starts to fall. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command. For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT. The TOFF_DELAY command is formatted as a linear mode two’s complement binary integer.

| COMMAND       | TOFF_DELAY |                                 |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| ------------- | ---------- | ------------------------------- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |            | Linear, two's complement binary |      |      |      |          |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7          | 6                               | 5    | 4    | 3    | 2        | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r          | r                               | r    | r    | r    | r        | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |            | Exponent                        |      |      |      | Mantissa |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0          | 0                               | 0    | 0    | 0    | 0        | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

##### 7.6.32.1 Exponent

default: 00000 (binary) 0 (decimal) (1 millisecond) These default settings are not programmable.

##### 7.6.32.2 Mantissa

The upper four bits are fixed at 0. The lower seven bits are programmable with a default value of 000 0000 0000 (binary) (0 ms). Only 16 fixed TOFF_DELAY times are available in the device. As such, the range of programmed TOFF_DELAY settings are sub-divided into 16 buckets that then selects one of the 16 supported times. Programmed values are rounded to the nearest bucket/transition rate as outlined in the table Supported TOFF_DELAY Values:

###### Table 11. Supported TOFF_DELAY Values

| EFFECTIVE TOFF\_DELAY (ms) | PROGRAMMED TOFF\_DELAY MANTISSA (decimal) |                       |
| -------------------------- | ----------------------------------------- | --------------------- |
|                            | Greater than                              | Less than or equal to |
| 0                          | —                                         | 0                     |
| 1                          | 0                                         | 1                     |
| 2                          | 1                                         | 2                     |
| 3                          | 2                                         | 3                     |
| 4                          | 3                                         | 4                     |
| 5                          | 4                                         | 5                     |
| 6                          | 5                                         | 6                     |
| 7                          | 6                                         | 9                     |
| 10                         | 9                                         | 12                    |
| 14                         | 12                                        | 17                    |
| 19                         | 17                                        | 22                    |
| 27                         | 22                                        | 32                    |
| 37                         | 32                                        | 44                    |
| 52                         | 44                                        | 62                    |

###### Table 11. Supported TOFF_DELAY Values (continued)

| EFFECTIVE TOFF\_DELAY (ms) | PROGRAMMED TOFF\_DELAY MANTISSA (decimal) |                       |
| -------------------------- | ----------------------------------------- | --------------------- |
|                            | Greater than                              | Less than or equal to |
| 72                         | 62                                        | 86                    |
| 100                        | 86                                        | —                     |

#### 7.6.33 TOFF_FALL (65h)

The TOFF_FALL command sets the time in milliseconds, from the end of the TOFF_DELAY time until the voltage reaches 0 V. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

Programming a value of 0 instructs the unit to bring its output voltage down to 0 as quickly as possible. For the TPS546C23 device, this results in actively ramping down the output voltage in 1 ms (the fastest supported ramp down).

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The TOFF_FALL command is formatted as a linear mode two’s complement binary integer.

| COMMAND       | TOFF_FALL |          |      |      |      |                                 |      |      |      |      |      |      |      |      |      |      |
| ------------- | --------- | -------- | ---- | ---- | ---- | ------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |           |          |      |      |      | Linear, two's complement binary |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7         | 6        | 5    | 4    | 3    | 2                               | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r         | r        | r    | r    | r    | r                               | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |           | Exponent |      |      |      |                                 |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0         | 0        | 0    | 0    | 0    | 0                               | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

##### 7.6.33.1 Exponent

default: 00000 (binary) 0 (decimal) (1 millisecond)

These default settings are not programmable.

##### 7.6.33.2 Mantissa

The upper four bits are fixed at 0. The lower seven bits are programmable with a default value of 000 0000 0000 (binary) (0 ms).

The supported TOFF_FALL times over PMBus are shown in Supported TOFF_FALL Values:

###### Table 12. Supported TOFF_FALL Values

| Effective TOFF\_FALL (ms) | Programmed TOFF\_FALL Mantissa (d) |                       |
| ------------------------- | ---------------------------------- | --------------------- |
|                           | Greater than                       | Less than or equal to |
| 1                         | —                                  | 1                     |
| 2                         | 1                                  | 2                     |
| 3                         | 2                                  | 3                     |
| 4                         | 3                                  | 4                     |
| 5                         | 4                                  | 5                     |
| 6                         | 5                                  | 6                     |
| 7                         | 6                                  | 9                     |
| 10                        | 9                                  | 12                    |
| 14                        | 12                                 | 17                    |
| 19                        | 17                                 | 22                    |
| 27                        | 22                                 | 32                    |
| 37                        | 32                                 | 44                    |
| 52                        | 44                                 | 62                    |

###### Table 12. Supported TOFF_FALL Values (continued)

| Effective TOFF\_FALL (ms) | Programmed TOFF_FALL Mantissa (d) Greater than | Less than or equal to |
| ------------------------- | ---------------------------------------------- | --------------------- |
| 72                        | 62                                             | 86                    |
| 100                       | 86                                             | —                     |

#### 7.6.34 STATUS_BYTE (78h)

The STATUS_BYTE command returns one byte of information with a summary of the most critical device faults.

| COMMAND       | STATUS_BYTE     |      |      |      |      |      |      |      |
| ------------- | --------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Unsigned binary |      |      |      |      |      |      |      |
| Bit Position  | 7               | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r               | r    | r    | r    | r    | r    | r    | r    |
| Function      | X               | OFF  | OVF  | OCF  | X    | OTFW | CML  | oth  |
| Default Value | 0               | X    | 0    | 0    | 0    | 0    | 0    | 1    |

A 1 in any of these bit positions indicates that:

- OFF: The device is not providing power to the output, regardless of the reason. In this family of devices, this flag means that the converter is not enabled.
- OVF: An output overvoltage fault has occurred. This bit directly reflects the state of STATUS_VOUT[7] – OVF. If the user wants this fault source to be masked and not trigger SMBALERT, they must do it by masking STATUS_VOUT[7]. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_VOUT that cause this bit to be set. For loop slave device, this bit is 0.
- OCF: An output overcurrent fault has occurred. This bit directly reflects the state of STATUS_IOUT[7] – OCF. If the user wants this fault source to be masked and not trigger SMBALERT, they must do it by masking STATUS_IOUT[7]. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_IOUT that cause this bit to be set.
- OTFW: A temperature fault or warning has occurred. Check STATUS_TEMPERATURE. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_TEMPERATURE that cause this bit to be set.
- CML: A communications, memory or logic fault has occurred. Check STATUS_CML. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_CML that cause this bit to be set.
- oth: A fault or warning not listed through bits 1-7 has occurred, which include an undervoltage fault, over current warning, overvoltage warning, undervoltage warning, TON_MAX_FAULT, LOW_VIN, VOUT_MAX_MIN_Warning, OTF_BG, or IV_PPV1. Check other status registers. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_VOUT, STATUS_IOUT, STATUS_IOUT (7Bh), or STATUS_MFR_SPECIFIC (80h) that cause this bit to be set. The default for this bit is 1 because the default of STATUS_INPUT[3] LOW_Vin defaulting to 1.

#### 7.6.35 STATUS_WORD (79h)

The STATUS_WORD command returns two bytes of information with a summary of the device fault and warning conditions. The low byte is identical to the STATUS_BYTE above. The additional byte reports the warning conditions for output overvoltage and overcurrent, as well as the power good status of the converter.

| COMMAND       |   | STATUS\_WORD (low byte) = STATUS\_BYTE |     |     |   |      |     |     |
| ------------- | - | -------------------------------------- | --- | --- | - | ---- | --- | --- |
| Format        |   | Unsigned binary                        |     |     |   |      |     |     |
| Bit Position  | 7 | 6                                      | 5   | 4   | 3 | 2    | 1   | 0   |
| Access        | r | r                                      | r   | r   | r | r    | r   | r   |
| Function      | X | OFF                                    | OVF | OCF | x | OTFW | CML | oth |
| Default Value | 0 | X                                      | 0   | 0   | 0 | 0    | 0   | 1   |

| COMMAND       |     | STATUS\_WORD (high byte) |       |     |          |   |   |   |
| ------------- | --- | ------------------------ | ----- | --- | -------- | - | - | - |
| Format        |     | Unsigned binary          |       |     |          |   |   |   |
| Bit Position  | 7   | 6                        | 5     | 4   | 3        | 2 | 1 | 0 |
| Access        | r   | r                        | r     | r   | rE       | r | r | r |
| Function      | VFW | OCFW                     | INPUT | MFR | PGOOD\_Z | X | X | X |
| Default Value | 0   | 0                        | X     | 0   | X        | 0 | 0 | 0 |

A 1 in any of the high byte bit positions indicates that:

- VFW An output voltage fault or warning has occurred (OVF or OVW or UVW or UVF or VOUT_MAX_Warning or TONMAXF). Check STATUS_VOUT. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_VOUT that cause this bit to be set.
- OCFW An output current warning or fault has occurred (OCF or OCW). Check STATUS_IOUT. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_IOUT that cause this bit to be set.
- INPUT INPUT fault or warning in STATUS_INPUT is present. Check STATUS_INPUT. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_INPUT that cause this bit to be set.
- MFR A manufacturer specific fault or warning condition has occurred (over temperature fault from Bandgap or IV_PPV1). Check STATUS_MFR_SPECIFIC. Per the PMBus v1.3 spec sections 10.2.4 and 10.2.5, this bit is not clearable through a PMBus write. In contrast, the bit is to be cleared by clearing the bits in STATUS_MFR_SPECIFIC that cause this bit to be set.
- PGOOD_Z Power is not good, and the following condition is present: output over or under voltage warning or fault, TON_MAX_FAULT, over temperature warning or fault, over current warning or fault, insufficient input voltage. Please refer to the FAULT RESPONSE table for the possible sources to trigger PGOOD_Z. The signal is unlatched and always represents the current state of the device. The factory default setting for PGOOD_Z mask bit is 1, indicating that PGOOD_Z itself cannot trigger SMBALERT by default. If unmask PGOOD_Z bit, the SMBALERT is set not to trigger before Power Good going high the first time, which is to avoid the device holding up SMBALERT bus when it is not commanded to start up and PGOOD stays low.

#### 7.6.36 STATUS_VOUT (7Ah)

The STATUS_VOUT command returns one byte of information relating to the status of the output voltage related faults.

| COMMAND       | STATUS\_VOUT    |      |      |      |                         |         |   |   |
| ------------- | --------------- | ---- | ---- | ---- | ----------------------- | ------- | - | - |
| Format        | Unsigned binary |      |      |      |                         |         |   |   |
| Bit Position  | 7               | 6    | 5    | 4    | 3                       | 2       | 1 | 0 |
| Access        | r/wE            | r/wE | r/wE | r/wE | r/wE                    | r/wE    | r | r |
| Function      | OVF             | OVW  | UVW  | UVF  | VOUT\_MAX\_MIN\_Warning | TONMAXF | X | X |
| Default Value | 0               | 0    | 0    | 0    | 0                       | 0       | 0 | 0 |

A 1 in any of these bit positions indicates that:

- OVF The device has seen the output voltage rise above the output overvoltage fault threshold VOUT_OV_FAULT_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. For loop slave device, this bit is forced to 0.
- OVW The device has seen the output voltage rise above the output overvoltage warn threshold VOUT_OV_WARN_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. For loop slave device, this bit is forced to 0.
- UVW The device has seen the output voltage fall below the output undervoltage warn threshold VOUT_UV_WARN_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. For loop slave device, this bit is forced to 0.
- UVF The device has seen the output voltage fall below the output undervoltage fault threshold VOUT_UV_FAULT_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. For loop slave device, this bit is forced to 0.
- VOUT_MAX_MIN_Warning An attempt is made to program the VOUT_COMMAND in excess of the value in VOUT_MAX or under the value in VOUT_MIN. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. For loop slave device, this bit is forced to 0.
- TONMAXF A TON_MAX_FAULT has occurred. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. For loop slave device, this bit is forced to 0.

#### 7.6.37 STATUS_IOUT (7Bh)

The STATUS_IOUT command returns one byte of information relating to the status of the output current related faults.

| COMMAND       | STATUS\_IOUT    |   |      |   |   |   |   |   |
| ------------- | --------------- | - | ---- | - | - | - | - | - |
| Format        | Unsigned binary |   |      |   |   |   |   |   |
| Bit Position  | 7               | 6 | 5    | 4 | 3 | 2 | 1 | 0 |
| Access        | r/wE            | r | r/wE | r | r | r | r | r |
| Function      | OCF             | X | OCW  | X | X | X | X | X |
| Default Value | 0               | 0 | 0    | 0 | 0 | 0 | 0 | 0 |

A 1 in any of these bit positions indicates that:

- OCF The device has seen the output current rise above the level set by IOUT_OC_FAULT_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.
- OCW The device has seen the output current rise above the level set by IOUT_OC_WARN_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.

#### 7.6.38 STATUS_INPUT (7Ch)

The STATUS_INPUT command returns one byte of information relating to the status of the input-related faults of the converter.

| COMMAND       |      | STATUS\_INPUT   |      |      |          |      |      |      |
| ------------- | ---- | --------------- | ---- | ---- | -------- | ---- | ---- | ---- |
| Format        |      | Unsigned binary |      |      |          |      |      |      |
| Bit Position  | 7    | 6               | 5    | 4    | 3        | 2    | 1    | 0    |
| Access        | r    | r               | r    | r    | r/wE     | r    | r    | r    |
| Function      | X    | X               | X    | X    | LOW\_Vin | X    | X    | X    |
| Default Value | 0    | 0               | 0    | 0    | 1        | 0    | 0    | 0    |

A 1 in any of these bit positions indicates that:

- LOW_Vin The unit is off because of insufficient input voltage. The bit sets when the unit powers up and stays set until the first time AVIN exceeds VIN_ON. During the initial power up, LOW_Vin is not latched and does not trigger SMBALERT. Once AVIN does exceed VIN_ON for the first time, any subsequent AVIN &#x3C; VIN_OFF events are latched, trigger SMBALERT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.

#### 7.6.39 STATUS_TEMPERATURE (7Dh)

The STATUS_TEMPERATURE command returns one byte of information relating to the status of the external temperature related faults.

| COMMAND       | STATUS\_TEMPERATURE |      |      |      |      |      |      |      |
| ------------- | ------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Unsigned binary     |      |      |      |      |      |      |      |
| Bit Position  | 7                   | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r/wE                | r/wE | r    | r    | r    | r    | r    | r    |
| Function      | OTF                 | OTW  | X    | X    | X    | X    | X    | X    |
| Default Value | 0                   | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

A 1 in any of these bit positions indicates that:

- OTF The measured external temperature value of READ_TEMPERATURE_1 is equal to or greater than the level set by OT_FAULT_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. However, once cleared, the bit is set again unless the value in READ_TEMPERATURE_1 has fallen 20°C from the OT_FAULT_LIMIT.
- OTW The measured external temperature value of READ_TEMPERATURE_1 is equal to or greater than the level set by OT_WARN_LIMIT. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK. However, once cleared, the bit is set again unless the value in READ_TEMPERATURE_1 has fallen 20°C from the OT_WARN_LIMIT.

#### 7.6.40 STATUS_CML (7Eh)

The STATUS_CML command returns one byte of information relating to the status of the communication-related faults of the converter.

| COMMAND       |                 | STATUS\_CML |      |      |      |      |      |      |
| ------------- | --------------- | ----------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        | Unsigned binary |             |      |      |      |      |      |      |
| Bit Position  | 7               | 6           | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r/wE            | r/wE        | r/wE | r/wE | r    | r    | r/wE | r    |
| Function      | ivc             | ivd         | pec  | mem  | X    | X    | oth  | X    |
| Default Value | 0               | 0           | 0    | 0    | 0    | 0    | 0    | 0    |

A 1 in any of these bit positions indicates that:

- ivc An invalid or unsupported command has been received. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.
- ivd An invalid or unsupported data has been received. This bit is writeable to clear and the EEPROM.

bit is for SMBALERT_MASK.

pec A packet error check failed. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.

mem A fault has been detected with the internal memory. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.

oth Some other communication fault or error has occurred. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.

#### 7.6.41 STATUS_MFR_SPECIFIC (80h)

The STATUS_MFR_SPECIFIC command returns one byte of information relating to the status of manufacturer-specific faults or warnings.

| COMMAND       |         | STATUS\_MFR\_SPECIFIC |           |          |          |   |           |           |
| ------------- | ------- | --------------------- | --------- | -------- | -------- | - | --------- | --------- |
| Format        |         | Unsigned binary       |           |          |          |   |           |           |
| Bit Position  | 7       | 6                     | 5         | 4        | 3        | 2 | 1         | 0         |
| Access        | r/wE    | r                     | r         | r/wE     | r        | r | r         | r         |
| Function      | otf\_bg | illzero               | illmany1s | iv\_ppv1 | iv\_ppv0 | 0 | is\_Slave | sync\_flt |
| Default Value | 0       | 0                     | 0         | 0        | 0        | 0 | 0         | 0         |

A 1 in any of these bit positions indicates that:

- otf_bg The internal temperature from bandgap is above the thermal shutdown (TSD) fault threshold. This bit is writeable to clear and the EEPROM bit is for SMBALERT_MASK.
- illzero The operation FSM has hit an illegal ZERO state. The FSM is a one-hot implementation, so all zeros in the state is illegal and should never occur. This event is informational only and would not trigger SMBALERT.
- illmany1s The operation FSM for has hit an illegal more than one hot state. The FSM is a one-hot implementation, so a state where multiple state bits are HI is illegal and should never occur. This event is informational only and would not trigger SMBALERT.
- iv_ppv1 The ADDR1 detection fails to resolve 4 consecutive values. To avoid initial turnon events from clearing this condition and the user not being aware why the default ADDR1 value was used, this bit is only clearable through the CLEAR_FAULTS command or writing a logic 1 to this bit, essentially off and on events do not clear it as with the other standard status bits. This condition will trigger SMBALERT.
- iv_ppv0
- sync_flt A synchronization fault. This could be because (a) Clock slave: an expected external SYNC was never present; or present, then lost, or (b) Clock master: an internal SYNC signal is not sensed on the SYNC pin. This bit is a live (essentially, unlatched) indicator. This event is informational only and would not trigger SMBALERT.

#### 7.6.42 READ_VOUT (8Bh)

The READ_VOUT commands returns two bytes of data in the linear data format that represent the output voltage of the converter. The output voltage is sensed at the remote sense amplifier output pin so voltage drop to the load is not accounted for. The data format is as shown below:

| COMMAND       | READ\_VOUT                      |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ------------- | ------------------------------- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Format        | Linear, two's complement binary |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Bit Position  | 7                               | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Access        | r                               | r | r | r | r | r | r | r | r | r | r | r | r | r | r | r |
| Function      | Mantissa                        |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Default Value | 0                               | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

##### 7.6.42.1 Exponent

Value fixed at 10111, Exponent for linear mode values is –9 (equivalent of 1.95 mV/count, specified in the VOUT_MODE command).

##### 7.6.42.2 Mantissa

Use Equation 12 to calculate the output voltage.

VOUT = Mantissa ´ 2Exponent (12)

#### 7.6.43 READ_IOUT (8Ch)

The READ_IOUT commands returns two bytes of data in the linear data format that represent the output current of the converter. The average output current is sensed according to the method described in Low-Side MOSFET Current Sensing and Overcurrent Protection. The data format is as shown below:

| COMMAND       |      |      |          |      |      | READ\_IOUT                      |      |      |      |      |      |      |      |      |      |      |
| ------------- | ---- | ---- | -------- | ---- | ---- | ------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |      |      |          |      |      | Linear, two's complement binary |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7    | 6    | 5        | 4    | 3    | 2                               | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r    | r    | r        | r    | r    | r                               | r    | r    | r    | r    | r    | r    | r    | r    | r    | r    |
| Function      |      |      | Exponent |      |      | Mantissa                        |      |      |      |      |      |      |      |      |      |      |
| Default Value | 1    | 1    | 1        | 0    | 0    | 0                               | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

The device scales the output current before it reaches the internal analog to digital converter so that resolution of the output current read is 62.5 mA. The maximum value that can be reported is 40 A. The user must set the IOUT_CAL_OFFSET parameter correctly to obtain accurate results. Use Equation 13 to calculate the output current.

IOUT = Mantissa * 2Exponent (13)

##### 7.6.43.1 Exponent

default: 11100 (binary) -4 (decimal) (62.5 mA LSB)

These default settings are not programmable.

##### 7.6.43.2 Mantissa

The lower 10 bits are the result of the ADC conversion of the average output current, as indicated by the output of the internal current sense amplifier. The 11th bit is fixed at 0 because only positive numbers are considered valid. Any computed negative current is reported as 0 A.

#### 7.6.44 READ_TEMPERATURE_1 (8Dh)

The READ_TEMPERATURE_1 command returns the external temperature in degrees Celsius.

| COMMAND      | READ\_TEMPERATURE\_1            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ------------ | ------------------------------- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Format       | Linear, two's complement binary |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Bit Position | 7                               | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Access       | r                               | r | r | r | r | r | r | r | r | r | r | r | r | r | r | r |
| Function     | Exponent                        |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

##### 7.6.44.1 Exponent

default: 00000 (binary) 0 (decimal)

These default settings are not programmable.

##### 7.6.44.2 Mantissa

The lower 11 bits are the result of the ADC conversion of the external temperature.

#### 7.6.45 PMBUS_REVISION (98h)

The PMBUS_REVISION command returns a single, unsigned binary byte that indicates that these devices are compatible with the 1.3 revision of the PMBus specification (Part I and Part II).

| COMMAND       |      |      | PMBUS\_REVISION |      |      |      |      |      |      |
| ------------- | ---- | ---- | --------------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |      |      | Unsigned binary |      |      |      |      |      |      |
| Bit Position  | 7    | 6    | 5               |      | 4    | 3    | 2    | 1    | 0    |
| Access        | r    | r    | r               |      | r    | r    | r    | r    | r    |
| Default Value | 0    | 0    | 1               |      | 1    | 0    | 0    | 1    | 1    |

#### 7.6.46 IC_DEVICE_ID (ADh)

The IC_DEVICE_ID command is a read-only block-read command that returns a single word (16 bits) with the unique device-code identifier for each device for which this device can be configured. The BYTE_COUNT field in the block read command is 2 (indicating 2 bytes follow): low byte first, high byte second.

| COMMAND       | IC\_DEVICE\_ID |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ------------- | -------------- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Format        | Linear, binary |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Bit Position  | 7              | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Access        | r              | r | r | r | r | r | r | r | r | r | r | r | r | r | r | r |
| Default Value | See below      |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

The default for the device identifier code is 4623h – Code Identifier for TPS546C23.

#### 7.6.47 IC_DEVICE_REV (AEh)

The IC_DEVICE_REV command is a read-only block-read command that returns a single word (16 bits) with the unique Device revision identifier. The DEVICE_REV starts at 0 with the first silicon and is incremented with each subsequent silicon revision. The BYTE_COUNT field in the Block Read command is 2 (indicating 2 bytes follow): low byte first, high byte second.

| COMMAND       | IC\_DEVICE\_REV |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ------------- | --------------- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Format        | Linear, binary  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Bit Position  | 7               | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Access        | r               | r | r | r | r | r | r | r | r | r | r | r | r | r | r | r |
| Default Value | See below       |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

The default of the device identifier code is 0001b.

#### 7.6.48 MFR_SPECIFIC_00 (D0h)

The MFR_SPECIFIC_00 command is dedicated as a user scratch pad. Only the lower 8 bits are writeable for users. This is a read word command, with only the lower 8 bits accessible. This command is not a read byte command. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

| COMMAND       |   |   |   | MFR\_SPECIFIC\_00 |   |   |   |   |      |      |      |      |      |      |      |      |
| ------------- | - | - | - | ----------------- | - | - | - | - | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |   |   |   | Unsigned binary   |   |   |   |   |      |      |      |      |      |      |      |      |
| Bit Position  | 7 | 6 | 5 | 4                 | 3 | 2 | 1 | 0 | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r | r | r | r                 | r | r | r | r | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |   |   |   | User scratch pad  |   |   |   |   |      |      |      |      |      |      |      |      |
| Default Value | 0 | 0 | 0 | 0                 | 0 | 0 | 0 | 0 | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

#### 7.6.49 VREF_TRIM (MFR_SPECIFIC_04) (D4h)

The VREF_TRIM command applies a fixed offset voltage to the Error Amplifier reference (EA_REF) voltage. It is most typically used to trim the output voltage at the time the PMBus device is assembled into the end user’s system. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The settings of the VOUT_MODE command determine the effect of VREF_TRIM command. In this device, the VOUT_MODE is fixed to Linear with an exponent of –9 (decimal).

EA_REF = [(VOUT_COMMAND × VOUT_SCALE_LOOP) + (VREF_TRIM + STEP_VREF_MARGIN_HIGH × OPERATION[5] + STEP_VREF_MARGIN_LOW × OPERATION[4])] × 1.953 mV (14)

The maximum trim ranges between –64*1.953 mV to +63*1.953 mV in 1.953-mV steps.

If a value outside this range is given with this command, the device sets the reference voltage to the upper or lower limit depending on the direction of the setting, asserts SMBALERT and sets the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML.

The value of EA_REF including VREF_TRIM is also limited by the values of VOUT_MAX, VOUT_MIN, VOUT_COMMAND, VOUT_SCALE_LOOP and STEP_VREF_MARGIN_HIGH/LOW. See VOUT_MAX and VOUT_MIN for additional details.

The EA_REF voltage transition occurs at the rate determined by the current state:

- Soft-Start: TON_RISE command
- Steady-State: VOUT_TRANSITION_RATE command
- TOFF_DELAY: VOUT_TRANSITION_RATE command
- Soft-Stop: TOFF_FALL command

The VREF_TRIM has two data bytes formatted as two’s complement binary integer and can have positive and negative values.

| COMMAND       |      |           | VREF\_TRIM                      |          |      |      |      |      |      |      |      |      |      |      |      |      |
| ------------- | ---- | --------- | ------------------------------- | -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format        |      |           | Linear, two’s complement binary |          |      |      |      |      |      |      |      |      |      |      |      |      |
| Bit Position  | 7    | 6         | 5                               | 4        | 3    | 2    | 1    | 0    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Access        | r/wE | r         | r                               | r        | r    | r    | r    | r    | r    | r    | r/wE | r/wE | r/wE | r/wE | r/wE | r/wE |
| Function      |      | High Byte |                                 | Low Byte |      |      |      |      |      |      |      |      |      |      |      |      |
| Default Value | 0    | 0         | 0                               | 0        | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    |

High Byte:

- default: 0000 0000 (binary) 0 (decimal)
- Minimum: 1111 1111 (binary) (sign extended)
- Maximum: 0000 0000 (binary) (sign extended)

Low Byte:

- default: 0000 0000 (binary) 0 (decimal)
- Minimum: 1100 0000 (binary) –64 (decimal) (–125 mV) (sign extended, two's compliment)
- Maximum: 0011 1111 (binary) 63 (decimal) (123 mV)

#### 7.6.50 STEP_VREF_MARGIN_HIGH (MFR_SPECIFIC_05) (D5h)

The STEP_VREF_MARGIN_HIGH command, specifying a positive offset voltage on EA_VREF, is used to increase the reference voltage by shifting the reference higher. When the OPERATION command is set to Margin High, the output will increase by the voltage indicated by this command.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The effect of this command is determined by the settings of the VOUT_MODE command. In this device, the VOUT_MODE is fixed to Linear with an exponent of –9 (decimal). The actual reference voltage commanded by a margin high command can be found in Equation 14.

The margin high range is between 0 and 31 × 1.953 mV in 1.953-mV steps.

If a value outside this range is given with this command, the device sets the reference voltage to the upper or lower limit depending on the direction of the setting, asserts SMBALERT and sets the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML.

The value of EA_REF including STEP_VREF_MARGIN_HIGH is also limited by the values of VOUT_MAX, VOUT_MIN, VOUT_COMMAND, VOUT_SCALE_LOOP and VREF_TRIM. See VOUT_MAX and VOUT_MIN for additional details.

The EA_REF voltage transition occurs at the rate determined by the current state:

- Soft-Start: TON_RISE command
- Steady-State: VOUT_TRANSITION_RATE command
- TOFF_DELAY: VOUT_TRANSITION_RATE command
- Soft-Stop: TOFF_FALL command

| COMMAND      |      | STEP\_VREF\_MARGIN\_HIGH        |           |      |      |      |      |      |      |          |      |      |      |      |      |      |
| ------------ | ---- | ------------------------------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format       |      | Linear, two's complement binary |           |      |      |      |      |      |      |          |      |      |      |      |      |      |
| Bit Position | 7    | 6                               | 5         | 4    | 3    | 2    | 1    | 0    | 7    | 6        | 5    | 4    | 3    | 2    | 1    | 0    |
| Access       | r    | r                               | r         | r    | r    | r    | r    | r    | r    | r        | r    | r/w  | r/w  | r/w  | r/w  | r/w  |
| Function     |      |                                 | High Byte |      |      |      |      |      |      | Low Byte |      |      |      |      |      |      |

High Byte:

- default: 0000 0000 (binary) 0 (decimal)

Low Byte:

- Minimum: 0000 0000 (binary) 0 (decimal) (0 mV)
- Maximum: 0001 1111 (binary) 31 (decimal) (60.5 mV)

The read-writeable bits in this register do NOT have direct EEPROM backup; however, the register does restore to one of two configurable values as determined by RSMHI_VAL in (E5h) MFR_SPECIFIC_21 (OPTIONS).

- RSMHI_VAL = 0: STEP_VREF_MARGIN_HIGH will restore to 0009h (9 decimal or 17.6 mV).
- RSMHI_VAL = 1: STEP_VREF_MARGIN_HIGH will restore to 000fh (15 decimal or 29.3 mV).

#### 7.6.51 STEP_VREF_MARGIN_LOW (MFR_SPECIFIC_06) (D6h)

The STEP_VREF_MARGIN_LOW command, specifying a negative offset voltage on EA_VREF, is used to decrease the reference voltage by shifting the reference lower. When the OPERATION command is set to Margin Low, the output will decrease by the voltage indicated by this command.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The effect of this command is determined by the settings of the VOUT_MODE command. In this device, the VOUT_MODE is fixed to Linear with an exponent of –9 (decimal). The actual reference voltage commanded by a margin low command can be found in Equation 14.

The margin low range is between -64*1.953 mV and -1*1.953 mV in 1.953-mV steps.

If a value outside this range is given with this command, the device sets the reference voltage to the upper or lower limit depending on the direction of the setting, asserts SMBALERT and sets the CML bit in STATUS_BYTE and the invalid data bit in STATUS_CML.

The value of EA_REF including STEP_VREF_MARGIN_LOW is also limited by the values of VOUT_MAX, VOUT_MIN, VOUT_COMMAND, VOUT_SCALE_LOOP and VREF_TRIM. See VOUT_MAX and VOUT_MIN for additional details.

The EA_REF voltage transition occurs at the rate determined by the current state:

- Soft-Start: TON_RISE command
- Steady-State: VOUT_TRANSITION_RATE command
- TOFF_DELAY: VOUT_TRANSITION_RATE command
- Soft-Stop: TOFF_FALL command

| COMMAND      |      | STEP_VREF_MARGIN_LOW            |           |      |      |      |      |      |      |          |      |      |      |      |      |      |
| ------------ | ---- | ------------------------------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Format       |      | Linear, two's complement binary |           |      |      |      |      |      |      |          |      |      |      |      |      |      |
| Bit Position | 7    | 6                               | 5         | 4    | 3    | 2    | 1    | 0    | 7    | 6        | 5    | 4    | 3    | 2    | 1    | 0    |
| Access       | r/w  | r                               | r         | r    | r    | r    | r    | r    | r    | r        | r/w  | r/w  | r/w  | r/w  | r/w  | r/w  |
| Function     |      |                                 | High Byte |      |      |      |      |      |      | Low Byte |      |      |      |      |      |      |

High Byte:

default: 1111 1111 (binary) (MSB is sign bit, sign extended)

Low Byte:

Minimum: 1100 0000 (binary) –64 (decimal) (–125 mV)

Maximum: 1111 1111 (binary) –1 (decimal) (–2 mV)

The read-writeable bits in this register do NOT have direct EEPROM backup; however, the register does restore to one of two configurable values as determined by RSMLO_VAL in (E5h) MFR_SPECIFIC_21 (OPTIONS).

- RSMLO_VAL = 0: STEP_VREF_MARGIN_LOW will restore to fff7h (–9 decimal or –17.6 mV)
- RSMLO_VAL = 1: STEP_VREF_MARGIN_LOW will restore to fff1h (–15 decimal or –29.3 mV)

#### 7.6.52 PCT_OV_UV_WRN_FLT_LIMITS (MFR_SPECIFIC_07) (D7h)

The PCT_OV_UV_WRN_FLT_LIMITS command is used to set the PGOOD, VOUT_UNDER_VOLTAGE (UV) and VOUT_OVER_VOLTAGE (OV) limits as a percentage of nominal.

For loop slave device, this command cannot be accessed. Any writes to this command will be ignored. An attempt to read or write this command will result in a NACK’d command, the reporting of an IVC fault, and triggering of SMB_ALERT.

The PCT_OV_UV_WRN_FLT_LIMITS takes a one byte data formatted as shown below:

| COMMAND       |      | **PCT_OV_UV_WRN_FLT_LIMITS** |      |      |      |      |         |         |
| ------------- | ---- | ---------------------------- | ---- | ---- | ---- | ---- | ------- | ------- |
| Format        |      | Unsigned binary              |      |      |      |      |         |         |
| Bit Position  | 7    | 6                            | 5    | 4    | 3    | 2    | 1       | 0       |
| Access        | r    | r                            | r    | r    | r    | r    | r/wE    | r/wE    |
| Function      | X    | X                            | X    | X    | X    | X    | PCT_MSB | PCT_LSB |
| Default Value | 0    | 0                            | 0    | 0    | 0    | 0    | 0       | 0       |

The PGOOD, VOUT_UNDER_VOLTAGE (UV) and VOUT_OVER_VOLTAGE (OV) settings are shown in Table 13, as a percentage of nominal reference voltage on the FB pin.

##### Table 13. OV/UV Protection Settings (Typical Values)

| PCT\_MSB | PCT\_LSB | UV FAULT | UV WARN | OV WARN | OV FAULT | UNIT    |
| -------- | -------- | -------- | ------- | ------- | -------- | ------- |
| 0        | 0        | –83%     | –88%    | 112%    | 117%     | EA\_REF |
| 0        | 1        | –88%     | –90%    | 110%    | 112%     | EA\_REF |
| 1        | 0        | –72%     | –78%    | 112%    | 117%     | EA\_REF |
| 1        | 1        | –58%     | –64%    | 112%    | 117%     | EA\_REF |

The PGOOD pin may trip if the output voltage is too high (using OV WARN) or too low (using UV WARN). Additionally, the PGOOD pin has hysteresis. When the OV WARN output voltage OV WARN is tripped, the FB voltage must lower below the 105% of EA_REF, before PGOOD is reset. Likewise, when output voltage UV WARN is tripped, the FB voltage must rise above 95% of EA_REF, before PGOOD is reset.

#### 7.6.53 OPTIONS (MFR_SPECIFIC_21) (E5h)

The OPTIONS register can be used for setting user selectable options, as shown below. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

| COMMAND           |      | OPTIONS         |                |      |                        |      |                           |      |                  |                         |      |      |      |                  |                 |                  |
| ----------------- | ---- | --------------- | -------------- | ---- | ---------------------- | ---- | ------------------------- | ---- | ---------------- | ----------------------- | ---- | ---- | ---- | ---------------- | --------------- | ---------------- |
| Format            |      | Unsigned binary |                |      |                        |      |                           |      |                  |                         |      |      |      |                  |                 |                  |
| Bit Position      | 7    | 6               | 5              | 4    | 3                      | 2    | 1                         | 0    | 7                | 6                       | 5    | 4    | 3    | 2                | 1               | 0                |
| Access            | r    | r/wE            | r/wE           | r/wE | r/wE                   | r/wE | r/w                       | r/wE | r/wE             | r/wE                    | r/wE | r/w  | r/w  | r/wE             | r/wE            | r/wE             |
| Function          | X    | RSMHI_VAL       | RSMLO_<br/>VAL | x    | RST_VOUT<br/>_<br/>oSD | x    | READ_VOUT_<br/>RANGE[1:0] |      | EN_AUTO_<br/>ARA | AVG_<br/>PROG[1:<br/>0] |      | DLO  | VSM  | EN_ADC_<br/>CNTL | EN_RESET_<br/>B | DIS_<br/>NEGILIM |
| Default<br/>Value | 0    | 0               | 0              | 1    | 0                      | 0    | 0                         | 1    | 1                | 0                       | 0    | 0    | 0    | 1                | 0               | 0                |

##### 7.6.53.1 DIS_NEGILIM Bit

When set, this bit disables the negative current limit protection on the LFET.

##### 7.6.53.2 EN_RESET_B Bit

When set, this bit enables the RESET_B functionality of the RESET/PGD pin.

| BIT VALUE | ACTION                   |
| --------- | ------------------------ |
| 0         | RESET/PGD pin = PGOOD    |
| 1         | RESET/PGD pin = RESET\_B |

##### 7.6.53.3 EN_ADC_CNTL Bit

This bit enables ADC operation used for voltage, current and temperature monitoring.

| BIT VALUE | ACTION                |
| --------- | --------------------- |
| 0         | Disable ADC operation |
| 1         | Enable ADC operation  |

NOTE

The EN_ADC_CNTL bit must be set to enable output voltage, current and temperature telemetry. When the EN_ADC_CNTL bit is zero, the READ_VOUT, READ_IOUT and READ_TEMPERATURE_2 registers do not update continuously, and retain the previous values from the last time EN_ADC_CNTL was set.

##### 7.6.53.4 VSM Bit

This bit configures the measurement system for fast, VOUT-only measurement mode. Setting this bit disables READ_IOUT, and READ_TEMPERATURE_1, and instead allows the device to update READ_VOUT more frequently. This bit does not have EEPROM backup.

| BIT VALUE | ACTION                              |
| --------- | ----------------------------------- |
| 0         | Measure VOUT, temperature, and IOUT |
| 1         | Measure only VOUT                   |

NOTE

For READ_VOUT, multiple samples (defined by AVG_PROG[1:0] Bits) are obtained and averaged. When entering and exiting VSM mode, the first calculated result could lose one sample, for example, 7 sampled value but averaged by 8, resulting the first updated READ_VOUT data point have worst case error about 1/8 of the nominal value.

##### 7.6.53.5 DLO Bit

This bit allows bypassing the normal valid data checks on register writes. This feature is included for flexibility during debug to quickly generate fault conditions and/or possibly work around any data limit protection mechanisms prohibiting output voltage programming. This bit does not have EEPROM backup.

| BIT VALUE | ACTION                                                                                                                                                                                                                                                                                                                         |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0         | Normal PMBus data write restrictions                                                                                                                                                                                                                                                                                           |
| 1         | Data write restrictions are overridden for the following registers: SMBALERT\_MASK, VOUT\_COMMAND, VOUT\_SCALE\_LOOP, VREF\_TRIM, STEP\_VREF\_MARGIN\_HIGH, STEP\_VREF\_MARGIN\_LOW, IOUT\_OC\_FAULT\_LIMIT, IOUT\_OC\_WARN\_LIMIT, OT\_FAULT\_LIMIT, OT\_WARN\_LIMIT, VOUT\_MIN, VOUT\_MAX, VIN\_ON, VIN\_OFF, and OPERATION. |

NOTE

CAUTION: Users should use this bit with extreme caution. Setting this bit allows invalid data conditions to be programmed into the device which can lead to damage. Invalid data written into any register when DLO is enabled does NOT set the IVD bit; nor trigger SMBALERT. The invalid data is simply allowed to be programmed. Furthermore, invalid data programmed into a command/status register while DLO is enabled, does not trigger SMBALERT upon deassertion of DLO. So, it is possible to exit DLO mode with invalid data in command/status registers. Use with extreme caution.

##### 7.6.53.6 AVG_PROG[1:0] Bits

These bits configure programmable digital measurement averaging. Bits provide programmable averaging for current (READ_IOUT), temperature (READ_TEMPERATURE_1), and voltage (READ_VOUT). The default (00b) yields 16x averaging for all three parameters; however, this default can be changed and stored in EEPROM, if necessary. The programming options are as follows:

| BIT VALUE | ACTION                                                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 00        | Accumulating Averaging = 16x                                                                                                                     |
| 01        | Accumulating Averaging = 0x. Use this setting to bypass the averagers. Every sample from measurement system updates corresponding READ\_XXX CSR. |
| 10        | Accumulating Averaging = 8x                                                                                                                      |
| 11        | Accumulating Averaging = 32x                                                                                                                     |

##### 7.6.53.7 EN_AUTO_ARA Bit

This bit enables auto-alert response address response. When this feature is enabled, and after the device has successfully responded to an ARA transaction, the hardware automatically masks any fault source currently set from reasserting SMBALERT. This prevents PMBus bus hogging in the case of a persistent fault in a device that consistently wins ARA arbitration because of the device address. In contrast, when this bit is cleared, immediate reassertion of SMBALERT is allowed in the event of a persistent fault and the responsibility is upon the host to mask each source individually.

##### 7.6.53.8 READ_VOUT_RANGE[1:0] Bits

The ADC input voltage range is limited to 0.9 V. For READ_VOUT, the output voltage is divided down before input to ADC. Large signal amplitude gives better signal-to-noise ratio. The READ_VOUT_RANGE[1:0] bits are used to force the input voltage divider of the internal ADC for output voltage measurement to one of the 3 possible values.

| VOUT\_SCALE\_LOOP | READ\_VOUT\_RANGE\[1:0] | OUT    |
| ----------------- | ----------------------- | ------ |
| 1                 | 00b                     | 1/2 IN |
| x                 | 11b                     |        |
| 0.5               | 00b                     | 1/4 IN |
| x                 | 10b                     |        |
| 0.25              | 00b                     | 1/8 IN |
| x                 | 01b                     |        |

##### 7.6.53.9 RST_VOUT_oSD Bit

When set high, this bit is used to force VOUT_COMMAND to the default value upon any shutdown or fault condition:

- FAULT with programmed shutdown response
- FAULT with programmed restart response
- Normal, controlled shutdown (e.g. CNTL pin)
- LOW_VIN

##### 7.6.53.10 RSMLO_VAL Bit

The restore step-margin low-value (RSMLO_VAL) bit is used to configure the default restore value for (D6h) MFR_SPECIFIC_06 (STEP_VREF_MARGIN_LOW).

| BIT VALUE | ACTION                                                                  |
| --------- | ----------------------------------------------------------------------- |
| 0         | STEP\_VREF\_MARGIN\_LOW will restore to fff7h (–9 decimal or –17.6 mV)  |
| 1         | STEP\_VREF\_MARGIN\_LOW will restore to fff1h (–15 decimal or –29.3 mV) |

##### 7.6.53.11 RSMHI_VAL Bit

This restore step margin high value (RSMHI_VAL) bit is used to configure the default restore value for (D5h) MFR_SPECIFIC_05 (STEP_VREF_MARGIN_HIGH).

| BIT VALUE | ACTION                                                                 |
| --------- | ---------------------------------------------------------------------- |
| 0         | STEP\_VREF\_MARGIN\_HIGH will restore to 0009h (9 decimal or 17.6 mV)  |
| 1         | STEP\_VREF\_MARGIN\_HIGH will restore to 000fh (15 decimal or 29.3 mV) |

#### 7.6.54 MISC_CONFIG_OPTIONS (MFR_SPECIFIC_32) (F0h)

This user-accessible register is used for miscellaneous options, as shown below. The contents of this register can be stored to nonvolatile memory using the STORE_DEFAULT_ALL command.

| COMMAND       |      | MISC_CONFIG_OPTION |      |      |      |      |      |                |                    |                |      |             |      |                     |      |             |
| ------------- | ---- | ------------------ | ---- | ---- | ---- | ---- | ---- | -------------- | ------------------ | -------------- | ---- | ----------- | ---- | ------------------- | ---- | ----------- |
| Format        |      | Unsigned binary    |      |      |      |      |      |                |                    |                |      |             |      |                     |      |             |
| Bit Position  | 7    | 6                  | 5    | 4    | 3    | 2    | 1    | 0              | 7                  | 6              | 5    | 4           | 3    | 2                   | 1    | 0           |
| Access        | r    | r                  | r    | r    | r    | r    | r    | r/wE           | r/wE               | r/wE           | r    | r/wE        | r    | r/wE                | r/wE | r/wE        |
| Function      | X    | X                  | X    | X    | X    | x    | X    | SYNC_FAULT_DIS | FORCE_SYNC_<br/>IN | FORCE_SYNC_OUT | X    | EN_AVS_USER | X    | HSOC_USER_TRIM[1:0] |      | OV_RESP_SEL |
| Default Value | 0    | 0                  | 0    | 0    | 0    | 0    | 0    | 0              | 0                  | 0              | 0    | 1           | 0    | 0                   | 1    | 1           |

##### 7.6.54.1 OV_RESP_SEL Bit

This bit selects between two options for low-side FET behavior after an output overvoltage fault condition. Regardless of the setting of this bit, the low-side FET latches on when an output OV fault is detected (if the OV_FAULT_RESPONSE is not programmed to ignore).

| BIT VALUE | ACTION                                                                                                                                                                                   |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0         | The low-side FET remains on until either the part initiates a new startup of the output voltage or the CLEAR\_FAULTS command is given while the part is in the DISABLE operational state |
| 1         | The low-side FET turns off as soon as the sensed output (at FB pin) drops below 0.2 V.                                                                                                   |

##### 7.6.54.2 HSOC_USER_TRIM[1:0] Bits

These trim bits are provided so the user can adjust the HSOC threshold to account for the application-specific requirements for input-voltage sensing parasitics and component-current handling. The bit settings are defined as follows:

| BIT VALUE | ACTION                            |
| --------- | --------------------------------- |
| 00        | HSOC change from default = 0      |
| 01        | HSOC change from default = 12.5%  |
| 10        | HSOC change from default = –25%   |
| 11        | HSOC change from default = –12.5% |

##### 7.6.54.3 EN_AVS_USER Bit

Setting this bit high is required enabling the COMP-level shifter that eliminates overshoot and undershoot of VOUT when the reference is ramped. The value of this bit is latched when the driver is enabled to switch which prevents the user from enabling or disabling the level shifter while the output is switching.

##### 7.6.54.4 FORCE_SYNC_OUT Bit

This bit forces the device to output the free-running clock on the SYNC pin.

##### 7.6.54.5 FORCE_SYNC_IN Bit

This bit forces the device to be synchronized to an external PWM clock applied on the SYNC pin.

##### 7.6.54.6 SYNC_FAULT_DIS Bit

When set, this bit disables any reporting (digital status) and response (analog and digital) upon SYNC_FAULT.

## 8 Applications and Implementation

NOTE

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

### 8.1 Application Information

The TPS546C23 devices are highly-integrated, synchronous step-down DC-DC converters. These devices are used to convert a higher DC-input voltage to a lower DC-output voltage, with a maximum output current of 35 A. Use the following design procedure to select key component values for this device, and set the appropriate behavioral options through the PMBus.

### 8.2 Typical Application

#### 8.2.1 4.5-V to 18-V Input, 1-V Typical Output, 35-A Converter

##### Figure 39. Typical Application Schematic, TPS546C23

| TP1                | TP2       | 1                  | J1             |
| ------------------ | --------- | ------------------ | -------------- |
| AVIN               | R1        | PVIN               | PVIN           |
| 2                  | ED120/2DS |                    |                |
| C3                 | 0         | C1                 | C2             |
| VIN = 4.5 - 18 VDC | 1μF       | C4                 | C5             |
| C6                 | C7        | C8                 | C9             |
| C10                | 100μF     | 100μF              |                |
| 6800pF             | 6800pF    | 6800pF             | 22μF           |
| 22μF               | 22μF      | 22μF               | 1              |
| J2                 | GND       | 2                  |                |
| TP3                | GND       | ED120/2DS          |                |
| U1                 | TPS546C23 | SW                 |                |
| 21                 | PVIN      | TP4                |                |
| 22                 | PVIN      | C11                | R2             |
| 23                 | PVIN      | BOOT               | 7              |
| 24                 | PVIN      | 0.1μF              | 0              |
| C12                | R3        | CHACHB             | 25             |
| PVIN               | SW        | 8                  | SLC1480-301MLB |
| 1200pF             | 1.10k     | TP5                | TP6            |
| 29                 | AVIN      | SW                 | 9              |
| 300 nH             | VOUT      | Vout=0.35-5.5V/35A | SW             |
| 10                 | R4        | R5                 | 35             |
| SW                 | 11        | L1                 | J3             |
| VOUT               | DIFFO     | SW                 | 12             |
| 1                  | 10.0k     | 49.9               | 36             |
| FB                 | C13       | TP7                | 2              |
| ED120/2DS          | R6        | C14                | 37             |
| COMP               | 1000pF    | C17                | C18            |
| C19                | C20       | C15                | C16            |
| 5.60k              | 2200p     | 39                 | SYNC           |
| R7                 | 47μF      | 47μF               | 47μF           |
| 47μF               | 470μF     | 470μF              | ED120/2DS      |
| C21                | CNTL      | 40                 | CNTL           |
| 1.0                | 1         | J4                 | GND            |
| 270p               | 27        | BP3                | RSP            |
| 33                 | GND       | R8                 | 2              |
| Rbias              | R9        | 28                 | BP6            |
| RSN                | 34        | C22                | 49.9           |
| Optional           | 10.0k     | 30                 | RESET/PGD      |
| 330pF              | R10       | 3                  | ADDR0          |
| ISHARE             | 31        | 49.9               |                |
| C23                | C24       | 2                  | ADDR1          |
| VSHARE             | 32        | GND                |                |
| 0.1μF              | 4.7μF     | R11                | R12            |
| CLK                | 5         | PMB\_CLK           |                |
| C25                | 34.8k     | 78.7k              | DATA           |
| 4                  | PMB\_DATA |                    |                |
| 2.2μF              |           | 1                  | RT             |
| SMBALRT            | 6         | SMB\_ALRT          | PGND           |
| 13                 | GND       | R13                | PGND           |
| 14                 | 68.1k     | PGND               | 15             |
| PGND               | 16        | 26                 | PGND           |
| 17                 | DRGND     | PGND               | 18             |
| 38                 | PGND      | 19                 | AGND           |
| PGND               | 20        | PAD                | 41             |

### Typical Application (continued)

##### 8.2.1.1 Design Requirements

For this design example, use the input parameters listed in Table 14.

###### Table 14. Design Parameters

| DESIGN PARAMETER |                                      | TEST CONDITIONS                     | MIN  | TYP  | MAX  | UNIT |
| ---------------- | ------------------------------------ | ----------------------------------- | ---- | ---- | ---- | ---- |
| VIN              | Input voltage                        |                                     | 4.5  | 12   | 18   | V    |
| VIN(ripple)      | Input ripple voltage                 | IOUT = 35 A                         |      | 0.3  |      | V    |
| VOUT             | Output voltage                       |                                     |      | 1    |      | V    |
| ΔVO(ΔVI)         | Line regulation                      | 4.5 V ≤ VIN ≤ 18 V                  |      |      | 0.5% |      |
| ΔVO(ΔIO)         | Load regulation                      | 0 V ≤ IOUT ≤ 35 A                   |      |      | 0.5% |      |
| VPP              | Output ripple voltage                | IOUT = 35 A                         |      | 12   |      | mV   |
| ∆VOUT            | VOUT deviation during load transient | ∆IOUT = 10 A, Vin = 12 V            |      | 30   |      | mV   |
| IOUT             | Output current                       | 4.5 V ≤ VIN ≤ 18 V                  | 0    |      | 35   | A    |
| tSS              | Soft-start time                      |                                     |      | 5    |      | ms   |
| IOC              | Output overcurrent trip point        |                                     |      | 40   |      | A    |
| η                | Efficiency                           | VOUT = 1 V, IOUT = 17 A, VIN = 12 V |      | 90%  |      |      |
| fSW              | Switching frequency                  |                                     |      | 300  |      | kHz  |

##### 8.2.1.2 Detailed Design Procedure

###### 8.2.1.2.1 Switching Frequency Selection

There is a tradeoff between higher and lower switching frequencies for buck converters. Higher switching frequencies may produce smaller solution size using lower valued inductors and smaller output capacitors compared to a power supply that switches at a lower frequency. However, the higher switching frequency causes extra switching losses, which decrease efficiency and impact thermal performance. In this design, a moderate switching frequency of 300 kHz achieves both a small solution size and a high-efficiency operation. With the frequency selected, use Equation 15 to calculate the timing resistor (RT). The standard value of 68.1 kΩ is used in the design.

RT = 2.01u 1010 / (fSW) = 2.01u 1010 / 300 kHz (15)

###### 8.2.1.2.2 Inductor Selection

Use Equation 16 to calculate the value of the output inductor (L). The coefficient, KIND, represents the amount of inductor-ripple current relative to the maximum output current. The output capacitor filters the inductor-ripple current. Therefore, selecting a high inductor-ripple current impacts the selection of the output capacitor because the output capacitor must have a ripple-current rating equal to or greater than the inductor-ripple current. Generally, the KIND coefficient should be kept between 0.2 and 0.3 for balanced performance. Using this target ripple current, the required inductor size can be calculated as shown in Equation 16.

L = (VOUT * VIN) / (VIN(Max) * fSW(Min) * IOUT(Max) * KIND) = (1 V * (18 V - 1 V)) / (18 V * 300 kHz * 35 * 0.3) = 299 nH (16)

Selecting a value of 0.3 for the KIND coefficient, the target inductance, L, is 299 nH. Considering the variation and derating of the inductance and the 300-nH inductor, use Equation 17, Equation 18, and Equation 19 to calculate the inductor-ripple current (IRIPPLE), RMS current (IL(rms)), and peak current (IL(peak)), respectively. These values should be used to select an inductor with approximately the target inductance value, and current ratings that allow normal operation with some margin.

IRIPPLE = (VOUT * VIN(Max)) / (VIN(Max) * fSW(Min) * L1) = (1 V * (18 V - 1 V)) / (18 V * 300 kHz * 300 nH) = 10.5 A (17)

IL(rms) = sqrt((IOUT(Max)^2) + (1/12) * (IRIPPLE^2)) = sqrt((35 A)^2 + (1/12) * (10.5 A)^2) = 35.13 A (18)

IL(peak) = IOUT + 1IRIPPLE = 35 A + 1 u 10.5 A = 40.25 A

Considering the required inductance, RMS current, and peak current, the 300-nH inductor, SLC1480-301ML, from Coilcraft was selected for this application.

###### 8.2.1.2.3 Output Capacitor Selection

Consider the following when selecting the value of the output capacitor:

- The output-voltage deviation during load transient
- The output-voltage ripple

###### 8.2.1.2.4 Output Voltage Deviation During Load Transient

The desired response to a load transient is the first criterion for output capacitor selection. The output capacitor must supply the load with the required current when not immediately provided by the regulator. When the output capacitor supplies load current, the impedance of the capacitor affects the magnitude of the voltage deviation during the transient.

To meet the requirements for control-loop stability, the device requires the addition of compensation components in the design of the error amplifier. While these compensation components provide for a stable control loop, they often also reduce the speed with which the regulator can respond to load transients. The delay in the regulator response to load changes can be two or more clock cycles before the control loop reacts to the change. During that time, the difference (delta) between the old and the new load current must be supplied (or absorbed) by the output capacitance. The output capacitor impedance must be designed to supply or absorb the delta current while maintaining the output voltage within acceptable limits. Equation 20 and Equation 21 show the relationship between the transient response overshoot (VOVER), the transient response undershoot (VUNDER), and the required output capacitance (COUT).

VOVER &#x3C; (ITRAN)² u L

VOUT u COUT

(20)

VUNDER &#x3C; (V (ITRAN)² u L

IN VOUT) u COUT

(21)

If

- VIN(min) > 2 × VOUT, use overshoot to calculate minimum output capacitance.
- VIN(min) &#x3C; 2 × VOUT, use undershoot to calculate minimum output capacitance.

In this case, the minimum designed input voltage, VIN(min), is greater than 2 × VOUT, so VOVER dictates the minimum output capacitance. Therefore, using Equation 22, the minimum output capacitance required to meet the transient requirement is 1000 μF.

COUT(Min) = (ITRAN)² u L / (VOUT u VOVER)

= (10 A)² u 300 nH / (1V u 30 mV)

= 1000 μF

(22)

###### 8.2.1.2.5 Output Voltage Ripple

The output-voltage ripple is the second criterion for output capacitor selection. Use Equation 23 to calculate the minimum output capacitance required to meet the output-voltage ripple specification.

COUT(Min) = 8 u 1 u IRIPPLE / (fSW u VOUT(RIPPLE))

= 10.5 A / (8 u 300 kHz u 12 mV)

= 364 μF

(23)

In this case, the target maximum output-voltage ripple is 12 mV. Under this requirement, the minimum output capacitance for ripple is 330 μF. Because this capacitance value is smaller than the output capacitance required for the transient response, select the output capacitance value based on the transient requirement. Considering the variation and derating of capacitance, in this design, two 470-μF low-ESR polymer bulk capacitors and four 47-μF ceramic capacitors were selected to meet the transient specification with sufficient margin. Therefore COUT is equal to 1128 μF.

With the target output capacitance value selected, use Equation 24 to calculate the maximum ESR that the output-capacitor bank allows to meet the output-voltage ripple specification. Equation 24 indicates the ESR should be less than 1.3 mΩ. Each 470-μF ceramic capacitor contributes approximately 1.3 mΩ, making the effective ESR of the output capacitor bank approximately 0.65 mΩ which is within the specification with sufficient margin.

ESRₘₐₓ = [Vᴏᴜᴛ(ʀɪᴘᴘʟᴇ) - (Iʀɪᴘᴘʟᴇ/(8×ғsᴡ×Cᴏᴜᴛ))] / Iʀɪᴘᴘʟᴇ = [12mV - (10.5A/(8×300kHz×1128µF))] / 10.5A = 1.14mΩ

(24)

###### 8.2.1.2.6 Input Capacitor Selection

The power-stage input-decoupling capacitance (effective capacitance at the PVIN and PGND pins) must be sufficient to supply the high switching currents demanded when the high-side MOSFET switches on, while providing minimal input-voltage ripple as a result. This effective capacitance includes any DC-bias effects. The voltage rating of the input capacitor must be greater than the maximum input voltage with derating. The capacitor must also have a ripple-current rating greater than the maximum input-current ripple to the device during full load. Use Equation 25 to estimate the input RMS current.

$ I_{\text{IN}(\text{ms})} = I_{\text{OUT}(\text{Max})} \times \sqrt{ \frac{V_{\text{OUT}}}{V_{\text{IN}(\text{Min})}} \times \frac{ (V_{\text{IN}(\text{Min})} - V_{\text{OUT}}) }{V_{\text{IN}(\text{Min})}} } = 70\,\text{A} \times \sqrt{ \frac{1\,\text{V}}{4.5\,\text{V}} \times \frac{(4.5\,\text{V} - 1\,\text{V})}{4.5\,\text{V}} } = 14.6\,\text{A} $ (25)

The minimum input capacitance and ESR values for a given input voltage-ripple specification, VIN(ripple), are shown in Equation 26 and Equation 27. The input ripple is composed of a capacitive portion (VRIPPLE(cap)) and a resistive portion (VRIPPLE(esr)).

$$
\mathrm{C}_{\text{IN(Min) }} = \frac { \mathrm{I}_{\text{OUT(Max)} } \times \mathrm{V}_{\text{OUT} } } { \mathrm{V}_{\text{RIPPLE(cap)}} \times \mathrm{V}_{\text{IN(Max)}} \times \mathrm{f}_{\text{SW} } } = \frac { 35 \mathrm{~A} \times 1 \mathrm{~V} } { 0.1 \mathrm{~V} \times 18 \mathrm{~V} \times 300 \mathrm{kHz} } = 64.8 \mu \mathrm{F}
$$

$$
\mathrm{ESR}_{\text{CIN(Max) }} = \frac { \mathrm{V}_{\text{RIPPLE(ESR)}} } { \mathrm{I}_{\text{OUT(Max)}} + \frac{1}{2} \times \mathrm{I}_{\text{RIPPLE} } } = \frac { 0.2 \mathrm{~V} } { 35 \mathrm{~A} + {\frac{1}{2} \times (10.5 \mathrm{~A}) } } = 5 \mathrm{~m} \Omega
$$

The value of a ceramic capacitor varies significantly over temperature and the amount of DC bias applied to the
capacitor. The capacitance variations because of temperature can be minimized by selecting a dielectric material
that is stable over temperature. X5R and X7R ceramic dielectrics are usually selected for power-regulator
capacitors because these components have a high capacitance-to-volume ratio and are fairly stable over
temperature. The input capacitor must also be selected with consideration of the DC bias. For this example
design, a ceramic capacitor with at least a 25-V voltage rating is required to support the maximum input voltage.
For this design, allow 0.1-V input ripple for VRIPPLE(cap) and 0.2-V input ripple for VRIPPLE(esr). Using Equation 26
and Equation 27, the minimum input capacitance for this design is 64.8 µF, and the maximum ESR is 5 mΩ. For
this design example, four 22-μF, 25-V ceramic capacitors, three 6800-pF, 25-V ceramic capacitors, and two
additional 100-μF, 25-V low-ESR electrolytic capacitors in parallel were selected for the power stage with
sufficient margin. A high-frequency PVIN-bypass capacitor is suggested to be placed close to power stage to help with ringing reduction.

###### 8.2.1.2.7 AVIN, BP6, BP3 Bypass Capacitor

The BP3 pin requires a minimum capacitance of 2.2 μF connected to AGND. The BP6 pin should have approximately 4.7 μF of capacitance connected to PGND. The PVIN pin should have approximately 1 μF of capacitance connected to PGND. To filter ripple on the AVIN pin, a small value resistor is recommended to be placed between PVIN pin and AVIN.

###### 8.2.1.2.8 Bootstrap Capacitor Selection

A ceramic capacitor with a value of 0.1 μF must be connected between the BOOT and SW pins for proper operation. TI recommends using a ceramic capacitor with X5R or better grade dielectric. The capacitor should have voltage rating of 25 V or higher.

###### 8.2.1.2.9 R-C Snubber

An R-C snubber must be placed between the switching node and PGND to reduce voltage spikes on the switching node. The power rating of the resistor must be larger than the power dissipation on the resistor with sufficient margin. To balance efficiency and spike level, a 1-nF capacitor and a 1-Ω resistors were selected for this design. In this example an 0805 resistor was selected, which is rated for 0.125 W.

###### 8.2.1.2.10 Output Voltage Setting and Frequency Compensation Selection

The device uses voltage-mode control with input feedforward. For an in-depth discussion of voltage-mode feedback and control, refer to *Under the Hood of Low-Voltage DC/DC Converters* (SLUP206). Frequency compensation can be accomplished using standard techniques. TI also provides a compensation calculator tool as part of the WEBENCH® selection simulation services to streamline compensation design. The tool provides the recommended compensation components and approximate bode plots. As a starting point, set the crossover frequency to 1/10 fSW and 2 to 5 times the resonant frequency of the output LC filter. The phase margin at crossover should be greater than 45°. The resulting plots should be reviewed for a few common considerations. The error-amplifier gain should not hit the error amplifier gain bandwidth product (GBWP). The error-amplifier gain at the switching frequency region is recommended to be approximately 6 dB in general. The high-frequency capacitor from the COMP to FB pins for this device must be above a typical value of 100 pF to 150 pF to lower the high-frequency gain for stability. Use the tool to calculate the system bode plot at different loading conditions to ensure that the phase does not drop below zero prior to crossover, as this condition is known as conditional stability. The design tool provides the compensation network values as a start point. Measuring the real-system bode plot after the design and adjusting the compensation values accordingly is always recommended.

###### Table 15. Frequency Compensation Values

| RESISTOR | VALUE (kΩ) | CAPACITOR | VALUE (pF) |
| -------- | ---------- | --------- | ---------- |
| R4       | 10         | C12       | 1200       |
| R3       | 1.1        | C14       | 2200       |
| R6       | 5.6        | C21       | 270        |
| RBias    | Open       | —         | —          |

###### 8.2.1.2.11 Key PMBus Parameter Selection

Some key design parameters for the device can be configured through PMBus, and stored to the non-volatile memory (NVM) for future use.

###### 8.2.1.2.12 Enable, UVLO

The ON_OFF_CONFIG command is used to select the turn-on behavior of the converter. For this example, the CNTL pin was used to enable or disable the converter, regardless of the state of OPERATION, as long as the input voltage is present and above the UVLO threshold. The CNTL pin is pulled to the BP6 pin through an internal 6-μA current source if it is floating.

###### 8.2.1.2.13 Soft-Start Time

The TON_RISE command sets the soft-start time. The charging current for the output capacitors must be considered when selecting the soft-start time. In some applications (for example, those with large amounts of output capacitance) this current can lead to false tripping of the overcurrent-protection circuitry if the soft-start time is not properly selected. To avoid false tripping, the output capacitor-charging current should be included when selecting a soft-start time and overcurrent threshold. Use Equation 28 to calculate the capacitor-charging current (ICAP).

ICAP = VOUT*COUT  / tSS = 1 V *1000 μF/5ms = 0.23 A

In this example, the soft-start time is selected to be the default value of 5 ms. In this case, the charging current, ICAP, is 0.23 A.

###### 8.2.1.2.14 Overcurrent Threshold and Response

The IOUT_OC_FAULT_LIMIT command sets the overcurrent threshold. The device uses inductor middle current
value for overcurrent detecting. The current limit should be set to the maximum load current, plus the output
capacitor charging current during start-up, plus some margin for load transients and component variation. The
amount of margin required depends on the individual application, but a suggested point is between 20% and
40%. For this application, the maximum load current is 35 A, the output capacitor charging current is 0.44 A. This
design allows some extra margin, so an overcurrent threshold of 40 A was selected.

The IOUT_OC_FAULT_RESPONE command sets the desired response to an overcurrent event. In this
example, the converter is configured to hiccup in the event of an overcurrent. The device can also be configured
to latch in the event of an overcurrent.

##### 8.2.1.3  Application Curves

|  Efficiency  |            | Efficiency   |            |
| :----------: | :--------: | ------------ | ---------- |
| VOUT = 0.8 V | VOUT = 1 V | VOUT = 1.2 V | VOUT = 5 V |
|      100     |     100    | 100          | 100        |
|      95      |     95     | 95           | 95         |
|      90      |     90     | 90           | 90         |
|      85      |     85     | 85           | 85         |
|      80      |     80     | 80           | 80         |
|      75      |     75     | 75           | 75         |
|      70      |     70     | 70           | 70         |
|      65      |     65     | 65           | 65         |
|      60      |     60     | 60           | 60         |

0   4   8   12  16  20  24  28  32  36

Load Current (A)  D001

VIN = 5 V  L = 300 nH  Snubber = 1 nF + 1 Ω

fSW = 300 kHz  RDCR = 0.2 mΩ  RBOOT = 0 Ω

###### Figure 40. Efficiency vs Output Current

###### Figure 41. Efficiency vs Output Current

|  Efficiency  |            | Efficiency   |            |
| :----------: | :--------: | ------------ | ---------- |
| VOUT = 0.8 V | VOUT = 1 V | VOUT = 1.2 V | VOUT = 5 V |
|      100     |     100    | 100          | 100        |
|      95      |     95     | 95           | 95         |
|      90      |     90     | 90           | 90         |
|      85      |     85     | 85           | 85         |
|      80      |     80     | 80           | 80         |
|      75      |     75     | 75           | 75         |
|      70      |     70     | 70           | 70         |
|      65      |     65     | 65           | 65         |
|      60      |     60     | 60           | 60         |

0   4  8  12  16  20  24  28  32  36

Load Current (A)  D001

VIN = 12 V  L = 300 nH  Snubber = 1 nF + 1 Ω

fSW = 300 kHz  RDCR = 0.2 mΩ  RBOOT = 0 Ω

###### Figure 42. Efficiency vs Output Current

###### Figure 43. Efficiency vs Output Current

0.9125

0.91

0.9075

0.905

Voltage

0.9025

Output

0.9

0.8975

0.895

0.8925

0  5  10  15  20  25  30  35

Output Current (A)  D001

VIN = 12 V  VOUT = 0.9 V

###### Figure 44. Load Regulation

###### Figure 45. Total-Loop Bode Plot

| (dB) | (°)  |
| ---- | ---- |
| 75   | 200  |
| 60   | 160  |
| 45   | 120  |
| 30   | 80   |
| 15   | 40   |
| -15  | -40  |
| -30  | -80  |
| -45  | -120 |
| -60  | -160 |
| -75  | -200 |

Frequency (Hz)

VIN = 12 V  VOUT = 0.9 V  IOUT = 20 A

###### Figure 46. Start-Up from CNTL

Time (500 μs/div)

VIN = 12 V  VOUT = 0.9 V  IOUT = 20 A

###### Figure 47. Shutdown from CNTL

Time (500 μs/div)

VIN = 12 V  VOUT = 0.9 V  IOUT = 20 A

###### Figure 48. Load Transient Response

###### Figure 49. VOUT Steady-State Ripple

###### Figure 50. Prebiased Start-Up

###### Figure 51. Hiccup Response

| VIN  | VOUT  | IOUT                  | Time       |
| ---- | ----- | --------------------- | ---------- |
| 12 V | 0.9 V | 0 A to 10 A, 2.5 A/μs | 100 μs/div |
| 12 V | 0.9 V | 20 A                  | 1 μs/div   |

| VIN  | VOUT  | ILOAD                    | PGOOD   | EN       |
| ---- | ----- | ------------------------ | ------- | -------- |
| 12 V | 0.9 V | 0 A                      | 5 V/div | 50 V/div |
| 12 V | 0.9 V | 0 A to 20 A, 20 A to 0 A | 1 V/div | 2 V/div  |

## 9 Power Supply Recommendations

The devices are designed to operate from an input voltage supply between 4.5 V and 18 V. This supply must be well regulated. These devices are not designed for split-rail operation. The PVIN and AVIN pins must be the same potential for accurate high-side short circuit protection. Proper bypassing of input supplies and internal regulators is also critical for noise performance, as is PCB layout and grounding scheme. See the recommendations in the Layout section.

## 10 Layout

### 10.1 Layout Guidelines

Layout is critical for good power-supply design. Figure 52 shows the recommended PCB-layout configuration. A list of PCB layout considerations using these devices is listed as follows:

- As with any switching regulator, several power or signal paths exist that conduct fast switching voltages or currents. Minimize the loop area formed by these paths and their bypass connections.
- Bypass the PVIN pins to PGND with a low-impedance path. The input bypass capacitors of the power-stage should be placed as close as physically possible to the PVIN and PGND pins. Additionally, a high-frequency bypass capacitor in a 0402 package on the PVIN pins can help reduce switching spikes. This capacitor which can be placed on the other side of the PCB directly underneath the device to keep a minimum loop.
- The BP6 bypass capacitor carries a large switching current for the gate driver. Bypassing the BP6 pin to PGND with a low-impedance path is very critical to the stable operation of the devices. Place the BP6 high-frequency bypass capacitors as close as possible to the device pins, with a minimum return loop back to ground.
- The AVIN and BP3 pins also require good local bypassing. Place bypass capacitors as close as possible to the device pins, with a minimum return loop back to ground. This return loop should be kept away from fast switching voltages, the main current path, and the BP6 current path. Poor bypassing on the AVIN and BP3 pins can degrade the performance of the device.
- Keep signal components local to the device, and place them as close as possible to the pins to which they are connected. These components include the feedback resistors and the RT resistor. These components should also be kept away from fast switching voltage and current paths. Those components can be terminated to AGND with a minimum return loop or bypassed to the copper area of a separate low-impedance analog ground (AGND) that is isolated from fast switching voltages and current paths and has single connection to PGND on the thermal pad through the AGND pin. For placement recommendations, see Figure 52.
- The PGND pin (pin 26) must be directly connected to the thermal pad of the device on the PCB, with a low-noise, low-impedance path to ensure accurate current monitoring.
- Minimize the SW copper area for best noise performance. Route sensitive traces away from the SW and BOOT pins as these nets contain fast switching voltages and lend easily to capacitive coupling.
- Snubber component placement is critical for effective ringing reduction. These components should be on the same layer as the devices, and be kept as close as possible to the SW and PGND copper areas.
- The PVIN and AVIN pins must be the same potential for accurate short circuit protection, but high-frequency switching noise on the AVIN pin can degrade performance. The AVIN pin should be connected to PVIN through a trace from the input copper area. Optionally form a small low-pass R-C between the PVIN and AVIN pins, with the AVIN bypass capacitor (1 μF) and a 0-2 Ω resistor between the PVIN and AVIN pins. See Figure 52 for placement recommendations.
- Route the RSP and RSN lines from the output capacitor bank at the load back to the device pins as a tightly coupled differential pair. These traces must be kept away from switching or noisy areas which can add differential-mode noise.
- Use caution when routing of the SYNC, VSHARE and ISHARE traces for 2-phase configurations. The SYNC trace carries a rail-to-rail signal and should be routed away from sensitive analog signals, including the VSHARE, ISHARE, RT, and FB signals. The VSHARE and ISHARE traces should also be kept away from fast switching voltages or currents formed by the PVIN, AVIN, SW, BOOT, BP6 pins.

### 10.2 Layout Example

(Not to scale)

Bypass for internal regulators BP3, BP6, AVIN. Use multiple vias to reduce parasitic inductance.

Place PVIN bypass capacitors as close as possible to IC, with best high frequency capacitor closest to PVIN/PGND pins.

#### Figure 52. PCB Layout Recommendation

|                                                                        |                                                           | PVIN                                           | Internal AGND Plane to reduce the BP3 bypass parasitics.       |      |      |
| ---------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------- | ---- | ---- |
| Keep feedback and compensation network components localized to the IC. | VSHARE                                                    | DRGND                                          | PGND                                                           |      |      |
| ISHARE                                                                 | RESET/                                                    | AVIN                                           | PVIN                                                           |      |      |
|                                                                        |                                                           | PVIN                                           | PVIN                                                           | PVIN | PVIN |
| RCOMP1                                                                 | CCOMP2                                                    | RSP                                            | Connect DRGND to PGND                                          |      |      |
| RBOT                                                                   | RTOP                                                      | RSN                                            | Thermal Pad                                                    |      |      |
| PGND                                                                   | IC                                                        | RSP                                            | RSN                                                            |      |      |
| DIFFO                                                                  | PGND                                                      | RCOMP2                                         | CCOMP2                                                         |      |      |
| FB                                                                     | Thermal Pad                                               | PGND                                           | CCOMP3                                                         |      |      |
| COMP                                                                   | Connect AGND to PGND                                      | RSN                                            | Thermal Pad                                                    |      |      |
| AGND                                                                   | Thermal Pad                                               | PGND                                           | SYNC                                                           |      |      |
| PGND                                                                   | RSNS±                                                     | CNTL                                           | PGND                                                           |      |      |
| ADDR0                                                                  | PMB\_DATA                                                 | SMBALERT                                       | Place best high frequency output capacitor between sense point |      |      |
| AGND                                                                   | and DRGND are only connected together on Thermal Pad.     | ADDR1                                          | PMB\_CLK                                                       |      |      |
| BOOT                                                                   | RT                                                        | SW                                             | SW                                                             |      |      |
| SW                                                                     | SW                                                        | SW                                             | SW                                                             |      |      |
| Minimize SW area                                                       | L1                                                        | For best efficiency, use a heavy weight copper | and place these planes on multiple PCB layers                  |      |      |
| Signal Communication                                                   | Keep sensitive traces away from SW and BOOT on all layers |                                                |                                                                |      |      |

### 10.3 Mounting and Thermal Profile Recommendation

Proper mounting technique adequately covers the exposed thermal pad with solder. Excessive heat during the reflow process can affect electrical performance. Figure 53 shows the recommended reflow-oven thermal profile. Proper post-assembly cleaning is also critical to device performance. Refer to QFN/SON PCB Attachment (SLUA271) for more information.

#### Figure 53. Recommended Reflow-Oven Thermal Profile

tP

TP

C) T (° L Temperature

TS(max) tL

TS(min)

tS rRAMP(up) rRAMP(down)

25 t25P

Time (s)

### Mounting and Thermal Profile Recommendation (continued)

| PARAMETER                 |                                                           | MIN  | TYP  | MAX  | UNIT |
| ------------------------- | --------------------------------------------------------- | ---- | ---- | ---- | ---- |
| **RAMP UP AND RAMP DOWN** |                                                           |      |      |      |      |
| rRAMP(up)                 | Average ramp-up rate, $ T_{S(max)} $ to $ T_{P} $         |      |      | 3    | °C/s |
| rRAMP(down)               | Average ramp-down rate, $ T_{P} $ to $ T_{S(max)} $       |      |      | 6    | °C/s |
| **PRE-HEAT**              |                                                           |      |      |      |      |
| $ T_{S} $                 | Preheat temperature                                       | 150  |      | 200  | °C   |
| $ t_{S} $                 | Preheat time, $ T_{S(min)} $ to $ T_{S(max)} $            | 60   |      | 180  | s    |
| **REFLOW**                |                                                           |      |      |      |      |
| $ T_{L} $                 | Liquidus temperature                                      |      | 217  |      | °C   |
| $ T_{P} $                 | Peak temperature                                          |      |      | 260  | °C   |
| $ t_{L} $                 | Time maintained above liquidus temperature, $ T_{L} $     | 60   |      | 150  | s    |
| $ t_{P} $                 | Time maintained within 5°C of peak temperature, $ T_{P} $ | 20   |      | 40   | s    |
| $ t_{25P} $               | Total time from 25°C to peak temperature, $ T_{P} $       |      |      | 480  | s    |

## 11 Device and Documentation Support

### 11.1 Device Support

#### 11.1.1 Development Support

##### 11.1.1.1 Texas Instruments Fusion Digital Power Designer

The devices are fully supported by Texas Instruments Digital Power Designer. Fusion Digital Power Designer is a graphical user interface (GUI) which can be used to configure and monitor the devices via PMBus using a Texas Instruments USB-to-GPIO adapter. Click this link to download the Texas Instruments Fusion Digital Power Designer software package.

##### 11.1.1.2 WEBENCH® Tool

The devices are supported by the Texas Instruments WEBENCH® Tool. This online tool can be used to design schematic and calculate frequency compensation components.

### 11.2 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper right corner, click on Alert me to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

### 11.3 Community Resources

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

- TI E2E™ Online Community: TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers.
- Design Support: TI's Design Support Quickly find helpful E2E forums along with design support tools and contact information for technical support.

### 11.4 Trademarks

NexFET, E2E are trademarks of Texas Instruments.

WEBENCH is a registered trademark of Texas Instruments.

PMBus, SMBus are trademarks of System Management Interface Forum (SMIF), Inc..

All other trademarks are the property of their respective owners.

### 11.5 Electrostatic Discharge Caution

These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam during storage or handling to prevent electrostatic damage to the MOS gates.

### 11.6 Glossary

SLYZ022 — TI Glossary. This glossary lists and explains terms, acronyms, and definitions.

## 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical packaging and orderable information. This information is the most current data available for the designated devices. These data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

## PACKAGE MATERIALS INFORMATION

PACKAGING INFORMATION

| Orderable Device | Status | Package Type | Package Drawing | pins | Package Qty | Eco Plan              | Lead/Ball Finish | MSL Peak Temp       | Op Temp (°C) | Device Marking | Samples |
| ---------------- | ------ | ------------ | --------------- | ---- | ----------- | --------------------- | ---------------- | ------------------- | ------------ | -------------- | ------- |
| TPS546C23RVFR    | ACTIVE | LQFN-CLIP    | RVF             | 40   | 2500        | Pb-Free (RoHS Exempt) | CU NIPDAU        | Level-2-260C-1 YEAR | -40 to 125   | TPS546C23      | Samples |
| TPS546C23RVFT    | ACTIVE | LQFN-CLIP    | RVF             | 40   | 250         | Pb-Free (RoHS Exempt) | CU NIPDAU        | Level-2-260C-1 YEAR | -40 to 125   | TPS546C23      | Samples |

Notes

(1) The marketing status values are defined as follows:

- ACTIVE: Product device recommended for new designs.
- LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
- NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
- PREVIEW: Device has been announced but is not in production. Samples may or may not be available.
- OBSOLETE: TI has discontinued the production of the device.

(2) Eco Plan - The planned eco-friendly classification: Pb-Free (RoHS), Pb-Free (RoHS Exempt), or Green (RoHS &#x26; no Sb/Br) - please check http://www.ti.com/productcontent for the latest availability information and additional product content details.

TBD: The Pb-Free/Green conversion plan has not been defined.

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

Reel Width (W1)

QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

|                        | Q1 | Q2 |   | Q1 | Q2 |
| ---------------------- | -- | -- | - | -- | -- |
|                        | Q3 | Q4 |   | Q3 | Q4 |
| User Direction of Feed |    |    |   |    |    |

Pocket Quadrants

| Device        | Package Type | Package Drawing | Pins | SPQ  | Reel Diameter (mm) | Reel Width (W1) (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| ------------- | ------------ | --------------- | ---- | ---- | ------------------ | -------------------- | ------- | ------- | ------- | ------- | ------ | ------------- |
| TPS546C23RVFR | LQFN-CLIP    | RVF             | 40   | 2500 | 330.0              | 16.4                 | 5.35    | 7.35    | 1.7     | 8.0     | 16.0   | Q1            |
| TPS546C23RVFT | LQFN-CLIP    | RVF             | 40   | 250  | 180.0              | 16.4                 | 5.35    | 7.35    | 1.7     | 8.0     | 16.0   | Q1            |

## PACKAGE MATERIALS INFORMATION

TAPE AND REEL BOX DIMENSIONS

*All dimensions are nominal

| Device        | Package Type | Package Drawing | Pins | SPQ  | Length (mm) | Width (mm) | Height (mm) |
| ------------- | ------------ | --------------- | ---- | ---- | ----------- | ---------- | ----------- |
| TPS546C23RVFR | LQFN-CLIP    | RVF             | 40   | 2500 | 367.0       | 367.0      | 38.0        |
| TPS546C23RVFT | LQFN-CLIP    | RVF             | 40   | 250  | 210.0       | 185.0      | 35.0        |

## GENERIC PACKAGE VIEW

RVF 40

LQFN-CLIP 1.52 mm max height

PLASTIC QUAD FLATPACK NO LEAD

TEXAS INSTRUMENTS

Images above are just a representation of the package family, actual package may vary: Refer to the product data sheet for package details

4211383/D

## PACKAGE OUTLINE

RVF0040A    LQFN-CLIP - 1.52 mm max height

PLASTIC QUAD FLATPACK - NO LEAD

|         | B             | 5.1              | A         | 4.9         |
| ------- | ------------- | ---------------- | --------- | ----------- |
|         |               | PIN 1 INDEX AREA |           |             |
|         |               | 7.1              |           | 6.9         |
| 1.52    |               | C                | 1.32      |             |
|         | SEATING PLANE | 0.05             | 0.08 C    | 0.00        |
|         | 2X 3.5        |                  |           |             |
|         | 3.3           | 0.1              | (0.2) TYP |             |
| 36X 0.5 | 13            | 20               | EXPOSED   | THERMAL PAD |
|         | 12            | 21               |           |             |
| 2X SYMM | 41            | 5.3              | 0.1       | 5.5         |
| 1       |               | 32               | 40X 0.3   |             |
|         | PIN 1 ID      | 40               | 33        | 0.2         |
|         | (OPTIONAL)    | SYMM             | 0.1       | C A B       |
|         | 40X 0.5       | 0.05             | 0.3       |             |

4222989/B      10/2017

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
4. Reference JEDEC registration MO-220.

## EXAMPLE BOARD LAYOUT

RVF0040A LQFN-CLIP - 1.52 mm max height

PLASTIC QUAD FLATPACK - NO LEAD

|             |           |           |       |       |            |    |        |           |    |      |    |        |       |       |
| ----------- | --------- | --------- | ----- | ----- | ---------- | -- | ------ | --------- | -- | ---- | -- | ------ | ----- | ----- |
|             |           |           | (3.3) | (1.4) |            |    |        |           |    |      |    |        |       |       |
| 40          | 33        | 40X (0.6) | 1     | 32    | 40X (0.25) | 2X | (1.12) | 36X (0.5) | 6X | SYMM | 41 | (1.28) | (6.8) | (5.3) |
| (R0.05) TYP | (0.2) TYP | VIA       | 12    | 21    | 13         | 20 | SYMM   | (4.8)     |    |      |    |        |       |       |

LAND PATTERN EXAMPLE

SCALE: 12X

ALL 0.07 MAX AROUND

0.07 MIN ALL AROUND

METAL

SOLDER MASK OPENING

SOLDER MASK

OPENING

NON SOLDER MASK DEFINED

SOLDER MASK DEFINED (PREFERRED)

SOLDER MASK DETAILS

4222989/B 10/2017

NOTES: (continued)

5. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).

## EXAMPLE STENCIL DESIGN

RVF0040A LQFN-CLIP - 1.52 mm max height

PLASTIC QUAD FLATPACK - NO LEAD

SYMM

| (0.815) TYP     | 40        | 33    |           |   |   |
| --------------- | --------- | ----- | --------- | - | - |
| 40X (0.6)       | 1         | 41    | 32        |   |   |
| 40X (0.25)      |           |       |           |   |   |
| (1.28) TYP      | 36X (0.5) |       |           |   |   |
| (0.64) SYMM TYP | (6.8)     |       |           |   |   |
| (R0.05) TYP     | 8X (1.08) |       |           |   |   |
|                 | 12        | 21    | METAL TYP |   |   |
|                 | 13        | 20    | 8X (1.43) |   |   |
|                 |           | (4.8) |           |   |   |

SOLDER PASTE EXAMPLE

BASED ON 0.125 mm THICK STENCIL

EXPOSED PAD 71% PRINTED SOLDER COVERAGE BY AREA

SCALE: 18X

4222989/B 10/2017

NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

## IMPORTANT NOTICE

Texas Instruments Incorporated (TI) reserves the right to make corrections, enhancements, improvements and other changes to its semiconductor products and services per JESD46, latest issue, and to discontinue any product or service per JESD48, latest issue. Buyers should obtain the latest relevant information before placing orders and should verify that such information is current and complete.

TI’s published terms of sale for semiconductor products (http://www.ti.com/sc/docs/stdterms.htm) apply to the sale of packaged integrated circuit products that TI has qualified and released to market. Additional terms may apply to the use or sale of other types of TI products and services.

Reproduction of significant portions of TI information in TI data sheets is permissible only if reproduction is without alteration and is accompanied by all associated warranties, conditions, limitations, and notices. TI is not responsible or liable for such reproduced documentation. Information of third parties may be subject to additional restrictions. Resale of TI products or services with statements different from or beyond the parameters stated by TI for that product or service voids all express and any implied warranties for the associated TI product or service and is an unfair and deceptive business practice. TI is not responsible or liable for any such statements.

Buyers and others who are developing systems that incorporate TI products (collectively, “Designers”) understand and agree that Designers remain responsible for using their independent analysis, evaluation and judgment in designing their applications and that Designers have full and exclusive responsibility to assure the safety of Designers' applications and compliance of their applications (and of all TI products used in or for Designers’ applications) with all applicable regulations, laws and other applicable requirements. Designer represents that, with respect to their applications, Designer has all the necessary expertise to create and implement safeguards that (1) anticipate dangerous consequences of failures, (2) monitor failures and their consequences, and (3) lessen the likelihood of failures that might cause harm and take appropriate actions. Designer agrees that prior to using or distributing any applications that include TI products, Designer will thoroughly test such applications and the functionality of such TI products as used in such applications.

TI’s provision of technical, application or other design advice, quality characterization, reliability data or other services or information, including, but not limited to, reference designs and materials relating to evaluation modules, (collectively, “TI Resources”) are intended to assist designers who are developing applications that incorporate TI products; by downloading, accessing or using TI Resources in any way, Designer (individually or, if Designer is acting on behalf of a company, Designer’s company) agrees to use any particular TI Resource solely for this purpose and subject to the terms of this Notice.

TI’s provision of TI Resources does not expand or otherwise alter TI’s applicable published warranties or warranty disclaimers for TI products, and no additional obligations or liabilities arise from TI providing such TI Resources. TI reserves the right to make corrections, enhancements, improvements and other changes to its TI Resources. TI has not conducted any testing other than that specifically described in the published documentation for a particular TI Resource.

Designer is authorized to use, copy and modify any individual TI Resource only in connection with the development of applications that include the TI product(s) identified in such TI Resource. NO OTHER LICENSE, EXPRESS OR IMPLIED, BY ESTOPPEL OR OTHERWISE TO ANY OTHER TI INTELLECTUAL PROPERTY RIGHT, AND NO LICENSE TO ANY TECHNOLOGY OR INTELLECTUAL PROPERTY RIGHT OF TI OR ANY THIRD PARTY IS GRANTED HEREIN, including but not limited to any patent right, copyright, mask work right, or other intellectual property right relating to any combination, machine, or process in which TI products or services are used. Information regarding or referencing third-party products or services does not constitute a license to use such products or services, or a warranty or endorsement thereof. Use of TI Resources may require a license from a third party under the patents or other intellectual property of the third party, or a license from TI under the patents or other intellectual property of TI.

TI RESOURCES ARE PROVIDED “AS IS” AND WITH ALL FAULTS. TI DISCLAIMS ALL OTHER WARRANTIES OR REPRESENTATIONS, EXPRESS OR IMPLIED, REGARDING RESOURCES OR USE THEREOF, INCLUDING BUT NOT LIMITED TO ACCURACY OR COMPLETENESS, TITLE, ANY EPIDEMIC FAILURE WARRANTY AND ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT OF ANY THIRD PARTY INTELLECTUAL PROPERTY RIGHTS. TI SHALL NOT BE LIABLE FOR AND SHALL NOT DEFEND OR INDEMNIFY DESIGNER AGAINST ANY CLAIM, INCLUDING BUT NOT LIMITED TO ANY INFRINGEMENT CLAIM THAT RELATES TO OR IS BASED ON ANY COMBINATION OF PRODUCTS EVEN IF DESCRIBED IN TI RESOURCES OR OTHERWISE. IN NO EVENT SHALL TI BE LIABLE FOR ANY ACTUAL, DIRECT, SPECIAL, COLLATERAL, INDIRECT, PUNITIVE, INCIDENTAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES IN CONNECTION WITH OR ARISING OUT OF TI RESOURCES OR USE THEREOF, AND REGARDLESS OF WHETHER TI HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Unless TI has explicitly designated an individual product as meeting the requirements of a particular industry standard (e.g., ISO/TS 16949 and ISO 26262), TI is not responsible for any failure to meet such industry standard requirements.

Where TI specifically promotes products as facilitating functional safety or as compliant with industry functional safety standards, such products are intended to help enable customers to design and create their own applications that meet applicable functional safety standards and requirements. Using products in an application does not by itself establish any safety features in the application. Designers must ensure compliance with safety-related requirements and standards applicable to their applications. Designer may not use any TI products in life-critical medical equipment unless authorized officers of the parties have executed a special contract specifically governing such use. Life-critical medical equipment is medical equipment where failure of such equipment would cause serious bodily injury or death (e.g., life support, pacemakers, defibrillators, heart pumps, neurostimulators, and implantables). Such equipment includes, without limitation, all medical devices identified by the U.S. Food and Drug Administration as Class III devices and equivalent classifications outside the U.S.

TI may expressly designate certain products as completing a particular qualification (e.g., Q100, Military Grade, or Enhanced Product). Designers agree that it has the necessary expertise to select the product with the appropriate qualification designation for their applications and that proper product selection is at Designers’ own risk. Designers are solely responsible for compliance with all legal and regulatory requirements in connection with such selection.

Designer will fully indemnify TI and its representatives against any damages, costs, losses, and/or liabilities arising out of Designer’s non-compliance with the terms and provisions of this Notice.

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2017, Texas Instruments Incorporated

