# Si5391 Reference Manual

Ultra Low Jitter, Any-Frequency, Any Output Clock Generator: Si5391 Reference Manual

## RELATED DOCUMENTS

The Si5391 Clock Generators combine MultiSynth™ technologies to enable any-frequency clock generation for applications that require the highest level of jitter performance. These devices are programmable via a serial interface with in-circuit programmable nonvolatile memory (NVM) ensuring power up with a known frequency configuration.

- Si5391 Data Sheet
- Si5391 Device Errata
- Si5391-EVB User Guide
- Si5391-EVB Schematics, BOM &#x26; Layout
- IBIS models

## Table of Contents

1. Work Flow Using ClockBuilder Pro and the Register Map............... 5
  1.1 Field Programming ............................ 5
2. Family Product Comparison.......................... 6
  2.1 Grade P (Precision) Restrictions and Requirements ................. 6
  2.2 Si5391P Grade Frequency Plan Rules ...................... 6
  2.2.1 Output Clock Domains .......................... 6
  2.2.2 Output Clock Locations.......................... 6
  2.2.3 Output Clock Format Restrictions ...................... 7
3. Functional Description............................ 8
  3.1 Dividers ................................ 9
4. Power-up, Reset, and Initialization ...................... 10
5. Dynamic PLL Changes............................11
  5.1 Dynamic Changes to Output Frequencies without Changing PLL Settings ..........11
  5.2 Dynamic Changes to Output Frequencies while Changing PLL Settings Using a CBPro Register
  Map .................................12
6. NVM Programming ............................ 13
7. Clock Inputs............................... 15
  7.1 Reference Input Selection (IN0, IN1, IN2, XA/XB) ..................16
  7.2 Types of Inputs ..............................17
  7.2.1 Crystal on XA/XB............................17
  7.2.2 Clock Input on XA/XB ..........................18
  7.2.3 Clock Inputs on IN2, IN1, IN0 .......................19
  7.2.4 Unused Inputs.............................20
  7.2.5 Input Clock Rise Time Considerations.....................20
  7.3 Fault Monitoring .............................21
  7.3.1 Status Indicators ............................22
  7.3.2 Interrupt Pin (INTR) ...........................23
8. Outputs ................................ 25
  8.1 Output Crosspoint Switch ..........................25
  8.2 Output Divider (R) Synchronization .......................26
  8.3 Performance Guidelines for Outputs .......................27
  8.4 Output Signal Format ............................28
  8.4.1 Differential Output Terminations .......................29
  8.4.2 Differential Output Swing Modes ......................30
  8.4.3 Programmable Common Mode Voltage for Differential Outputs ............31
  8.4.4 LVCMOS Output Terminations .......................31
  8.4.5 LVCMOS Output Impedance and Drive Strength Selection ..............31
  8.4.6 LVCMOS Output Signal Swing .......................32
  8.4.7 LVCMOS Output Polarity .........................33
9. 8.4.8 Output Driver Settings for LVPECL, LVDS, HCSL, and CML .............34
  8.4.9 Setting the Differential Output Driver to Non-Standard Amplitudes ...........35
  8.5 Output Enable/Disable ...........................37
  8.5.1 Output Driver State When Disabled .....................38
  8.5.2 Synchronous Output Enable/Disable Feature ..................38
  8.6 Output Buffer Supply Voltage Selection......................38
  8.7 Output Delay Control ............................39
  9. Zero Delay Mode (All Si5391 Devices Except Si5391P) ............... 40
  10. Digitally-Controlled Oscillator (DCO) Mode (All Si5391 Devices Except Si5391P) .... 41
      10.1 Using the N Dividers for DCO Applications ....................41
      10.1.1 DCO with Frequency Increment/Decrement Pins/Bits ...............41
      10.1.2 DCO with Direct Register Writes ......................41
      10.2 Using the M Divider for DCO Applications ....................41
  11. Serial Interface ............................. 42
      11.1 I2C Interface ..............................44
      11.2 SPI Interface ..............................46
  12. Crystal, XO and Device Circuit Layout Recommendations ............. 51
      12.1 64-Pin QFN Si5391/Si5391P Layout Recommendations ...............51
      12.1.1 Si5391 with an External Reference (Not Relevant to the Si5391P) ..........51
      12.1.2 Si5391/Si5391P Crystal Guidelines .....................52
      12.1.3 Si5391/Si5391P Output Clocks ......................58
  13. Power Management ........................... 60
      13.1 Power Management Features ........................60
      13.2 Power Supply Recommendations .......................60
      13.3 Power Supply Sequencing .........................61
      13.4 Grounding Vias .............................61
  14. Register Map .............................. 62
      14.1 Base vs. Factory Preprogrammed Devices ....................62
      14.2 “Base” Devices (a.k.a. “Blank” Devices) .....................62
      14.3 “Factory Preprogrammed” (Custom OPN) Devices .................62
      14.4 Register Map Overview and Default Settings Values .................63
  15. Si5391A/B Register Map .......................... 64
      15.1 Page 0 Registers Si5391 ..........................64
      15.2 Page 1 Registers Si5391 ..........................73
      15.3 Page 2 Registers Si5391 ..........................78
      15.4 Page 3 Registers Si5391 ..........................84
      15.5 Page 9 Registers Si5391 ..........................87
      15.6 Page A Registers Si5341 ..........................89
  16. 15.7 Page B Registers Si5391 ..........................91
      16. Revision History............................. 93

## 1. Work Flow Using ClockBuilder Pro and the Register Map

This reference manual is to be used to describe all the functions and features of the parts in the product family with register map details on how to implement them. It is important to understand that the intent is for customers to use the ClockBuilder Pro to provide the initial configuration for the device. Although the register map is documented, all the details of the algorithms to implement a valid frequency plan are fairly complex and are beyond the scope of this document. Real-time changes to the frequency plan and other operating settings are supported by the devices. However, describing all the possible changes is not a primary purpose of this document. Refer to the applications notes within the ClockBuilder Pro GUI for information on how to implement the most common, real-time frequency plan changes.

The primary purpose of the software is to enable use of the device without an in-depth understanding of its complexities. The software abstracts the details from the user to allow focus on the high level input and output configuration, making it intuitive to understand and configure for the end application. The software walks the user through each step, with explanations about each configuration step in the process to explain the different options available. The software will restrict the user from entering an invalid combination of selections. The final configuration settings can be saved, written to an EVB and a custom part number can be created for customers who prefer to order a factory preprogrammed device. The final register maps can be exported to text files, and comparisons can be done by viewing the settings in the register map described in this document.

### 1.1 Field Programming

To simplify design and software development of systems using the Si5391/Si5391P, a field programmer is available in addition to the evaluation board. The ClockBuilder Pro Field Programmer supports both “in-system” programming (for devices already mounted on a PCB), as well as “in-socket” programming of Si5391/Si5391P sample devices. Refer to https://www.skyworksinc.com/en/Products/Timing for information about this kit.

## 2. Family Product Comparison

The following table is a comparison of the different parts in the product family showing the differences in the inputs, MultiSynths, outputs and package type.

### Table 2.1. Family Feature Comparison

| Part Number | Number of Inputs | Number of Fractional Dividers | Number of Outputs | Package Type |
| ----------- | ---------------- | ----------------------------- | ----------------- | ------------ |
| Si5391      | 4                | 5                             | 12                | 64-pin QFN   |

### 2.1 Grade P (Precision) Restrictions and Requirements

Some applications like 56G PAM4 SERDES require even higher performance than is already provided by standard clock generators.

The Si5391P (Precision) grade internally calibrates out linearity errors to deliver the world's best jitter performance for output clocks of 156.25, 312.5, and 625 MHz frequencies. The grade 'P' part XTAL frequency is fixed at 48 MHz and variation must be within ±100 ppm across temperature, load capacitance mismatch and aging. The P (Precision) grade part has various restrictions compared to the highly flexible A grade device. These restrictions are required to guarantee the 100-fs integrated jitter specification in the 12kHz-20MHz frequency band for 156.25MHz, 312.5MHz, and 625MHz output frequencies.

This section identifies most of the restrictions/rules required to achieve &#x3C;100 fs jitter.

### 2.2 Si5391P Grade Frequency Plan Rules

In order to achieve &#x3C;100 fs jitter on the 156.25/312.5/625 output clocks there are various restrictions/rules that must be met regarding output clock placement, format, and separation. The following restrictions/rules and a few more are implemented in CBPro with visual feedback so that it is simple to develop a plan that guarantees &#x3C;100 fs jitter on the 156.25/312.5/625 MHz output clocks. A 156.25/312.5/625 MHz output will be labeled by CBPro as “Precision” when it will achieve less than 100 fs jitter.

#### 2.2.1 Output Clock Domains

The Si5391P is only allowed to output a fixed set of frequencies. These frequencies are grouped into 3 clock domains.

- Domain1: 125/156.25/312.5/625 MHz
- Domain2: 25/50/100/125/200 MHz
- Domain3: 322.265625/644.53125 MHz

125 MHz is a part of domain 1 and domain 2 because 125 MHz does not cause any crosstalk issues with the 156.25/312.5/625 MHz outputs. Therefore, a 125 MHz output clock can be placed on any output location.

#### 2.2.2 Output Clock Locations

The following are the clock locations to achieve &#x3C; 100 fs jitter on the 156.25/312.5/625 MHz outputs. Additional rules that create gaps between domain 1 clock locations and domain 2&#x26;3 locations are enforced by CBPro.

If Only Domain 1 Output Frequencies are Present:

Domain 1 frequencies can be placed in any output location and achieve &#x3C;100 fs jitter on the 156.25/312.5/625 MHz outputs.

If Domain 1 as well as Domain 2 or 3 Output Frequencies are Present:

If only domain 1 and 2 output frequencies are present, then Table 2.2 applies. If domain 1, 2, and 3 output frequencies are present, then Table 2.3 applies. If only domain 1 and 3 output frequencies are present, then Table 2.4 applies.

##### table 2.2 Only Domain 1 and 2 Output Frequencies

|                          | **Output Clock Location allowed?** |      |      |      |      |      |      |      |      |      |      |
| ------------------------ | ---------------------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Output Clock Frequencies | 0A                                 | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9A   |
| 125/156.25/312/625       | yes                                | yes  | yes  | yes  | yes  | yes  | yes  | no   | no   | no   | no   |
| 25/125/200               | no                                 | no   | no   | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  |
| 50/100                   | no                                 | no   | no   | no   | yes  | yes  | yes  | yes  | yes  | yes  | yes  |

##### table 2.3 Domain 1, 2, and 3 Output Frequencies

|                          | Output Clock Location allowed? |      |      |      |      |      |      |      |      |      |      |      |
| ------------------------ | ------------------------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Output Clock Frequencies | 0A                             | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 9A   |
| 125/156.25/312/625       | yes                            | yes  | yes  | yes  | yes  | yes  | yes  | no   | no   | no   | no   | no   |
| 25/125/200               | no                             | no   | no   | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  |
| 50/100                   | no                             | no   | no   | no   | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  |
| 322.265625/644.53125     | no                             | no   | no   | no   | no   | no   | no   | no   | yes  | yes  | yes  | yes  |

##### table 2.4 Only Domain 1 and 3 Output Frequencies

|                          | Output Clock Location allowed? |      |      |      |      |      |      |      |      |      |      |      |
| ------------------------ | ------------------------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Output Clock Frequencies | 0A                             | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 9A   |
| **125**                  | yes                            | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  | yes  |
| **156.25/312/625**       | yes                            | yes  | yes  | yes  | no   | no   | no   | no   | no   | no   | no   | no   |
| **322.265625/644.53125** | no                             | no   | no   | no   | no   | no   | no   | no   | no   | no   | yes  | yes  |

156.25MHz/312.5MHz/625MHz Separation Rules to Domain 2 and 3 Clocks:

Even though the Si5391P has minimal coupling between adjacent clocks, a domain 2 or 3 clock that is adjacent to 156.25/312.5/625 MHz may couple too much energy to allow these Domain 1 clocks to meet &#x3C;100 fs clocks. Therefore domain 2 and 3 clocks must be isolated from 156.25/312.5/625 MHz outputs. In addition to the tables above, ClockBuilder Pro enforces gaps between domain 1 and domain 2 outputs. ClockBuilder Pro makes it simple to achieve 156.25/312.5/625 MHz outputs that are guaranteed to have &#x3C;100 fs rms jitter. Only when the output clock locations meet all the rules, ClockBuilder Pro will classify a 156.25/312.5/625 MHz output as being "precision" and guaranteed to achieve &#x3C;100fs rms jitter.

#### 2.2.3 Output Clock Format Restrictions

For the 156.25/312.5/625 MHz clocks to achieve &#x3C; 100 fs jitter there are restrictions on the output formats as follows:

1. 156.25/312.5/625 MHz clocks can only be LVPECL or LVDS.
2. Domain 2 outputs can only be LVPECL, LVDS or HCSL.
3. Domain 3 outputs can only be LVPECL or LVDS.
4. If any domain 2 or 3 output is LVPECL or HCSL, then 156.25/312.5/625 MHz outputs must be LVPECL.

## 3. Functional Description

The Si5391 uses next generation MultiSynth™ technology to offer the industry’s most frequency-flexible, high performance clock generator. The internal Phase-Locked Loop (PLL) locks to either an external crystal (XA/XB) or to an external input on XAXB, IN0, IN1 or IN2. The input frequency (crystal or external input) is multiplied by the PLL and divided by the MultiSynth™ stage (N divider) and R divider to any frequency in the range of 100 Hz to 712.5 MHz per output. The PLL is fully contained and does not require external loop filter components to operate. Its function is to phase lock to the selected input and provide a common reference to all the output MultiSynth high-performance fractional dividers (N dividers). The high-resolution fractional MultiSynth™ dividers enable true any-frequency input to any-frequency output. A cross-point mux connects any of the MultiSynth divided frequencies to any of the output drivers. Additional integer output dividers (R) provide further frequency division if required. The frequency configuration of the device is programmed by setting the input dividers (P), the PLL feedback fractional divider (M_NUM/M_DEN), the MultiSynth fractional dividers (N_NUM/N_DEN), and the output integer dividers (R). Skyworks’ Clockbuilder Pro configuration utility determines the optimum divider values for any desired input and output frequency plan.

The output drivers offer flexible output formats which are independently configurable on each of the outputs. This clock generator is fully configurable via its serial interface (I2C/SPI) and includes in-circuit programmable non-volatile memory. The block diagram for the Si5391 is shown in the figure below.

### Figure 3.1. Si5391 Block Diagram

| A              |             | D         | D           | D       | D                    | V         | V         | 3           |
| -------------- | ----------- | --------- | ----------- | ------- | -------------------- | --------- | --------- | ----------- |
| IN\_ SEL\[1:0] | Si5391      | Dividers/ |             | Clock   | Generator            | VDDO0     | OUT0      | OUT0b       |
| IN0            | ~~÷P~~ 0    | ~~÷R~~0   | OUT0A       | OUT0Ab  | IN1                  | ~~÷P~~ 1  | PLL       | ~~÷R~~ 0A   |
| IN1b           | IN2         | ~~÷P~~ 2  | LPF         | ~~÷R~~1 | OUT1                 | OUT1b     | VDDO1     | VDDO2       |
| IN2b           | ~~÷ Mn~~    | ~~÷ Md~~  | ~~÷R~~2     | OUT2    | OUT2b                | VDDO3     | ~~÷R~~3   | OUT3        |
| OUT3b          | VDDO4       | ~~÷R~~4   | OUT4        | OUT4b   | Si5391P: 48 MHz only | XA        | ~~÷ N1n~~ | ~~÷ N1d~~ 1 |
| Zero Delay     | Mode        | ~~÷ N2n~~ | ~~÷ N2d~~ 2 | ~~÷R~~6 | OUT6                 | OUT6b     | FB\_IN    | FB\_INb     |
| ~~÷ N3n~~      | ~~÷ N3d~~ 3 | ~~÷R~~7   | OUT7        | OUT7b   | ~~÷ N4n~~            | ~~÷ N4d~~ | ~~÷R~~8   | OUT8        |
| OUT8b          | VDDO9       | ~~÷R~~9   | OUT9        | OUT9b   | OUT9A                | ~~÷R~~9A  | OUT9Ab    |             |

I2C_ SEL

SDA/ SDIO

SPI / I²C

NVM

Status

Frequency

Control

A0/CSb

Tb

Lb

FINC

Cb

OEb

S

Rb

FDEC

N

R

O

T

L

N

Y

I

S

### 3.1 Dividers

There are five main divider classes within the Si5391/Si5391P shown above in the Figure 3.1 Si5391 Block Diagram on page 8.

1. Wide range input dividers Pfb, P2, P1, P0
- Only integer divider values
- Range is from 1 to 216 – 1
- Since the input to the phase detector needs to be > 10 MHz, the practical range is limited to ~75 on the high side.
- Each divider has an update bit that must be written to cause a newly written divider value to take effect.
2. Narrow range input divider Pxaxb
- Only divides by 1, 2, 4, 8
3. Feedback M divider
- Ultra low jitter in fractional and integer modes
- MultiSynth divider
- Integer or fractional divide values
- 44 bit numerator, 32 bit denominator
- Practical range limited by phase detector range of 10–120 MHz and VCO range of 13500–14256 MHz
- This divider has an update bit that must be written to cause a newly written divider value to take effect.
4. Output N dividers
- Ultra low jitter in fractional and integer modes
- MultiSynth divider
- Integer or fractional divide values
- 44 bit numerator, 32 bit denominator
- Min value is 10
- Maximum value is 212 – 1
- Each N divider has an update bit that must be written to cause a newly written divider value to take effect. In addition there is a global update bit that when written updates all N dividers.
5. Output R divider
- Only even integer divide values
- Min value is 2
- Maximum value is 225 – 2

Additionally, FSTEPW can be used to adjust the nominal output frequency in DCO mode. See Section 10. Digitally-Controlled Oscillator (DCO) Mode (All Si5391 Devices Except Si5391P) for more information and block diagrams on DCO mode.

## 4. Power-up, Reset, and Initialization

Once power is applied, the device begins an initialization period where it downloads default register values and configuration data from NVM and performs other initialization tasks. Communicating with the device through the serial interface is possible once this initialization period is complete. No clocks will be generated until the initialization is complete.

### Figure 4.1. Initialization from Power-up, Hard Reset, and Soft Reset

|                        | Power-Up | Hard Reset | RST bit asserted |                |
| ---------------------- | -------- | ---------- | ---------------- | -------------- |
| NVM download           |          | Soft Reset | bit asserted     | Initialization |
| Serial interface ready |          |            |                  |                |

There are two types of commanded resets available.

1. The first is the hard reset. A hard reset is functionally similar to a device power-up. All registers will be restored to the values stored in NVM, and all circuits will be restored to their initial state including the serial interface. A hard reset is initiated using the RST pin or by asserting the hard reset register bit.
2. The second type of reset is a soft reset. Asserting the soft reset register bit bypasses the NVM download and simply re-starts the internal initialization sequence.

### Figure 4.2. Si5391/Si5391P Memory Configuration

NVM Download

| NVM | 2x | RAM |
| --- | -- | --- |

### Table 4.1. Reset Control Registers

| Hex Address \[Bit Field] Si5391 | Register Name | Function                                                     |
| ------------------------------- | ------------- | ------------------------------------------------------------ |
| 001E\[1]                        | HARD\_RST     | Performs the same function as power cycling the device. All registers will be restored to their default values. |
| 001C\[0]                        | SOFT\_RST     | Performs a soft reset. Resets the device while it does not re-download the register configuration from NVM. |

The Si5391/Si5391P is fully configurable using the serial interface (I2C or SPI). At power-up the device downloads its default register values from internal non-volatile memory (NVM). Application specific default configurations can be pre-written into NVM allowing the device to generate specific clock frequencies at power-up. Writing default values to NVM is in-circuit programmable with normal operating power supply voltages applied to its VDD (1.8 V) and VDDA (3.3 V) pins. Neither VDDOx or VDDS supplies are required to write the NVM.

## 5. Dynamic PLL Changes

It is possible for the PLL to become unresponsive (i.e., lose lock indefinitely) when it is dynamically reprogrammed or changed via the serial port. Any change that causes the VCO frequency to change by more than 250 ppm since Power-up, a NVM download, assertion of SOFT_RST, or changes to any of the following list of registers will require the special PLL re-initialization sequence below

### Registers:

- XAXB_FREQ_OFFSET
- PXAXB
- MXAXB_NUM
- MXAXB_DEN
- M_NUM
- M_DEN

### PLL Re-Initialization Sequence:

1. First, the preamble:
- Write 0x0B24 = 0xC0
- Write 0x0B25 = 0x00
2. Wait 300 ms for Grade A/B/C/D, Wait 625ms for Grade P
3. Then, perform the desired register modifications.
4. Write SOFT_RST - 0x001C[0] = 1
5. Write the post-amble:
- Write 0x0B24 = 0xC3
- Write 0x0B25 = 0x02

Note: This programming sequence applies only to Rev D and later revisions. The preamble and postamble values for updating certain registers during device operation are different for earlier revisions. Either the new or old values below may be written to revision D or later devices without issue. No system software changes are necessary for legacy systems. When writing old values, note that reading back these registers will not give the written old values, but will reflect the new values. Skyworks recommends using the new values for all revision D (described above) and later designs, since the write and read values will match. Please contact Skyworks if you need information about an earlier revision. Please always ensure to use the correct sequence for the correct revision of the device. Also check for the latest information online. This information is updated from time to time. The latest information is always posted online.

### 5.1 Dynamic Changes to Output Frequencies without Changing PLL Settings

This section applies to the following scenario:

1. A CBPro generated register map "was" used to program either the volatile or the non-volatile memory of a Si5391. Changes to output frequencies without changing the PLL settings are desired.
2. The CBPro project file can be used to look for the VCO frequency (FVCO), Ry, Nx values for each OUTy in the design report and/or the datasheet addendum.

OUTy = FVCO/(Nx * Ry)

Solve for Nx based on the desired OUTy. The Nx dividers can be digitally controlled to so that all outputs connected to the Nx divider change frequency in real time without any transition glitches. There are two ways to control the Nx divider to accomplish this task:

1. Use the Frequency Increment/Decrement Pins or register bits.
2. Write directly to the numerator or denominator of the Nx divider.

The details of both methods are covered in 10.1 Using the N Dividers for DCO Applications.

### 5.2 Dynamic Changes to Output Frequencies while Changing PLL Settings Using a CBPro Register Map

This section applies to the following scenario:

1. A CBPro generated register map "is" used to program either the volatile or the non-volatile memory of a Si5391.
2. This needs a register write sequence provided in the CBPro export section as shown below.

#### Figure 5.1. CBPro Register Write Sequence While Changing PLL Settings

Si5391 Export

Open Sample Project - ClockBuilder Pro

Introduction Register File Settings File Multi-Project Register /Settings Regmap

ClockBuilderPro V4.1.5.100 Do

This export will contain the registers that need to be written to the Si5391 to achieve your design/configuration:

CBProProjectRegistersExport --help from command line version of this tool is available: Type command prompt to learn more:

Options

Step 1 of 11 Design ID &#x26; Notes

Loaded sample design 5391AEVB. You can review or edit the configuration by clicking link in the "Edit Configuration" section below or using the pulldown step menu above:

Edit Configuration with Wizard

No EVB Present

No evaluation board has been connected/power; including USB cable

Export Type:

Comma Separated Values (CSV) File

Each line in the file is an address, data pair in hexadecimal format; comma separates the address and data fields:

