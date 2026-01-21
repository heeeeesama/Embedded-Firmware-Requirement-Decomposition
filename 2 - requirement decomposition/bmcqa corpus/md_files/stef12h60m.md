# STEF12H60M 60 A electronic fuse for 12 V DC rail

## Features

- 60 A continuous current
- Input voltage range from 5 to 18 V
- Adjustable current limit
- Input undervoltage lockout
- Integrated 0.85 mΩ Power MOSFET
- Enable/Disable pin
- Programmable turn-on time
- Accurate current monitor signal
- Precise temperature monitor
- Overcurrent and Fault status flags
- Internal MOSFET self-diagnostic
- Parallel operation
- Thermal protection
- Fault management: latch-off or auto-retry versions
- QFN32- 5 x 5 package
- Temperature range: -40°C to 125°C

## Applications

- Server main eFuse
- Hot-swap boards
- High power industrial 12 V rail protection

## Description

The STEF12H60M is a 60 A integrated electronic fuse optimized for monitoring the
output current and the input voltage, over the 12 V DC power lines.
When connected in series to the main power rail, it is able to detect and react to
overcurrent conditions. When an overload condition occurs, the device limits the
output current to a safe value defined by the user.
A precise current monitor signal provides continuous information about the load
current to the system controller IC.
Similarly, a precise temperature sensor generates a monitor signal that permits the
system controller to keep the device power dissipation under control.
Turn-on time is programmable, which helps control the inrush current during start-up
operations.
Multiple devices can work in parallel and smoothly share the current during the start-
up phase, thanks to a dedicated current balancing feature.
The device also embeds the undervoltage lockout feature, self-diagnostic and
absolute thermal protection.

## Diagram

### Figure 1. Block diagram

|                                                  |            |                  | VDD               |                 | Gate   |       |                    |      |
| ------------------------------------------------ | ---------- | ---------------- | ----------------- | --------------- | ------ | ----- | ------------------ | ---- |
| VINF                                             |            |                  |                   |                 |        |       |                    |      |
|                                                  | Charge     |                  | 5 V LDO           |                 |        |       |                    |      |
|                                                  | 3.0 V      |                  |                   |                 |        | VIN   |                    |      |
|                                                  | 5mA        | SS error amp.    |                   |                 |        |       |                    |      |
|                                                  |            |                  |                   | Copy 1          | Copy 2 | Power | Voltage Monitoring |      |
| SS                                               | OUT        | R1               | ISHORT comparator |                 |        |       |                    |      |
|                                                  | 3.0V       | R2               |                   |                 |        |       |                    |      |
| CLREF                                            | 10mA       | GND              | ILIM error amp.   |                 |        |       |                    |      |
|                                                  |            |                  | Overcurrent       |                 |        | IOUT  | VOUT               | IMON |
|                                                  |            |                  |                   |                 |        | IMON  | I                  | CS   |
| Safe startup and current limit Reference circuit |            |                  |                   |                 |        |       |                    |      |
|                                                  |            | Gate             | GND               | UVLO detector   | 5.4V   |       |                    |      |
| Ref. OUT pull-down                               | Vᵍ         |                  | VDD               | 4.3V monitoring |        |       |                    |      |
|                                                  |            | D\_OC comparator | GND               | D\_OC           |        |       |                    |      |
| GATE cir.                                        | 85% CLREF  | D\_OC\_n         | Short             |                 |        |       |                    |      |
| 3.0V                                             | 5mA        | ON comparator    | G\_DCH            |                 |        |       |                    |      |
|                                                  |            | PD               | GND               | GOK             |        |       |                    |      |
| UVLO                                             | ON/PD      | G\_OK\_n         | 1.4V              |                 |        |       |                    |      |
|                                                  |            |                  | VDD               | Core logic      |        |       |                    |      |
| OFF comparator                                   |            | GND              | ON                | 3.7V            |        |       |                    |      |
| 1.2V                                             | OFF        | Thermal prot.    | Temperature       |                 |        |       |                    |      |
| PD\_OFF                                          | monitoring | PD comparator    | VTEMP             |                 |        |       |                    |      |
| 0.8V                                             | 50mA       | GND              | GND               |                 |        |       |                    |      |
|                                                  |            | GND              |                   |                 |        |       |                    |      |

## 2  Pin configuration

### Figure 2. Pin connection (top view)

NC

NC (reserved)

D_OC

ON/PD

GOK

NC (reserved)

VINF

NC (reserved)

DS13608 - Rev 6

VOUT VOUT VOUT VOUT VOUT VOUT VOUT VOUT

32  31         30  29  28  27  26  25

24  CLREF

23  CS

22  IMON

EXPOSED PAD                       21  VDD

(VIN )                        20  GND

19  SS

18  VTEMP

17  Gate

9   10         11  12  13    14  15  16

VIN  VIN       VIN  VIN  VIN  VIN  VIN  VIN

### Table 1. Pin description

| Pin #       | Symbol      | Function                                                     |
| ----------- | ----------- | ------------------------------------------------------------ |
| **25 - 32** | VOUT        | Output voltage of the eFuse. All pins must be connected together on the PCB |
| **3**       | D_OC        | Output pin, driven low if the current set-point is exceeded. 5V compliant open drain output |
| **4**       | ON/PD       | Enable/disable pin. Internally pulled up. Pull below threshold to disable, above to enable. Controls output pull-down resistance. |
| **5**       | GOK         | Gate-OK output pin. Signals shutdown not commanded by enable pin. 5V compliant open drain output, low during fault conditions |
| **1**       | NC          | Not internally connected. Can be connected to any voltage    |
| **6,8**     | NC/reserved | Reserved pins. Must be left floating                         |
| **2**       | NC/reserved | Reserved pin. Can be connected to any voltage up to VIN      |
| **7**       | VINF        | Input voltage for internal circuits. Connected to VIN through R-C filter |
| **9 - 16**  | VIN         | Input voltage of the eFuse. All pins must be connected together and to the exposed pad |
| **17**      | Gate        | Gate pin of internal MOSFET. Must be left floating or bypassed to GND with R-C filter to prevent oscillation |
| **18**      | VTEMP       | Temperature monitor pin. Bypass to GND with 0.1 pF capacitor |
| **19**      | SS          | Soft-start pin. Capacitor to GND determines soft-start time. Floating ≈300μs start-up |

| Pin #    | Symbol | Function                                                                                                                                                                                                                         |
| -------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 20       | GND    | Analog device ground                                                                                                                                                                                                             |
| 21       | VDD    | Internal LDO output and compensation pin. It provides a regulated 5 V auxiliary output. This pin must be bypassed to GND via a 1 μF capacitor to ensure the correct functionality of the device                                  |
| 22       | IMON   | Current monitor pin. A resistor (RMON) connected between this pin and GND generates a voltage proportional to the output current. It is suggested to connect a capacitor (CMON) in parallel to RMON to filter the monitor signal |
| 23       | CS     | Current feedback. A resistor (RCS) connected between this pin and GND provides a feedback voltage for the current limit circuit and the overcurrent indicator (D\_OC). Do not connect any capacitance to this pin                |
| 24       | CLREF  | Current limit set-point pin. Connect a resistor to GND or force an external control voltage to define the current limit set-point                                                                                                |
| EXP. PAD | VIN    | Input voltage, internally connected to the power FET drain                                                                                                                                                                       |