C Code Header File

The register write sequence is expressed in C code via an array of address, data pairs. This can be used directly in firmware code.

Include summary header

If checked; an informational header will be included at the top of the file: Each line in the header will be prefixed by the character. The header will contain some basic information about the design; tool; and timestamp:

Include pre and post-write control register writes:

Certain control registers must be written before and after writing the volatile configuration. This ensures the device is stable during configuration download and resumes normal operation after the download is complete: You can turn inclusion of this sequence off if your host system is managing this process already:

Design Report &#x26; Datasheet Addendum

Documentation

You can view design report (text) or create draft datasheet addendum (PDE) for your design:

- Si5391 Reference Manual
- Si5391 Data Sheet
- Si5391 EVB User's Guide

Silicon Labs Cloud Services

Ask for Help

You can create custom part number for your design; which can be used to order factory pre-programmed devices or request a phase noise report for this design:

Frequency Plan Valid Design OK

Typical Pd 1.35 W; Tj 48 *

Preview Export

Save to File

## 6. NVM Programming

Devices have two categories of non-volatile memory: user NVM and Factory (Skyworks) NVM. Each type is segmented into NVM banks. There are three NVM banks, one of which is used for factory programming (whether a base part or an Orderable Part Number). Two user NVM banks remain; therefore, the device NVM can be re-burned in the field up to two times. Factory NVM cannot be modified, and contains fixed configuration information for the device.

The ACTIVE_NVM_BANK device setting can be used to determine which user NVM bank is currently being used and therefore how many banks, if any, are available to burn. The following table describes possible values:

### Table 6.1. NVM Bank Burning Values

| Active NVM BANK Value (Decimal) | Number of User Banks Burned | Number of User Banks Available to Burn |
| ------------------------------- | --------------------------- | -------------------------------------- |
| 3 (factory state)               | 1                           | 2                                      |
| 15                              | 2                           | 1                                      |
| 63                              | 3                           | 0                                      |

Note: While polling DEVICE_READY during the procedure below, the following conditions must be met to ensure the correct values are written into the NVM:

- VDD and VDDA power must both be stable throughout the process.
- No additional registers may be written or read during DEVICE_READY polling. This includes the PAGE register at address 0x01. DEVICE_READY is available on every register page, so no page change is needed to read it.
- Only the DEVICE_READY register (0xFE) should be read during this time.

The procedure for writing registers into NVM is as follows:

1. Write registers as needed for desired device operation. Verify device operation to ensure the device is configured correctly before proceeding. Do not skip this important step.
2. You may write to the user scratch space (Registers 0x026B to 0x0272 DESIGN_ID0-DESIGN_ID7) to identify the contents of the NVM bank.
3. Write 0xC7 to NVM_WRITE register. This starts the internal NVM burn sequence, writing NVM from the internal registers. Do not access ANY other registers than DEVICE_READY during the NVM burn process. Doing so may corrupt the NVM burn in progress.
4. Poll DEVICE_READY until DEVICE_READY=0x0F (waiting for completion of NVM burn sequence).
5. Set NVM_READ_BANK 0x00E4[0]=1. This will download the NVM contents back into non-volatile memory (registers).
6. Poll DEVICE_READY until DEVICE_READY=0x0F (waiting for NVM download to complete).
7. Read ACTIVE_NVM_BANK and verify that the value is the next highest value in the table above. For example, from the factory it will be a 3. After NVM_WRITE, the value will be 15.

Alternatively, steps 5 and 6 can be replaced with a Hard Reset, either by RSTb pin, HARD_RST register bit, or power cycling the device to generate a POR. All of these actions will load the new NVM contents back into the device registers.

The ClockBuilder Pro Field Programmer kit is a USB attached device to program supported devices either in-system (wired to your PCB) or in-socket (by purchasing the appropriate field programmer socket). ClockBuilder Pro software is then used to burn a device configuration (project file). Learn more at https://www.skyworksinc.com/en/products/timing/evaluation-kits/general/clockbuilder-pro-field-programmer.

### Table 6.2. NVM Programming Registers

| Register Name     | Hex Address  | Function                                             |
| ----------------- | ------------ | ---------------------------------------------------- |
| ACTIVE\_NVM\_BANK | 0x00E2\[7:0] | Identifies the active NVM bank.                      |
| NVM\_WRITE        | 0x00E3\[7:0] | Initiates an NVM write when written with value 0xC7. |
| NVM\_READ\_BANK   | 0x00E4\[0]   | Download register values with content stored in NVM. |

| Register Name | Hex Address  | Function                                                     |
| ------------- | ------------ | ------------------------------------------------------------ |
| DEVICE\_READY | 0x00FE\[7:0] | Indicates that the device is ready to accept commands when value = 0x0F. |

Warning: Any attempt to read or write any register other than DEVICE_READY before DEVICE_READY reads as 0x0F may corrupt the NVM programming and may corrupt the register contents, as they are read from NVM. Note that this includes accesses to the PAGE register.

## 7. Clock Inputs

Clock inputs can be used on all Si5391 grades except for Si5391P. The PLL in the Si5391 (not P grade) requires a clock input at the XAXB pins or IN2, 1, 0 input pins or a clock from a crystal connected across the XAXB pins. The PLL of the Si5391P requires a 48 MHz crystal, not input clock, connected at the XAXB pins and does not use the IN0, 1, 2 inputs.

### Figure 7.1. Clock Inputs Example

| A                    | D         | D         | D        | D         | V          | V       | 3     |         |      |       |
| -------------------- | --------- | --------- | -------- | --------- | ---------- | ------- | ----- | ------- | ---- | ----- |
| IN\_ SEL\[1:0]       | Si5391    | Dividers/ | Clock    | Drivers   |            |         |       |         |      |       |
| IN0                  | ~~÷P~~    | 0         | ~~÷R~~0  | OUT0      | OUT0b      |         |       |         |      |       |
| IN1                  | ~~÷P~~    | 1         | PLL      | ~~÷R~~0A  | OUT0A      |         |       |         |      |       |
| IN1b                 | PD        | OUT0Ab    |          |           |            |         |       |         |      |       |
| IN2                  | ~~÷P~~    | VDDO1     | 2        | LPF       | ~~÷R~~1    | OUT1    |       |         |      |       |
| IN2b                 | OUT1b     |           |          |           |            |         |       |         |      |       |
| ÷ Mn                 | VDDO2     | M         | ~~÷R~~   | OUT2      | OUT2b      |         |       |         |      |       |
| VDDO3                | ÷ PXAXB   | ~~÷R~~3   | OUT3     | OUT3b     |            |         |       |         |      |       |
| 25-54 MHz            | ÷ N0n     | ~~t~~     | VDDO4    | XTAL      | OSC        | N0d     | 0     | ~~÷R~~4 | OUT4 | OUT4b |
| Si5391P: 48 MHz only | XA        | ÷ N1n     | ~~t~~    | VDDO5     | Zero Delay | N1d     | 1     | ~~÷R~~5 | OUT5 | OUT5b |
|                      | ÷ N2n     | ~~t~~     | VDDO6    | N2d       | 2          | ~~÷R~~6 | OUT6  | OUT6b   |      |       |
| FB\_IN               | ÷Pfb      | OUT6b     |          |           |            |         |       |         |      |       |
| FB\_ INb             | ÷ N3n     | ~~t~~     | VDDO7    | N3d       | 3          | ~~÷R~~7 | OUT7  | OUT7b   |      |       |
|                      | ÷ N4n     | ~~t₄~~    | VDDO8    | N4d       | ~~÷R~~8    | OUT8    | OUT8b |         |      |       |
| VDDO9                | ~~÷R~~9   | OUT9      | OUT9b    |           |            |         |       |         |      |       |
| I2C\_ SEL            | SDA/ SDIO | SPI /     | ~~÷R~~9A | OUT9A     |            |         |       |         |      |       |
| A1/ SDO              | I²C       | NVM       | Status   | Frequency | OUT9Ab     |         |       |         |      |       |
| SCLK                 | Monitors  | Control   |          |           |            |         |       |         |      |       |
| A0/CSb               | Tb        | Lb        | FINC     | Cb        | OEb        |         |       |         |      |       |
| S                    | R         | b         | FDEC     | N         |            |         |       |         |      |       |
| R                    | O         | T         | L        | NI        | Y          |         |       |         |      |       |
| S                    |           |           |          |           |            |         |       |         |      |       |

### 7.1 Reference Input Selection (IN0, IN1, IN2, XA/XB)

The active clock input is selected using the IN_SEL1,0 pins or by register control. The register bit IN_SEL_REGCTRL determines input selection as pin or register selectable.

Note: If the selected input does not have a clock, all output clocks will be shut off (squelched) until a valid input clock is present.

#### Table 7.1. Manual Input Selection Using IN_SEL[1:0] Pins

| IN\_SEL\[1:0] | Selected Input |
| ------------- | -------------- |
| 0 0           | IN0            |
| 0 1           | IN1            |
| 1 0           | IN2            |
| 1 1           | XA/XB          |

#### Table 7.2. Input Control Registers

| Register Name       | Hex Address \[Bit Field] | Function                                                                                                                                                                                        |
| ------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| XAXB\_FREQ\_OFFSET1 | 0202\[7:0]–0205\[7:0]    | 1. Do NOT use this register on any version of the Si5391.                                                                                                                                       |
| XAXB\_EXTCLK\_EN    | 090E\[0]                 | Selects between the XTAL or external reference clock on the XA/XB pins. Default is 0, XTAL. Set to 1 to use an external reference oscillator. It must always be set to 0 (default) for Si5391P. |
| IN\_SEL\_REGCTRL    | 0021\[0]                 | Determines pin or register clock input selection.                                                                                                                                               |
| IN\_SEL             | 0021\[2:1]               | Selects the input when in register input selection mode.                                                                                                                                        |
| IN\_EN              | 0949\[3:0]               | Allows enabling/disabling IN0, IN1, IN2 and FB\_IN when not in use.                                                                                                                             |

#### Table 7.3. XAXB Pre-Scale Divide Ratio Register

| Setting Name | Hex Address \[Bit Field] | Function                                                        |
| ------------ | ------------------------ | --------------------------------------------------------------- |
| PXAXB        | 0x0206\[1:0]             | Sets the XAXB input divider value according to the table below. |

The following table lists the values, along with the corresponding divider ratio.

#### Table 7.4. XAXB Pre-Scale Divide Values

| Value (Decimal) | PXAXB Divider Value |
| --------------- | ------------------- |
| 0               | 1                   |
| 1               | 2                   |
| 2               | 4                   |
| 3               | 8                   |

### 7.2 Types of Inputs

#### 7.2.1 Crystal on XA/XB

An external standard crystal (XTAL) is connected to XA/XB when this input is configured as a crystal oscillator. For all Si5391 devices, except the Si5391P, a crystal frequency of 25 MHz can be used, although crystals in the frequency range of 48 MHz to 54 MHz are highly recommended for the best jitter performance. All Si5391 devices, except Si5391P, include a built-in XTAL load capacitance (CL) of 8 pF, but crystals with CL specifications as high as 18 pF can also be used. When using crystals with CL specs higher than 8 pF it is not generally recommended to use external capacitors from XA/XB to ground to increase the crystal load capacitance. See Section 12. Crystal, XO and Device Circuit Layout Recommendations for the PCB layout guidelines.

For Si5391P devices, the crystal frequency MUST be 48 MHz and have a loading capacitance of 8 pF. No external loading capacitors are needed since the device has a built-in loading capacitance of 8 pF.

#### 7.2.2 Clock Input on XA/XB

The Si5391P must use a 48 MHz crystal on XA/XB, not a clock.

An external clock can also be input on the XA/XB pins of all Si5391 devices except the Si5391P. Selection between the external crystal or clock is controlled by register configuration. The device includes internal 8 pF crystal loading capacitors which eliminates the need for external capacitors when using a crystal. The internal crystal load capacitors (CL) are disabled in external clock mode. Because the input buffer at XA/XB is a lower noise buffer than the buffers on IN2,1,0, a very clean input clock at XA/XB, such as a very high quality TCXO or XO, will, in some cases, produce lower output clock jitter than the same input at IN2,1,0. If the XA/XB input is unused and powered down then the XA and XB inputs can be left floating. Note that ClockBuilder Pro will power down the XA/XB input if it is selected as “unused”. If XA/XB is powered up but no input is applied then the XA input should be left floating and the XB input must be connected directly to ground. Both a single-ended or a differential clock can be connected to the XA/XB pins as shown in the following figure:

##### Figure 7.2. Crystal Resonator and External Reference Clock Connection Options

| Differential Connection |                         |                    |                      |     |        | Single-ended XO Connection |      |
| ----------------------- | ----------------------- | ------------------ | -------------------- | --- | ------ | -------------------------- | ---- |
| nc X1                   | nc X2                   |                    |                      |     |        | Note: 2.0 Vpp\_se max      | 2xCL |
| 0.1 μf 50               | XA                      | 0.1 μf             | XA                   |     |        |                            |      |
| 50                      | XB                      |                    | XO with Clipped Sine |     | 0.1 μf |                            |      |
| 0.1 μf                  | 2xCL                    | Si5391 Wave Output | 2xCL Si5391          |     |        |                            |      |
| Note: 2.5 Vpp diff max  | Single-ended Connection |                    |                      |     |        |                            |      |
|                         | nc X1                   | nc X2              |                      |     |        |                            |      |
| CMOS/XO Output          | Note: 2.0 Vpp\_se max   |                    | 2xCL                 |     |        | X1                         |      |
|                         | R1                      | 0.1 μf             | XA                   | OSC |        |                            |      |
| L                       | XO VDD                  | R1                 |                      |     |        |                            |      |
| 3.3 V                   | 523 Ohms                | 422 Ohms           | 0.1 μf               |     |        |                            |      |
| 2.5 V                   | 475 Ohms                | 649 Ohms           |                      |     |        |                            |      |
| 1.8 V                   | 158 Ohms                | 866 Ohms           |                      |     |        |                            |      |

In addition to crystal operations, the Si5391 accepts a clipped sine wave, CMOS, or differential reference clock on the XA/XB interface. Most clipped sine wave and CMOS TCXOs have insufficient drive strength to drive a 100 Ω or 50 Ω load. For this reason, place the TCXO as close to the Si5391 as possible to minimize PCB trace length. In addition, ensure that both the Si5391 and the TCXO are both connected directly to the ground plane. The above figure includes the recommended method of connecting a clipped sine wave TCXO to the Si5391. Because the Si5391 provides DC bias at the XA and XB pins, the ~800 mV peak-peak swing can be input directly into the XA interface of the Si5391 once it has been ac-coupled.

The above figure also illustrates the recommended method of connecting a CMOS rail-to-rail output to the XA/XB inputs of the Si5391. Because the signal is single-ended, the XB input is ac-coupled to ground. The resistor network attenuates the rail-to-rail output swing to ensure that the maximum input voltage swing at the XA pin is less than the data sheet specification. The signal is ac-coupled before connecting it to the Si5391 XA input. Again, since the signal is single-ended, the XB input should be ac-coupled to ground.

If an external oscillator is used as the XA/XB reference, it is important to use a low jitter source because there is effectively no jitter attenuation from the XA/XB pins to the outputs. To minimize jitter at the XA/XB pins, the rise time of the XA/XB signals should be as fast as possible.

Si5391 Reference Manual • Clock Inputs

For best jitter performance, use a XAXB frequency above 40 MHz. Also, for XAXB frequencies higher than 125 MHz, the PXAXB control must be used to divide the input frequency down below 125 MHz.

In most applications, using the internal OSC with an external crystal provides the best phase noise performance. See AN905: External References; Optimizing Performance for more information on the performance of various XO's with these devices.

The recommended crystal and oscillator suppliers are listed in the Si534x/8x Jitter Attenuators Recommended Crystal, TCXO and OCXOs Reference Manual.

#### 7.2.3 Clock Inputs on IN2, IN1, IN0

This section applies to all Si5391 devices except the Si5391P. The Si5391P cannot accept an input clock on IN0,1, 2.

A single ended or differential clock may be input to the IN2, 1, 0 inputs as shown below. All input signals must be ac-coupled. When INx (x = 0, 1, 2) is unused and powered down the plus and minus input can be left floating. ClockBuilder Pro will power down any INx input that is selected as “unused.” If any INx is powered up but does not have any input signal then the plus input should be left floating and the minus input should be directly connected to ground. If the plus input is left floating and the minus input is connected to ground with a 4.7 kΩ or smaller resistor, then the INx can be powered up or down when it does not have an input. The recommended input termination schemes are shown in the figure below. Unused inputs can be disabled by register configuration.

##### Figure 7.3. Terminations for Differential and Single-Ended Inputs

Standard AC-Coupled Differential

0.1uF *

| 50  | Clock IC |
| --- | -------- |
| 100 | INx      |
| 50  | INxb     |

LVDS, LVPECL, CML 0.1uF *

* These caps should have &#x3C; ~5 ohms capacitive reactance at the clock input frequency.

Standard AC-Coupled Single-Ended

| C1 | RS                      | 50 | R1   | 0.1uF | INx | Standard | Clock IC |
| -- | ----------------------- | -- | ---- | ----- | --- | -------- | -------- |
|    | 3.3V, 2.5V, 1.8V LVCMOS | R2 | INxb |       |     |          |          |

RS matches the CMOS driver to a 50 ohm transmission line (if used)

0.1uF *

**

*This cap should have less than ~20 ohms of capacitive reactance at the clock input frequency.

** Only when 3.3V LVCMOS driver is present, use R2 = 845 ohm and R1 = 267 ohm if needed to keep the signal at INx &#x3C; 3.6 Vpp_se. Including C1 = 6 pf may improve the output jitter due to faster input slew rate at INx. If attenuation is not needed for Inx&#x3C;3.6Vppse, make R1 = 0 ohm and omit C1, R2 and the capacitor below R2. C1, R1, and R2 should be physically placed as close as practicle to the device input pins.

#### 7.2.4 Unused Inputs

Unused inputs can be disabled and left unconnected. Register 0x0949[3:0] defaults the input clocks to being enabled. Clearing the unused input bits will disable them. Enabled inputs not actively being driven by a clock may benefit from pull up or pull down resistors to avoid them responding to system noise.

#### 7.2.5 Input Clock Rise Time Considerations

It is well known that slow rise time input clocks with low slew rates are a cause of increased jitter. If the slew rate is low enough, the output jitter will increase. The following figure shows the effect of a low slew rate on RMS jitter for a differential clock input. It shows the relative increase in the amount of RMS jitter due to slow rise time and is not intended to show absolute jitter values.

#### Figure 7.4. Effect of Low Slew Rate on RMS Jitter

| IN\_X Slew Rate in Differential Mode |                   |
| ------------------------------------ | ----------------- |
| Jitter Relative                      | Input Slew (V/us) |
| 5                                    | 0                 |
| 4.5                                  | 100               |
| 4                                    | 200               |
| 3.5                                  | 300               |
| 3                                    | 400               |
| 2.5                                  | 500               |
| 2                                    | 600               |
| 1.5                                  |                   |
| JTYP 1                               |                   |
| 0.5                                  |                   |
| 0                                    |                   |

### 7.3 Fault Monitoring

The Si5391 provides fault indicators which monitor loss of signal (LOS) of the inputs (IN0, IN1, IN2, XA/XB, FB_IN) and loss of lock (LOL) for the PLL, as shown in the diagram below. These fault conditions, as well as other internal status indications, are provided through a combination of internal registers and externally provided signals (LOLb and INTRb). Usage and configuration of status/fault monitoring features, as well as mapping these to the INTRb output, are described on following sub sections.

#### Figure 7.5. Fault Monitors

| IN0     | ~~÷P~~ | ~~LOS0~~ | Si5391 |
| ------- | ------ | -------- | ------ |
| IN0b    | 0      |          | LOL    |
| IN1     | ~~÷P~~ | ~~LOS1~~ |        |
| IN1b    | 1      |          |        |
| IN2     | ~~÷P~~ | ~~LOS2~~ | PD LPF |
| IN2b    | 2      |          |        |
| XA      | OSC    |          |        |
| XB      |        |          |        |
| FB\_IN  | ÷Pfb   | LOSFB    |        |
| FB\_INb |        |          |        |
|         |        | LOLb     | INTRb  |

#### 7.3.1 Status Indicators

The state of the status monitors are accessible by reading registers through the serial interface or with dedicated pin (LOLb). Each of the status indicator register bits has a corresponding sticky bit (_FLG) in a separate register location. Once a status bit is asserted its corresponding _FLG bit will remain asserted until cleared. Writing a logic zero to a _FLG register bit clears its state.

##### Table 7.5. Status Monitor Bits

| Setting Name         | Hex Address \[Bit Field] | Function                                                     |
| -------------------- | ------------------------ | ------------------------------------------------------------ |
| Status Register Bits |                          |                                                              |
| SYSINCAL             | 0x000C\[0]               | Asserted when in calibration.                                |
| LOSXAXB              | 0x000C\[1]               | Loss of Signal at the XA input. The Xb input does not have an LOS detector. |
| LOSREF               | 0x000C\[2]               | Loss of Signal for the input that has been selected.         |
| LOL                  | 0x000C\[3]               | Loss of Lock for the PLL.                                    |
| SMBUS\_TIMEOUT       | 0x000C\[5]               | The SMB bus has a timeout.                                   |
| LOSIN\[3:0]          | 0x000D\[3:0]             | Loss of Signal for the FB\_IN, IN2, IN1, IN0 inputs.         |

| Setting Name                | Hex Address \[Bit Field] | Function                             |
| --------------------------- | ------------------------ | ------------------------------------ |
| Sticky Status Register Bits |                          |                                      |
| SYSINCAL\_FLG               | 0x0011\[0]               | Sticky bit for SYSINCAL              |
| LOSXAXB\_FLG                | 0x0011\[1]               | Sticky bit for LOSXAXB               |
| LOSREF\_FLG                 | 0x0011\[2]               | Sticky bit for LOSREF                |
| LOL\_FLG                    | 0x0011\[3]               | Sticky bit for LOL                   |
| SMBUS\_TIMEOUT\_FLG         | 0x0011\[5]               | Sticky bit for SMBUS\_TIMEOUT        |
| LOSIN\_FLG                  | 0x0012\[3:0]             | Sticky bit for FB\_IN, IN2, IN1, IN0 |

#### 7.3.2 Interrupt Pin (INTR)

An interrupt pin (INTR) indicates a change in state with any of the status indicators for any of the DSPLLs. All status indicators are maskable to prevent assertion of the interrupt pin. The state of the INTR pin is reset by clearing the sticky status registers.

##### Table 7.6. Interrupt Mask Registers

| Hex Address \[Bit Field] | Setting Name           | Function                                                         |
| ------------------------ | ---------------------- | ---------------------------------------------------------------- |
| 0x0017\[0]               | SYSINCAL\_INTR\_MSK    | 1 = SYSINCAL\_FLG is prevented from asserting the INTR pin       |
| 0x0017\[1]               | LOSXAXB\_INTR\_MSK     | 1 = LOSXAXB\_FLG is prevented from asserting the INTR pin        |
| 0x0017\[2]               | LOSREF\_INTR\_MSK      | 1 = LOSREF\_FLG is prevented from asserting the INTR pin         |
| 0x0017\[3]               | LOL\_INTR\_MSK         | 1 = LOL\_FLG is prevented from asserting the INTR pin            |
| 0x0017\[5]               | SMB\_TMOUT\_INTR\_MSK  | 1 = SMBUS\_TIMEOUT\_FLG is prevented from asserting the INTR pin |
| 0x0018\[3:0]             | LOSIN\_INTR\_MSK\[3:0] | 1 = LOS\_FLG is prevented from asserting the INTR pin            |

##### Figure 7.6. Interrupt Triggers and Masks

mask

LOSIN_FLG[0]

mask

LOSIN_FLG[1]

mask

LOSIN_FLG[2]

mask

LOSIN_FLG[3]

mask

LOSXAXB_FLG

mask

LOL_FLG

The _FLG bits are “sticky” versions of the alarm bits and will stay high until cleared. A _FLG bit can be cleared by writing a zero to the _FLG bit. When a _FLG bit is high and its corresponding alarm bit is low, the _FLG bit can be cleared.

During run time, the source of an interrupt can be determined by reading the _FLG register values and logically ANDing them with the corresponding _MSK register bits (after inverting the _MSK bit values). If the result is a logic one, then the _FLG bit will cause an interrupt.

For example, if LOS_FLG[0] is high and LOS_INTR_MSK[0] is low, then the INTR pin will be active (low) and cause an interrupt. If LOS[0] is zero and LOS_MSK[0] is one, writing a zero to LOS_MSK[0] will clear the interrupt (assuming that there are no other interrupt sources). If LOS[0] is high, then LOS_FLG[0] and the interrupt cannot be cleared.

Note: The INTR pin may toggle during reset.

## 8. Outputs

The Si5391 supports twelve differential output drivers which can be independently configured as differential or LVCMOS.

### 8.1 Output Crosspoint Switch

A crosspoint switch allows any of the output drivers to connect with any of the MultiSynths as shown in Figure 8.1 MultiSynth to Output Driver Crosspoint on page 25. The crosspoint configuration is programmable and can be stored in NVM so that the desired output configuration is ready at power up. Any MultiSynth output can connect to multiple output drivers.

#### Figure 8.1. MultiSynth to Output Driver Crosspoint

Output Crosspoint Switch

| A              | D         | D         | D                    | D         | V         | V          | 3        |
| -------------- | --------- | --------- | -------------------- | --------- | --------- | ---------- | -------- |
| IN\_ SEL\[1:0] | Si5391    | Dividers/ | Clock                | Drivers   |           |            |          |
| IN0            | Generator | VDDO0     | IN0b                 | ~~÷P~~0   | ~~÷R~~0   | OUT0       | OUT0b    |
| IN1            | ~~÷P~~1   | PLL       | ~~÷R~~0A             | OUT0A     | IN1b      | PD         | OUT0Ab   |
| IN2            | ~~÷P~~2   | LPF       | ~~÷R~~1              | OUT1      | IN2b      | OUT1b      |          |
| ÷ Mⁿ           | VDDO2     | ~~÷R~~2   | OUT2                 | OUT2b     |           |            |          |
| VDDO3          | ÷ PXAXB   | ~~÷R~~3   | OUT3                 | OUT3b     | XB        | MultiSynth |          |
| 25-54 MHz      | ÷ N⁰ⁿ     | ~~t~~     | VDDO4                | XTAL      | OSC       | N0d        | 0        |
| ~~÷R~~4        | OUT4      | OUT4b     | Si5391P: 48 MHz only | XA        | ~~÷ N¹ⁿ~~ | ~~t~~      | VDDO5    |
| Zero Delay     | N1d       | 1         | ~~÷R~~5              | OUT5      | OUT5b     |            |          |
| ~~÷ N²ⁿ~~      | ~~t~~     | VDDO6     | N2d                  | 2         | ~~÷R~~6   | OUT6       | OUT6b    |
| FB\_IN         | ÷Pfb      | OUT6b     | FB\_ INb             | ÷ N³ⁿ     | ~~t~~     | VDDO7      | N3d      |
| 3              | ~~÷R~~7   | OUT7      | OUT7b                |           |           |            |          |
| ~~÷ N⁴ⁿ~~      | ~~t₄~~    | VDDO8     | N4d                  | ~~÷R~~8   | OUT8      | OUT8b      |          |
| VDDO9          | ~~÷R~~9   | OUT9      | OUT9b                | I2C\_ SEL | SDA/ SDIO | SPI /      | ~~÷R~~9A |
| OUT9A          | A1/ SDO   | I²C       | NVM                  | Status    | Frequency | OUT9Ab     |          |
| SCLK           | Monitors  | Control   | A0/CSb               |           |           |            |          |
| Tb             | Lb        | FDEC      | Cb                   | OEb       |           |            |          |
| S              | Rb        | FINC      | N                    | R         | O         | T          | L        |
| NI             | Y         | S         |                      |           |           |            |          |

### 8.1. Output Driver Crosspoint Configuration Registers

| Setting Name    | Hex Address | Function                                                                                                             |
| --------------- | ----------- | -------------------------------------------------------------------------------------------------------------------- |
| OUT0A\_MUX\_SEL | 0106\[2:0]  | Connects the output drivers to one of the N dividers. Selections are N0, N1, N2, N3, and N4 for each output divider. |
| OUT0\_MUX\_SEL  | 010B\[2:0]  |                                                                                                                      |
| OUT1\_MUX\_SEL  | 0110\[2:0]  |                                                                                                                      |
| OUT2\_MUX\_SEL  | 0115\[2:0]  |                                                                                                                      |
| OUT3\_MUX\_SEL  | 011A\[2:0]  |                                                                                                                      |
| OUT4\_MUX\_SEL  | 011F\[2:0]  |                                                                                                                      |
| OUT5\_MUX\_SEL  | 0124\[2:0]  |                                                                                                                      |
| OUT6\_MUX\_SEL  | 0129\[2:0]  |                                                                                                                      |
| OUT7\_MUX\_SEL  | 012E\[2:0]  |                                                                                                                      |
| OUT8\_MUX\_SEL  | 0133\[2:0]  |                                                                                                                      |
| OUT9\_MUX\_SEL  | 0138\[2:0]  |                                                                                                                      |
| OUT9A\_MUX\_SEL | 013D\[2:0]  |                                                                                                                      |

### 8.2 Output Divider (R) Synchronization

All the output R dividers are reset to the default NVM register state after a power-up or a hard reset. This ensures consistent and repeatable phase alignment across all output drivers coming from the same N divider. Resetting the device using the RSTb pin or asserting the hard reset bit will have the same result. The SYNCb pin provides another method of realigning the R dividers without resetting the device. This pin is positive edge triggered. Asserting the sync register bit provides the same function. Note that using the SYNCb bit/pin guarantees that the outputs will align to within the datasheet specifications for outputs that come from the same N divider only.

### 8.3 Performance Guidelines for Outputs

Whenever a number of high frequency, fast rise time, large amplitude signals are all close to one another there will be some amount of crosstalk. The jitter generation of the Si5391/Si5391P is so low that crosstalk can become a significant portion of the final measured output jitter. Some of the crosstalk will come from the Si5391/Si5391P, and some will be introduced by the PCB. It is difficult (and possibly irrelevant) to allocate the jitter portions between these two sources since the Si5391/Si5391P must be attached to a board in order to measure jitter.

For extra fine tuning and optimization in addition to following the usual PCB layout guidelines, crosstalk can be minimized by modifying the arrangements of different output clocks. For example, consider the following lineup of output clocks in following table.

#### Table 8.2. Example of Output Clock Placement

| Output | Not Recommended (Frequency MHz) | Recommended (Frequency MHz) |
| ------ | ------------------------------- | --------------------------- |
| 0      | 155.52                          | 155.52                      |
| 1      | 156.25                          | 155.52                      |
| 2      | 155.52                          | 622.08                      |
| 3      | 156.25                          | Not used                    |
| 4      | 200                             | 156.25                      |
| 5      | 100                             | 156.25                      |
| 6      | 622.08                          | 625                         |
| 7      | 625                             | Not used                    |
| 8      | Not used                        | 200                         |
| 9      | Not used                        | 100                         |

Using this example, a few guidelines are illustrated:

1. Avoid adjacent frequency values that are close. For example, a 155.52 MHz clock should not be placed next to a 156.25 MHz clock. If the jitter integration bandwidth goes up to 20 MHz then keep adjacent frequencies at least 20 MHz apart.
2. Adjacent frequency values that are integer multiples of one another are allowed, and these outputs should be grouped together when possible. Noting that because 155.52 MHz x 4 = 622.08 MHz, it is okay to place the pair of these frequency values close to one another.
3. Unused outputs can be used to separate clock outputs that might otherwise interfere with one another.

If some outputs have tight jitter requirements while others are relatively loose, rearrange the clock outputs so that the critical outputs are the least susceptible to crosstalk. These guidelines need to be followed by those applications that wish to achieve the highest possible levels of jitter performance. Because CMOS outputs have large pk-pk swings, are single ended, and do not present a balanced load to the VDDO supplies, they generate much more crosstalk than differential outputs. For this reason, CMOS outputs should be avoided in jitter-sensitive applications. When CMOS clocks are unavoidable, even greater care must be taken with respect to the above guidelines. For more information on these issues, see application note, AN862: Optimizing Jitter Performance in Next Generation Internet Infrastructure Systems.

The ClockBuilder Pro Clock Placement Wizard is an easy way to reduce crosstalk for a given frequency plan. This feature can be accessed on the “Define Output Clocks” page of ClockBuilder Pro in the lower left hand corner of the page. It is recommended to use this tool after each project frequency plan change.

### 8.4 Output Signal Format

The differential output swing and common mode voltage are both fully programmable covering a wide variety of signal formats including LVDS, LVPECL, and HCSL. For CML applications, see Section 8.4.9 Setting the Differential Output Driver to Non-Standard Amplitudes. The differential formats can be either normal or low power. Low power format uses less power for the same amplitude but has the drawback of slower rise/fall times. The source impedance in low power format is much higher than 100 Ω. See Section 8.4.9 Setting the Differential Output Driver to Non-Standard Amplitudes for register settings to implement variable amplitude differential outputs. In addition to supporting differential signals, any of the outputs can be configured as LVCMOS (3.3, 2.5, or 1.8 V) drivers providing up to 8 (for the Si5391) single-ended outputs, or any combination of differential and single-ended outputs. Note also that CMOS output can create much more crosstalk than differential outputs so extra care must be taken in their pin replacement so that other clocks that need the lowest jitter are not on nearby pins. See AN862: Optimizing Jitter Performance in Next Generation Internet Infrastructure Systems for additional information.

#### Table 8.3. Output Signal Format Control Registers

| Setting Name  | Hex Address \[Bit Field] | Function                                                                                                               |
| ------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| OUT0A\_FORMAT | 0104\[2:0]               | Selects the output signal format as normal differential, low power differential, in phase CMOS, or complementary CMOS. |
| OUT0\_FORMAT  | 0109\[2:0]               |                                                                                                                        |
| OUT1\_FORMAT  | 010E\[2:0]               |                                                                                                                        |
| OUT2\_FORMAT  | 0113\[2:0]               |                                                                                                                        |
| OUT3\_FORMAT  | 0118\[2:0]               |                                                                                                                        |
| OUT4\_FORMAT  | 011D\[2:0]               |                                                                                                                        |
| OUT5\_FORMAT  | 0122\[2:0]               |                                                                                                                        |
| OUT6\_FORMAT  | 0127\[2:0]               |                                                                                                                        |
| OUT7\_FORMAT  | 012C\[2:0]               |                                                                                                                        |
| OUT8\_FORMAT  | 0131\[2:0]               |                                                                                                                        |
| OUT9\_FORMAT  | 0136\[2:0]               |                                                                                                                        |
| OUT9A\_FORMAT | 013B\[2:0]               |                                                                                                                        |

#### 8.4.1 Differential Output Terminations

The differential output drivers support both ac and dc-coupled terminations as shown in the following figure.

##### Figure 8.2. Supported Differential Output Terminations

| DC Coupled LVDS               |                   | AC Coupled CML |         |
| ----------------------------- | ----------------- | -------------- | ------- |
| LVDS: VDDO = 3.3V, 2.5V, 1.8V | VDDO = 3.3V, 2.5V | 50             | 50      |
| OUTx                          | 50                | OUTx           | 50      |
| OUTxb                         | 100               | OUTxb          |         |
| 50                            |                   | 50             | 0.1uF\* |

| AC Coupled LVDS/LVPECL        |                         | AC Coupled HCSL |          |
| ----------------------------- | ----------------------- | --------------- | -------- |
| LVDS: VDDO = 3.3V, 2.5V, 1.8V | VDDO = 3.3V, 2.5V, 1.8V | VDDRX           |          |
| LVPECL: VDDO = 3.3V, 2.5V     | OUTx                    | 0.1uF\*         | 50       |
| OUTxb                         | 50                      | Internally      |          |
|                               | self-biased             | OUTxb           | 50       |
|                               | 0.1uF\*                 | Standard        | HCSL     |
|                               | R1                      | R1              |          |
|                               | R2                      | R2              | Receiver |
| For VCM = 0.35 V              |                         | VDDRX           |          |
| 3.3 V                         | 442                     | 56.2            |          |
| 2.5 V                         | 332                     | 59.0            |          |
| 1.8 V                         | 243                     | 63.4            |          |

*All caps should have &#x3C; 5 ohms capacitive reactance at the clock output frequency

#### 8.4.2 Differential Output Swing Modes

There are two selectable differential output swing modes: Normal and High (also called low power mode). Each output can support a unique mode.

Differential Normal Swing Mode

This is the usual selection for differential outputs and should be used, unless there is a specific reason to do otherwise. When an output driver is configured in normal swing mode, its output swing is selectable as one of 7 settings ranging from 200 mVppse to 800 mVppse in increments of 100 mV. Differential Output Voltage Swing Control Registers lists the registers that control the output voltage swing. The output impedance in the Normal Swing Mode is 100 Ω differential. Any of the terminations shown in Figure 8.2 Supported Differential Output Terminations on page 29 are supported in this mode.

Differential High Swing Mode

When an output driver is configured in high swing mode, its output swing is configurable as one of 7 settings ranging from 400 mVppse to 1600 mVppse in increments of 200 mV. The output driver is in high impedance mode and supports standard 50 Ω PCB traces. Any of the terminations shown in Figure 8.2 Supported Differential Output Terminations on page 29 are supported. The use of High Swing mode will result in larger pk-pk output swings that draw less power. The trade off will be slower rise and fall times.

Vppdiff is 2 x Vppse as shown below.

##### Figure 8.3. Vpp_se and Vpp_diff

OUTx                Vcm               Vpp_se  Vcm                    Vpp_diff = 2*Vpp_se

Vcm               Vpp_se
OUTx

##### Table 8.4. Differential Output Voltage Swing Control Registers

| Setting Name | Hex Address \[Bit Field] | Function                                                     |
| ------------ | ------------------------ | ------------------------------------------------------------ |
|              | Si5391/Si5391P           |                                                              |
| OUT0A\_AMPL  | 0105\[6:4]               | Sets the voltage swing (amplitude) for the differential output drivers when in |
| OUT0\_AMPL   | 010A\[6:4]               | Normal differential format and Low Power differential format (Table 8.10 Settings for LVDS, LVPECL, and HCSL on page 34). |
| OUT1\_AMPL   | 010F\[6:4]               |                                                              |
| OUT2\_AMPL   | 0114\[6:4]               |                                                              |
| OUT3\_AMPL   | 0119\[6:4]               |                                                              |
| OUT4\_AMPL   | 011E\[6:4]               |                                                              |
| OUT5\_AMPL   | 0123\[6:4]               |                                                              |
| OUT6\_AMPL   | 0128\[6:4]               |                                                              |
| OUT7\_AMPL   | 012D\[6:4]               |                                                              |
| OUT8\_AMPL   | 0132\[6:4]               |                                                              |
| OUT9\_AMPL   | 0137\[6:4]               |                                                              |
| OUT9A\_AMPL  | 013C\[6:4]               |                                                              |

#### 8.4.3 Programmable Common Mode Voltage for Differential Outputs

The common mode voltage (VCM) for the differential Normal and High Swing modes is programmable in 100 mV increments from 0.7 to 2.3 V depending on the voltage available at the output's VDDO pin. Setting the common mode voltage is useful when dc coupling the output drivers. High swing mode may also cause an increase in the rise/fall time.

##### Table 8.5. Differential Output Common Mode Voltage Control Registers

| Setting Name | Hex Address \[Bit Field] | Function                                                     |
| ------------ | ------------------------ | ------------------------------------------------------------ |
|              | Si5391/Si5391P           |                                                              |
| OUT0A\_CM    | 0105\[3:0]               | Sets the common mode voltage for the differential output driver. |
| OUT0\_CM     | 010A\[3:0]               | See Table 8.10 Settings for LVDS, LVPECL, and HCSL on page 34 for more information. |
| OUT1\_CM     | 010F\[3:0]               |                                                              |
| OUT2\_CM     | 0114\[3:0]               |                                                              |
| OUT3\_CM     | 0119\[3:0]               |                                                              |
| OUT4\_CM     | 011E\[3:0]               |                                                              |
| OUT5\_CM     | 0123\[3:0]               |                                                              |
| OUT6\_CM     | 0128\[3:0]               |                                                              |
| OUT7\_CM     | 012D\[3:0]               |                                                              |
| OUT8\_CM     | 0132\[3:0]               |                                                              |
| OUT9\_CM     | 0137\[3:0]               |                                                              |
| OUT9A\_CM    | 013C\[3:0]               |                                                              |

#### 8.4.4 LVCMOS Output Terminations

LVCMOS outputs are dc-coupled as shown in Figure 8.4 LVCMOS Output Terminations on page 31.

##### Figure 8.4. LVCMOS Output Terminations

DC Coupled LVCMOS

VDDO = 3.3V, 2.5V, 1.8V

LVCMOS

OUTx

Rs

OUTx

Rs

#### 8.4.5 LVCMOS Output Impedance and Drive Strength Selection

Each LVCMOS driver has a configurable output impedance to accommodate different trace impedances and drive strengths. A source termination resistor is recommended to help match the selected output impedance to the trace impedance. There are three programmable output impedance selections for each VDDO option as shown below. The value for the OUTx_CMOS_DRIVE bits are given.

##### Table 8.6. Output Impedance and Drive Strength Selections

| VDDO  | OUTx\_CMOS\_DRV | Source Impedance (ZS) |
| ----- | --------------- | --------------------- |
| 3.3 V | 0x01            | 38 Ω                  |
|       | 0x02            | 30 Ω                  |
|       | 0x031           | 22 Ω                  |
| 2.5 V | 0x01            | 43 Ω                  |
|       | 0x02            | 35 Ω                  |
|       | 0x031           | 24 Ω                  |
| 1.8 V | 0x02            | 46 Ω                  |
|       | 0x031           | 31 Ω                  |

Note: This setting is strongly recommended.

##### Table 8.7. LVCMOS Drive Strength Control Registers

| Setting Name     | Hex Address \[Bit Field] | Function                                     |
| ---------------- | ------------------------ | -------------------------------------------- |
| OUT0A\_CMOS\_DRV | 0104\[7:6]               | LVCMOS output impedance. See previous table. |
| OUT0\_CMOS\_DRV  | 0109\[7:6]               |                                              |
| OUT1\_CMOS\_DRV  | 010E\[7:6]               |                                              |
| OUT2\_CMOS\_DRV  | 0113\[7:6]               |                                              |
| OUT3\_CMOS\_DRV  | 0118\[7:6]               |                                              |
| OUT4\_CMOS\_DRV  | 011D\[7:6]               |                                              |
| OUT5\_CMOS\_DRV  | 0122\[7:6]               |                                              |
| OUT6\_CMOS\_DRV  | 0127\[7:6]               |                                              |
| OUT7\_CMOS\_DRV  | 012C\[7:6]               |                                              |
| OUT8\_CMOS\_DRV  | 0131\[7:6]               |                                              |
| OUT9\_CMOS\_DRV  | 0136\[7:6]               |                                              |
| OUT9A\_CMOS\_DRV | 013B\[7:6]               |                                              |

#### 8.4.6 LVCMOS Drive Strength Control Registers

The signal swing (VOL/VOH) of the LVCMOS output drivers is set by the voltage on the VDDO pins. Each output driver has its own VDDO pin allowing a unique output voltage swing for each of the LVCMOS drivers.

#### 8.4.7 LVCMOS Output Polarity

When a driver is configured as an LVCMOS output it generates a clock signal on both pins (OUTx and OUTxb). By default the clock on the OUTx pin is generated with the same polarity (in phase) with the clock on the OUTxb pin. The polarity of these clocks is configurable enabling complimentary clock generation and/or inverted polarity with respect to other output drivers.

##### Table 8.8. LVCMOS Output Polarity Control Registers

| Setting Name | Hex Address \[Bit Field] | Function                                                                 |
| ------------ | ------------------------ | ------------------------------------------------------------------------ |
| OUT0A\_INV   | 0106\[7:6]               | Controls output polarity of the OUTx and OUTxb pins when in LVCMOS mode. |
| OUT0\_INV    | 010B\[7:6]               | Selections are as below in the Output Polarity Registers.                |
| OUT1\_INV    | 0110\[7:6]               |                                                                          |
| OUT2\_INV    | 0115\[7:6]               |                                                                          |
| OUT3\_INV    | 011A\[7:6]               |                                                                          |
| OUT4\_INV    | 011F\[7:6]               |                                                                          |
| OUT5\_INV    | 0124\[7:6]               |                                                                          |
| OUT6\_INV    | 0129\[7:6]               |                                                                          |
| OUT7\_INV    | 012E\[7:6]               |                                                                          |
| OUT8\_INV    | 0133\[7:6]               |                                                                          |
| OUT9\_INV    | 0138\[7:6]               |                                                                          |
| OUT9A\_INV   | 013D\[7:6]               |                                                                          |

##### Table 8.9. Output Polarity of OUTx and OUTxb Pins in LVCMOS Mode

| OUTx\_INV | OUTx | OUTxb | Comment                 |
| --------- | ---- | ----- | ----------------------- |
| 00        | CLK  | CLK   | Both in phase (default) |
| 01        | CLK  | CLKb  | OUTxb inverted          |
| 10        | CLKb | CLKb  | OUTx and OUTxb inverted |
| 11        | CLKb | CLK   | OUTx inverted           |

#### 8.4.8 Output Driver Settings for LVPECL, LVDS, HCSL, and CML

Each differential output has four settings for control:

- Normal or Low Power Format
- Amplitude (sometimes called Swing)
- Common Mode Voltage
- Stop High or Stop Low

The normal Format setting has a 100 Ω internal resistor between the plus and minus output pins. The Low Power Format setting removes this 100 Ω internal resistor and then the differential output resistance will be > 500 Ω. However, as long as the termination impedance matches the differential impedance of the PCB traces, the signal integrity across the termination impedance will be good. For the same output amplitude, the Low Power Format will use less power than the Normal Format. The Low Power Format also has a lower rise/fall time than the Normal Format. See the Si5391/Si5391P data sheet for the rise/fall time specifications. For LVPECL and LVDS standards, ClockBuilder Pro does not support the Low Power Differential Format. Stop High means that when the output driver is disabled, the plus output will be high and the minus output will be low. Stop Low means that when the output driver is disabled, the plus output will be low and the minus output will be high.

The Format, Amplitude and Common Mode settings for the various supported standards are shown in Table 8.10 Settings for LVDS, LVPECL, and HCSL on page 34.

##### Table 8.10. Settings for LVDS, LVPECL, and HCSL