## 3  Typical application

### Figure 3. Typical application diagram (external controller used for CLREF pin)

| VCC  | D₁    | RINF  | VIN   | VOUT      | D2    | COUT |
| ---- | ----- | ----- | ----- | --------- | ----- | ---- |
| VINF |       | VDD   |       | VDD (5 V) |       |      |
| CINF |       |       | CDD   |           |       |      |
| IMON | R     | IMON  | VTEMP | C         | VTEMP |      |
| CMON | MON   |       | TEMP  |           |       |      |
|      |       | D\_OC |       | ON        | GOK   |      |
| OFF  | ON/PD | CLREF | SS    | Gate      | CSS   | GND  |
| CS   | RGate |       |       | RCS       | CGate |      |

### Figure 4. Typical application diagram (current limit fixed via RCL)

| VCC  |       |      | VIN | VOUT  | VOUT  |           |       |     |       |
| ---- | ----- | ---- | --- | ----- | ----- | --------- | ----- | --- | ----- |
|      | D₁    | RINF |     |       |       | D₂        | COUT  |     |       |
|      | VINF  |      |     | VDD   |       | VDD (5 V) |       |     |       |
|      | CINF  |      |     |       | CDD   |           |       |     |       |
| IMON |       | IMON |     | VTEMP | VTEMP |           |       |     |       |
|      | CMON  | RMON |     |       |       | CTEMP     |       |     |       |
|      | D\_OC |      | OFF | ON    |       |           |       |     |       |
|      |       |      |     | ON/PD | GOK   |           | Gate  |     |       |
|      |       | CSS  | SS  |       | CLREF |           | RGate |     |       |
|      |       |      |     |       | GND   | CS        | RCS   | RCL | CGate |

### Figure 5. Typical application diagram (multiple e-fuses in parallel)

| VIN   | VCC    | VIN   |       | VOUT   | VOUT             |       |      |
| ----- | ------ | ----- | ----- | ------ | ---------------- | ----- | ---- |
|       |        | RINF  |       |        |                  | COUT  | VINF |
|       |        | CINF  |       | VDD    | CDD              |       |      |
| VTEMP | IMON   | IMON  |       | eFuse1 | System           |       |      |
|       | ON/PD  | (1)   | ON/PD | CS     | RCS              |       |      |
| GOK   | D\_OC  | CLREF |       | GND    | SS               |       |      |
| CMON  | RMON   | VIN   |       | VOUT   | RINF             |       |      |
| VINF  |        | CINF  |       | VDD    | CDD              | VTEMP |      |
| IMON  | eFuse2 | ON/PD |       | CS     | (1)              |       |      |
| GOK   | RCS    | D\_OC | CLREF | GND    |                  |       |      |
| SS    | VIN    |       |       | VOUT   | RINF             |       |      |
| VINF  |        | CINF  |       | VDD    | CDD              | VTEMP |      |
| IMON  | eFuse3 | ON/PD |       | CS     | (1)              |       |      |
| GOK   | RCS    | D\_OC | CLREF | GND    |                  |       |      |
|       |        |       |       | SS     | To other E-fuses |       |      |

Note: Connect all the GOK and ON/PD pins when using the auto-retry version (STEF12H60MAPUR) in parallel configuration, to achieve synchronous restart cycle. Refer to Section 6.11: Parallel operation for further details.

## 4 Maximum ratings

### Table 2. Absolute maximum ratings

| Symbol         | Parameter                      | Value       | Unit |
| -------------- | ------------------------------ | ----------- | ---- |
| VIN            | Input supply voltage           | -0.3 to 20  | V    |
| VINF           | Input supply voltage           | -0.3 to VIN | V    |
| VOUT           | Output voltage                 | -0.3 to VIN | V    |
| VDD            | LDO output voltage             | -0.3 to 7   | V    |
| All other pins | Pin voltage                    | -0.3 to 6   | V    |
| IOUT           | Continuous output current      | 75          | A    |
| IDD            | LDO continuous output current  | 60          | mA   |
| ESD            | Charge device model            | ± 500       | V    |
|                | Human body model               | ± 2000      |      |
| TJ-OP (1)      | Operating junction temperature | -40 to 125  | °C   |
| TJ-MAX         | Maximum junction temperature   | 150         | °C   |
| TSTG           | Storage temperature            | -55 to 150  | °C   |

1. The thermal limit is set above the maximum operating temperature. It is not recommended to operate the device at temperatures greater than the maximum ratings for extended periods of time.

Note: Absolute maximum ratings are those values beyond which damage to the device may occur. Functional operation under these conditions is not implied. Exposure to absolute-maximum-rated conditions may affect device reliability.

### Table 3. Thermal data

| Symbol | Parameter                                                    | Value | Unit |
| ------ | ------------------------------------------------------------ | ----- | ---- |
| RθJA   | Thermal resistance junction-ambient (1)                      | 26    | °C/W |
|        | Thermal resistance junction to ambient, forced moving air (2) | 22    |      |
| RθJCT  | Thermal resistance junction to Top case                      | 15    |      |
| RθJCB  | Thermal resistance junction to Bottom case                   | 1.4   |      |
| RθJB   | Thermal resistance junction to Board (1)                     | 5.4   |      |
| RθJC   | Thermal resistance junction to Case (1)                      | 1.4   |      |

1. JEDEC still air natural convection test as per JESD 51-2 A, at ambient temperature of 25 ºC by using JEDEC (JESD 51-7) 4L PCB FR4 board using 1 sq−in pad, 1 oz Cu.

2. Forced moving air environment (100 LFM).

Note: Functional operation beyond the recommended operating conditions is not implied.

### Table 4. Recommended operating conditions

| Symbol | Parameter                     | Test conditions | Min. | Typ. | Max. | Unit |
| ------ | ----------------------------- | --------------- | ---- | ---- | ---- | ---- |
| VIN    | Input voltage                 |                 | 8    | 12   | 15   | V    |
| IOUT   | Continuous output current     |                 |      |      | 60   | A    |
| IDD    | LDO continuous output current | VINF = 5.5 V    |      |      | 50   | mA   |
| RCS    | Current set resistor          |                 | 1.8  |      | 4    | kΩ   |
| VCLREF | Control voltage range         |                 | 0.2  |      | 1.4  | V    |
| COUT   | Output capacitance (1)        |                 | 47   |      |      | μF   |
| tss    | Soft-start duration           |                 | 10   | 50   | 100  | ms   |
| CDD    | VDD capacitor value (2)       |                 | 1    | 2.2  | 10   | μF   |

1. The maximum allowed output capacitance to obtain a successful startup, without triggering internal fault protections, depends on the device soft-start time, RCS resistor and output load during power-up.

2. VDD capacitor is mandatory to ensure the internal regulator stability and the device functionality.

Note: Functional operation beyond the recommended operating conditions is not implied.

## 5 Electrical characteristics