| OUTx\_FORMAT                 | Standard | VDDO Volts | OUTx\_CM | OUTx\_AMPL |
| ---------------------------- | -------- | ---------- | -------- | ---------- |
| 001 = Normal Differential    | LVPECL   | 3.3        | 11       | 6          |
| 001 = Normal Differential    | LVPECL   | 2.5        | 11       | 6          |
| 002 = Low Power Differential | LVPECL   | 3.3        | 11       | 3          |
| 002 = Low Power Differential | LVPECL   | 2.5        | 11       | 3          |
| 001 = Normal Differential    | LVDS     | 3.3        | 3        | 3          |
| 001 = Normal Differential    | LVDS     | 2.5        | 11       | 3          |
| 001 = Normal Differential    | Sub-LVDS | 1.8        | 13       | 3          |
| 002 = Low Power Differential | LVDS     | 3.3        | 3        | 1          |
| 002 = Low Power Differential | LVDS     | 2.5        | 11       | 1          |
| 002 = Low Power Differential | Sub-LVDS | 1.8        | 13       | 1          |
| 002 = Low Power Differential | HCSL     | 3.3        | 11       | 3          |
| 002 = Low Power Differential | HCSL     | 2.5        | 11       | 3          |
| 002 = Low Power Differential | HCSL     | 1.8        | 13       | 3          |

Note:

1. The low-power format will cause the rise/fall time to increase by approximately a factor of two. See the Si5391/Si5391P data sheet for more information.
2. The common-mode voltage produced is not compliant with LVDS standards; therefore, AC coupling the driver to an LVDS receiver is highly recommended.
3. Creates HCSL compatible signal.

The output differential driver can produce a wide range of output amplitudes that includes CML amplitudes. See Section 8.4.9 Setting the Differential Output Driver to Non-Standard Amplitudes for additional information.

#### 8.4.9 Setting the Differential Output Driver to Non-Standard Amplitudes

In some applications, it may be desirable to have larger or smaller differential amplitudes than those produced by the standard LVPECL and LVDS settings, as selected by CBPro. In these cases, the following information describes how to implement these amplitudes by writing to the OUTx_CM and OUTx_AMPL setting names. Contact Skyworks for assistance if you want your custom configured device to be programmed for any of the settings described here.

The differential output driver has a variable output amplitude capability and two basic formats, normal and low-power format. The difference between these two formats is that the normal format has an output impedance of ~100 Ω differential, and the low-power format has an output impedance of > 500 Ω differential. Note that the rise/fall time is slower when using the Low Power Differential Format. See the Si5391/Si5391P data sheet for rise/fall time specifications.

If the standard LVDS or LVPECL compatible output amplitudes will not work for a particular application, the variable amplitude capability can be used to achieve higher or lower amplitudes. For example, a “CML” format is sometimes desired for an application. However, CML is not a defined standard, and hence the amplitude of a CML signal for one receiver may be different than that of another receiver.

When the output amplitude needs to be different than standard LVDS or LVPECL, the Common Mode Voltage settings must be set as shown in Table 8.11 Output Differential Common Mode Voltage Settings on page 35. No settings other than these are supported as the signal integrity could be compromised. In addition, the output driver should be ac-coupled to the load so that the common-mode voltage of the driver is not affected by the load.

##### Table 8.11. Output Differential Common Mode Voltage Settings

| VDDOx (Volts) | Differential Format | OUTx\_FORMAT | Common Mode Voltage (Volts) | OUTx\_CM |
| ------------- | ------------------- | ------------ | --------------------------- | -------- |
| 3.3           | Normal              | 0x1          | 2.0                         | 0xB      |
| 3.3           | Low Power           | 0x2          | 1.6                         | 0x7      |
| 2.5           | Normal              | 0x1          | 1.3                         | 0xC      |
| 2.5           | Low Power           | 0x2          | 1.1                         | 0xA      |
| 1.8           | Normal              | 0x1          | 0.8                         | 0xD      |
| 1.8           | Low Power           | 0x2          | 0.8                         | 0xD      |

The differential amplitude can be set as shown in the following table.

##### Table 8.12. Typical Differential Amplitudes1

| OUTx\_AMPL | Normal Differential Format (Vpp SE mV – Typical) | Low-Power Differential Format (Vpp SE mV – Typical) |
| ---------- | ------------------------------------------------ | --------------------------------------------------- |
| 0          | 130                                              | 200                                                 |
| 1          | 230                                              | 400                                                 |
| 2          | 350                                              | 620                                                 |
| 3          | 450                                              | 820                                                 |
| 4          | 575                                              | 1010                                                |
| 5          | 700                                              | 1200                                                |
| 6          | 810                                              | 1350                                                |
| 7          | 920                                              | 1600                                                |

Note:

1. These amplitudes are based upon a 100 Ω differential termination.
2. In low-power mode and VDDOx = 1.8 V, OUTx_AMPL may not be set to 6 or 7.

Note: High-Speed Differential Mode in ClockBuilder Pro output setting page sets OUTx_AMP to 7 in order to compensate for channel loss at high frequency.

See the register map portion of this document for additional information about OUTx_FORMAT, OUTx_CM and OUTx_AMPL. Contact Skyworks for assistance if you require a factory-programmed device to be configured for any of the output driver settings listed above.

### 8.5 Output Enable/Disable

Clock outputs are disabled by four signals within Si5391 and the OEB pin:

- OUTALL_DISABLE_LOW
- SYSINCAL
- OUTx_OE
- LOL
- OEB pin

The following figure shows the logic of how these disable/enables occur.

#### Figure 8.5. Output Enable

1 instance of this is used per output driver

LOL

OUTALL_DISABLE_LOW

OEB Pin

Enable to Individual Output Drivers

OUTX_OE

SYSINCAL

OUTX_OE are the individual Output Driver enables as shown in the table below

#### Table 8.13. Output Enable/Disable Control Registers

| Setting Name         | Hex Address Si5391/Si5391P | Function                                                     |
| -------------------- | -------------------------- | ------------------------------------------------------------ |
| OUTALL\_DISABLE\_LOW | 0102\[0]                   | 0 = Disables all outputs. 1 = All outputs are not disabled by this signal but may be disabled by other signals or the OEB pin. See figure above. |
| OUT0A\_OE            | 0103\[1]                   | 0 = Specific output disabled.                                |
| OUT0\_OE             | 0108\[1]                   | 1 = Specific output is not disabled. The OEB pin or other signals within the device may be causing an output disable. See figure above. |
| OUT1\_OE             | 010D\[1]                   |                                                              |
| OUT2\_OE             | 0112\[1]                   |                                                              |
| OUT3\_OE             | 0117\[1]                   |                                                              |
| OUT4\_OE             | 011C\[1]                   |                                                              |
| OUT5\_OE             | 0121\[1]                   |                                                              |
| OUT6\_OE             | 0126\[1]                   |                                                              |
| OUT7\_OE             | 012B\[1]                   |                                                              |
| OUT8\_OE             | 0130\[1]                   |                                                              |
| OUT9\_OE             | 0135\[1]                   |                                                              |
| OUT9A\_OE            | 013A\[1]                   |                                                              |

#### 8.5.1 Output Driver State When Disabled

The disabled state of an output driver is configurable as disable low or disable high. When the output driver is disabled, the outputs will drive either logic high or logic low, selectable by the user. The output common mode voltage is maintained while the driver is disabled, reducing enable/disable transients. By contrast, powering down the driver rather than disabling it increases output impedance and shuts off the output common mode voltage. For all output drivers connected in the system, it is recommended to use Disable rather than Powerdown to reduce enable/disable common mode transients. Unused outputs may be left unconnected, powered down to reduce current draw, and, with the corresponding VDDOx, left unconnected.

#### 8.5.2 Synchronous Output Enable/Disable Feature

The output drivers provide a selectable synchronous enable/disable feature when OUTx_SYNC_EN = 1. Output drivers with this feature turned on will wait until a clock period has completed before the driver is disabled or enabled. This prevents unwanted runt pulses from occurring when disabling an output. When this feature is turned off OUTx_SYNC_EN = 0, the output clock will disable immediately without waiting for the period to complete and will enable immediately without waiting a period to complete. The default state is for the synchronous output disable/enable to be turned on OUTx_SYNC_EN = 1.

##### Table 8.14. Synchronous Disable Control Registers

| Setting Name    | Hex Address | Function                                                                                                                                                         |
| --------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OUT0A\_SYNC\_EN | 0104\[3]    | When this bit is high, the output will turn on/off (enable/disable) without                                                                                      |
| OUT0\_SYNC\_EN  | 0109\[3]    | generating runt pulses or glitches. The default for this bit is high. When this bit is low, the outputs will turn on/off asynchronously. In this case, there may |
| OUT1\_SYNC\_EN  | 010E\[3]    | be glitches on the output when it turns on/off.                                                                                                                  |
| OUT2\_SYNC\_EN  | 0113\[3]    |                                                                                                                                                                  |
| OUT3\_SYNC\_EN  | 0118\[3]    |                                                                                                                                                                  |
| OUT4\_SYNC\_EN  | 011D\[3]    |                                                                                                                                                                  |
| OUT5\_SYNC\_EN  | 0122\[3]    |                                                                                                                                                                  |
| OUT6\_SYNC\_EN  | 0127\[3]    |                                                                                                                                                                  |
| OUT7\_SYNC\_EN  | 012C\[3]    |                                                                                                                                                                  |
| OUT8\_SYNC\_EN  | 0131\[3]    |                                                                                                                                                                  |
| OUT9\_SYNC\_EN  | 0136\[3]    |                                                                                                                                                                  |
| OUT9A\_SYNC\_EN | 013B\[3]    |                                                                                                                                                                  |

### 8.6 Output Buffer Supply Voltage Selection

These power supply settings must match the actual VDDOx voltage so that the output driver operates properly.

#### Table 8.15. OUTx VDD Settings

| Setting Name       | Description                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| OUTx\_VDD\_SEL\_EN | These bits are set to 1 and should not be changed                                                          |
| OUTx\_VDD\_SEL     | These bits are set by CBPro to match the expected VDDOx voltage. 0: 3.3 V; 1: 1.8 V; 2: 2.5 V; 3: Reserved |

### 8.7 Output Delay Control

The input to output skew can be adjusted dynamically. This involves changing the output phase of the N divider; so the phase for all outputs that are driven by a given Nx will change together. The dynamic phase adjust can be initiated at any time under register control. This adjustment can change the output phase by up to 360 degrees (i.e. one UI). The resolution values listed in the table below assume a VCO frequency of 14 GHz for a Tvco of 71.43 psec. The skew value may change after each reset or power cycle.

#### Table 8.16. Input-Output Skew Control Registers

| Type    | Setting Names                     | Setting Address Start | Typical Resolution |
| ------- | --------------------------------- | --------------------- | ------------------ |
| Dynamic | Nx\_PHASE\_STEP, Nx\_PHASE\_COUNT | 0x0A38                | TVCO = 71.43 ps    |

For more details on how these registers are enabled and programmed, see the appropriate register map section toward the end of this reference manual.

## 9. Zero Delay Mode (All Si5391 Devices Except Si5391P)

A zero delay mode is available, in all Si5391 devices except for Si5391P, for applications that require fixed and consistent minimum delay between the selected input and outputs. The zero delay mode is configured by opening the internal feedback loop through software configuration and closing the loop externally as shown in Figure 9.1 Si5391 Zero Delay Mode Setup on page 40. This helps to cancel out the internal delay introduced by the dividers, the crosspoint, the input, and the output drivers. Any one of the outputs can be fed back to the FB_IN pins, although using the output driver that achieves the shortest trace length will help to minimize the input-to-output delay. The OUT11 and FB_IN pins are recommended for the external feedback connection in the Si5391. The FB_IN input pins must be terminated and ac-coupled when zero delay mode is used. A differential external feedback path connection is necessary for best performance. For this reason, customers should avoid using CMOS outputs for driving the external feedback path. Zero Delay Mode performance will degrade with low values of phase detector frequency (Fpfd). For this reason, ClockBuilder Pro will not enable Zero Delay Mode with an Fpfd of less than 128 kHz.

When the DSPLL is set for Zero-Delay Mode (ZDM), a hard reset request from either the RSTb pin or RST_REG register bit will have a delay of ~750 ms before executing. Any subsequent register writes to the device should be made after this time expires or they will be overwritten with the NVM values. Please contact Skyworks technical support for information on reducing this ZDM hard reset time.

### Figure 9.1. Si5391 Zero Delay Mode Setup

| VDDO0          | OUT0       | OUT0b    |
| -------------- | ---------- | -------- |
| IN0            | ~~÷ ~~P₀   | OUT 0A   |
| fIN            | IN0b       | OUT 0Ab  |
| IN1            | ~~÷ ~~P₁   | VDDO1    |
| IN1b           | OUT1       | OUT1b    |
| IN2            | ~~÷ ~~P₂   | VDDO2    |
| IN2b           | OUT2       | OUT2b    |
| IN\_ SEL\[1:0] | MultiSynth |          |
| IN3/FB\_IN     | Zero Delay | PLL      |
| fFB = fIN      | 1          | ÷P       |
| 0              | fb         |          |
| 0              | ÷ Mⁿ       | VDDO 9   |
| IN3b/FB\_INb   | Md         | OUT 9    |
| OUT 9b         | ÷ N⁹ⁿ      | ~~÷R~~11 |
| OUT 9A         | N9d        | OUT 9Ab  |

The following table gives the register used for the Zero Delay mode.

### Table 9.1. Zero Delay Mode Register:

| Reg Address | Bit Field | Type | Setting Name | Description                                                                 |
| ----------- | --------- | ---- | ------------ | --------------------------------------------------------------------------- |
| 0x091C      | 2:0       | R/W  | ZDM\_EN      | 3 = Zero delay mode. 4 = Normal mode. All other values must not be written. |

## 10. Digitally-Controlled Oscillator (DCO) Mode (All Si5391 Devices Except Si5391P)

An output that is controlled as a DCO is useful for simple tasks such as frequency margining, CPU speed control, or just changing the output frequency. The output can also be used for more sophisticated tasks such as FIFO management by adjusting the frequency of the read or write clock to the FIFO or using the output as a variable Local Oscillator in a radio application.

### 10.1 Using the N Dividers for DCO Applications

The N dividers can be digitally controlled to so that all outputs connected to the N divider change frequency in real time without any transition glitches. There are two ways to control the N divider to accomplish this task:

- Use the Frequency Increment/Decrement Pins or register bits.
- Write directly to the numerator or denominator of the N divider.

The output N divider can be changed from its minimum value of 10 to its maximum value of 4095 in very small fractional increments or a single very large increment. Each N divider has a value of Nx_NUM/Nx_DEN. Nx_NUM is a 44 bit word and Nx_DEN is a 32 bit word. Clockbuilder Pro left shifts these values as far as possible before writing them to the actual Nx_NUM and Nx_DEN registers. For example, an integer Nx divider of 30/1, when left shifted, becomes Nx_NUM = 6442509440 (decimal) and Nx_DEN = 2147483648 (decimal). By adjusting the size of the Nx_NUM and Nx_DEN but keeping the ratio the same, the resolution of the LSbit of numerator or denominator can be controlled.

When changing the N divider(s) to fractional values, the setting name N_PIBYP[4:0] must be a 0 for the N divider that is being changed. This applies when using FINC/FDEC or when directly writing to the N divider.

#### 10.1.1 DCO with Frequency Increment/Decrement Pins/Bits

The FSTEPW (Frequency STEP Word) is a 44 bit word that is used to change the value of the Nx_NUM word. Whenever an FINC or FDEC is asserted, the FSTEPW will automatically add or subtract from the Nx_NUM word so that the output frequency will increment (FINC) or decrement (FDEC) respectively.

Each of the N dividers can be independently stepped up or down in numerical predefined steps with a maximum resolution that varies from ~ 0.05 ppb to a ~0.004 ppb depending upon the frequency plan. One or more N dividers can be controlled by FINC/FDEC at the same time by use of the N_FSTEP_MSK bits. Any N divider that is masked by its corresponding bit in the N_FSTEP_MSK field will not change when FINC or FDEC is asserted. The magnitude of the frequency change caused by FINC or FDEC is determined by the value of the FSTEPW word and the magnitude of the word in Nx_NUM. For a specific frequency step size it may be necessary to adjust the Nx_NUM value while keeping the ratio of Nx_NUM/Nx_DEN the same. When the FINC or FDEC pin or register bit is asserted the selected N dividers will have their numerator changed by the addition or subtraction of the Nx_FSTEPW so that an FINC will increase the output frequency and an FDEC will decrease the output frequency. An FINC or FDEC can be followed by another FINC or FDEC in 1 μs minimum.

Because the output frequency = FVCO * Nx_DEN/(Rx * Nx_NUM), subsequent changes to Nx_NUM by the FSTEPW will not produce exactly the same output frequency change. The amount of error in the frequency step is extremely small and in a vast number of applications will not cause a problem. When consecutive frequency steps must be exactly the same, it is possible to set FINC and FDEC to change the Nx_DEN instead of Nx_NUM and then consecutive FINCs or FDECs will be exactly the same frequency change. However, there are some special setups that are necessary to achieve this. For more information contact Skyworks Support.

#### 10.1.2 DCO with Direct Register Writes

When a N divider numerator (Nx_NUM) and its corresponding update bit (Nx_UPDATE) is written, the new numerator value will take effect and the output frequency will change without any glitches. The N divider numerator and denominator terms (Nx_NUM and Nx_DEN) can be left and right shifted so that the least significant bit of the numerator word represents the exact step resolution that is needed for your application. Each N divider has an update bit (Nx_UPDATE) that must be written to cause the written values to take effect. All N dividers can be updated at the same time by writing the N_UPDATE_ALL bit. Note that writing this bit will not cause any output glitching on an N divider that did not have its numerator or denominator changed.

When changing the N divider denominator (Nx_DEN) it is remotely possible that a small phase change of ~550 fs may occur at the exact time of the frequency change. However with the proper setup it is possible to change Nx_DEN and never have a phase change. If your application requires changing an N divider denominator, contact Skyworks Support.

### 10.2 Using the M Divider for DCO Applications

The VCO can be treated as a DCO by changing the value of the M feedback divider. By changing the M divider, all the output frequencies will change by the same amount in ppm. Changing the M divider is only valid for small changes in the output frequencies. Contact Skyworks Support for assistance in the implementation of this capability.

Si5391 Reference Manual • Serial Interface

## 11. Serial Interface

Configuration and operation of the Si5391/Si5391P is controlled by reading and writing registers using the I2C or SPI serial interface. The I2C_SEL pin selects between I2C or SPI operation. The Si5391/Si5391P supports communication with either a 3.3 V or 1.8 V host by setting the IO_VDD_SEL (0x0943[0]) configuration bit. The SPI mode supports 4-wire (default) or 3-wire by setting the SPI_3WIRE configuration bit. See the figure below for supported modes of operation and settings. The I2C pins are open drain and are ESD clamped to 3.3 V, regardless of the host supply level. The I2C pins are clamped to 3.3 V so that they may be externally pulled up to 3.3 V regardless of IO_VDD_SEL (in register 0x0943).

Table 11.1 I2C/SPI Register Settings on page 43 lists register settings of interest for the I2C/SPI.

### Figure 11.1. I2C/SPI Device Connectivity Configurations

|                            | I²C                 |      | SPI 4-Wire         |                    |      | SPI 3-Wire |      |      |          |          |   |
| -------------------------- | ------------------- | ---- | ------------------ | ------------------ | ---- | ---------- | ---- | ---- | -------- | -------- | - |
|                            | I2C\_SEL pin = High |      | I2C\_SEL pin = Low | I2C\_SEL pin = Low |      |            |      |      |          |          |   |
| IO\_VDD\_SEL = 0 (Default) |                     |      | 1.8V               | 3.3V               | 1.8V | 1.8V       | 3.3V | 1.8V |          |          |   |
| Host = 1.8V                | 1.8V                | 1.8V | 3.3V               | 1.8V               | VDDA | VDD        |      |      |          |          |   |
| I²C                        | SDA                 | SDA  | HOST               | SDO                | SDI  | HOST       |      |      |          |          |   |
| HOST                       |                     |      |                    | SDI                | SDO  |            | SCLK | SCLK |          |          |   |
|                            |                     |      |                    |                    |      | SCLK       | SCLK |      | Clock IC | Clock IC |   |
|                            | IO\_VDD\_SEL = 1    |      |                    |                    |      |            |      |      |          |          |   |
|                            |                     |      |                    | 3.3V               | 3.3V | 1.8V       | 3.3V | 3.3V | 1.8V     |          |   |
| Host = 3.3V                | 3.3V                | 3.3V | 3.3V               | 1.8V               | VDDA | VDD        |      |      |          |          |   |
| I²C                        | SDA                 | SDA  | HOST               | SDO                | SDI  | HOST       |      |      |          |          |   |
| HOST                       |                     |      |                    | SDI                | SDO  |            | SCLK | SCLK |          |          |   |
|                            |                     |      |                    |                    |      | SCLK       | SCLK |      | Clock IC | Clock IC |   |

If neither serial interface is used, leave I2C_SEL unconnected. Pull pins SDA/SDIO, SCLK, A1/SDO, and A0/CS all low.

Note that the Si5391/Si5391P is not I2C fail-safe upon loss of power. Applications that require fail-safe operation should isolate the device from a shared I2C bus.

### Table 11.1. I2C/SPI Register Settings

| Setting Name | Hex Address \[Bit Field] Si5391/Si5391P | Function                                                     |
| ------------ | --------------------------------------- | ------------------------------------------------------------ |
| IO\_VDD\_SEL | 0x0943\[0]                              | The IO\_VDD\_SEL configuration bit optimizes the VIL, VIH, VOL, and VOH thresholds to match the VDDS voltage. By default the IO\_VDD\_SEL bit is set to the VDD option. The serial interface pins are always 3.3 V tolerant even when the device's VDD pin is supplied from a 1.8 V source. When the I2C or SPI host is operating at 3.3 V and the Si5391/Si5391P at VDD = 1.8 V, the host must write the IO\_VDD\_SEL configuration bit to the VDDA option. This will ensure that both the host and the serial interface are operating at the optimum voltage thresholds. |
| SPI\_3WIRE   | 0x002B\[3]                              | The SPI\_3WIRE configuration bit selects the option of 4-wire or 3-wire SPI communication. By default, this configuration bit is set to the 4-wire option. In this mode the Si5391/Si5391P will accept write commands from a 4-wire or 3-wire SPI host allowing configuration of device registers. For full bidirectional communication in 3-wire mode, the host must write the SPI\_3WIRE configuration bit to “1”. |

### 11.1 I2C Interface

When in I2C mode, the serial interface operates in slave mode with 7-bit addressing and can operate in Standard-Mode (100 kbps) or Fast-Mode (400 kbps) and supports burst data transfer with auto address increments. The I2C bus consists of a bidirectional serial data line (SDA) and a serial clock input (SCL) as shown in the figure below. Both the SDA and SCL pins must be connected to a supply via an external pull-up (4.7 kΩ) as recommended by the I2C specification as shown in the figure below. Two address select bits (A0, A1) are provided allowing up to four Si5391/Si5391P devices to communicate on the same bus. This also allows four choices in the I2C address for systems that may have other overlapping addresses for other I2C devices.

#### Figure 11.2. I2C Configuration

The 7-bit slave device address of the Si5391/Si5391P consists of a 5-bit fixed address plus 2 pins which are selectable for the last two bits, as shown in the following figure.

#### Figure 11.3. 7-bit I2C Slave Address Bit-Configuration

Data is transferred MSB first in 8-bit words as specified by the I2C specification. A write command consists of a 7-bit device (slave) address + a write bit, an 8-bit register address, and 8 bits of data as shown in Figure 11.6 SPI Interface Connections on page 46. A write burst operation is also shown where subsequent data words are written using to an auto-incremented address.

#### Figure 11.4. I2C Write Operation

Write Operation – Single Byte

S Slv Addr [6:0]                       0 A Reg Addr [7:0]  A                Data [7:0]   A   P

Write Operation - Burst (Auto Address Increment)

S Slv Addr [6:0]  0 A Reg Addr [7:0]  A Data [7:0]  A Data [7:0]  A                                      P

1 – Read                      Reg Addr +1

Host  Clock IC      0 – Write

A – Acknowledge (SDA LOW)

Host  Clock IC      N – Not Acknowledge (SDA HIGH)

S – START condition

P – STOP condition

A read operation is performed in two stages. A data write is used to set the register address, then a data read is performed to retrieve the data from the set address. A read burst operation is also supported. This is shown in the following figure.

#### Figure 11.5. I2C Read Operation

Read Operation – Single Byte

| S | Slv Addr \[6:0] | 0 | A | Reg Addr \[7:0] | A | P |
| - | --------------- | - | - | --------------- | - | - |
| S | Slv Addr \[6:0] | 1 | A | Data \[7:0]     | N | P |

Read Operation - Burst (Auto Address Increment)

| S | Slv Addr \[6:0] | 0 | A | Reg Addr \[7:0] | A | P           |   |   |
| - | --------------- | - | - | --------------- | - | ----------- | - | - |
| S | Slv Addr \[6:0] | 1 | A | Data \[7:0]     | A | Data \[7:0] | N | P |

Reg Addr +1

Host Clock IC: 1 – Read, 0 – Write

Host Clock IC: A – Acknowledge (SDA LOW), N – Not Acknowledge (SDA HIGH), S – START condition, P – STOP condition

The SMBUS interface requires a timeout. The error flags are found in the registers listed below.

#### Table 11.2. SMBus Timeout Error Bit Indicators

| Register Name       | Hex Address \[Bit Field] | Function                             |
| ------------------- | ------------------------ | ------------------------------------ |
| SMBUS\_TIMEOUT      | 0x000C\[5]               | 1 if there is a SMBus timeout error. |
| SMBUS\_TIMEOUT\_FLG | 0x0011\[5]               | 1 if there is a SMBus timeout error. |

### 11.2 SPI Interface

When in SPI mode, the serial interface operates in 4-wire or 3-wire depending on the state of the SPI_3WIRE configuration bit. The 4-wire interface consists of a clock input (SCLK), a chip select input (CS), serial data input (SDI), and serial data output (SDO). The 3-wire interface combines the SDI and SDO signals into a single bidirectional data pin (SDIO). Both 4-wire and 3-wire interface connections are shown in the following figure.

#### Figure 11.6. SPI Interface Connections

|      |      |          | SPI 4-Wire     | SPI 3-Wire     |      |
| ---- | ---- | -------- | -------------- | -------------- | ---- |
|      |      |          | SPI\_3WIRE = 0 | SPI\_3WIRE = 1 |      |
| CSb  | CSb  |          |                |                |      |
|      |      | SDI      | To SPI         | To SPI         | SDIO |
| Host | SCLK | Clock IC | Host           |                |      |
|      |      |          | SCLK           |                |      |

#### Table 11.3. SPI Command Format

| Instruction                    | 1st Byte1 | 2nd Byte      | 3rd Byte   | Nth Byte2,3 |
| ------------------------------ | --------- | ------------- | ---------- | ----------- |
| Set Address                    | 000x xxxx | 8-bit Address | —          | —           |
| Write Data                     | 010x xxxx | 8-bit Data    | —          | —           |
| Read Data                      | 100x xxxx | 8-bit Data    | —          | —           |
| Write Data + Address Increment | 011x xxxx | 8-bit Data    | —          | —           |
| Read Data + Address Increment  | 101x xxxx | 8-bit Data    | —          | —           |
| Burst Write Data               | 1110 0000 | 8-bit Address | 8-bit Data | 8-bit Data  |

Note:

1. X = don’t care (1 or 0).
2. The Burst Write Command is terminated by de-asserting CSb (CSb = high).
3. There is no limit to the number of data bytes that follow the Burst Write Command, but the address will wrap around to zero in the byte after address 255 is written.

Writing or reading data consist of sending a “Set Address” command followed by a “Write Data” or “Read Data” command. The 'Write Data + Address Increment' or “Read Data + Address Increment” commands are available for cases where multiple byte operations in sequential address locations is necessary. The “Burst Write Data” instruction provides a compact command format for writing data since it uses a single instruction to define starting address and subsequent data bytes. Figure 11.7 Example Writing Three Data Bytes using the SPI Write Commands on page 47 shows an example of writing three bytes of data using the write commands. As can be seen, the “Write Burst Data” command is the most efficient method for writing data to sequential address locations. Figure 11.8 Example of Reading Three Data Bytes Using the SPI Read Commands on page 47 provides a similar comparison for reading data with the read commands. Note that there is no equivalent burst read; the read increment function is used in this case.

#### Figure 11.7. Example Writing Three Data Bytes using the SPI Write Commands

‘Set Address’ and ‘Write Data’

| ‘Set Addr’ | Addr \[7:0] | ‘Write Data’ | Data \[7:0] |
| ---------- | ----------- | ------------ | ----------- |
| ‘Set Addr’ | Addr \[7:0] | ‘Write Data’ | Data \[7:0] |
| ‘Set Addr’ | Addr \[7:0] | ‘Write Data’ | Data \[7:0] |

‘Set Address’ and ‘Write Data + Address Increment’

| ‘Set Addr’              | Addr \[7:0] | ‘Write Data + Addr Inc’ | Data \[7:0] |
| ----------------------- | ----------- | ----------------------- | ----------- |
| ‘Write Data + Addr Inc’ |             |                         | Data \[7:0] |
| ‘Write Data + Addr Inc’ |             |                         | Data \[7:0] |

‘Burst Write Data’

| ‘Burst Write Data’ | Addr \[7:0] | Data \[7:0] | Data \[7:0] | Data \[7:0] |
| ------------------ | ----------- | ----------- | ----------- | ----------- |

Host  Clock IC

Host  Clock IC

#### Figure 11.8. Example of Reading Three Data Bytes Using the SPI Read Commands

‘Set Address’ and ‘Read Data’

| ‘Set Addr’ | Addr \[7:0] | ‘Read Data’ | Data \[7:0] |
| ---------- | ----------- | ----------- | ----------- |
| ‘Set Addr’ | Addr \[7:0] | ‘Read Data’ | Data \[7:0] |
| ‘Set Addr’ | Addr \[7:0] | ‘Read Data’ | Data \[7:0] |

‘Set Address’ and ‘Read Data + Address Increment’

| ‘Set Addr’             | Addr \[7:0] | ‘Read Data + Addr Inc’ | Data \[7:0] |
| ---------------------- | ----------- | ---------------------- | ----------- |
| ‘Read Data + Addr Inc’ |             |                        | Data \[7:0] |
| ‘Read Data + Addr Inc’ |             |                        | Data \[7:0] |

Host  Clock IC

## 11. SPI Command Timing

The timing diagrams for the SPI commands are shown in Figures Figure 11.9 SPI “Set Address” Command Timing on page 48, Figure 11.10 SPI “Write Data” and “Write Data+ Address Increment” Instruction Timing on page 49, Figure 11.11 SPI “Read Data” and “Read Data + Address Increment” Instruction Timing on page 50, and Figure 11.12 SPI “Burst Data Write” Instruction Timing on page 50.

### Figure 11.9. SPI “Set Address” Command Timing

‘Set Address’ Command

| Previous | Command                 | Next         |
| -------- | ----------------------- | ------------ |
| >95 ns   | Set Address Instruction | Base Address |

| CS                  | SCLK            | 4-Wire | SDI            |
| ------------------- | --------------- | ------ | -------------- |
| 1 0 7 6 5 4 3 2 1 0 | 7 6 5 4 3 2 1 0 | 7 6    | High Impedance |

| SDO                 | 3-Wire          | SDIO |
| ------------------- | --------------- | ---- |
| 1 0 7 6 5 4 3 2 1 0 | 7 6 5 4 3 2 1 0 | 7 6  |

Host Clock IC Don’t Care

### Figure 11.10. SPI “Write Data” and “Write Data+ Address Increment” Instruction Timing

Previous                                      ‘Write Data’              Next

Command                                                                 Command

>95 ns                                                          Data byte @ base address    >95 ns

or

CS                                        Write Data instruction    Data byte @ base address + 1

SCLK

4-Wire

| SDI | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 |
| --- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |

SDO

3-Wire

| SDIO | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 |
| ---- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |

Host        Clock IC              Host       Clock IC            Don’t Care              High Impedance

### Figure 11.11. SPI “Read Data” and “Read Data + Address Increment” Instruction Timing

Read Data Command

Read byte @ base address or

Read byte @ base address + 1

| CS     |      |   |   | Read Data instruction |   |   |   |   |   |   |   |   |   |   |
| ------ | ---- | - | - | --------------------- | - | - | - | - | - | - | - | - | - | - |
| SCLK   |      |   |   |                       |   |   |   |   |   |   |   |   |   |   |
| 4-Wire | SDI  | 1 | 0 | 7                     | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 |   |
| SDO    | 1    | 0 |   |                       | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 |
| 3-Wire | SDIO | 1 | 0 | 7                     | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 |   |

Host Clock IC Host Clock IC Don’t Care High Impedance

### Figure 11.12. SPI “Burst Data Write” Instruction Timing

Burst Data Write Command

Base address 1st data byte @ base address nth data byte @ base address + n

| CS     |      |   | Burst Write Instruction |   |   |   |   |   |   |   |   |   |   |
| ------ | ---- | - | ----------------------- | - | - | - | - | - | - | - | - | - | - |
| SCLK   |      |   |                         |   |   |   |   |   |   |   |   |   |   |
| 4-Wire | SDI  | 1 | 0                       | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 |
| SDO    |      |   |                         |   |   |   |   |   |   |   |   |   |   |
| 3-Wire | SDIO | 1 | 0                       | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 7 | 6 |

Host Clock IC Host Clock IC Don’t Care High Impedance

Note that for all SPI communication the chip select (CS) must be high for the minimum time period between commands. When chip select goes high it indicates the termination of the command. The SCLK can be turned off between commands, particularly if there are very long delays between commands.

## 12. Crystal, XO and Device Circuit Layout Recommendations

The following are recommendations for crystal layout (for devices that require an external reference), as well as device layout for all variants. The main layout issues that should be carefully considered include the following:

- Number and size of the ground vias for the Epad
- Output clock trace routing
- Input clock trace routing
- Control and Status signals to input or output clock trace coupling
- Xtal signal coupling (external reference devices)
- Xtal layout (external reference devices)

If the application uses a crystal for the XAXB inputs a shield should be placed underneath the crystal connected to the X1 and X2 pins to provide the best possible performance. The shield should not be connected to the ground plane(s), and the layers underneath should have as little area under the shield as possible. It may be difficult to do this for all the layers, but it is important to do this for the layers that are closest to the shield.

Go to the Skyworks Timing page to obtain Si5391 evaluation board schematics, layouts, and component BOM files.

### 12.1 64-Pin QFN Si5391/Si5391P Layout Recommendations

This section details the recommended guidelines for the external reference layout of the 64-pin Si5391/Si5391P device using an example 8-layer PCB. The following are the descriptions of each of the eight layers.

- Layer 1: device layer, with low speed CMOS control/status signals
- Layer 2: crystal shield (applies to external reference devices only)
- Layer 3: ground plane
- Layer 4: power distribution
- Layer 5: power routing layer
- Layer 6: input clocks
- Layer 7: output clocks layer
- Layer 8: ground layer

The 64 pin QFN crystal guidelines show the top layer layout of the Si5391/Si5391P device mounted on the top PCB layer. This particular layout was designed to implement either a crystal or an external oscillator as the XAXB reference. Note this applies only to external reference devices. The crystal/oscillator area is outlined with the white box around it. In this case, the top layer is flooded with ground. Note that this layout has a resistor in series with each pin of the crystal. In typical applications, these resistors should be removed.

#### 12.1.1 Si5391 with an External Reference (Not Relevant to the Si5391P)

For devices that use an external reference like an XO, pins X1 and X2 should not be connected to "ground" and should be left as "no-connects". An external reference does not need a crystal shield or the voids underneath the shield. The XA/XB connection should be treated as a high speed critical path that is ac-coupled and terminated at the end of the etch run. The layout should minimize the stray capacitance from the XA pin to the XB pin. Jitter is very critical at the XA/XB pins and therefore split termination and differential signaling should be used whenever possible.

Si5391 Reference Manual • Crystal, XO and Device Circuit Layout Recommendations

#### 12.1.2 Si5391/Si5391P Crystal Guidelines

The following are five recommended crystal guidelines used with external reference devices:

1. Place the crystal as close as possible to the XA/XB pins.
2. DO NOT connect the crystal's GND pins to PCB gnd.
3. Connect the crystal's GND pins to the DUT's X1 and X2 pins via a local crystal GND shield placed around and under the crystal. See Figure 12.1 64-pin Si5391/Si5391P Crystal Layout Recommendations Top Layer (Layer 1) on page 52 at the bottom left for an illustration of how to create a crystal GND shield by placing vias connecting the top layer traces to the shield layer underneath. Note that a zoom view of the crystal shield layer on the next layer down is shown in Figure 12.2 Zoom View Crystal Shield Layer, Below the Top Layer (Layer 2) on page 53.
4. Minimize traces adjacent to the crystal/oscillator area especially if they are clocks or frequently toggling digital signals.
5. In general do not route GND, power planes/traces, or locate components on the other side, below the crystal GND shield. As an exception if it is absolutely necessary to use the area on the other side of the board for layout or routing, then place the next reference plane in the stack-up at least two layers away or at least 0.05 inches away. The Si5391/Si5391P should have all layers underneath the ground shield removed if possible.

##### Figure 12.1. 64-pin Si5391/Si5391P Crystal Layout Recommendations Top Layer (Layer 1)

##### Figure 12.2. Zoom View Crystal Shield Layer, Below the Top Layer (Layer 2)

Figure 12.2 Zoom View Crystal Shield Layer, Below the Top Layer (Layer 2) on page 53 shows the layer that implements the shield underneath the crystal. The shield extends underneath the entire crystal and the X1 and X2 pins. This layer also has the clock input pins. The clock input pins go to layer 2 using vias to avoid crosstalk. As soon as the clock inputs are on layer 2, they have a ground shield above, below, and on the sides for protection.

##### Figure 12.3 Crystal Ground Plane (Layer 3)

Figure 12.3 Crystal Ground Plane (Layer 3) on page 54 is the ground plane and shows a void underneath the crystal shield.

##### Figure 12.4 Power Plane (Layer 4)

Figure 12.4 Power Plane (Layer 4) on page 55 is a power plane and shows the clock output power supply traces. The void underneath the crystal shield is continued.

##### Figure 12.5. Layer 5 Power Routing on Power Plane (Layer 5)

Figure 12.5 Layer 5 Power Routing on Power Plane (Layer 5) on page 56 shows layer 5, which is the power plane with the power routed to the clock output power pins.

##### Figure 12.6 Ground Plane (Layer 6)

on page 57 is another ground plane similar to layer 3.

#### 12.1.3 Si5391/Si5391P Output Clocks

Figure 12.7 Output Clock Layer (Layer 7) on page 58 shows the output clocks. Similar to the input clocks the output clocks have vias that immediately go to a buried layer with a ground plane above them and a ground flooded bottom layer. There is a ground flooding between the clock output pairs to avoid crosstalk. There should be a line of vias through the ground flood on either side of the output clocks to ensure that the ground flood immediately next to the differential pairs has a low inductance path to the ground plane on layers 3 and 6.

##### Figure 12.7. Output Clock Layer (Layer 7)

##### Figure 12.8. Bottom Layer Ground Flooded (Layer 8)

## 13. Power Management

### 13.1 Power Management Features

Several unused functions can be powered down to minimize power consumption. The registers listed below are used for powering down different features.

#### Table 13.1. Power-Down Registers

| Register Name  | Hex Address \[Bit Field] | Function                                                                                               |
| -------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ |
| Si5391/Si5391P | PDN 0x001E\[0]           | This bit allows powering down the device. The serial interface remains powered during power down mode. |
| OUT0A\_PDN     | 0x0103\[0]               | Powers down unused clock outputs.                                                                      |
| OUT0\_PDN      | 0x0108\[0]               |                                                                                                        |
| OUT1\_PDN      | 0x010D\[0]               |                                                                                                        |
| OUT2\_PDN      | 0x0112\[0]               |                                                                                                        |
| OUT3\_PDN      | 0x0117\[0]               |                                                                                                        |
| OUT4\_PDN      | 0x011C\[0]               |                                                                                                        |
| OUT5\_PDN      | 0x0121\[0]               |                                                                                                        |
| OUT6\_PDN      | 0x0126\[0]               |                                                                                                        |
| OUT7\_PDN      | 0x012B\[0]               |                                                                                                        |
| OUT8\_PDN      | 0x0130\[0]               |                                                                                                        |
| OUT9\_PDN      | 0x0135\[0]               |                                                                                                        |
| OUT9A\_PDN     | 0x013A\[0]               |                                                                                                        |
| OUT\_PDN\_ALL  | 0x0145\[0]               | Power down all output drivers                                                                          |
| XAXB\_PDNB     | 0x090E\[1]               | 0-Power down the oscillator and buffer circuitry at the XA/XB pins 1- No power down                    |

### 13.2 Power Supply Recommendations

The power supply filtering generally is important for optimal timing performance. The Si5391/Si5391P devices have multiple stages of on-chip regulation to minimize the impact of board level noise on clock jitter. Following conventional power supply filtering and layout techniques will further minimize signal degradation from the power supply.

It is recommended to use a 1 μF 0402 ceramic capacitor on each VDD for optimal performance. It is also suggested to include an optional, single 0603 (resistor/ferrite) bead in series with each supply to enable additional filtering if needed.

### 13.3 Power Supply Sequencing

Four classes of supply voltages exist on the Si5391/Si5391P:

1. VDD = 1.8 V (Core digital supply)
2. VDDA = 3.3 V (Analog supply)
3. VDDOx = 1.8/2.5/3.3 V ± 5% (Clock output supply)
4. VDDS = 1.8/3.3V ± 5% (Digital I/O supply)

There is no requirement for power supply sequencing unless the output clocks are required to be phase aligned with each other. In this case, the VDDO of each clock which needs to be aligned must be powered up before VDD and VDDA. VDDS has no effect on output clock alignment.

If output-to-output alignment is required for applications where it is not possible to properly sequence the power supplies, then the output clocks can be aligned by asserting the SOFT_RST 0x001C[0] or Hard Reset 0x001E[1] register bits or driving the RSTB pin. Note that using a hard reset will reload the register with the contents of the NVM and any unsaved changes will be lost.

One may observe that when powering up the VDD = 1.8 V rail first, that the VDDA = 3.3 V rail will initially follow the 1.8 V rail. Likewise, if the VDDA rail is powered down first then it will not drop far below VDD until VDD itself is powered down. This is due to the pad I/O circuits which have large MOSFET switches to select the local supply from either the VDD or VDDA rails. These devices are relatively large and yield a parasitic diode between VDD and VDDA. Please allow for both VDD and VDDA to power-up and power-down before measuring their respective voltages.

### 13.4 Grounding Vias

The pad on the bottom of the device functions as both the sole electrical ground and primary heat transfer path. Hence it is important to minimize the inductance and maximize the heat transfer from this pad to the internal ground plane of the PCB. Use no fewer than 25 vias from the center pad to a ground plane under the device. In general, more vias will perform better. Having the ground plane near the top layer will also help to minimize the via inductance from the device to ground and maximize the heat transfer away from the device.

## 14. Register Map

### 14.1 Base vs. Factory Preprogrammed Devices

The Si5391/Si5391P devices can be ordered as “base” or “factory-preprogrammed” (also known as “custom OPN”) versions.

### 14.2 “Base” Devices (a.k.a. “Blank” Devices)

Example “base” orderable part numbers (OPNs) are of the form “Si5391A-E-GM” or “Si5391B-E-GM”.

Base devices are available for applications where volatile reads and writes are used to program and configure the device for a particular application.

Base devices do not power up in a usable state (all output clocks are disabled).

Base devices are, however, configured by default to use a 48 MHz crystal on the XA/XB reference and a 1.8 V compatible I/O voltage setting for the host I2C/SPI interface.

Additional programming of a base device is mandatory to achieve a usable configuration.

See the on-line lookup utility at: https://www.skyworksinc.com/en/Application-Pages/Timing-Lookup-Customize to access the default configuration plan and register settings for any base OPN.

### 14.3 “Factory Preprogrammed” (Custom OPN) Devices

Factory preprogrammed devices use a “custom OPN”, such as Si5391A-E-xxxxx-GM, where xxxxx is a sequence of characters assigned by Skyworks for each customer-specific configuration. These characters are referred to as the “OPN ID”. Customers must initiate custom OPN creation using the ClockBuilder Pro software.

Many customers prefer to order devices which are factory preprogrammed for a particular application that includes specifying the XA/XB reference frequency/type, the clock input frequencies, the clock output frequencies, as well as the other options, such as automatic clock selection, loop BW, etc. The ClockBuilder software is required to select among all of these options and to produce a project file which Skyworks uses to preprogram all devices with custom orderable part number (“custom OPN”).

Custom OPN devices contain all of the initialization information in their non-volatile memory (NVM) so that it powers up fully configured and ready to go.

Because preprogrammed device applications are inherently quite different from one another, the default power up values of the register settings can be determined using the custom OPN utility at: https://www.skyworksinc.com/en/Application-Pages/Timing-Lookup-Customize.

Custom OPN devices include a device top mark which includes the unique OPN ID. Refer to the device data sheet's Ordering Guide and Top Mark sections for more details.

Both “base” and “factory preprogrammed” devices can have their operating configurations changed at any time using volatile reads and writes to the registers. Both types of devices can also have their current register configuration written to the NVM by executing an NVM bank burn sequence (see Section .)

### 14.4 Register Map Overview and Default Settings Values

The Si5391/Si5391P family parts have large register maps that are divided into separate “Pages” of register banks. This allows more register addresses than either the I2C or SPI serial interface standards 8-bit addressing provide. Each page has a maximum of 256 addresses, however not all addresses are used on every page. Every register has a maximum data size of 8-bits, or 1 byte. Writing the page number to the 8-bit serial interface address of 0x01 on any page (0x0001, 0x0101, 0x0201, etc.) updates the page selection for subsequent register reads and writes. For example, to access the value in register 0x040E, it is first necessary to write the page value 0x04 to serial interface register address 0x01. At this point, the value of serial interface address 0x0E (0x040E) may be read or written. Note that is it not necessary to write the page select register again when accessing other registers on the same page. Similarly, the read-only DEVICE_READY status is available from every page at serial interface address 0xFE (0x00FE, 0x01FE, 0x02FE, etc.).

It is recommended to use dynamic Read-Modify-Write methods when writing to registers which contain multiple settings, such as register 0x0011. To do this, first read the current contents of the register. Next, update only the select bit or bits that are being modified. This may involve using both logical AND and logical OR operations. Finally, write the updated contents back to the register. Writing to pages, registers, or bits not documented below may cause undesired behavior in the device.