TJ = -40 °C to +125 °C, typical values refer to TJ = 25 °C, VIN = VINF = 12 V, VON/PD = 3.3 V; COUT = 100 μF; unless otherwise specified. Min. and max. values are guaranteed by design and characterization through statistical correlation.

### Table 5. Electrical characteristics

| Symbol                                    | Parameter                                                    | Test conditions                                           | Min. | Typ. | Max. | Unit        |
| ----------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------- | ---- | ---- | ---- | ----------- |
| Input section                             |                                                              |                                                           |      |      |      |             |
| VIN                                       | Operating input voltage                                      |                                                           | 5    | 12   | 18   | V           |
| Iq                                        | Quiescent current                                            | Device operating, no load(VON/PD > 1.4 V)                 |      | 650  | 1000 | μA          |
|                                           |                                                              | Fault condition                                           |      | 300  |      |             |
|                                           |                                                              | Off-state, VON/PD = 0 V, VINF = 16 V                      |      | 200  | 400  |             |
| LDD                                       |                                                              |                                                           |      |      |      |             |
| VDD                                       | LDO output voltage                                           | IDD = 1 mA, VINF = 6 V                                    | 4.6  | 4.9  | 5.2  | V           |
| IDDmax                                    | LDO short circuit current (1)                                | VDD = 0 V                                                 | 60   | 120  |      | mA          |
| VDROP                                     | LDO dropout voltage                                          | IDD = 30 mA                                               | 66   | 100  | 160  | mV          |
| VDD\_ON                                   | UVLO rising threshold                                        |                                                           | 4.1  | 4.3  | 4.6  | V           |
| VDD\_OFF                                  | UVLO falling threshold                                       |                                                           | 3.8  | 4.0  | 4.2  | V           |
| Start-up                                  |                                                              |                                                           |      |      |      |             |
| ISS                                       | Soft-start capacitor charging current                        |                                                           | 4.5  | 5.2  | 6    | μA          |
| tSSMAX                                    | Soft-start max time                                          | if VOUT < 90% of VIN after tSSMAX shutdown is forced      |      | 200  |      | ms          |
| AS                                        | Soft-start gain                                              | Relation between internal soft-start signal ramp and VOUT |      | 10   |      | V/V         |
| PowerMOSFET                               |                                                              |                                                           |      |      |      |             |
| RDSon                                     | On-resistance                                                | TJ = 25 °C                                                |      | 0.85 | 1.1  | mΩ          |
| IL                                        | Off-state leakage current                                    | VON/PD = 0 V, VIN = 16 V, TJ = 25 °C                      |      |      | 1    | μA          |
| Current limit and current monitor circuit |                                                              |                                                           |      |      |      |             |
| VCS\_TH                                   | Current limit activation threshold(VCS = IRCS x RCS)         | VOUT > 80% of VIN                                         | 97   | 100  | 103  | V% of CLREF |
| VCL\_MAX (2)                              | Maximum CL reference voltage                                 |                                                           | 1.5  | 1.6  | 1.65 | V           |
| VCL\_FD                                   | Internal voltage reference for foldback current limit at startup | VOUT is lower than 40% of VIN                             | 130  | 150  | 170  | mV          |
| VCL\_ST                                   | Internal voltage reference for current limit at startup      | VOUT is between 40% and 80%                               | 470  | 500  | 530  | mV          |
| tCL                                       | Current limit response time (3)                              | from VCS > VCLREF until current limit                     |      | 100  |      | μs          |
| ICL                                       | CL pin internal biasing current                              | From CL pin into 1 V source                               | 9.4  | 10   | 10.4 | μA          |
| VCL\_HI                                   | Maximum voltage of the CLREF pin internal biasing source     |                                                           |      | 3.0  |      | V           |

| Symbol                      | Parameter                                     | Test conditions                                             | Min. | Typ. | Max. | Unit          |
| --------------------------- | --------------------------------------------- | ----------------------------------------------------------- | ---- | ---- | ---- | ------------- |
| IRCS/IMON                   | Current sense/monitor accuracy                | TJ = 25 °C, 10 A < IOUT < 60 A (3)(4)                       | -3   |      | 3    | %             |
| ACS, AMON                   | Current sense and current monitor gain        | IRCS/IOUT, IMON/IOUT, Tj = 25 °C, 10 A < IOUT < 60 A (3)(4) | 9.7  | 10   | 10.3 | μA/A          |
| tSH                         | Shutdown timer (3)                            | From current limit detection to MOSFET turn-off             |      | 250  |      | μs            |
| ISC                         | Short-circuit current limit (3)               |                                                             |      | 100  |      | A             |
| tSC                         | Short-circuit protection response time (3)    | From IOUT > ISC until MOSFET gate pulldown                  |      | 500  |      | ns            |
| VMON\_MAX                   | Internal current source maximum voltage       | Internal pull-up voltage on IMON pin                        |      | 3.0  |      | V             |
| ON/PD (chip enable pin)     |                                               |                                                             |      |      |      |               |
| VOFF                        | Low level input voltage                       | Output disabled/PD activated                                | 1.11 | 1.2  | 1.29 | V             |
| VON                         | High level input voltage                      | Output enabled                                              | 1.3  | 1.4  | 1.5  | V             |
| VPD                         | Pull-down de-activation threshold             | Pull-down de-activated                                      | 0.71 | 0.8  | 0.89 | V             |
| tON                         | Initial delay time                            | From VON/PD > VON to soft-start beginning                   | 0.8  | 1    | 1.2  | ms            |
| ION/PD                      | Enable pin bias current                       |                                                             | 4    | 5    | 6    | μA            |
| VON/PD\_MAX                 | Internal current source maximum voltage       | Internal pull-up voltage on ON/PD pin                       |      | 3.0  |      | V             |
| RPD                         | Output pull-down resistance                   | VOUT = 12 V, pull-down activated                            |      | 0.72 |      | kΩ            |
| tPD                         | Output pull-down delay timer                  | From VOFF < VON/PD < VPD                                    |      | 2    |      | ms            |
| Temperature monitor         |                                               |                                                             |      |      |      |               |
| VTEMP                       | Voltage                                       | T = 25 °C                                                   |      | 450  |      | mV            |
|                             | Temp coefficient (3)                          | T = 0 °C to 125 °C                                          |      | 10   |      | mV/°C         |
|                             | Load capability                               | Maximum current                                             |      |      | 4    | mA            |
|                             | Pull-down current                             | T = 25 °C                                                   |      | 50   |      | μA            |
| Status line                 |                                               |                                                             |      |      |      |               |
| GOK                         | Gate-OK output voltage                        | ISINK = 1 mA                                                |      |      | 0.1  | V             |
|                             | Leakage current                               | VGOK = 5 V                                                  |      |      | 1    | μA            |
| VOC                         | Overcurrent detection threshold               | VCS voltage threshold that triggers D\_OC low               | 83   | 85   | 87   | % <br/>VCLREF |
| D\_OC                       | Overcurrent monitor signal active low voltage | ISINK = 1 mA VCS > VOC                                      |      |      | 0.1  | V             |
|                             | Leakage current                               | VD\_OC = 5 V VCS < VOC                                      |      |      | 1    | μA            |
| tD                          | D\_OC signal response time (3)                |                                                             |      | 1    |      | μs            |
| Thermal protection          |                                               |                                                             |      |      |      |               |
| tSD                         | Shutdown temperature (3)                      | GOK pulled low                                              | 130  | 140  | 150  | °C            |
| tRetry                      | Autoretry delay time (only on STEF12H60MAPUR) | From shutdown due to fault to automatic restart             |      | 1    |      | s             |
| Internal MOSFET diagnostics |                                               |                                                             |      |      |      |               |
| VDS\_TH                     | Drain-source short detection threshold        | If VOUT > VDS\_TH at startup, startup is postponed          |      | 90   |      | % of VIN      |
| VDS\_OK                     | Drain-source voltage good detection threshold | If VOUT < VDS\_OK startup is resumed                        |      | 70   |      | % of VIN      |

| Symbol    | Parameter                                    | Test conditions                                              | Min. | Typ. | Max. | Unit     |
| --------- | -------------------------------------------- | ------------------------------------------------------------ | ---- | ---- | ---- | -------- |
| VOUT\_LOW | Low VOUT detection threshold                 | After startup, if VOUT < VOUT\_LOW, the device is turned off |      | 90   |      | % of VIN |
| VDG\_SH   | Gate-drain short detection voltage threshold | If VG > VDG\_SH after enable by ON pin, startup is postponed |      | 3.1  |      | V        |
| VDG\_OK   | Gate-drain voltage good detection threshold  | If VG < VDG-OK startup is resumed                            |      | 3    |      | V        |
| VG\_LOW   | Gate fault detection threshold               | If VGD < VG\_LOW device is turned off                        |      | 5.7  |      | V        |
| tG\_LOW   | Get fault timer in normal operation          | After tSSMAX elapses, time from VGD < VG\_LOW transition to gate fault detection |      | 200  |      | ms       |

1. Pulsed test. The internal LDO is not equipped with thermal protection. Short-circuit duration must not be longer than 1 ms to avoid damage.
2. If the voltage on CLREF pin is higher than VCL_MAX internal reference, the current limit reference voltage is clamped to VCL_MAX.
3. Guaranteed by design, but not tested in production.
4. MOSFET fully conducting, at minimum RON.

## 6 Device functional description

The STEF12H60M is a 12 V electronic fuse (eFuse), which is able to limit the current during fault events, such as output overload or short-circuit. The current limiting loop is also used during the start-up phase of the eFuse to avoid startups into faulty loads. During normal operation, the eFuse works as a low-resistance power switch, therefore the output voltage follows the input one. In case of overcurrent event, the eFuse limits the VGS of the internal MOSFET switch, in order to clamp the output current to a safe value. If the fault persists, after a predefined safety timer, or in case the die temperature hits the thermal protection threshold, due to the increased power dissipation, the device goes into shutdown, the internal switch is turned off and the load is disconnected from the power supply. The device is latched in this off-state until a power supply re-cycle is performed. The auto-retry version instead, is able to re-try starting the device after a fault event, with a typical delay of 1 ms. The current limit and soft-start features are programmable by the user, through external components.

### 6.1 UVLO ON/PD function