Details of the register and settings information are organized hierarchically below. To find the relevant information for your application, first choose the section corresponding to the base part number, Si5391 for your design. Then, choose the section under that for the page containing the desired register(s).

Default register contents and settings differ for each device part number, or OPN. This information may be found by searching for the Custom OPN for your device using the link below. Both Base/Blank and Custom OPNs are available there. See the previous section on “Base vs. Factory Preprogrammed Devices" for more information on part numbers. The Private Addendum to the data sheet lists the default settings and frequency plan information. You must be logged into the Skyworks website to access this information. The Public addendum gives only the general frequency plan information (https://www.skyworksinc.com/en/Application-Pages/Timing-Lookup-Cus-tomize).

#### Table 14.1. Register Map Paging Descriptions

| Page   | Start Address (Hex) | Start Address (Decimal) | Contents                                          |
| ------ | ------------------- | ----------------------- | ------------------------------------------------- |
| Page 0 | 0000h               | 0                       | Alarms, interrupts, reset, device ID, revision ID |
| Page 1 | 0100h               | 256                     | Clock output configuration                        |
| Page 2 | 0200h               | 512                     | P,R dividers, scratch area                        |
| Page 3 | 0300h               | 768                     | Output N dividers, N divider FINC/FDEC            |
| Page 9 | 0900h               | 2304                    | Control IO configuration                          |

R = Read Only

R/W = Read Write

S = Self Clearing

A self-clearing bit will be cleared by the device once the operation initiated by this bit is complete. Registers with “sticky” flag bits, such as LOS0_FLG, are cleared by writing “0” to the bit that has been automatically set high by the device.

## 15. Si5391A/B Register Map

### 15.1 Page 0 Registers Si5391

| Reg Address | Bit Field | Type | Setting Name | Description                                                               |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------------------- |
| 0x0000      | 3:0       | R    | DIE\_REV     | 4-bit Die Revision Number 0 = Silicon Revision A0 1 = Silicon Revision A1 |

### Table 15.2. 0x0001 Page

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                                                                                                                                                                          |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0001      | 7:0       | R/W  | PAGE         | Selects one of 256 possible pages. There is the “Page Register” which is located at address 0x01 on every page. When read, it will indicate the current page. When written, it will change the page to the value entered. There is a page register at address 0x0001, 0x0101, 0x0201, 0x0301, … etc. |

### Table 15.3. 0x0002–0x0003 Base Part Number

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                 |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------------------------------------- |
| 0x0002      | 7:0       | R    | PN\_BASE     | Four-digit “base” part number, one nibble per digit                                         |
| 0x0003      | 15:8      | R    | PN\_BASE     | Example: Si5391A-A-GM. The base part number (OPN) is 5391, which is stored in this register |

### Table 15.4. 0x0004 Device Speed/Synthesis Mode Grade

| Reg Address | Bit Field | Type | Setting Name | Description                                                                           |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------------------------------- |
| 0x0004      | 7:0       | R    | GRADE        | One ASCII character indicating the device speed grade: 0 = A 1 = B 2 = C 3 = D 15 = P |

### Table 15.5. 0x0005 Device Revision

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                          |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0005      | 7:0       | R    | DEVICE\_REV  | One ASCII character indicating the device revision level: 0 = A; 1 = B Example: in Si5391C-A12345-GM, the device revision is “A” and is stored as 0. |

### Table 15.6. 0x0009 Temperature Grade

| Reg Address | Bit Field | Type | Setting Name | Description                                                                      |
| ----------- | --------- | ---- | ------------ | -------------------------------------------------------------------------------- |
| 0x0009      | 7:0       | R    | TEMP\_GRADE  | Device temperature grading 0 = Industrial (–40 ° C to 85 ° C) ambient conditions |

### Table 15.7. 0x000A Package ID

| Reg Address | Bit Field | Type | Setting Name | Description                                    |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------- |
| 0x000A      | 7:0       | R    | PKG\_ID      | Package ID 0 = 9x9 mm 64 QFN 1 = 7x7 mm 44 QFN |

Part numbers are of the form:

Si&#x3C;Part Num Base>&#x3C;Grade>-&#x3C;Device Revision>&#x3C;OPN ID>-&#x3C;Temp Grade>&#x3C;Package ID>

Examples:

- Si5391C-A12345-GM
Applies to a “custom” OPN (Ordering Part Number) device. These devices are factory pre-programmed with the frequency plan and all other operating characteristics defined by the user’s ClockBuilder Pro project file.
- Si5391C-A-GM
Applies to a “base” or “blank” OPN device. Base devices are factory pre-programmed to a specific base part type (e.g., Si5391 but exclude any user-defined frequency plan or other user-defined operating characteristics selected in ClockBuilder Pro.

### Table 15.8. 0x000B I2C Address

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                       |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------------------------------------------- |
| 0x000B      | 6:2       | R/W  | I2C\_ADDR    | The upper 5 bits of the 7-bit I2C address. The lower 2 bits are controlled by the A1 and A0 pins. |

### Table 15.9. 0x000C Status Bits

| Reg Address | Bit Field | Type | Setting Name   | Description                                                                                |
| ----------- | --------- | ---- | -------------- | ------------------------------------------------------------------------------------------ |
| 0x000C      | 0         | R    | SYSINCAL       | 1 if the device is calibrating.                                                            |
| 0x000C      | 1         | R    | LOSXAXB        | 1 if there is no signal at the XA pin as the LOS detector is only connected to the XA pin. |
| 0x000C      | 2         | R    | LOSREF         | 1 if the Phase Frequency detector does not have a signal from XAXB, IN2, IN1, or IN0.      |
| 0x000C      | 3         | R    | LOL            | 1 if the DSPLL is out of lock.                                                             |
| 0x000C      | 5         | R    | SMBUS\_TIMEOUT | 1 if there is an SMBus timeout error.                                                      |

### Table 15.10. 0x000D INx Loss of Signal (LOS) Alarms

| Reg Address | Bit Field | Type | Setting Name | Description                                          |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------- |
| 0x000D      | 3:0       | R    | LOSIN        | 1 if no clock is present at \[FB\_IN, IN2, IN1, IN0] |

Note that each bit corresponds to the input. The LOS bits are not sticky.

- Input 0 (IN0) corresponds to LOS at 0x000D [0]
- Input 1 (IN1) corresponds to LOS at 0x000D [1]
- Input 2 (IN2) corresponds to LOS at 0x000D [2]
- FB_IN corresponds to LOS at 0x000D[3]
- See also LOSXAXB for LOS at the XAXB input

### Table 15.11. 0x0011 Sticky Versions of Status Bits

| Reg Address | Bit Field | Type | Setting Name        | Description                                                    |
| ----------- | --------- | ---- | ------------------- | -------------------------------------------------------------- |
| 0x0011      | 0         | R/W  | SYSINCAL\_FLG       | Sticky version of SYSINCAL. Write a 0 to clear the flag.       |
| 0x0011      | 1         | R/W  | LOSXAXB\_FLG        | Sticky version of LOSXAXB. Write a 0 to clear the flag.        |
| 0x0011      | 2         | R/W  | LOSREF\_FLG         | Sticky version of LOSREF. Write a 0 to clear the flag.         |
| 0x0011      | 3         | R/W  | LOL\_FLG            | Sticky version of LOL. Write a 0 to clear the flag.            |
| 0x0011      | 5         | R/W  | SMBUS\_TIMEOUT\_FLG | Sticky version of SMBUS\_TIMEOUT. Write a 0 to clear the flag. |

### Table 15.12. 0x0012 INx LOS Flags

| Reg Address | Bit Field | Type | Setting Name | Description                                                     |
| ----------- | --------- | ---- | ------------ | --------------------------------------------------------------- |
| 0x0012      | 3:0       | R/W  | LOSIN\_FLG   | Sticky version of LOS. Write a 0 to clear each individual flag. |

### Table 15.13. 0x0017 Status Flag Interrupt Masks

| Reg Address | Bit Field | Type | Setting Name          | Description                                             |
| ----------- | --------- | ---- | --------------------- | ------------------------------------------------------- |
| 0x0017      | 0         | R/W  | SYSINCAL\_INTR\_MSK   | 1 to mask SYSINCAL\_FLG from causing an interrupt       |
| 0x0017      | 1         | R/W  | LOSXAXB\_INTR\_MSK    | 1 to mask the LOSXAXB\_FLG from causing an interrupt    |
| 0x0017      | 2         | R/W  | LOSREF\_INTR\_MSK     | 1 to mask LOSREF\_FLG from causing an interrupt         |
| 0x0017      | 3         | R/W  | LOL\_INTR\_MSK        | 1 to mask LOL\_FLG from causing an interrupt            |
| 0x0017      | 5         | R/W  | SMB\_TMOUT\_INTR\_MSK | 1 to mask SMBUS\_TIMEOUT\_FLG from causing an interrupt |

These are the interrupt mask bits for the fault flags in Register 0x0011. If a mask bit is set, the alarm will be blocked from causing an interrupt.

### Table 15.14. 0x0018 Interrupt Masks

| Reg Address | Bit Field | Type | Setting Name     | Description                                 |
| ----------- | --------- | ---- | ---------------- | ------------------------------------------- |
| 0x0018      | 3:0       | R/W  | LOSIN\_INTR\_MSK | 1 to mask the interrupt from LOS\_FLG\[3:0] |

- Input 0 (IN0) corresponds to LOSIN_INTR_MSK 0x0018 [0]
- Input 1 (IN1) corresponds to LOSIN_INTR_MSK 0x0018 [1]
- Input 2 (IN2) corresponds to LOSIN_INTR_MSK 0x0018 [2]
- FB_IN corresponds to LOSIN_INTR_MSK 0x0018[3]

### Table 15.15. 0x001C Soft Reset

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                                                                                                                     |
| ----------- | --------- | ---- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x001C      | 0         | S    | SOFT\_RST    | 1 Performs a soft reset. Resets the device while not re-downloading the register configuration from NVM. If output-output skew is needed and VDDOx does not come up before VDD/VDDA then a soft reset will align the output clocks. 0 No effect |

This bits are of type “S”, which is self-clearing.

### Table 15.16. 0x001D FINC, FDEC

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                          |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------- |
| 0x001D      | 0         | S    | FINC         | 1 A rising edge will cause a frequency increment. See also N\_FSTEP\_MSK and Nx\_FSTEPW. 0 No effect |
| 0x001D      | 1         | S    | FDEC         | 1 A rising edge will cause a frequency decrement. See also N\_FSTEP\_MSK and Nx\_FSTEPW. 0 No effect |

### Table 15.17. 0x001E Sync, Power Down and Hard Reset

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                                                                                |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x001E      | 0         | R/W  | PDN          | 1 to put the device into low power mode                                                                                                                                                                    |
| 0x001E      | 1         | R/W  | HARD\_RST    | 1 causes hard reset. The same as power up except that the serial port access is not held at reset. NVM is re-downloaded. This does not self-clear, so after setting the bit it must be cleared. 0 No reset |
| 0x001E      | 2         | S    | SYNC         | 1 to reset all output R dividers to the same state                                                                                                                                                         |

### Table 15.18. 0x0021 Input Clock Selection

| Reg Address | Bit Field | Type | Setting Name     | Description                                                                                                                                                                                                               |
| ----------- | --------- | ---- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0021      | 0         | R/W  | IN\_SEL\_REGCTRL | Selects between register controlled reference clock selection and pin controlled clock selection using IN\_SEL1 and IN\_SEL0 pins: 0 for pin controlled clock selection; 1 for register clock selection via IN\_SEL bits. |
| 0x0021      | 2:1       | R/W  | IN\_SEL          | Selects the reference clock input to the PLL when IN\_SEL\_REGCTRL=1. 0 IN0 1 IN1 2 IN2 3 XA/XB                                                                                                                           |

### Table 15.19. 0x002B SPI 3 vs. 4 Wire

| Reg Address | Bit Field | Type | Setting Name | Description                        |
| ----------- | --------- | ---- | ------------ | ---------------------------------- |
| 0x002B      | 3         | R/W  | SPI\_3WIRE   | 0 for 4-wire SPI, 1 for 3-wire SPI |

### Table 15.20. 0x002C LOS Enable

| Reg Address | Bit Field | Type | Setting Name | Description                                                   |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------- |
| 0x002C      | 3:0       | R/W  | LOS\_EN      | 1 to enable LOS for the inputs other than XAXB; 0 for disable |
| 0x002C      | 4         | R/W  | LOSXAXB\_DIS | 1 to disable LOS for the XAXB input                           |

- Input 0 (IN0): LOS_EN[0]
- Input 1 (IN1): LOS_EN[1]
- Input 2 (IN2): LOS_EN[2]
- FB_IN: LOS_EN[3]

### Table 15.21. 0x002D Loss of Signal Requalification Time

| Reg Address | Bit Field | Type | Setting Name    | Description                  |
| ----------- | --------- | ---- | --------------- | ---------------------------- |
| 0x002D      | 1:0       | R/W  | LOS0\_VAL\_TIME | Clock Input 0                |
|             |           |      |                 | 0 for 2 msec                 |
|             |           |      |                 | 1 for 100 msec               |
|             |           |      |                 | 2 for 200 msec               |
|             |           |      |                 | 3 for one second             |
| 0x002D      | 3:2       | R/W  | LOS1\_VAL\_TIME | Clock Input 1, same as above |
| 0x002D      | 5:4       | R/W  | LOS2\_VAL\_TIME | Clock Input 2, same as above |
| 0x002D      | 7:6       | R/W  | LOS3\_VAL\_TIME | Clock Input 3, same as above |

When an input clock is gone (and therefore has an active LOS alarm), if the clock returns, there is a period of time that the clock must be within the acceptable range before the alarm is removed. This is the LOS_VAL_TIME.

### Table 15.22. 0x002E–0x002F LOS0 Trigger Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x002E      | 7:0       | R/W  | LOS0\_TRG\_THR | 16-bit Threshold Value |
| 0x002F      | 15:8      | R/W  | LOS0\_TRG\_THR |                        |

ClockBuilder Pro calculates the correct LOS register threshold trigger value for Input 0, given a particular frequency plan.

### Table 15.23. 0x0030–0x0031 LOS1 Trigger Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x0030      | 7:0       | R/W  | LOS1\_TRG\_THR | 16-bit Threshold Value |
| 0x0031      | 15:8      | R/W  | LOS1\_TRG\_THR |                        |

ClockBuilder Pro calculates the correct LOS register threshold trigger value for Input 1, given a particular frequency plan.

### Table 15.24. 0x0032–0x0033 LOS2 Trigger Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x0032      | 7:0       | R/W  | LOS2\_TRG\_THR | 16-bit Threshold Value |
| 0x0033      | 15:8      | R/W  | LOS2\_TRG\_THR |                        |

ClockBuilder Pro calculates the correct LOS register threshold trigger value for Input 2, given a particular frequency plan.

### Table 15.25. 0x0034–0x0035 LOS3 Trigger Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x0034      | 7:0       | R/W  | LOS3\_TRG\_THR | 16-bit Threshold Value |
| 0x0035      | 15:8      | R/W  | LOS3\_TRG\_THR |                        |

ClockBuilder Pro calculates the correct LOS register threshold trigger value for Input 3, given a particular frequency plan.

### Table 15.26. 0x0036–0x0037 LOS0 Clear Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x0036      | 7:0       | R/W  | LOS0\_CLR\_THR | 16-bit Threshold Value |
| 0x0037      | 15:8      | R/W  | LOS0\_CLR\_THR |                        |

ClockBuilder Pro calculates the correct LOS register clear threshold value for Input 0, given a particular frequency plan.

### Table 15.27. 0x0038–0x0039 LOS1 Clear Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x0038      | 7:0       | R/W  | LOS1\_CLR\_THR | 16-bit Threshold Value |
| 0x0039      | 15:8      | R/W  | LOS1\_CLR\_THR |                        |

ClockBuilder Pro calculates the correct LOS register clear threshold value for Input 1, given a particular frequency plan.

### Table 15.28. 0x003A–0x003B LOS2 Clear Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x003A      | 7:0       | R/W  | LOS2\_CLR\_THR | 16-bit Threshold Value |
| 0x003B      | 15:8      | R/W  | LOS2\_CLR\_THR |                        |

ClockBuilder Pro calculates the correct LOS register clear threshold value for Input 2, given a particular frequency plan.

### Table 15.29. 0x003C–0x003D LOS3 Clear Threshold

| Reg Address | Bit Field | Type | Setting Name   | Description            |
| ----------- | --------- | ---- | -------------- | ---------------------- |
| 0x003C      | 7:0       | R/W  | LOS3\_CLR\_THR | 16-bit Threshold Value |
| 0x003D      | 15:8      | R/W  | LOS3\_CLR\_THR |                        |

ClockBuilder Pro calculates the correct LOS register clear threshold value for Input 3, given a particular frequency plan.

### Table 15.30. 0x0041–0x0044 LOS Pre-Divider for IN0, IN1, IN3, FB_IN

| Reg Address | Bit Field | Type | Setting Name   | Description                                          |
| ----------- | --------- | ---- | -------------- | ---------------------------------------------------- |
| 0x0041      | 7:0       | R/W  | LOS0\_DIV\_SEL | A pre-divider that is configured by ClockBuilder Pro |
| 0x0042      | 7:0       | R/W  | LOS1\_DIV\_SEL | A pre-divider that is configured by ClockBuilder Pro |
| 0x0043      | 7:0       | R/W  | LOS2\_DIV\_SEL | A pre-divider that is configured by ClockBuilder Pro |
| 0x0044      | 7:0       | R/W  | LOS3\_DIV\_SEL | A pre-divider that is configured by ClockBuilder Pro |

The following are the pre-divider values for the above-listed registers values.

| Register Value (Decimal) | Divider Value |
| ------------------------ | ------------- |
| 0                        | 1 (bypass)    |
| 1                        | 2             |
| 2                        | 4             |
| 3                        | 8             |
| 4                        | 16            |
| 5                        | 32            |
| 6                        | 64            |
| 7                        | 128           |
| 8                        | 256           |
| 9                        | 512           |
| 10                       | 1024          |
| 11                       | 2048          |
| 12                       | 4096          |
| 13                       | 8192          |
| 14                       | 16384         |
| 15                       | 32768         |
| 16                       | 65536         |

### Table 15.31. 0x009E

| Reg Address | Bit Field | Type | Setting Name  | Description                                |
| ----------- | --------- | ---- | ------------- | ------------------------------------------ |
| 0x009E      | 7:4       | R/W  | LOL\_SET\_THR | Configures the loss of lock set thresholds |

### Table 15.32. 0x00E2 Active NVM Bank

| Reg Address | Bit Field | Type | Setting Name      | Description                                                                                                                                                                                                                                                           |
| ----------- | --------- | ---- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00E2      | 7:0       | R    | ACTIVE\_NVM\_BANK | 0x03 when no NVM burn by customer 0x0F when 1 NVM bank has been burned by customer 0x3F when 2 NVM banks have been burned by customer When ACTIVE\_NVM\_BANK = 0x3F, the last bank has already been burned. See for a detailed description of how to program the NVM. |

### Table 15.33. 0x00E3

| Reg Address | Bit Field | Type | Setting Name | Description                              |
| ----------- | --------- | ---- | ------------ | ---------------------------------------- |
| 0x00E3      | 7:0       | R/W  | NVM\_WRITE   | Write 0xC7 to initiate an NVM bank burn. |

### Table 15.34. 0x00E4

| Reg Address | Bit Field | Type | Setting Name    | Description                                                         |
| ----------- | --------- | ---- | --------------- | ------------------------------------------------------------------- |
| 0x00E4      | 0         | S    | NVM\_READ\_BANK | When set, this bit will read the NVM down into the volatile memory. |

### Table 15.35. 0x00F6

| Reg Address | Bit Field | Type | Setting Name    | Description  |
| ----------- | --------- | ---- | --------------- | ------------ |
| 0x00F6      | 0         | R    | REG\_0XF7\_INTR | Set by CBPro |
| 0x00F6      | 1         | R    | REG\_0XF8\_INTR | Set by CBPro |
| 0x00F6      | 2         | R    | REG\_0XF9\_INTR | Set by CBPro |

### Table 15.36. 0x00F7

| Reg Address | Bit Field | Type | Setting Name           | Description  |
| ----------- | --------- | ---- | ---------------------- | ------------ |
| 0x00F7      | 0         | R    | SYSINCAL\_INTR         | Set by CBPro |
| 0x00F7      | 1         | R    | LOSXAXB\_INTR          | Set by CBPro |
| 0x00F7      | 2         | R    | LOSREF\_INTR           | Set by CBPro |
| 0x00F7      | 3         | R    | LOL\_INTR              | Set by CBPro |
| 0x00F7      | 4         | R    | LOSVCO\_INTR           | Set by CBPro |
| 0x00F7      | 5         | R    | SMBUS\_TIME\_OUT\_INTR | Set by CBPro |

### Table 15.37. 0x00F8

| Reg Address | Bit Field | Type | Setting Name | Description  |
| ----------- | --------- | ---- | ------------ | ------------ |
| 0x00F8      | 3:0       | R    | LOS\_INTR    | Set by CBPro |

### Table 15.38. 0x00FE Device Ready

| Reg Address | Bit Field | Type | Name          | Description                                                                                                                                                                                                                    |
| ----------- | --------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x00FE      | 7:0       | R    | DEVICE\_READY | Ready Only byte to indicate device is ready. When read data is 0x0F one can safely read/write registers. This register is repeated on every page therefore a page write is not ever required to read the DEVICE\_READY status. |

### Table 15.39. 0x0102 All Output Clock Driver Disable

| Reg Address | Bit Field | Type | Setting Name  | Description                                                                                                               |
| ----------- | --------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 0x0102      | 0         | R/W  | OUTALL\_DISA- | 0: Disables all output drivers. 1: No output drivers are disabled by this bit, but other signals may disable the outputs. |

### Table 15.40. 0x0103 Clock Output 0A Configs and R0A Divider Configuration

| Reg Address | Bit Field | Type | Setting Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | --------- | ---- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x0103      | 0         | R/W  | OUT0A\_PDN       | Powerdown output driver. 0: Normal Operation (default) 1: Powerdown output driver When powered down, outputs pins will be high impedance with a light pull down effect.                                                                                                                                                                                                                                                  |
| 0x0103      | 1         | R/W  | OUT0A\_OE        | Enable/Disable individual output. 0: Disable output (default) 1: Enable output                                                                                                                                                                                                                                                                                                                                           |
| 0x0103      | 2         | R/W  | OUT0A\_RDIV\_FOR | Force R0A output divider divide-by-2. 0: R0A\_REG sets divide value (default) 1: Divide value forced to divide-by-2 Setting R0A\_REG=0 will not set the divide value to divide-by-2 automatically. OUT0A\_RDIV\_FORCE2 must be set to a value of 1 to force R0A to divide-by-2. Note that the R0A\_REG value will be ignored while OUT0A\_RDIV\_FORCE2 = 1. See R0A\_REG registers, 0x0247-0x0249, for more information. |

### Table 15.41. 0x0104 Clock Output 0A Format

| Reg Address | Bit Field | Type | Setting Name         | Description                                                  |
| ----------- | --------- | ---- | -------------------- | ------------------------------------------------------------ |
| 0x0104      | 2:0       | R/W  | OUT0A\_FORMAT        | 0: Reserved 1: normal differential 2: low power differential 3: reserved 4: LVCMOS 5–7: Reserved |
| 0x0104      | 3         | R/W  | OUT0A\_SYNC\_EN      | 0 disable 1: Enable Enable/disable synchronized (glitchless) operation. When enabled, the power down and output enables are synchronized to the output clock. |
| 0x0104      | 5:4       | R/W  | OUT0A_DIS_STAT<br/>E | Determines the state of an output driver when disabled,<br/>selectable as:<br/>0: Disable in low state<br/>1: Disable in high state<br/>2: Reserved<br/>3: Reserved |
| 0x0104      | 7:6       | R/W  | OUT0A_CMOS_DR<br/>V  | LVCMOS output impedance. See 8.4.8 Output Driver<br/>Settings for LVPECL, LVDS, HCSL, and CML. |

See 8.3 Performance Guidelines for Outputs.

### Table 15.42. 0x0105 Clock Output 0A Amplitude and Common Mode Voltage

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                                                                                                  |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0105      | 3:0       | R/W  | OUT0A\_CM    | This field only applies when OUT0A\_FORMAT=1 or 2. See 8.4.8 Output Driver Settings for LVPECL, LVDS, HCSL, and CML and 8.4.9 Setting the Differential Output Driver to Non-Standard Amplitudes for details of the settings. |
| 0x0105      | 6:4       | R/W  | OUT0A\_AMPL  | This field only applies when OUT0A\_FORMAT=1 or 2. See 8.4.8 Output Driver Settings for LVPECL, LVDS, HCSL, and CML and 8.4.9 Setting the Differential Output Driver to Non-Standard Amplitudes for details of the settings. |

### Table 15.43. 0x0106 Clock Output 0A Mux and Inversion

| Reg Address | Bit Field | Type | Setting Name        | Description                                                                                                                                                           |
| ----------- | --------- | ---- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0106      | 2:0       | R/W  | OUT0A\_MUX\_SEL     | OUT0A output source divider select. This selects the multisynth (N divider) that is connected to the output driver. 0: N0, 1: N1, 2: N2, 3: N3, 4: N4, 5-7: Reserved. |
| 0x0106      | 3         | R/W  | OUT0A\_VDD\_SEL\_EN | Output Driver VDD Select Enable. Set to 1 for normal operation.                                                                                                       |

| Reg Address | Bit Field | Type | Setting Name    | Description                                                                         |
| ----------- | --------- | ---- | --------------- | ----------------------------------------------------------------------------------- |
| 0x0106      | 5:4       | R/W  | OUT0A\_VDD\_SEL | Output Driver VDD Select 0: 3.3V 1: 1.8V 2: 2.5V 3: Reserved                        |
| 0x0106      | 7:6       | R/W  | OUT0A\_INV      | 0: CLK and CLK not inverted 1: CLK inverted 2: CLK and CLK inverted 3: CLK inverted |

Each output can be independently configured to use one of the N0-N4 divider outputs as its source. Nx_NUM and Nx_DEN for each N divider are set in registers 0x0302-0x0337 for N0 to N4. Five different frequencies can be set in the N-dividers (N0-N4) and each of the 12 outputs can be configured to use any of the five different frequencies.

The 12 output drivers are all identical. The single set of descriptions above for output driver 0A applies to the other 11 output drivers.

### Table 15.44. Registers for OUT0,1,2,3,4,5,6,7,8,9,9A as per Above for OUT0A

| Register Address | Description                                                   | (Same as) Address |
| ---------------- | ------------------------------------------------------------- | ----------------- |
| 0x0108           | OUT0\_PDN, OUT0\_OE, OUT0\_RDIV\_FORCE2                       | 0x0103            |
| 0x0109           | OUT0\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV             | 0x0104            |
| 0x010A           | OUT0\_CM, OUT0\_AMPL                                          | 0x0105            |
| 0x010B           | OUT0\_MUX\_SEL, OUT0\_VDD\_SEL\_EN, OUT0\_VDD\_SEL, OUT0\_INV | 0x0106            |
| 0x010D           | OUT1\_PDN, OUT1\_OE, OUT1\_RDIV\_FORCE2                       | 0x0103            |
| 0x010E           | OUT1\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV             | 0x0104            |
| 0x010F           | OUT1\_CM, OUT1\_AMPL                                          | 0x0105            |
| 0x0110           | OUT1\_MUX\_SEL, OUT1\_VDD\_SEL\_EN, OUT1\_VDD\_SEL, OUT1\_INV | 0x0106            |
| 0x0112           | OUT2\_PDN, OUT2\_OE, OUT2\_RDIV\_FORCE2                       | 0x0103            |
| 0x0113           | OUT2\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV             | 0x0104            |
| 0x0114           | OUT2\_CM, OUT2\_AMPL                                          | 0x0105            |
| 0x0115           | OUT2\_MUX\_SEL, OUT2\_VDD\_SEL\_EN, OUT2\_VDD\_SEL, OUT2\_INV | 0x0106            |
| 0x0117           | OUT3\_PDN, OUT3\_OE, OUT3\_RDIV\_FORCE2                       | 0x0103            |
| 0x0118           | OUT3\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV             | 0x0104            |
| 0x0119           | OUT3\_CM, OUT3\_AMPL                                          | 0x0105            |
| 0x011A           | OUT3\_MUX\_SEL, OUT3\_VDD\_SEL\_EN, OUT3\_VDD\_SEL, OUT3\_INV | 0x0106            |
| 0x011C           | OUT4\_PDN, OUT4\_OE, OUT4\_RDIV\_FORCE2                       | 0x0103            |
| 0x011D           | OUT4\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV             | 0x0104            |
| 0x011E           | OUT4\_CM, OUT4\_AMPL                                          | 0x0105            |
| 0x011F           | OUT4\_MUX\_SEL, OUT4\_VDD\_SEL\_EN, OUT4\_VDD\_SEL, OUT4\_INV | 0x0106            |
| 0x0121           | OUT5\_PDN, OUT5\_OE, OUT5\_RDIV\_FORCE2                       | 0x0103            |
| 0x0122           | OUT5\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV             | 0x0104            |

| Register Address | Description                                                  | (Same as) Address |
| ---------------- | ------------------------------------------------------------ | ----------------- |
| 0x0123           | OUT5\_CM, OUT5\_AMPL                                         | 0x0105            |
| 0x0124           | OUT5\_MUX\_SEL, OUT5\_VDD\_SEL\_EN, OUT5\_VDD\_SEL, OUT5\_INV | 0x0106            |
| 0x0126           | OUT6\_PDN, OUT6\_OE, OUT6\_RDIV\_FORCE2                      | 0x0103            |
| 0x0127           | OUT6\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV            | 0x0104            |
| 0x0128           | OUT6\_CM, OUT6\_AMPL                                         | 0x0105            |
| 0x0129           | OUT6\_MUX\_SEL, OUT6\_VDD\_SEL\_EN, OUT6\_VDD\_SEL, OUT6\_INV | 0x0106            |
| 0x012B           | OUT7\_PDN, OUT7\_OE, OUT7\_RDIV\_FORCE2                      | 0x0103            |
| 0x012C           | OUT7\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV            | 0x0104            |
| 0x012D           | OUT7\_CM, OUT7\_AMPL                                         | 0x0105            |
| 0x012E           | OUT7\_MUX\_SEL, OUT7\_VDD\_SEL\_EN, OUT7\_VDD\_SEL, OUT7\_INV | 0x0106            |
| 0x0130           | OUT8\_PDN, OUT8\_OE, OUT8\_RDIV\_FORCE2                      | 0x0103            |
| 0x0131           | OUT8\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV            | 0x0104            |
| 0x0132           | OUT8\_CM, OUT8\_AMPL                                         | 0x0105            |
| 0x0133           | OUT8\_MUX\_SEL, OUT8\_VDD\_SEL\_EN, OUT8\_VDD\_SEL, OUT8\_INV | 0x0106            |
| 0x0135           | OUT9\_PDN, OUT9\_OE, OUT9\_RDIV\_FORCE2                      | 0x0103            |
| 0x0136           | OUT9\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV            | 0x0104            |
| 0x0137           | OUT9\_CM, OUT9\_AMPL                                         | 0x0105            |
| 0x0138           | OUT9\_MUX\_SEL, OUT9\_VDD\_SEL\_EN, OUT9\_VDD\_SEL, OUT9\_INV | 0x0106            |
| 0x013A           | OUT9A\_PDN, OUT9A\_OE, OUT9A\_RDIV\_FORCE2                   | 0x0103            |
| 0x013B           | OUT9A\_FORMAT, \_SYNC\_EN, DIS\_STATE, \_CMOS\_DRV           | 0x0104            |
| 0x013C           | OUT9A\_CM, OUT9A\_AMPL                                       | 0x0105            |
| 0x013D           | OUT9A\_MUX\_SEL, OUT9A\_VDD\_SEL\_EN, OUT9A\_VDD\_SEL, OUT9A\_INV | 0x0106            |

### Table 15.45. 0x013F–0x0140

| Reg Address | Bit Field | Type | Setting Name     | Description                                              |
| ----------- | --------- | ---- | ---------------- | -------------------------------------------------------- |
| 0x013F      | 7:0       | R/W  | OUTX\_ALWAYS\_ON | This setting is managed by CBPro during zero delay mode. |
| 0x0140      | 11:8      | R/W  | OUTX\_ALWAYS\_ON |                                                          |

### Table 15.46. 0x0141

| Reg Address | Bit Field | Type | Setting Name      | Description  |
| ----------- | --------- | ---- | ----------------- | ------------ |
| 0x0141      | 5         | R/W  | OUT\_DIS\_LOL\_MS | Set by CBPro |
| 0x0141      | 7         | R/W  | OUT\_DIS\_MSK\_LO | Set by CBPro |

### Table 15.47. 0x0145 Power Down All Outputs

| Reg Address | Bit Field | Type | Setting Name  | Description                              |
| ----------- | --------- | ---- | ------------- | ---------------------------------------- |
| 0x0145      | 0         | R/W  | OUT\_PDN\_ALL | 0- no effect 1- all drivers powered down |

### Table 15.48. 0x0202-0x0205 XAXB Frequency Adjust

| Reg Address | Bit Field | Type | Setting Name        | Description                                 |
| ----------- | --------- | ---- | ------------------- | ------------------------------------------- |
| 0x0202      | 7:0       | R/W  | XAXB\_FREQ\_OFF-    | 32 bit 2’s complement offset adjustment SET |
| 0x0203      | 15:8      | R/W  | XAXB\_FREQ\_OFF-SET |                                             |
| 0x0204      | 23:16     | R/W  | XAXB\_FREQ\_OFF-SET |                                             |
| 0x0205      | 31:24     | R/W  | XAXB\_FREQ\_OFF-SET |                                             |

The clock that is present on XAXB pins is used to create an internal frequency reference for the PLL. The XAXB_FREQ_OFFSET word is added to the M_NUM to shift the VCO frequency to compensate for a crystal that does not have an 8 pf CL specification.

### Table 15.49. 0x0206 PXAXB Divider

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                               |
| ----------- | --------- | ---- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0206      | 1:0       | R/W  | PXAXB        | Sets the value for the divider on the XAXB input. • 0 = divider value 1 • 1 = divider value 2 • 2 = divider value 4 • 3 = divider value 8 |

The following registers configure the P-dividers, which are located at the four input clocks seen in 3.1 Dividers. ClockBuilder Pro calculates the correct values for the P-dividers. The Px_Update (register 0x0230) bit for the appropriate channel must be updated for the new P value to take effect.

### Table 15.50. 0x0208-0x020D P0 Dividers

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x0208      | 7:0       | R/W  | P0           | 48-bit Integer Number |
| 0x0209      | 15:8      | R/W  | P0           |                       |
| 0x020A      | 23:16     | R/W  | P0           |                       |
| 0x020B      | 31:24     | R/W  | P0           |                       |
| 0x020C      | 39:32     | R/W  | P0           |                       |
| 0x020D      | 47:40     | R/W  | P0           |                       |

### Table 15.51. 0x020E-0x0211 P0 Divider Enable/Set

| Reg Address | Bit Field | Type | Setting Name | Description  |
| ----------- | --------- | ---- | ------------ | ------------ |
| 0x020E      | 7:0       | R/W  | P0\_SET      | Set by CBPro |
| 0x020F      | 15:8      | R/W  | P0\_SET      |              |
| 0x0210      | 23:16     | R/W  | P0\_SET      |              |
| 0x0211      | 31:24     | R/W  | P0\_SET      |              |

### Table 15.52. 0x0212-0x0217 P1 Dividers

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x0212      | 7:0       | R/W  | P1           | 48-bit Integer Number |
| 0x0213      | 15:8      | R/W  | P1           |                       |
| 0x0214      | 23:16     | R/W  | P1           |                       |
| 0x0215      | 31:24     | R/W  | P1           |                       |
| 0x0216      | 39:32     | R/W  | P1           |                       |
| 0x0217      | 47:40     | R/W  | P1           |                       |

### Table 15.53. 0x0218-0x021B P1 Divider Enable/Set

| Reg Address | Bit Field | Type | Setting Name | Description  |
| ----------- | --------- | ---- | ------------ | ------------ |
| 0x0218      | 7:0       | R/W  | P1\_SET      | Set by CBPro |
| 0x0219      | 15:8      | R/W  | P1\_SET      |              |
| 0x021A      | 23:16     | R/W  | P1\_SET      |              |
| 0x021B      | 31:24     | R/W  | P1\_SET      |              |

### Table 15.54. 0x021C-0x0221 P2 Dividers

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x021C      | 7:0       | R/W  | P2           | 48-bit Integer Number |
| 0x021D      | 15:8      | R/W  | P2           |                       |
| 0x021E      | 23:16     | R/W  | P2           |                       |
| 0x021F      | 31:24     | R/W  | P2           |                       |
| 0x0220      | 39:32     | R/W  | P2           |                       |
| 0x0221      | 47:40     | R/W  | P2           |                       |

### Table 15.55. 0x0222-0x0225 P2 Divider Enable/Set

| Reg Address | Bit Field | Type | Setting Name | Description  |
| ----------- | --------- | ---- | ------------ | ------------ |
| 0x0222      | 7:0       | R/W  | P2\_SET      | Set by CBPro |
| 0x0223      | 15:8      | R/W  | P2\_SET      |              |
| 0x0224      | 23:16     | R/W  | P2\_SET      |              |
| 0x0225      | 31:24     | R/W  | P2\_SET      |              |

### Table 15.56. 0x0226-0x022B P3 Dividers

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x0226      | 7:0       | R/W  | P3           | 48-bit Integer Number |
| 0x0227      | 15:8      | R/W  | P3           |                       |
| 0x0228      | 23:16     | R/W  | P3           |                       |
| 0x0229      | 31:24     | R/W  | P3           |                       |
| 0x022A      | 39:32     | R/W  | P3           |                       |
| 0x022B      | 47:40     | R/W  | P3           |                       |

### Table 15.57. 0x022C-0x022F P3 Divider Enable/Set

| Reg Address | Bit Field | Type | Setting Name | Description  |
| ----------- | --------- | ---- | ------------ | ------------ |
| 0x022C      | 7:0       | R/W  | P3\_SET      | Set by CBPro |
| 0x022D      | 15:8      | R/W  | P3\_SET      |              |
| 0x022E      | 23:16     | R/W  | P3\_SET      |              |
| 0x022F      | 31:24     | R/W  | P3\_SET      |              |

### Table 15.58. 0x0230 P Divider Update Bits

| Reg Address | Bit Field | Type | Setting Name | Description                                                  |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------ |
| 0x0230      | 0         | S    | P0\_UPDATE   | Must write a 1 to this bit to cause a change to the P0 divider to take effect. |
| 0x0230      | 1         | S    | P1\_UPDATE   | Must write a 1 to this bit to cause a change to the P1 divider to take effect. |
| 0x0230      | 2         | S    | P2\_UPDATE   | Must write a 1 to this bit to cause a change to the P2 divider to take effect. |
| 0x0230      | 3         | S    | P3\_UPDATE   | Must write a 1 to this bit to cause a change to the P3 divider to take effect. |

Bits 7:4 of this register have no function and can be written to any value

### Table 15.59. 0x0235-0x023A M Divider Numerator

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x0235      | 7:0       | R/W  | M\_NUM       | 44-bit Integer Number |
| 0x0236      | 15:8      | R/W  | M\_NUM       |                       |
| 0x0237      | 23:16     | R/W  | M\_NUM       |                       |
| 0x0238      | 31:24     | R/W  | M\_NUM       |                       |
| 0x0239      | 39:32     | R/W  | M\_NUM       |                       |
| 0x023A      | 43:40     | R/W  | M\_NUM       |                       |

### Table 15.60. 0x023B-0x023E M Divider Denominator

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x023B      | 7:0       | R/W  | M\_DEN       | 32-bit Integer Number |
| 0x023C      | 15:8      | R/W  | M\_DEN       |                       |
| 0x023D      | 23:16     | R/W  | M\_DEN       |                       |
| 0x023E      | 31:24     | R/W  | M\_DEN       |                       |

The M-divider numerator and denominator is determined by ClockBuilder Pro for a given frequency plan.

### Table 15.61. 0x023F M Divider Update Bit

| Reg Address | Bit Field | Type | Setting Name | Description                                                           |
| ----------- | --------- | ---- | ------------ | --------------------------------------------------------------------- |
| 0x023F      | 0         | S    | M\_UPDATE    | Must write a 1 to this bit to cause M divider changes to take effect. |

Bits 7:1 of this register have no function and can be written to any value.

### Table 15.62. 0x0247-0x0248 R0A Divider

| Reg Address | Bit Field | Type | Setting Name | Description                                                  |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------ |
| 0x0247      | 7:0       | R/W  | R0A\_REG     | 24-bit Integer Number. Divide value = (R0A\_REG+1) x 2 To set R0A = 2, set OUT0A\_RDIV\_FORCE2 = 1, and then the R0A\_REG value is irrelevant. When OUT0A_RDIV_FORCE2 = 0, then setting R0A_REG=0 will disable the divider. |
| 0x0248      | 15:8      | R/W  | R0A\_REG     |                                                              |
| 0x0249      | 23:16     | R/W  | R0A\_REG     |                                                              |

The final output R dividers are even dividers beginning with divide-by-2. While all other values follow the formula in the bit description above, divide-by-2 requires an extra bit to be set. For divide-by-2, set OUT0A_RDIV_FORCE2 = 1. See the description for register bit 0x0103[2] in this register map.

The R0-R9A dividers follow the same format as the R0A divider description above.

### Table 15.63. R Dividers for Outputs 0,1,2,3,4,5,6,7,8,9,9A

| Register Address | Setting Name | Size                  | Same as Address |
| ---------------- | ------------ | --------------------- | --------------- |
| 0x024A-0x024C    | R0\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x024D-0x024F    | R1\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x0250-0x0252    | R2\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x0253-0x0255    | R3\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x0256-0x0258    | R4\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x0259-0x025B    | R5\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x025C-0x025E    | R6\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x025F-0x0261    | R7\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x0262-0x0264    | R8\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x0265-0x0267    | R9\_REG      | 24-bit Integer Number | 0x0247-0x0249   |
| 0x0268-0x026A    | R9A_REG      | 24-bit Integer Number | 0x0247-0x0249   |

### Table 15.64. 0x026B–0x0272 Design ID

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                    |
| ----------- | --------- | ---- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| 0x026B      | 7:0       | R/W  | DESIGN\_ID0  | ASCII encoded string defined by CBPro user, with user                                                          |
| 0x026C      | 15:8      | R/W  | DESIGN\_ID1  | defined space or null padding of unused characters. A user will normally include a configuration ID + revision |
| 0x026D      | 23:16     | R/W  | DESIGN\_ID2  | ID. For example, “ULT.1A” with null character padding sets:                                                    |
| 0x026E      | 31:24     | R/W  | DESIGN\_ID3  | DESIGN\_ID0: 0x55                                                                                              |
| 0x026F      | 39:32     | R/W  | DESIGN\_ID4  | DESIGN\_ID1: 0x4C                                                                                              |
| 0x0270      | 47:40     | R/W  | DESIGN\_ID5  | DESIGN\_ID2: 0x54                                                                                              |
| 0x0271      | 55:48     | R/W  | DESIGN\_ID6  | DESIGN\_ID3: 0x2E                                                                                              |
| 0x0272      | 63:56     | R/W  | DESIGN\_ID7  | DESIGN\_ID4: 0x31 DESIGN\_ID5: 0x41 DESIGN\_ID6: 0x00 DESIGN\_ID7: 0x00                                        |

Registers 0x026B - 0x0272 can also be used as User Scratch.

### Table 15.65. 0x0278-0x027C OPN Identifier

| Reg Address | Bit Field | Type | Setting Name | Description                                                      |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------- |
| 0x0278      | 7:0       | R/W  | OPN\_ID0     | OPN unique identifier. ASCII encoded. For example,               |
| 0x0279      | 15:8      | R/W  | OPN\_ID1     | with OPN:                                                        |
| 0x027A      | 23:16     | R/W  | OPN\_ID2     | 5391C-A12345-GM, 12345 is the OPN unique identifier, which sets: |
| 0x027B      | 31:24     | R/W  | OPN\_ID3     | OPN\_ID0: 0x31                                                   |
| 0x027C      | 39:32     | R/W  | OPN\_ID4     | OPN\_ID1: 0x32 OPN\_ID2: 0x33 OPN\_ID3: 0x34 OPN\_ID4: 0x35      |

Part numbers are of the form:

Si&#x3C;Part Num Base>&#x3C;Grade>-&#x3C;Device Revision>&#x3C;OPN ID>-&#x3C;Temp Grade>&#x3C;Package ID>

Examples:

Si5391C-A12345-GM.

Applies to a “custom” OPN (Ordering Part Number) device. These devices are factory pre-programmed with the frequency plan and all other operating characteristics defined by the user’s ClockBuilder Pro project file.

Si5391C-A-GM.

Applies to a “base” or “blank” OPN device. Base devices are factory pre-programmed to a specific base part type (e.g., Si5391 but exclude any user-defined frequency plan or other user-defined operating characteristics selected in ClockBuilder Pro.

### Table 15.66. 0x027D OPN Revision

| Reg Address | Bit Field | Type | Setting Name  | Description                                                                     |
| ----------- | --------- | ---- | ------------- | ------------------------------------------------------------------------------- |
| 0x027D      | 7:0       | R/W  | OPN\_Revision | ClockBuilder Pro sets this value based upon changes to the NVM for a given OPN. |

### Table 15.67. 0x027E Baseline ID

| Reg Address | Bit Field | Type | Setting Name | Description                                                                      |
| ----------- | --------- | ---- | ------------ | -------------------------------------------------------------------------------- |
| 0x027E      | 7:0       | R/W  | BaseLine ID  | An identifier for the device NVM without the frequency plan programmed into NVM. |

### Table 15.68. 0x0302–0x0307 N0 Numerator

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x0302      | 7:0       | R/W  | N0\_NUM      | 44-bit Integer Number |
| 0x0303      | 15:8      | R/W  | N0\_NUM      |                       |
| 0x0304      | 23:16     | R/W  | N0\_NUM      |                       |
| 0x0305      | 31:24     | R/W  | N0\_NUM      |                       |
| 0x0306      | 39:32     | R/W  | N0\_NUM      |                       |
| 0x0307      | 43:40     | R/W  | N0\_NUM      |                       |

The N dividers are interpolative dividers that are used as output dividers that feed into the R dividers. ClockBuilder Pro calculates the correct values for the N-dividers.

### Table 15.69. 0x0308–0x030B N0 Denominator

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x0308      | 7:0       | R/W  | N0\_DEN      | 32-bit Integer Number |
| 0x0309      | 15:8      | R/W  | N0\_DEN      |                       |
| 0x030A      | 23:16     | R/W  | N0\_DEN      |                       |
| 0x030B      | 31:24     | R/W  | N0\_DEN      |                       |

### Table 15.70. 0x030C N0 Divider Update Bit

| Reg Address | Bit Field | Type | Setting Name | Description                                                            |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------- |
| 0x030C      | 0         | S    | N0\_UPDATE   | Must write a 1 to this bit to cause N0 divider changes to take effect. |

This bit is provided so that all of the N0 divider bits can be changed at the same time. First, write all of the new values to the divider; then, set the update bit.

### Table 15.71. N1, N2, N3 Numerator and Denominators

| Register Address | Setting Name | Size                  | Same as Address |
| ---------------- | ------------ | --------------------- | --------------- |
| 0x030D-0x0312    | N1\_NUM      | 44-bit Integer Number | 0x0302-0x0307   |
| 0x0313-0x0316    | N1\_DEN      | 32-bit Integer Number | 0x0308-0x030B   |
| 0x0318-0x031D    | N2\_NUM      | 44-bit Integer Number | 0x0302-0x0307   |
| 0x031E-0x0321    | N2\_DEN      | 32-bit Integer Number | 0x0308-0x030B   |
| 0x0323-0x0328    | N3\_NUM      | 44-bit Integer Number | 0x0302-0x0307   |
| 0x0329-0x032C    | N3\_DEN      | 32-bit Integer Number | 0x0308-0x030B   |
| 0x032E-0x0333    | N4\_NUM      | 44-bit Integer Number | 0x0302-0x0307   |
| 0x0334-0x0337    | N4\_DEN      | 32-bit Integer Number | 0x0308-0x030B   |

### Table 15.72. 0x0317 N1 Divider Update Bit

| Reg Address | Bit Field | Type | Setting Name | Description                                                            |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------- |
| 0x0317      | 0         | S    | N1\_UPDATE   | Must write a 1 to this bit to cause N1 divider changes to take effect. |

### Table 15.73. 0x0322 N2 Divider Update Bit

| Reg Address | Bit Field | Type | Setting Name | Description                                                            |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------- |
| 0x0322      | 0         | S    | N2\_UPDATE   | Must write a 1 to this bit to cause N2 divider changes to take effect. |

### Table 15.74. 0x032D N3 Divider Update Bit

| Reg Address | Bit Field | Type | Setting Name | Description                                                            |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------- |
| 0x032D      | 0         | S    | N3\_UPDATE   | Must write a 1 to this bit to cause N3 divider changes to take effect. |

### Table 15.75. 0x0338 N4 Divider Update Bit

| Reg Address | Bit Field | Type | Setting Name | Description                                                            |
| ----------- | --------- | ---- | ------------ | ---------------------------------------------------------------------- |
| 0x0338      | 0         | S    | N4\_UPDATE   | Must write a 1 to this bit to cause N4 divider changes to take effect. |

### Table 15.76. 0x0338 All N Dividers Update Bit

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                                                                                                                                                         |
| ----------- | --------- | ---- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0338      | 1         | S    | N\_UPDATE    | Writing a 1 to this bit will update all N dividers to the latest value written to them. A specific N divider that has not been changed will not be affected by writing a 1 to this bit. When this bit is written to a 1, all other bits in this byte should only be written to a 0. |

This bit is provided so that all of the divider bits can be changed at the same time. First, write all of the new values to the divider, then set the update bit.

Note: If the intent is to write to the N_UPDATE_ALL to have all dividers update at the same time, then make sure only bit 1 N_UPDATE_ALL bit gets set.

### Table 15.77. 0x0339 FINC/FDEC Masks

| Reg Address | Bit Field | Type | Setting Name  | Description                                                  |
| ----------- | --------- | ---- | ------------- | ------------------------------------------------------------ |
| 0x0339      | 4:0       | R/W  | N\_FSTEP\_MSK | 0 to enable FINC/FDEC updates 1 to disable FINC/FDEC updates |

- Bit 0 corresponds to MultiSynth N0 N_FSTEP_MSK 0x0339[0]
- Bit 1 corresponds to MultiSynth N1 N_FSTEP_MSK 0x0339[1]
- Bit 2 corresponds to MultiSynth N2 N_FSTEP_MSK 0x0339[2]
- Bit 3 corresponds to MultiSynth N3 N_FSTEP_MSK 0x0339[3]
- Bit 4 corresponds to MultiSynth N4 N_FSTEP_MSK 0x0339[4]

### Table 15.78. 0x033B–0x0340 N0 Frequency Step Word

| Reg Address | Bit Field | Type | Setting Name | Description           |
| ----------- | --------- | ---- | ------------ | --------------------- |
| 0x033B      | 7:0       | R/W  | N0\_FSTEPW   | 44-bit Integer Number |
| 0x033C      | 15:8      | R/W  | N0\_FSTEPW   |                       |
| 0x033D      | 23:16     | R/W  | N0\_FSTEPW   |                       |
| 0x033E      | 31:24     | R/W  | N0\_FSTEPW   |                       |
| 0x033F      | 39:32     | R/W  | N0\_FSTEPW   |                       |
| 0x0340      | 43:40     | R/W  | N0\_FSTEPW   |                       |

This is a 44-bit integer value which is directly added (FDEC) or subtracted (FINC) from the Nx_NUM parameter when FINC or FDEC is asserted. ClockBuilder Pro calculates the correct values for the N0 Frequency Step Word. Each N divider has the ability to add or subtract up to a 44-bit value. The Nx_NUM register value does not change when an FINC or FDEC is performed so that the starting point of Nx_NUM is in the Nx_NUM register.

### Table 15.79. Frequency Step Word for N1, N2, N3, N4

| Register Address | Setting Name | Size                  | Same as Address |
| ---------------- | ------------ | --------------------- | --------------- |
| 0x0341-0x0346    | N1\_FSTEPW   | 44-bit Integer Number | 0x033B-0x0340   |
| 0x0347-0x034C    | N2\_FSTEPW   | 44-bit Integer Number | 0x033B-0x0340   |
| 0x034D-0x0352    | N3\_FSTEPW   | 44-bit Integer Number | 0x033B-0x0340   |
| 0x0353-0x0358    | N4\_FSTEPW   | 44-bit Integer Number | 0x033B-0x0340   |

### Table 15.80. 0x090E XAXB Configuration

| Reg Address | Bit Field | Type | Setting Name     | Description                                                                                                                                    |
| ----------- | --------- | ---- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x090E      | 0         | R/W  | XAXB\_EXTCLK\_EN | 0 to use a crystal at the XAXB pins 1 to use an external clock source at the XAXB pins. A singled ended clock must be applied at the XA input. |
| 0x090E      | 1         | R/W  | XAXB\_PDNB       | 0-Power down the oscillator and buffer circuitry at the XA/XB pins 1- No power down                                                            |

### Table 15.81. 0x091C Enable Zero Delay Mode

| Reg Address | Bit Field | Type | Setting Name | Description                                                                 |
| ----------- | --------- | ---- | ------------ | --------------------------------------------------------------------------- |
| 0x091C      | 2:0       | R/W  | ZDM\_EN      | 3 = Zero delay mode. 4 = Normal mode. All other values must not be written. |

### Table 15.82. 0x0943 Status and Control I/O Voltage Select

| Reg Address | Bit Field | Type | Setting Name | Description                                                       |
| ----------- | --------- | ---- | ------------ | ----------------------------------------------------------------- |
| 0x0943      | 0         | R/W  | IO\_VDD\_SEL | 0 for 1.8 V external connections 1 for 3.3 V external connections |

The IO_VDD_SEL configuration bit selects the option of operating the serial interface voltage thresholds from the VDD or the VDDA pin. By default the IO_VDD_SEL bit is set to the VDD option. The serial interface pins are always 3.3 V tolerant even when the device's VDD pin is supplied from a 1.8 V source. When the I2C or SPI host is operating at 3.3 V and the Si5391 IO_VDD_SEL = 1.8 V, the host should write the IO_VDD_SEL configuration bit to the VDDA option. This will ensure that both the host and the serial interface are operating at the optimum voltage thresholds. The IO_VDD_SEL bit also affects the status pin levels and control pin thresholds. When IO_VDD_SEL = 0, the status outputs will have a VOH of ~1.8 V. When IO_VDD_SEL = 1 the status outputs will have a VOH of ~3.3 V. When IO_VDD_SEL=0, the control input pins will have an input threshold based upon the VDD supply voltage of 1.8 V. When IO_VDD_SEL=1, the control input pins will have an input threshold based upon the VDDA supply voltage of 3.3 V. See Table 4 and Table 6 of the Si5391 data sheet for details.

### Table 15.83. 0x0949 Clock Input Control

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                                                                                                                                          |
| ----------- | --------- | ---- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0949      | 3:0       | R/W  | IN\_EN       | Enables for the four inputs clocks, IN0 through FB\_IN. 1 to enable, 0 to disable • Input 0 corresponds to IN\_EN 0x0949 \[0]. • Input 1 corresponds to IN\_EN 0x0949 \[1]. • Input 2 corresponds to IN\_EN 0x0949 \[2]. • FB\_IN corresponds to IN\_EN 0x0949 \[3]. |

### Table 15.84. 0x094A Input Clock Routing Enable

| Reg Address | Bit Field | Type | Setting Name     | Description                                                                                                                                                                                                                                |
| ----------- | --------- | ---- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x094A      | 6:4       | R/W  | INx\_TO\_PFD\_EN | When = 1, enables the routing of the 3 input clocks IN0,1,2 to the Phase Detector. Each bit corresponds to the inputs as follows \[6:4] = \[IN2 IN1 IN0]. IN\_SEL is used to select the input clock that is applied to the phase detector. |

### Table 15.85. 0x095E

| Reg Address | Bit Field | Type | Setting Name | Description  |
| ----------- | --------- | ---- | ------------ | ------------ |
| 0x095E      | 0         | R/W  | M\_INTEGER   | Set by CBPro |

### Table 15.86. 0x0A03 N Divider Clocks

| Reg Address | Bit Field | Type | Name                 | Description                                                                                                                                                                |
| ----------- | --------- | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0A03      | 4:0       | R/W  | N\_CLK\_TO\_OUTX\_EN | Bits in this field correspond to the N dividers as \[N4 N3 N2 N1 N0]. If an N divider is used, the corresponding bit must be 1. See also registers 0x0A05 and 0x0B4A\[4:0] |

### Table 15.87. 0x0A04 N Divider Phase Interpolator Bypass

| Reg Address | Bit Field | Type | Name     | Description                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | --------- | ---- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0A04      | 4:0       | R/W  | N\_PIBYP | Bypasses the Phase Interpolator of the N Multisynth divider. Set to a 1 when the value of N divider is integer and will not be used as a DCO. Set to a 0 when the value of N is fractional (used as a DCO). Slightly lower output jitter may occur when the Phase Interpolator is bypassed (=1). Bits in this field correspond to the N dividers as \[N4 N3 N2 N1 N0] |

A soft reset reg 0x001C [0] should be asserted after changing any of these bits. If it is expected that any of the N dividers will be changing from integer to fractional, it is recommended that the corresponding bits be initialized to 0 so that when the change from integer to fractional occurs there will be no need for a soft reset. For this reason DCO (digitally controlled oscillator) and FOTF (frequency on the fly) applications should have zeros for these bits. See AN858: DCO Applications with Jitter Attenuators.

### Table 15.88. 0x0A05 N Divider Power Down

| Reg Address | Bit Field | Type | Name    | Description                                                                                                                                                                                                            |
| ----------- | --------- | ---- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0A05      | 4:0       | R/W  | N\_PDNB | Powers down the N divider. If an N divider is not used, set the respective bit to 0 to power it down. Bits in this field correspond to the N dividers as \[N4 N3 N2 N1 N0]. See also registers 0x0A03 and 0x0B4A\[4;0] |

### Table 15.89. 0x0A38 N0 Dynamic Phase Adjust Step Size

| Reg Address | Bit Field | Type | Name            | Description                                                  |
| ----------- | --------- | ---- | --------------- | ------------------------------------------------------------ |
| 0x0A38      | 7:0       | R/W  | N0\_PHASE\_STEP | N0 step size from 1 to 255 in units of Tvco, the VCO period. |

N0_PHASE_STEP and N0_PHASE_COUNT are used to produce a phase change anywhere from 0 degrees to 360 degrees with a resolution of the VCO period. N0_PHASE_STEP can be invoked multiple times by using N0_PHASE_COUNT. The phase change is initiated by writing to either N0_PHASE_INC or N0_PHASE_DEC (at addr 0x0A3B). The resulting phase change will be:

N0_PHASE_STEP * N0_PHASE_COUNT * Tvco, for Tvco = 1 / Fvco

### Table 15.90. 0x0A39 N0 Dynamic Phase Adjust Step Size Count

| Reg Address | Bit Field | Type | Name             | Description                                   |
| ----------- | --------- | ---- | ---------------- | --------------------------------------------- |
| 0x0A39      | 7:0       | R/W  | N0\_PHASE\_COUNT | Lower byte of number of N0 step size changes. |
| 0x0A3A      | 15:8      | R/W  | N0\_PHASE\_COUNT | Upper byte of number of N0 step size changes. |

### Table 15.91. 0x0A3B N0 Dynamic Phase Adjust Command

| Reg Address | Bit Field | Type | Name           | Description                              |
| ----------- | --------- | ---- | -------------- | ---------------------------------------- |
| 0x0A3B      | 0         | R/W  | N0\_PHASE\_INC | Writing a 1 initiates a phase increment. |
| 0x0A3B      | 1         | R/W  | N0\_PHASE\_DEC | Writing a 1 initiates a phase decrement. |

Once set, these register bits will self clear as soon as the entire phase adjust sequence has completed.

N1 dynamic phase adjust works the same as N0 dynamic phase adjust (0xA38).

### Table 15.92. 0x0A3C N1 Dynamic Phase Adjust Step Size

| Reg Address | Bit Field | Type | Name            | Description                                                  |
| ----------- | --------- | ---- | --------------- | ------------------------------------------------------------ |
| 0x0A3C      | 7:0       | R/W  | N1\_PHASE\_STEP | N1 step size from 1 to 255 in units of Tvco, the VCO period. |

### Table 15.93. 0x0A3D N1 Dynamic Phase Adjust Step Size Count

| Reg Address | Bit Field | Type | Name             | Description                                   |
| ----------- | --------- | ---- | ---------------- | --------------------------------------------- |
| 0x0A3D      | 7:0       | R/W  | N1\_PHASE\_COUNT | Lower byte of number of N1 step size changes. |
| 0x0A3E      | 15:8      | R/W  | N1\_PHASE\_COUNT | Upper byte of number of N1 step size changes. |

### Table 15.94. 0x0A3F N1 Dynamic Phase Adjust Command

| Reg Address | Bit Field | Type | Name           | Description                              |
| ----------- | --------- | ---- | -------------- | ---------------------------------------- |
| 0x0A3F      | 0         | R/W  | N1\_PHASE\_INC | Writing a 1 initiates a phase increment. |
| 0x0A3F      | 1         | R/W  | N1\_PHASE\_DEC | Writing a 1 initiates a phase decrement. |

N2 dynamic phase adjust works the same as N0 dynamic phase adjust (0xA38).

### Table 15.95. 0x0A40 N2 Dynamic Phase Adjust Step Size

| Reg Address | Bit Field | Type | Name            | Description                                                  |
| ----------- | --------- | ---- | --------------- | ------------------------------------------------------------ |
| 0x0A40      | 7:0       | R/W  | N2\_PHASE\_STEP | N2 step size from 1 to 255 in units of Tvco, the VCO period. |

### Table 15.96. 0x0A41 N2 Dynamic Phase Adjust Step Size Count

| Reg Address | Bit Field | Type | Name             | Description                                   |
| ----------- | --------- | ---- | ---------------- | --------------------------------------------- |
| 0x0A41      | 7:0       | R/W  | N2\_PHASE\_COUNT | Lower byte of number of N2 step size changes. |
| 0x0A42      | 15:8      | R/W  | N2\_PHASE\_COUNT | Upper byte of number of N2 step size changes. |

### Table 15.97. 0x0A43 N2 Dynamic Phase Adjust Command

| Reg Address | Bit Field | Type | Name           | Description                              |
| ----------- | --------- | ---- | -------------- | ---------------------------------------- |
| 0x0A43      | 0         | R/W  | N2\_PHASE\_INC | Writing a 1 initiates a phase increment. |
| 0x0A43      | 1         | R/W  | N2\_PHASE\_DEC | Writing a 1 initiates a phase decrement. |

N3 dynamic phase adjust works the same as N0 dynamic phase adjust (0xA38).

### Table 15.98. 0x0A44 N3 Dynamic Phase Adjust Step Size

| Reg Address | Bit Field | Type | Name            | Description                                                  |
| ----------- | --------- | ---- | --------------- | ------------------------------------------------------------ |
| 0x0A44      | 7:0       | R/W  | N3\_PHASE\_STEP | N3 step size from 1 to 255 in units of Tvco, the VCO period. |

### Table 15.99. 0x0A45 N3 Dynamic Phase Adjust Step Size Count

| Reg Address | Bit Field | Type | Name             | Description                                   |
| ----------- | --------- | ---- | ---------------- | --------------------------------------------- |
| 0x0A45      | 7:0       | R/W  | N3\_PHASE\_COUNT | Lower byte of number of N3 step size changes. |
| 0x0A46      | 15:8      | R/W  | N3\_PHASE\_COUNT | Upper byte of number of N3 step size changes. |

### Table 15.100. 0x0A47 N3 Dynamic Phase Adjust Command

| Reg Address | Bit Field | Type | Name           | Description                              |
| ----------- | --------- | ---- | -------------- | ---------------------------------------- |
| 0x0A47      | 0         | R/W  | N3\_PHASE\_INC | Writing a 1 initiates a phase increment. |
| 0x0A47      | 1         | R/W  | N3\_PHASE\_DEC | Writing a 1 initiates a phase decrement. |

N4 dynamic phase adjust works the same as N0 dynamic phase adjust (0xA38).

### Table 15.101. 0x0A48 N4 Dynamic Phase Adjust Step Size

| Reg Address | Bit Field | Type | Name            | Description                                                  |
| ----------- | --------- | ---- | --------------- | ------------------------------------------------------------ |
| 0x0A48      | 7:0       | R/W  | N4\_PHASE\_STEP | N4 step size from 1 to 255 in units of Tvco, the VCO period. |

### Table 15.102. 0x0A49 N4 Dynamic Phase Adjust Step Size Count

| Reg Address | Bit Field | Type | Name             | Description                                   |
| ----------- | --------- | ---- | ---------------- | --------------------------------------------- |
| 0x0A49      | 7:0       | R/W  | N4\_PHASE\_COUNT | Lower byte of number of N4 step size changes. |
| 0x0A4A      | 15:8      | R/W  | N4\_PHASE\_COUNT | Upper byte of number of N4 step size changes. |

### Table 15.103. 0x0AB N4 Dynamic Phase Adjust Command

| Reg Address | Bit Field | Type | Name           | Description                              |
| ----------- | --------- | ---- | -------------- | ---------------------------------------- |
| 0x0A4B      | 0         | R/W  | N4\_PHASE\_INC | Writing a 1 initiates a phase increment. |
| 0x0A4B      | 1         | R/W  | N4\_PHASE\_DEC | Writing a 1 initiates a phase decrement. |

### Table 15.104. 0x0B2E Synchronous Output Disable Timeout Value

| Reg Address | Bit Field | Type | Name                   | Description                                                                |
| ----------- | --------- | ---- | ---------------------- | -------------------------------------------------------------------------- |
| 0x0B2E      | 6:0       | R/W  | MS\_OD\_G\_TIMEOUT     | Controls the synchronous output disable timeout value during a hard reset. |
| 0x0B2E      | 7         | R/W  | MS\_OD\_G\_TIMEOUT\_EN |                                                                            |

### Table 15.105. 0x0B44 Loss of Signal Clock Disable

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                                                                                                                                                          |
| ----------- | --------- | ---- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0x0B44      | 3:0       | R/W  | PDIV\_ENB    | Clock disable for the fractional divide of the input P dividers. \[P3, P2, P1, P0]. Must be set to 0 if the P divider has a fractional value. 0: Enable the clock to the fractional divide part of the P divider 1: Disable the clock to the fractional divide part of the P divider |

### Table 15.106. 0x0B4A Divider Clock Disables

| Reg Address | Bit Field | Type | Setting Name | Description                                                                                                                                         |
| ----------- | --------- | ---- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0B4A      | 4:0       | R/W  | N\_CLK\_DIS  | Controls the clock to the N divider. If an N divider is used the corresponding bit must be 0. \[N3 N2 N1 N0]. See also registers 0x0A03 and 0x0A05. |

### Table 15.107. 0x0B57

| Reg Address | Bit Field | Type | Name                 | Description  |
| ----------- | --------- | ---- | -------------------- | ------------ |
| 0x0B57      | 7:0       | R/W  | VCO\_RESET\_CAL-CODE | 12-bit value |
| 0x0B58      | 11:8      | R/W  | VCO\_RESET\_CAL-CODE |              |

## 16. Revision History

Revision 0.5

July 2020

- Updated Grade P Rules in Section 7.2.3 Clock Inputs on IN2, IN1, IN0

Revision 0.4

March 2020

- Updated Grade P Rules in Section 2.2 Si5391P Grade Frequency Plan Rules
- Changed preamble and post-amble registers and updated figure 5.1 in Section 5. Dynamic PLL Changes
- Combined section on XAXB references (Section 12 in Rev0.3) with the sections in 7. Clock Inputs and removed it
- Removed section on Static Skew and added details about Dynamic Skew 8.7 Output Delay Control
- Corrected the ZDM register table
- Removed tool version tables
- Removed SOFTCAL setting in register 0x001C[5]
- Register 0x001E bit field 1 type changed from S to R/W and bit 2 description changed
- Corrected description for register 0x00E2
- Changed Type of registers 0x00F6, 0x00F7 and 0x00F8 from R/W to R
- Added table for register 0x00FE (Device Ready)
- Changes made to Page 1 register tables (16.40 through 16.44) to include OUT0A and OUT9A
- Corrected text below table 16.43
- Added description for register 0x0141
- Removed the User Scratch table
- Added table 16.49 for registers 0x013F and 0x0140
- Description and type added for P0, P1, P2 and P3 divider Enable/Set tables
- Description added for table 16.59 for M divider numerator
- Changes made to R divider register tables (16.62 and 16.63) to include OUT0A and OUT9A
- Text below table 16.62 updated
- Text added below Table 16.65 to indicate User Scratch
- Text added below table 16.76 about register 0x0338
- Removed tables about Nx_DELAY registers
- Description added for register 0x095E
- Text added below table 16.87 about register 0x0A04
- Added tables to describe the dynamic skew control registers
- Added description for register 0x0B2E
- Added description for register 0x0B44

Revision 0.3

September 2019

- Updated Grade P Rules in Section 2.2 Si5391P Grade Frequency Plan Rules
- Updated the Dynamic PLL Section to clarify the 625 ms wait time for the P grade.

Revision 0.2

July 2018

- Updated Section 2.1 Grade P (Precision) Restrictions and Requirements

Revision 0.1

June 2018

- Initial Release