The device is supplied through the VIN pins, which carry the power directly to the internal power MOSFET drain connection, and the VINF pin, which is the input of the internal regulator, used to supply the analog and logic circuits. This pin must be connected externally to VIN through an R-C filter (see Section 3: Typical application). The UVLO (undervoltage lockout) monitors the voltage of the internally regulated VDD node and turns on the device when VDD > VDD_ON (typically 4.3 V). If VDD falls below the UVLO hysteresis threshold (VDD &#x3C; VDD_OFF), the device is turned off including the reset of fault state.

### 6.2 ON/PD function

During turn-on, provided that the UVLO rising threshold has been surpassed, the start-up procedure begins once the device is enabled via the ON/PD pin. The ON/PD is a logical input with a dual functionality, according to the following description:

1. Enable/disable the device: when VON/PD > VON, the device is enabled. If VON/PD is pulled down to VOFF or a lower voltage, the device is disabled and the output is shut down. In case the shutdown occurred due to a fault (thermal, overcurrent, failed startup), the device cannot be turned on again via the ON/PD pin. To reset the device from this latched status, a power supply re-cycle is necessary. Alternatively, a reset can be forced without turning off the power supply, by pulling VDD pin below the UVLO voltage and then releasing it.
2. Activate/deactivate the output discharge feature (PD – output pulldown): if VON/PD is kept between VPD (typ. 0.8 V) and VOFF (typ. 1.2 V) for at least 2 ms (tPD), the integrated 0.77 kΩ RPD discharging resistor is connected between VOUT and GND.

The ON/PD pin has an internal pull-up current generator connected to the internal LDO, therefore, if the pin is not connected to an external controller IC, it goes to the ON-state (device enabled). The 5 μA ON/PD bias current can be used to charge an external capacitor; in this manner prolonging the initial delay time, defined as the time interval between power supply reaching the UVLO threshold and the output voltage controlled ramp-up initialization.

### 6.3 Soft-start

The device provides monotonic, controlled start-up ramp, in order to keep the inrush current under control. The output voltage rise time can be set by an external CSS, which is charged with a constant current during the start-up phase. The soft-start range is adjustable from 1 to 100 ms. Given the required ramp-up time, the CSS capacitance can be calculated according to the following equation:

CSS = N × tSS × ISS × 10 /VIN(1)

where VIN is typically 12 V, tSS is in the 10-100 ms range and N is the number of eFuses in parallel.

The table below shows typical values of soft-start duration calculated with standard capacitors and typical ISS value.

#### Table 6. Output voltage rise time vs. CSS value (VIN = 12 V)

| Symbol   |      | Value |      |      |      |      |      |     |
| -------- | ---- | ----- | ---- | ---- | ---- | ---- | ---- | --- |
| CSS (nF) | 47   | 82    | 120  | 180  | 220  | 270  | 330  | 390 |
| tSS (ms) | 10.8 | 18.9  | 27.7 | 41.5 | 50.8 | 62.3 | 76.2 | 90  |

Important: Soft-start capacitor must be always connected to ensure controlled operation during startup. In case of absence/bad connection of the CSS, the start-up phase is short (300 μs). This might result in significantly high charging current, eventually leading to the device shutdown for an overcurrent/overtemperature fault. To prevent the device from starting in faulty loads (such as: resistive load, or damaged bulk output capacitors) the following start-up control flow is applied:

- Start-up fold-back current limit: current limit value during start-up phase is dependent on the sensed output voltage. At the very beginning of startup, when the output voltage is close to zero, the current limit internal reference voltage is reduced to VCL_FD. Any higher current limit value set by the user via the CLREF pin is overridden by the device.
- Start-up current limit: during the ramp-up phase, the current limit internal reference voltage is reduced to VCL_ST. Any higher current limit value, set by the user via the CLREF pin, is overridden by the device.
- Maximum start-up time: startup longer than 200 ms is always aborted by the device. If VOUT does not reach 90% of VIN in 200 ms, the device is turned off and the GOK fault indicator is asserted low.

Normal CLREF functionality is resumed at the end of the start-up phase (VOUT > 80 % of VIN). Adding a capacitor in parallel to the ON/PD pin, the initial tON delay time between valid VIN value and controlled output ramp-up start (VOUT = 1 V) can be increased. The default delay time without CON capacitor is typically 1.25 ms.

### 6.4 Normal operating conditions

Once the start-up phase ends, the STEF12H60M eFuse behaves like a mechanical fuse, supplying the load connected to its output with the same voltage shown at its input, minus the small voltage fall due to the N-channel MOSFET RDS(on). The status line open-drain indicators GOK and D_OC provide information about the status of the device.

### 6.5 Current sensing and current limit

When an overload event occurs, the current limiting circuit reduces the conductivity of the power MOSFET, in order to clamp the output current at the value defined by the user by the voltage set on CLREF pin. Current limit function consists of two sub-circuits:

- the current sense (CS) circuit, responsible for sensing the load current and providing a feedback signal to detect overcurrent. It relies on a small copy-MOSFET built into the integrated power MOSFET to generate a replica of the load current; proportional by ACS = IRCS/IOUT = 10 μA/A, into the external RCS resistor attached to the eFuse. This current creates a variable VCS voltage across the resistor, defining the eFuse working current CS, which is continuously compared to the current limit reference voltage present on the CLREF pin.
- the current limit (CL) circuit defines the reference threshold for the intervention of the current limitation function. This reference point is a voltage (VCLREF) usually provided externally by the system control IC to the CLREF pin, and continuously compared internally to the feedback signal from CS circuit. In this manner, the current limit point can be throttled to satisfy the system power requirements during operation. In simple standalone designs, such as the one shown in Figure 4. Typical application diagram (current limit fixed via RCL), where no control IC is present, the reference signal can be generated by connecting a resistor between CLREF pin and GND. An integrated bias generator sources 10 μA of current to the RCL resistor, generating a fixed VCLREF, which sets the current limit thresholds. To ensure reliability, the signal on CLREF is internally clamped to VCL_MAX, therefore, even in case of wrong signal provided externally on the pin, a safety current limit threshold is always present.

An overcurrent event is detected when the voltage on the CS pin overcomes the VOC threshold, which is typically 85% of the voltage at the CLREF pin (VCS > VOC). In this case the status D_OC indicator is pulled down. If the load status reverts to normality (VCS falls below 75% of VCLREF), D_OC is released. Based on the value of the RCS resistor, the load current level for D_OC triggering can be evaluated by using the following equation:

IOUT =  VOC  /（RCS ×Acs）(2)

In case of overcurrent detection, when VCS surpasses VCLREF, the VGS of the internal MOSFET is immediately modulated in order to clamp the load current to the ILIM value defined by the user via the CLREF pin, according to the following:

ILIM = VCLREF/（RCS × Acs）  (3)

During current limitation, additional protection features are activated, in order to keep the total power dissipation under control and protect the device and the system. In particular, a 250 μs current limit timer (tSH) starts after overload detection. Once the timer elapses, the internal MOSFET is shut down and the GOK indicator is pulled to low status, to inform the system controller that a shutdown not due to ON/PD (fault) occurred. Moreover, due to high power dissipation in current limit condition, if the die temperature increases too much and hits the thermal protection threshold (140 °C typ.), the thermal protection intervenes, turning off the internal MOSFET and asserting GOK low. A second level current limit (ISC) is quickly activated in case the load current surpasses 100 A. This additional protection, fixed by design, is able to respond to short-circuit events on the output. In such an occurrence, the device is immediately shut down and the D_OC pin is asserted.

### 6.6 Current monitor

The device is equipped with a current monitoring capability that allows the system controller to read the current flowing through the fuse. An IMON current proportional to the load current flowing through the eFuse is imposed on an external RMON, converting the sensed current into a voltage for further processing by the ADC. The IMON signal is the output of a chopper amplifier, therefore an external bypass capacitor is suggested to reduce the output ripple and to provide a smooth signal (see figure below). The suggested minimum value for the filter capacitor is 3.9 nF. Lower values result in a worse ripple amplitude. The current monitoring amplifier gain is defined as AI = IMON / IOUT, is typically 10 μA/A.

#### Figure 6. Current monitor simplified circuit

| IMON | to ADC |
| ---- | ------ |
| RMON | CMON   |

### 6.7 Temperature monitor and thermal shutdown functions

The STEF12H60M embeds two thermal sensors, each one accomplishing a specific function:

- Overtemperature sensor: this is embedded into the power MOSFET. It monitors the power MOSFET temperature, which is subjected to very fast increases during overload events. If the device temperature exceeds the thermal threshold, typically 140 °C, the thermal shutdown circuit turns the power MOSFET off, thus disconnecting the load. The GOK pin is pulled down. The thermal shutdown protection is always active and overrides any other protection/control feature of the device.
- Temperature sensor: this consists of precise thermal sensors embedded in the controller die. The purpose is to statically monitor the overall device temperature, and generate a precise monitor signal (VTEMP) accordingly. Overall typical accuracy is +/- 5 °C. To ensure a stable regulation of the temperature monitor signal in all operating conditions, it is recommended to bypass this pin to GND via a 0.1 μF CTEMP capacitor, as shown in Figure 3 and Figure 4.

The device can be reset from a thermal shutdown condition by pulling the VDD pin below the UVLO threshold or by re-cycling the supply voltage. In parallel configuration, to accomplish simultaneous reset, each device must have its dedicated reset switch, for instance a MOSFET. All the gates of the reset MOSFETS must be tied together to the common reset signal.

### 6.8 Status indicators and fault conditions

Two open-drain flags can be used to monitor the status of the eFuse, along with the current and temperature monitor signals.

- D_OC - Overcurrent indicator: in normal operation and during startup it is released. It is pulled down upon detection of an overload (see Section 6.5: Current sensing and current limit)
- GOK - gate ok indicator: this indicator informs that there was a shutdown that was not commanded by the enable pin (ON/PD). In particular, this pin is pulled low when:
- too low input voltage: VDD lower than UVLO threshold
- too long start-up time: VOUT does not reach 90% of VIN in 200 ms
- too long current limit: a current limit event is longer than tSH (250 μs typ.)

During the startup, GOK is released once UVLO is reached, under the condition that Vout is below VDS_OK (drain to source short detection, see Section 6.9), therefore it cannot be used directly as a Power Good flag. GOK is also pulled to low level in the case of any of the faults described in Section 6.9.

### 6.9 Diagnostic functions and protections

The STEF12H60M embeds several internal diagnostic features that prevent fault condition induced internally that may affect the application (refer to Section 5: Electrical characteristics):

- Power MOSFET gate leakage check during startup and normal operation (VGate-VIN &#x3C; 5.6 V)
- Gate shorted-to-VIN
- Drain to source short in disabled mode (ON pin low). This protection prevents a new startup until the VOUT falls below the VDS_Ok value.
- VOUT too low (VOUT &#x3C; 90% of VIN) after soft-start
- VOUT does not reach 90% of VIN in 200 ms during startup
- Charge pump error
- Pull-down circuit error

In any case of fault, the GOK indicator is pulled down and the soft-start capacitor is discharged.

### 6.10 Latch (STEF12H60MPUR) and auto-retry versions (STEF12H60MAPUR)

The STEF12H60M electronic fuse is offered in two variants that differ in how the device reacts after a fault condition (see Section 6.8 and Section 6.9). In particular, the STEF12H60MPUR latches off after a fault and can be reset by pulling the VDD pin below the UVLO threshold or by re-cycling the supply voltage. The STEF12H60MAPUR instead stays in OFF mode for 1 s. (tRetry) and after restarts automatically, initiating a soft-start cycle. The number of restart cycles is not internally limited.

### 6.11 Parallel operation

Figure 5 shows a typical circuit configuration used to protect high power systems. In this case multiple STEF12H60M are used in a parallel configuration to increase the total current capability. In such design the following guidelines must be followed:

- The ON_PD pins of all eFuses must be tied together to achieve a simultaneous startup.
- All the SS pins must be connected together to a single CSS capacitor. The value of this capacitor should be calculated by using Eq. (1), taking into account that each device provides its ISS charging current to the capacitor. The SS pin is also used to discharge the CSS capacitor during shutdown. In case one eFuse shuts down, the common CSS capacitor is discharged causing simultaneous shutdown of all the paralleled devices.
- All the CLREF pins must be tied together to a single RCL resistor or to common VCLREF control signal from the system controller to set the current limit reference. When using the RCL resistor, the ICL bias current coming from each device must be accounted.
- Each CS pin must be connected to a local RCS, to ensure the current sensing circuit is able to read the single eFuse current.
- The IMON pins can be all tied together to a single RMON / CMON filter. In this way the IMON currents coming from each eFuse all contribute to the voltage generated on the resistor, that results proportional to the total system current. If it is necessary to read the single eFuse current, the local RMON resistor approach can be used.
- The VTEMP pins can be all tied together in Or-ing configuration, therefore the system controller reads the highest temperature among all the eFuses.
- When needed, all of the D_OC and all of the GOK fault flag pins can be tied together and pulled up via a single resistor.
- To accomplish simultaneous reset, each device must have its dedicated reset switch, for instance a MOSFET, connected to VDD pin. All the gates of the reset MOSFETS must be tied together to the common reset signal.
- If the auto-retry version (STEF12H60MAPUR) is used in parallel configuration, dedicated circuital provision should be made. Specifically, it is recommended to connect all the ON/PD pins to the GOK ones as shown in Figure 7 to ensure a proper synchronization of the auto-retry cycle. A common Enable signal can be used to start up the devices.
- During power-up in parallel operation, keeping the load current through each eFuse lower than 1.5 A (typical) helps to prevent overstress in the internal power MOSFETS at each soft-start cycle.

#### Figure 7. Additional connections for multiple STEF12H60MAPUR (autoretry version)

| Common Enable    | ON/PD      |     |   |   |
| ---------------- | ---------- | --- | - | - |
|                  | GOK eFuse1 | GND |   |   |
| ON/PD            | GOK eFuse2 | GND |   |   |
| ON/PD            | GOK eFuse3 | GND |   |   |
| To other E-fuses |            |     |   |   |

### 6.12 Application suggestions and PCB layout guidelines

STEF12H60M eFuse is used into high-power systems where high current flows through the power path. In case of overload or short circuit events, the device instantaneously interrupts the current flow. In such cases, the input/output stray inductances cause voltage overshoots on the input and undershoots on the output of the device, which can overcome the absolute maximum ratings and damage the eFuse.

To reduce the effects of such transients, it is recommended to adopt the following application design guidelines:

- Minimize the inductance of the input and output tracks
- Use TVS diodes on the input to absorb inductive spikes, see D1 in Figure 3. The ST's SMC50J12CA high-power TVS diode is a tested and recommended solution to protect the STEF12H60M, for operation over the 12V bus.
- Place a Schottky diode on the output to absorb negative spikes, see D2 in Figure 3. ST's FERD15S50 field-effect rectifier is a tested and recommended protection against output voltage undershoot.
- Use a combination of ceramic and electrolytic capacitors on the output.


## 7 Typical characteristics

CIN = 1 μF; COUT = 10 μF, TJ = 25 °C unless otherwise specified.

### Figure 8. Quiescent current vs. temperature

### Figure 9. Shutdown current vs. temperature

VIN = VINF = 12 V, IOUT = 0 mA

| Temperature \[ºC]       | -50 | -25 | 0   | 25  | 50  | 75  | 100 | 125 | 150 |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Quiescent Current \[μA] | 800 | 750 | 700 | 650 | 600 | 550 | 500 | 450 | 400 |

| Temperature \[ºC]      | -50 | -25 | 0   | 25  | 50  | 75  | 100 | 125 | 150 |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shutdown Current \[μA] | 400 | 350 | 300 | 250 | 200 | 150 | 100 | 50  | 0   |

### Figure 10. IMON gain accuracy vs. load current and temperature

### Figure 11. I MON current vs. load current

VIN = 12V, IOUT from 0 to 70 A, NO CIN, NO COUT, VCLREF = 1.5V

| Load Current \[A] | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 | 65 | 70 |
| ----------------- | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| IMON \[μA]        | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 | 65 | 70 |

### Figure 12. CS current vs. temperature

### Figure 13. VCLREF threshold vs. temperature

VIN = 12V, IOUT from 0 to 70 A, NO CIN, NO COUT, VCLREF = 1.5V

| Temperature \[ºC] | -50   | -25   | 0     | 25    | 50    | 75    | 100   | 125   | 150 |
| ----------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | --- |
| CS Current \[μA]  | 800.0 | 700.0 | 600.0 | 500.0 | 400.0 | 300.0 | 200.0 | 100.0 | 0.0 |

| Temperature \[ºC] | -50   | -25   | 0     | 25    | 50    | 75    | 100  | 125  | 150  |      |      |
| ----------------- | ----- | ----- | ----- | ----- | ----- | ----- | ---- | ---- | ---- | ---- | ---- |
| VCLREF \[%]       | 101.0 | 100.8 | 100.6 | 100.4 | 100.2 | 100.0 | 99.8 | 99.6 | 99.4 | 99.2 | 99.0 |

### Figure 14. CLREF pin bias current vs. temperature

| \[μA] | Temperature \[ºC] |
| ----- | ----------------- |
| 12.0  | -50               |
| 11.5  | -25               |
| 11.0  | 0                 |
| 10.5  | 25                |
| 10.0  | 50                |
| 9.5   | 75                |
| 9.0   | 100               |
| 8.5   | 125               |
| 8.0   | 150               |

Figure 16. VTEMP voltage vs. temperature

| \[mV] | Ambient Temperature \[ºC] |
| ----- | ------------------------- |
| 2.000 | -50                       |
| 1.800 | -25                       |
| 1.600 | 0                         |
| 1.400 | 25                        |
| 1.200 | 50                        |
| 1.000 | 75                        |
| 800   | 100                       |
| 600   | 125                       |
| 400   | 150                       |

### Figure 18. ON/PD thresholds vs. temperature

| \[V] | Temperature \[ºC] |
| ---- | ----------------- |
| 1.7  | -50               |
| 1.5  | -25               |
| 1.3  | 0                 |
| 1.1  | 25                |
| 0.9  | 50                |
| 0.7  | 75                |
| 0.5  | 100               |
|      | 125               |
|      | 150               |

### Figure 15. VDD voltage vs. temperature

| VDD \[V] | Temperature \[ºC] |
| -------- | ----------------- |
| 5.200    | -50               |
| 5.100    | -25               |
| 5.000    | 0                 |
| 4.900    | 25                |
| 4.800    | 50                |
| 4.700    | 75                |
| 4.600    | 100               |
|          | 125               |
|          | 150               |

### Figure 17. UVLO thresholds vs. temperature

| VDD \[V] | Temperature \[ºC] |
| -------- | ----------------- |
| 5.0      | -50               |
| 4.8      | -25               |
| 4.6      | 0                 |
| 4.4      | 25                |
| 4.2      | 50                |
| 4.0      | 75                |
| 3.8      | 100               |
| 3.6      | 125               |
| 3.4      | 150               |

### Figure 19. ON/PD pin current vs. temperature

| ION/PD \[μA] | Temperature \[ºC] |
| ------------ | ----------------- |
| 7.0          | -50               |
| 6.5          | -25               |
| 6.0          | 0                 |
| 5.5          | 25                |
| 5.0          | 50                |
| 4.5          | 75                |
| 4.0          | 100               |
| 3.5          | 125               |
| 3.0          | 150               |

### Figure 20. SS pin bias current vs. temperature

| \[μA] | 7.0 |
| ----- | --- |
|       | 6.5 |
|       | 6.0 |
|       | 5.5 |
| ISS   | 5.0 |
|       | 4.5 |
|       | 4.0 |
|       | 3.5 |
|       | 3.0 |

-50  -25  0  25  50  75  100  125  150

Temperature [ºC]

### Figure 22. On-resistance vs. temperature

VIN = VINF = 12 V, IOUT= 20 A

| \[mΩ]   | 1.70 |
| ------- | ---- |
|         | 1.50 |
|         | 1.30 |
|         | 1.10 |
| RDS\_ON | 0.90 |
|         | 0.70 |
|         | 0.50 |

-50  -25  0  25  50  75  100  125  150

Temperature [ºC]

### Figure 24. Startup by VIN (no load)

| INPut VOLTAGE | OUTPUT VOLTAGE | VTEMP VOLTAGE | ON VOLTAGE | DOC VOLTAGE | CLREF VOLTAGE | IMON VOLTAGE | Input Current |
| ------------- | -------------- | ------------- | ---------- | ----------- | ------------- | ------------ | ------------- |
| lWmie         | Santi Ilb      |               |            |             |               |              |               |

### Figure 21. Turn-on initial delay vs. temperature

| \[ms] | 2.0 |
| ----- | --- |
|       | 1.8 |
|       | 1.6 |
|       | 1.4 |
|       | 1.2 |
| tON   | 1.0 |
|       | 0.8 |
|       | 0.6 |
|       | 0.4 |
|       | 0.2 |
|       | 0.0 |

-50  -25  0  25  50  75  100  125  150

Temperature [ºC]

### Figure 23. Off-state leakage current vs. temperature

VIN=16 V, ON/PD=LOW, NO CIN, NO COUT

2.0
1.8
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
0.0

-50  -25  0  25  50  75  100  125  150

Temperature [ºC]

### Figure 25. Shutdown by VIN (no load)

| INPut VOLTAGE | OUTPUT VOLTAGE | VTEMP VOLTAGE | ON VOLTAGE | DOC VOLTAGE | CLREF VOLTAGE | IMON VOLTAGE | Input Current |
| ------------- | -------------- | ------------- | ---------- | ----------- | ------------- | ------------ | ------------- |
| ln            | EGbia          |               |            |             |               |              |               |

page 20/32

STEF12H60M

### Figure 26. Startup by VIN (COUT = 6200 μF, no load)

### Figure 27. Startup by VIN (COUT = 6200 μF, 15 A, res. load)

| INPUT VOLTAGE | OUTPUT VOLTAGE | ONiPD VOLTAGE | VDD VOLTAGE | D\_OC VOLTAGE | G\_OK VOLTAGE | Output Current |
| ------------- | -------------- | ------------- | ----------- | ------------- | ------------- | -------------- |

### Figure 28. Startup by ON/PD (no load)

### Figure 29. Shutdown by ON/PD (no load)

| INPUT VOLTAGE | OUTPUT VOLTAGE | ONiPD VOLTAGE | VDD VOLTAGE | D\_OC VOLTAGE | G\_OK VOLTAGE | Output Current | TEMP VOLTAGE |
| ------------- | -------------- | ------------- | ----------- | ------------- | ------------- | -------------- | ------------ |

### Figure 30. Startup by ON/PD (IOUT = 15 A, COUT = 6800 μF)

### Figure 31. Shutdown by ON/PD (IOUT = 15 A, COUT = 6800 μF)

| INPut VOLTAGE | OUTPUT VOLTAGE | ONpD VOLTAGE | VDD VOLTAGE | D\_CC VOLTAGE | G\_Ok VOLTAGE | Output CuRRENT | TEMP VOLTAGE |
| ------------- | -------------- | ------------ | ----------- | ------------- | ------------- | -------------- | ------------ |

### Figure 32. Startup into output short-circuit

### Figure 33. Output short-circuit during operation

| INPUT VOLTAGE | OUTPUT VOLTAGE | TEMPERATURE VOLTAGE | D\_OC VOLTAGE | Gok VOLTAGE | IMON VOLTAGE   | OUTPUT Current |
| ------------- | -------------- | ------------------- | ------------- | ----------- | -------------- | -------------- |
|               |                |                     |               |             |                |                |
| INPUT VOLTAGE | OUTPUT VOLTAGE | ON VOLTAGE          | VTEMP VOLTAGE | GK VOLTAGE  | OUTPUT CURRENT |                |


## 8 Package information

To meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, depending on their level of environmental compliance. ECOPACK specifications, grade definitions, and product status are available at: www.st.com. ECOPACK is an ST trademark.

### 8.1 QFN 32 (5 x 5) package information

#### Figure 34. QFN 32 (5 x 5) package outline

STEF12H60M

#### Table 7. QFN 32 (5 x 5) package mechanical data

| Dim. | Min. | Typ. | Max. |
| ---- | ---- | ---- | ---- |
| A    | 0.90 | 0.95 | 1    |
| A1   |      | 0.20 |      |
| D    | 4.90 | 5.00 | 5.10 |
| D1   | 3.40 | 3.50 | 3.60 |
| E    | 4.90 | 5.00 | 5.10 |
| E1   | 3.25 | 3.35 | 3.45 |
| e    |      | 0.50 |      |
| b    | 0.20 | 0.25 | 0.30 |
| L    | 0.30 | 0.40 | 0.50 |

#### Figure 35. QFN 32 (5 x 5) recommended footprint

0.22

0.30

### 8.2 QFN 32 (5 x 5) packing information

Figure 36. QFN 32 (5 x 5) carrier tape

Figure 37. Pin 1 orientation in tape

Dzcr dirocbon ottocd

#### Figure 38. QFN 32 (5 x 5) reel outline

#### Table 8. QFN 32 (5 x 5) reel data

| Reel size | Tape width | A (max.) | B (min.) | C        | D (min.) | G (max.) | N (min.) | T (max.) | Unit |
| --------- | ---------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | ---- |
| 13”       | 0.90       | 330      | 1.5      | 13 ± 0.2 | 20.2     | 12.6     | 100      | 18.4     | mm   |

## 9 Ordering information</h9>
### Table 9. Order codes</h9>
| Order code     | Package       | Packaging  | Marking  |
| -------------- | ------------- | ---------- | -------- |
| STEF12H60MPUR  | QFN32 (5 x 5) | Latch      | EF12M60  |
| STEF12H60MAPUR |               | Auto-retry | EF12M60A |

## Revision history

### Table 10. Document revision history

| Date        | Revision | Changes                                              |
| ----------- | -------- | ---------------------------------------------------- |
| 13-Jan-2021 | 1        | Initial release.                                     |
| 19-Mar-2021 | 2        | Removed footnote in Table 9.                         |
| 11-May-2021 | 3        | Updated Figure 3 and Figure 4.                       |
| 12-May-2022 | 4        | Updated Table 3. Thermal data.                       |
| 08-Sep-2022 | 5        | Updated Figure 8. Quiescent current vs. temperature. |
| 14-Jan-2025 | 6        | Added Section 6.12.                                  |

## Contents

1. Diagram.. . . . 2
2. Pin configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3. Typical application.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4. Maximum ratings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
5. Electrical characteristics.. . . . . . . . . . . . . . . . . . . . . . . 9
6. Device functional description. . . . . . . . . . . . . . . . . . . . . . . . . .12
1. UVLO ON/PD function. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2. ON/PD function. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3. Soft-start.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4. Normal operating conditions. . . . . . . . . . . . . . . . . . . . . . . . . 13
5. Current sensing and current limit. . . . . . . . . . . . . . . . . . . . . . . . . 13
6. Current monitor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
7. Temperature monitor and thermal shutdown functions.. . . . . . . . . . . 15
8. Status indicators and fault conditions. . . . . . . . . . . . . . . . . . 15
9. Diagnostic functions and protections. . . . . . . . . . . . . . . . . . 15
10. Latch (STEF12H60MPUR) and auto-retry versions (STEF12H60MAPUR). . . . . . . . . 15
11. Parallel operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
12. Application suggestions and PCB layout guidelines. . . . . . . . . . . . . . 17
7. Typical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
8. Package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
1. QFN 32 (5 x 5) package information. . . . . . . . . . . . . . . . . . . 23
2. QFN 32 (5 x 5) packing information. . . . . . . . . . . . . . . . . . . 25
9. Ordering information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

## List of tables

| Table 1.  | Pin description                                     | 3  |
| --------- | --------------------------------------------------- | -- |
| Table 2.  | Absolute maximum ratings                            | 7  |
| Table 3.  | Thermal data                                        | 7  |
| Table 4.  | Recommended operating conditions                    | 8  |
| Table 5.  | Electrical characteristics                          | 9  |
| Table 6.  | Output voltage rise time vs. CSS value (VIN = 12 V) | 13 |
| Table 7.  | QFN 32 (5 x 5) package mechanical data              | 24 |
| Table 8.  | QFN 32 (5 x 5) reel data                            | 26 |
| Table 9.  | Order codes                                         | 27 |
| Table 10. | Document revision history                           | 28 |

## List of figures

| Figure 1.  | Block diagram                                                          | 2  |
| ---------- | ---------------------------------------------------------------------- | -- |
| Figure 2.  | Pin connection (top view)                                              | 3  |
| Figure 3.  | Typical application diagram (external controller used for CLREF pin)   | 5  |
| Figure 4.  | Typical application diagram (current limit fixed via RCL)              | 5  |
| Figure 5.  | Typical application diagram (multiple e-fuses in parallel)             | 6  |
| Figure 6.  | Current monitor simplified circuit                                     | 14 |
| Figure 7.  | Additional connections for multiple STEF12H60MAPUR (autoretry version) | 17 |
| Figure 8.  | Quiescent current vs. temperature                                      | 18 |
| Figure 9.  | Shutdown current vs. temperature                                       | 18 |
| Figure 10. | IMON gain accuracy vs. load current and temperature                    | 18 |
| Figure 11. | IMON current vs. load current                                          | 18 |
| Figure 12. | CS current vs. temperature                                             | 18 |
| Figure 13. | VCLREF threshold vs. temperature                                       | 18 |
| Figure 14. | CLREF pin bias current vs. temperature                                 | 19 |
| Figure 15. | VDD voltage vs. temperature                                            | 19 |
| Figure 16. | VTEMP voltage vs. temperature                                          | 19 |
| Figure 17. | UVLO thresholds vs. temperature                                        | 19 |
| Figure 18. | ON/PD thresholds vs. temperature                                       | 19 |
| Figure 19. | ON/PD pin current vs. temperature                                      | 19 |
| Figure 20. | SS pin bias current vs. temperature                                    | 20 |
| Figure 21. | Turn-on initial delay vs. temperature                                  | 20 |
| Figure 22. | On-resistance vs. temperature                                          | 20 |
| Figure 23. | Off-state leakage current vs. temperature                              | 20 |
| Figure 24. | Startup by VIN (no load)                                               | 20 |
| Figure 25. | Shutdown by VIN (no load)                                              | 20 |
| Figure 26. | Startup by VIN (COUT = 6200 μF, no load)                               | 21 |
| Figure 27. | Startup by VIN (COUT = 6200 μF, 15 A, res. load)                       | 21 |
| Figure 28. | Startup by ON/PD (no load)                                             | 21 |
| Figure 29. | Shutdown by ON/PD (no load)                                            | 21 |
| Figure 30. | Startup by ON/PD (IOUT = 15 A, COUT = 6800 μF)                         | 21 |
| Figure 31. | Shutdown by ON/PD (IOUT = 15 A, COUT = 6800 μF)                        | 21 |
| Figure 32. | Startup into output short-circuit                                      | 22 |
| Figure 33. | Output short-circuit during operation                                  | 22 |
| Figure 34. | QFN 32 (5 x 5) package outline                                         | 23 |
| Figure 35. | QFN 32 (5 x 5) recommended footprint                                   | 24 |
| Figure 36. | QFN 32 (5 x 5) carrier tape                                            | 25 |
| Figure 37. | Pin 1 orientation in tape                                              | 25 |
| Figure 38. | QFN 32 (5 x 5) reel outline                                            | 26 |

## IMPORTANT NOTICE – READ CAREFULLY

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST products are sold pursuant to ST’s terms and conditions of sale in place at the time of order acknowledgment.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to www.st.com/trademarks. All other product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

