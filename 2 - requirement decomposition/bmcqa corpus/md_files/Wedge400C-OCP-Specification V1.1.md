# Wedge 400C Design Specification V1.1

Author: George Kurio, Hardware Engineer, Meta

Author: Lingjun Wu, Hardware Engineer, Meta

Author: Ivy Wu, Mechanical Engineer, Meta

Author: Vignesh Vijayanath, TPM, Meta

Open Compute Project • Wedge 400C Design Specification
## Contents

1. License 4
    1.2 Acknowledgements 5
2. OCP Tenets Compliance 5
    2.1 Openness 5
    2.2 Efficiency 6
    2.3 Impact 6
    2.4 Scale 6
3. Revision Table 7
4. Introduction 8
    4.1. Scope 8
    4.2. System Description 8
    4.3. Common Terms 9
5. System Architecture 10
    5.1. System Architecture 10
    5.2. Chassis Design 11
    5.3. Data Plane 13
    5.3.1. Switch Element.......................................................................................................14
    5.3.2. Front Port-mapping................................................................................................14
    5.3.3. Switch ASIC Port-mapping....................................................................................15
    5.4. Control Plane 22
    5.4.1. Clock Tree...............................................................................................................23
    5.4.2. PCIe Assignments..................................................................................................23
    5.5. Chassis management Plane 24
    5.5.1. BSM (BMC Storage Module)..................................................................................25
    5.5.2. UART Connection ..................................................................................................29
    5.5.3. OOB Switch ............................................................................................................30
    5.5.4. RackMon Interface .................................................................................................30
    5.6. System Powerup Sequence 31
    5.7. Switch Main Board (SMB) 32
    5.7.1. Block Diagram of SMB...........................................................................................33
    5.7.2. BMC I2C diagram ...................................................................................................33
    5.7.3. BMC I2C mapping ..................................................................................................34
6. 5.7.4. BMC SPI diagram ...................................................................................................35
    5.7.5. PWR_CPLD Registers............................................................................................36
    Register 0x25: GB_FREQ_SET - PUC_DIFF_REG. ........................................................39
    Table 12 – GB Frequency Register....................................................................................39
    5.7.6. SMB sys_CPLD Registers .....................................................................................39
    Register 0x70 Scratchpad Register................................................................................51
    5.8. System Control Module (SCM) 51
    5.8.1. System Control Module Block Diagram................................................................51
    5.8.2. 10G KR interface ....................................................................................................52
    5.8.3. SCM LPC bus .........................................................................................................52
    5.8.4. COM-Express CPU Module....................................................................................52
    5.8.5. SCM Sys_CPLD Registers.....................................................................................54
    5.9. Fan Control Module(FCM) and Fan-tray 61
    5.9.1. Fan_CPLD Registers..............................................................................................62
    5.9.2. Fan Control Mechanism.........................................................................................63
    5.10. LED 72
    5.10.1. LED Controlling....................................................................................................72
    5.10.2. System Information LED (SIM)............................................................................73
    5.10.3. Management OOB port LEDs ..............................................................................75
    5.10.4. QSFP Port LEDs ...................................................................................................75
  6. Modules Interfaces 77

    6.1. Interfaces between SCM and SMB 77
    6.2. Interfaces between FMC and SMB 77
    6.3. Interfaces between PDB and SMB 78
    6.4. Interfaces between Rackmon board and SMB 78
    6.5. Interfaces between Timing board and SMB 78
  7. Transceivers and cables 79
  8. Wedge400C Power and Mechanical 80

    8.1. DC/DC Power Extension Module (PEM) 80
    8.2. AC/DC PSU 80
    8.3. Power Circuits Design Target 83
    8.4. Power Tree 83
    8.5. Voltage Detection Sensors 85
    8.6. Current Detection Sensors 86
  9. Thermal design 88

    9.1. Fan tray 88
    9.2. Temperature Sensors 90
  10. Regulatory Compliance Requirements 91

    10.1. CE Declaration to the following Regulatory Directives by ODMs 91
    10.2. Safety Certification 91
    10.3. EMC Certification 91
    10.4. Immunity Levels 92
    10.5. Sound 92
    10.6. Environmental Compliance 93
  11. Labels and Markings 94

    11.1. PCBA Labels and Markings 94
    11.2. Chassis Labels and Markings 94
  12. References (OPTIONAL) 95

    Appendix A - Requirements for IC Approval 96
    Appendix B _ - OCP Supplier Information (to be provided by the Supplier of Product within 120 
    days) 96

## 1. License

Contributions to this Specification are made under the terms and conditions set forth in Open Web Foundation Contributor License Agreement (“OWF CLA 1.0”) (“Contribution License”) by:

Meta Platforms, Inc.

You can review the applicable Specification License(s) executed by the above referenced contributors to this Specification on the OCP website at http://www.opencompute.org/participate/legal-documents/

Notes:

- 1) The following clarifications, which distinguish technology licensed in the Contribution License and/or Specification License from those technologies merely referenced (but not licensed), were accepted by the Incubation Committee of the OCP: None
- 2) The above license does not apply to the Appendix or Appendices. The information in the Appendix or Appendices is for reference only and non‑normative in nature.

NOTWITHSTANDING THE FOREGOING LICENSES, THIS SPECIFICATION IS PROVIDED BY OCP "AS IS" AND OCP EXPRESSLY DISCLAIMS ANY WARRANTIES (EXPRESS,

IMPLIED, OR OTHERWISE), INCLUDING IMPLIED WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR A PARTICULAR PURPOSE, OR TITLE, RELATED TO THE SPECIFICATION. NOTICE IS HEREBY GIVEN, THAT OTHER RIGHTS NOT GRANTED AS SET FORTH ABOVE, INCLUDING WITHOUT LIMITATION, RIGHTS OF THIRD PARTIES WHO DID NOT EXECUTE THE ABOVE LICENSES, MAY BE IMPLICATED BY THE IMPLEMENTATION OF OR COMPLIANCE WITH THIS SPECIFICATION. OCP IS NOT RESPONSIBLE FOR IDENTIFYING RIGHTS FOR WHICH A LICENSE MAY BE REQUIRED IN ORDER TO IMPLEMENT THIS SPECIFICATION. THE ENTIRE RISK AS TO IMPLEMENTING OR OTHERWISE USING THE SPECIFICATION IS ASSUMED BY YOU. IN NO EVENT WILL OCP BE LIABLE TO YOU FOR ANY MONETARY DAMAGES WITH RESPECT TO ANY CLAIMS RELATED TO, OR ARISING OUT OF YOUR USE OF THIS SPECIFICATION, INCLUDING BUT NOT LIMITED TO ANY LIABILITY FOR LOST PROFITS OR ANY CONSEQUENTIAL, INCIDENTAL, INDIRECT, SPECIAL OR PUNITIVE DAMAGES OF ANY CHARACTER FROM ANY CAUSES OF ACTION OF ANY KIND WITH RESPECT TO THIS SPECIFICATION, WHETHER BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, AND EVEN IF OCP HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### 1.2 Acknowledgements

The Contributors of this Specification would like to acknowledge the following companies for their feedback: List all companies or individuals who may have assisted you with the specification by providing feedback and suggestions but did not provide any IP.

## 2. OCP Tenets Compliance

Note: The ideals behind open sourcing stipulate that everyone benefits when we share and work together. Any open source project is designed to promote sharing of design elements with peers and to help them understand and adopt those contributions. There is no purpose in sharing if all parties aren't aligned with that philosophy. The IC will look beyond the contribution for evidence that the contributor is aligned with this philosophy. The contributor actions, past and present, are evidence of alignment and conviction to all the tenets.

### 2.1 Openness

The measure of openness is the ability of a third party to build, modify, or personalize the device or platform from the contribution. OCP strives to achieve completely open platforms, inclusive of all programmable devices, firmware, software, and all mechanical and electrical design elements. Any software utilities necessary to modify or use design contributions should also be open sourced. Barriers to achieving this goal should be constantly addressed and actions taken to remove anything that prevents an open platform. Openness can also be demonstrated through collaboration and willingness to share, seek feedback, and accept changes to design and specification contributions under consideration.

W400C: The electrical design and mechanical design of W400C is fully open, and all the PCB and chassis design files have been included in the design package.

### 2.2 Efficiency

Continuous improvement has been a fundamental value of the industry. New contributions (and updates to existing contributions) shall be more efficient than existing or prior generation contributions. Efficiency can be measured in many ways - OpEx and CapEx reduction, performance, capacity, power or water consumption, raw materials, utilization, size or floorspace are some examples. The goal is to express efficiency with clear metrics, valued by end-users, when the contribution is proposed.

W400C: The system comes in a 2RU form factor, slightly larger than to W100S, its 32 x 100G predecessor, while quadrupling the switching throughput both in terms of bandwidth and packets per second. The SCM is FRU-able in W400C, which increases the efficiency in fleet maintenance.

### 2.3 Impact

OCP contributions should have a transformative impact on the industry. This impact can come from introducing new technology, time-to-market advantage of technology, and/or enabling technology through supply chains that deliver to many customers in many regions of the world. New technologies are impactful when such technology is enabled through a global supply channel. One example is the NIC 3.0 specification which achieved global impact by having over 12 companies author, adopt, and supply products that conformed to the specification. Another example is emerging and open security features that establish and verify trust of a product.

W400C leverages the latest generation of switch ASIC, utilizes the 50G PAM4 SerDes technology at scale, and achieves efficiency gains outlined above.

### 2.4 Scale

OCP contributions must have sufficient enabling, distribution and sales support (pre and post) to scale to Fortune 100 as well as large hyperscale customers. Demonstration of this tenet can be accomplished by providing sales data or by providing go-to-market plans that involve either platform/component providers or systems integrator/VAR (direct and/or channel). Platform/component providers or systems integrators/VARs that can use this contribution to obtain product recognition (OCP Accepted™ or OCP Inspired™) and create Integrated Solutions which would also demonstrate scale. Software projects can also demonstrate this tenet when software is adopted across business segments or geographies, when software is a key factor in accelerating new technology, or when software provides scale of new hardware which meets OCP tenets.

W400C: It is designed with FRU-able switch control module (microserver), fan, and PSU for easy field maintenance. There are multiple hardware sensors built-in, and OpenBMC has necessary utilities for hardware monitoring. It has been and will continue to be deployed as a top of rack switch in large quantities.

## 3. Revision Table

| Date      | Revision # | Author       | Description                       |
| --------- | ---------- | ------------ | --------------------------------- |
| 1/14/2022 | V1.0       | George Kurio | Facebook->Meta                    |
| 1/31/2022 | V1.1       | George Kurio | Added license and tenets sections |

## 4. Introduction

### 4.1. Scope

The purpose of this document is to provide a system description of the Meta Wedge400C platform. This document also introduces Wedge400C’s software accessible interfaces and required software actions to properly manage the hardware at the system level.

### 4.2. System Description

Wedge400C is Meta’s new generation Top of Rack switch. It can be used as rack (OpenRack v2) switch of data center network of Meta. The main attributes are:

- Box Size
- 87.5mm(H) x 440mm(W) x 558.8 mm(D)
- Traffic Ports
- 16 x QSFP-DD: 400G/200G/100G ports
- 32 x QSFP56: 200GE/100GE ports or 2*50GE/4*25GE/4*10GE breakout ports
- Management Ports
- one RJ45 as RS232 console port to BMC.
- One RJ45 as OOB GE management port, it supports 1000M/100M/10M Base-T.
- USB 2.0 compatible, supports OCP debug card.
- Rackmon: 3 x RJ45 as RS485 ports, 1 x RJ45 as GPIO.
- Switch Main Board (SMB)
- Switch Main Board has Switch ASIC, BMC, and front panel ports.
- Data plane:
- Switching ASIC: Cisco Q200L, 12.8Tbps, 256*50G PAM4 SERDES.
- Management Plane:
- BMC: Aspeed AST2520
- Located on SMB board
- UART mux for supporting sol.sh
- I2C system management bus
- JTAG controller for programming CPLDs
- 128MB flashes and 8G eMMC for BMC, located on SCM, a.k.a. BMC Storage Module (BSM).
- GbE Switch: for all COM-e, BMC, and front RJ45 OOB port (one of the SGMII interfaces reserved to Rackmon connector for future use to replace the GPIO port)
- System Controller Module (SCM)

• Minilake, developed for Meta, as industrial standard COM-Express CPU module, Type 7.

• SCM is pluggable on rear side.

• One M.2 SSD slot:

- NMVe PCIe 3.0 x4;

• One M.2 BSM slot:

- BMC Storage Module, it includes 2 flashes and 1 eMMC;

### 4.3. Common Terms

The following terms are used in Wedge400C project:

- • 100GE – 100 Gigabit Ethernet
- • 200GE – 200 Gigabit Ethernet
- • 400GE – 400 Gigabit Ethernet
- • SMB – Switch Main Board
- • SCM – System Controller Module
- • FCM – Fan Controller Module
- • PDB – Power Distribution board
- - o PDB-T – Power Distribution board, this is for top PSU/PEM plugged in.
- o PDB-B – Power Distribution board, this is for bottom PSU/PEM plugged in.

• COM-E – COM-Express CPU module
- • PSU – Power Supply Unit
- • PEM – Power Extension Module
- • QSFP28 – Quad Small Form-factor Pluggable (QSFP) at 4 x 28Gbps, used for 100GBE
- • QSFP56 – Quad Small Form-factor Pluggable (QSFP) at 4 x 56Gbps, used for 200GBE
- • QSFP-DD – Quad Small Form-factor Pluggable Double Density at 8 x 56Gbps, used for 400GBE
- • BMC -- Baseboard Management Controller
- • BSM -- BMC Storage Module
- • Rackmon – Rack Monitor Interface

Date: 1/31/2022    Page 9Open Compute Project • Wedge 400C Design Specification

## 5. System Architecture

### 5.1. System Architecture

Wedge400C is a single switch ASIC modular system, it only has one 12.8T switch ASIC, one System Control Module (SCM) and one BMC. It has four 80mm x 80mm x 80mm CR fan trays to cool the system. The following picture shows the system diagram of Wedge400C switch:

#### Figure 1: System architecture of Wedge400C

DC/DC to Q200L

The System Control Module (SCM) carries one COM-e Broadwell-DE CPU module, and can be plugged into the chassis from rear side. The Broadwell-DE CPU module provides the control function of Wedge400C.

Switch Main Board (SMB) is fixed to the chassis, it consists of switch ASIC, BMC system, and 
connectors to SCM. The switch ASIC is controlled by Broadwell-DE CPU of SCM through PCIe 
Gen3 interface.

### 5.2. Chassis Design

Wedge400C is standard 19” wide, 2-RU height modular switch.

#### Figure 2: Wedge400C Chassis top View

| Fan Modules                       | PSU/PEM           |   |
| --------------------------------- | ----------------- | - |
| SCM                               | Fan Control Board |   |
| SMB                               | PDBs              |   |
| Vertical PCB                      | PSU/PEM           |   |
|                                   | Air Channel       |   |
| For Rackmon Connectors, USB, LEDs |                   |   |

#### Figure 3: Wedge400C with ORv2 Tray

Wedge400/Wedge400C System

ORv2 Power Cable

ORv2 Tray

Rackmon Extension Cables

Ground Cable

#### Figure 4: Wedge400C SCM module

M.2 BSM

NVMe

Date: 1/31/2022

Page 12Open Compute Project • Wedge 400C Design Specification

#### Figure 5: Wedge 400C Front View

#### Figure 6: Wedge 400C Rear View

### 5.3. Data Plane

Wedge 400C has 12.8T switch ASIC as the main data plane chip. The switch ASIC supports 32 x 400G port configuration, or 64 x 200G port configuration, or 128 x 100G port configuration.

#### 5.3.1. Switch Element

Wedge400C uses the Meta unique switch element to form the fabric. One switch element has one BMC, one CPU module and one switch ASIC. This unique switch element architecture makes our data center network disaggregated, easily managed and easy to scale. Wedge400C is one switch element which can support 16 x 400/200/100G + 32 x 200/100G. It’s designed to be used as the Top of Rack switch for ORv2 in Meta data centers.

##### Figure 7: Switch Element

BMC

| 400G-#1 |           | 400G-#2  |          |
| ------- | --------- | -------- | -------- |
| PCIe    | Switching | COM      | ASIC     |
| EXP     | 12.8T     | 400G-#16 | 200G-#1  |
|         |           | 200G-#2  | 200G-#32 |

#### 5.3.2. Front Port-mapping

In Wedge400C system, the logic connection of switching ASIC port mapping is shown below:

##### Figure 8: Front port Connection to Switching ASIC

| Q200L  | A1    |       |       |
| ------ | ----- | ----- | ----- |
| IFG 11 | IFG 0 |       |       |
| IFG 10 | IFG 1 |       |       |
| IFG 9  |       | IFG 2 |       |
| IFG 8  |       | IFG 3 |       |
| IFG 7  | IFG 6 | IFG 5 | IFG 4 |

| 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      | 10     | 11     | 12     | 13     | 14     | 15     | 16     |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   | Q-DD   |
| 17     | 19     | 21     | 23     | 25     | 27     | 29     | 31     | 33     | 35     | 37     | 39     | 41     | 43     | 45     | 47     |
| QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 |
| 18     | 20     | 22     | 24     | 26     | 28     | 30     | 32     | 34     | 36     | 38     | 40     | 42     | 44     | 46     | 48     |
| QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 | QSFP56 |

There are 256 SERDES lanes from switching ASIC to the front panel traffic ports. The following table shows the port mapping of ASIC SERDES and ports.

#### 5.3.3. Switch ASIC Port-mapping

There are 16 QSFP-DD ports and 32 QSFP56 ports on Wedge400C. The front panel placement is shown as below.

##### Figure 9: Wedge400C Faceplate Port Numbering

| QDD\_P1  | QDD\_P2  | QDD\_P3  | QDD\_P4  | QDD\_PS  | QDD\_P6  | QDD\_P7  | QDD\_P8  | QDD\_P9  | QDD\_P10 | QDD\_P11 | QDD\_P12 | QDD\_P13 | QDD\_P14 | QDD\_P15 | QDD\_P16 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| Q56\_P17 | Q56\_P19 | Q56\_P21 | Q56\_P23 | Q56\_P25 | Q56\_P27 | Q56\_P29 | Q56\_P31 | Q56\_P33 | Q56\_P35 | Q56\_P37 | Q56\_P39 | Q56\_P41 | Q56\_P43 | Q56\_P45 | Q56\_P47 |
| Q56\_P18 | Q56\_P20 | Q56\_P22 | Q56\_P24 | Q56\_P26 | Q56\_P28 | Q56\_P30 | Q56\_P32 | Q56\_P34 | Q56\_P36 | Q56\_P38 | Q56\_P40 | Q56\_P42 | Q56\_P44 | Q56\_P46 | Q56\_P48 |

The routing connections from switch ASIC to front panel connector are indicated in table below.

##### Table 1: switch ASIC SerDes Lane and P/N swap list

| IFG Number | GB TX TD Ln | PN Swap | GB RX RX Ln | P/N Swap | Physical Port No. | Lane |
| ---------- | ----------- | ------- | ----------- | -------- | ----------------- | ---- |
| IFG 0      | 00          | Y       | 01          | N        | Q56\_P39          | 1    |
|            | 01          | N       | 02          | N        |                   | 2    |
|            | 02          | Y       | 00          | N        |                   | 3    |
|            | 03          | N       | 03          | Y        |                   | 4    |
|            | 04          | N       | 04          | N        | Q56\_P40          | 1    |
|            | 05          | N       | 05          | Y        |                   | 2    |
|            | 06          | N       | 07          | N        |                   | 3    |
|            | 07          | N       | 06          | Y        |                   | 4    |
|            | 14          | N       | 13          | N        | QDD\_P12          | 1    |
|            | 15          | Y       | 15          | Y        |                   | 2    |
|            | 12          | N       | 14          | Y        |                   | 4    |
|            | 13          | N       | 12          | Y        |                   | 4    |
|            | 10          | N       | 11          | N        |                   | 5    |
|            | 11          | Y       | 09          | Y        |                   | 6    |
|            | 08          | N       | 10          | Y        |                   | 7    |
|            | 09          | N       | 08          | Y        |                   | 8    |
|            | 22          | Y       | 20          | N        | QDD\_11           | 1    |
|            | 23          | N       | 21          | N        |                   | 2    |
|            | 21          | N       | 22          | N        |                   | 3    |
|            | 20          | N       | 23          | N        |                   | 4    |
|            | 19          | Y       | 16          | N        |                   | 5    |
|            | 18          | Y       | 19          | Y        |                   | 6    |
|            | 16          | Y       | 18          | N        |                   | 7    |
|            | 17          | N       | 17          | Y        |                   | 8    |

| IFG 1 | 01   | N    | 03   | Y    | QDD\_P16 | 1    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 00   | N    | 00   | Y    |          | 2    |
|       | 03   | Y    | 01   | N    |          | 3    |
|       | 02   | N    | 02   | Y    |          | 4    |
|       | 06   | Y    | 04   | Y    |          | 5    |
|       | 07   | N    | 05   | N    |          | 6    |
|       | 04   | N    | 06   | Y    |          | 7    |
|       | 05   | Y    | 07   | Y    |          | 8    |
|       | 11   | Y    | 10   | N    | Q56\_P48 | 1    |
|       | 10   | N    | 09   | N    |          | 2    |
|       | 08   | Y    | 08   | Y    |          | 3    |
|       | 09   | N    | 11   | Y    |          | 4    |

| IFG 1 | 14   | N    | 12   | Y    | Q56_P47  | 1    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 15   | Y    | 13   | Y    |          | 2    |
|       | 12   | N    | 14   | Y    |          | 3    |
|       | 13   | Y    | 15   | Y    |          | 4    |
|       | 21   | Y    | 20   | N    | QDD\_P15 | 1    |
|       | 20   | Y    | 21   | N    |          | 2    |
|       | 22   | Y    | 22   | Y    |          | 3    |
|       | 23   | Y    | 23   | N    |          | 4    |
|       | 19   | N    | 16   | Y    |          | 5    |
|       | 18   | Y    | 17   | N    |          | 6    |
|       | 17   | Y    | 18   | Y    |          | 7    |
|       | 16   | N    | 19   | Y    |          | 8    |

| IFG 2 | 01   | Y    | 01   | Y    | Q56\_P46 | 1    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 00   | Y    | 02   | N    |          | 2    |
|       | 02   | N    | 00   | N    |          | 3    |
|       | 03   | N    | 03   | Y    |          | 4    |
|       | 05   | Y    | 04   | Y    | Q56\_P45 | 1    |
|       | 04   | Y    | 05   | Y    |          | 2    |
|       | 06   | N    | 06   | Y    |          | 3    |
|       | 07   | N    | 07   | Y    |          | 4    |

| IFG 2 | 11   | N    | 11   | Y    | Q56\_P43 | 1    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 10   | N    | 09   | N    |          | 2    |
|       | 08   | N    | 08   | Y    |          | 3    |
|       | 09   | N    | 10   | N    |          | 4    |
|       | 13   | Y    | 12   | Y    | Q56\_P44 | 1    |
|       | 12   | Y    | 13   | N    |          | 2    |

| IFG 2 | 14   | N    | 14   | N    |          | 3    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 15   | N    | 15   | N    |          | 4    |
|       | 23   | Y    | 23   | Y    | QDD\_P14 | 1    |
|       | 22   | N    | 20   | Y    |          | 2    |
|       | 20   | N    | 22   | N    |          | 3    |
|       | 21   | Y    | 21   | N    |          | 4    |
|       | 18   | Y    | 19   | Y    |          | 5    |
|       | 19   | N    | 16   | Y    |          | 6    |
|       | 17   | N    | 18   | N    |          | 7    |
|       | 16   | N    | 17   | N    |          | 8    |
| IFG 3 | 00   | Y    | 03   | Y    | QDD\_P13 | 1    |
|       | 01   | N    | 00   | Y    |          | 2    |
|       | 02   | Y    | 02   | N    |          | 3    |
|       | 03   | N    | 01   | N    |          | 4    |
|       | 04   | N    | 04   | Y    |          | 5    |
|       | 05   | N    | 07   | Y    |          | 6    |
|       | 06   | Y    | 06   | N    |          | 7    |
|       | 08   | N    | 08   | Y    | Q56\_P42 | 1    |
|       | 09   | Y    | 09   | N    |          | 2    |
|       | 10   | Y    | 11   | N    |          | 3    |
|       | 11   | N    | 10   | Y    |          | 4    |
|       | 12   | N    | 12   | Y    | Q56_P41  | 1    |
|       | 13   | N    | 14   | N    |          | 2    |
|       | 14   | N    | 15   | Y    |          | 3    |
|       | 15   | N    | 13   | N    |          | 4    |
| IFG 4 | 01   | N    | 00   | N    | Q56\_P38 | 1    |
|       | 00   | N    | 01   | Y    |          | 2    |
|       | 03   | N    | 03   | N    |          | 3    |
|       | 02   | N    | 02   | N    |          | 4    |
|       | 04   | N    | 04   | Y    | Q56_P37  | 1    |
|       | 05   | Y    | 05   | Y    |          | 2    |
|       | 07   | N    | 06   | Y    |          | 3    |
|       | 06   | N    | 07   | N    |          | 4    |
|       | 08   | Y    | 11   | N    | Q56_P35  | 1    |
|       | 09   | N    | 09   | Y    |          | 2    |
|       | 10   | N    | 08   | Y    |          | 3    |
|       | 11   | N    | 10   | Y    |          | 4    |

| IFG 4 | 12   | Y    | 12   | Y    | Q56\_P36 | 1    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 13   | N    | 13   | Y    |          | 2    |
|       | 14   | N    | 14   | N    |          | 3    |
|       | 15   | Y    | 15   | Y    |          | 4    |
| IFG 5 | 06   | N    | 06   | Y    | QDD\_P10 | 1    |
|       | 07   | Y    | 05   | Y    |          | 2    |
|       | 04   | Y    | 07   | Y    |          | 3    |
|       | 05   | N    | 04   | Y    |          | 4    |
|       | 02   | N    | 02   | N    |          | 5    |
|       | 03   | N    | 01   | N    |          | 6    |
|       | 01   | N    | 00   | Y    |          | 7    |
|       | 00   | N    | 03   | N    |          | 8    |
|       | 08   | Y    | 08   | N    | Q56\_P33 | 1    |
|       | 09   | N    | 11   | N    |          | 2    |
|       | 10   | N    | 09   | N    |          | 3    |

| IFG 5 | 11   | N    | 10   | N    |          | 4    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 12   | N    | 12   | Y    | Q56\_P34 | 1    |
|       | 13   | N    | 15   | Y    |          | 2    |
|       | 14   | Y    | 14   | Y    |          | 3    |
|       | 15   | N    | 13   | Y    |          | 4    |
|       | 22   | N    | 22   | N    | QDD\_P9  | 1    |
|       | 23   | N    | 21   | Y    |          | 2    |
|       | 20   | N    | 20   | N    |          | 3    |
|       | 21   | N    | 23   | Y    |          | 4    |
|       | 19   | Y    | 17   | N    |          | 5    |
|       | 18   | N    | 18   | N    |          | 6    |
|       | 16   | N    | 16   | Y    |          | 7    |
|       | 17   | N    | 19   | Y    |          | 8    |
| IFG 6 | 02   | N    | 00   | N    | Q56\_P30 | 1    |
|       | 03   | N    | 01   | N    |          | 2    |
|       | 00   | N    | 02   | Y    |          | 3    |
|       | 01   | Y    | 03   | N    |          | 4    |

| IFG 6 | 06   | N    | 07   | N    | Q56\_P29 | 1    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 07   | N    | 05   | N    |          | 2    |
|       | 04   | N    | 06   | N    |          | 3    |
|       | 05   | N    | 04   | Y    |          | 4    |
|       | 08   | Y    | 09   | Y    | QDD\_P8  | 1    |
|       | 09   | N    | 11   | N    |          | 2    |

| IFG 6 | 10   | N    | 10   | Y    |          | 3    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 11   | N    | 08   | N    |          | 4    |
|       | 12   | N    | 14   | Y    |          | 5    |
|       | 13   | N    | 15   | N    |          | 6    |
|       | 14   | N    | 13   | Y    |          | 7    |
|       | 15   | N    | 12   | N    |          | 8    |
|       | 16   | N    | 16   | N    | Q56\_P32 | 1    |
|       | 17   | N    | 17   | N    |          | 2    |
|       | 18   | N    | 18   | Y    |          | 3    |
|       | 19   | N    | 19   | N    |          | 4    |
|       | 22   | N    | 22   | N    | Q56\_P31 | 1    |
|       | 23   | N    | 20   | N    |          | 2    |
|       | 20   | Y    | 21   | N    |          | 3    |
|       | 21   | N    | 23   | N    |          | 4    |
| IFG 7 | 02   | N    | 02   | Y    | Q56\_P28 | 1    |
|       | 03   | N    | 03   | N    |          | 2    |
|       | 00   | N    | 00   | Y    |          | 3    |
|       | 01   | N    | 01   | N    |          | 4    |
|       | 07   | N    | 07   | Y    | Q56\_P29 | 1    |
|       | 06   | N    | 05   | Y    |          | 2    |
|       | 05   | Y    | 04   | Y    |          | 3    |

| IFG7 | 04   | N    | 06   | Y    |          | 4    |
| ---- | ---- | ---- | ---- | ---- | -------- | ---- |
|      | 08   | N    | 09   | Y    | QQDD\_P7 | 1    |
|      | 09   | N    | 10   | N    |          | 2    |
|      | 10   | Y    | 08   | N    |          | 3    |
|      | 11   | Y    | 11   | N    |          | 4    |
|      | 13   | N    | 14   | N    |          | 4    |
|      | 12   | N    | 13   | Y    |          | 5    |
|      | 14   | N    | 12   | N    |          | 6    |
|      | 15   | N    | 15   | Y    |          | 7    |
| IFG8 | 00   | N    | 01   | N    | Q56\_23  | 1    |
|      | 01   | N    | 03   | Y    |          | 2    |
|      | 02   | N    | 00   | Y    |          | 3    |

| IFG8 | 03   | N    | 02   | N    |         | 4    |
| ---- | ---- | ---- | ---- | ---- | ------- | ---- |
|      | 04   | N    | 04   | N    | QDD\_P4 | 1    |
|      | 05   | N    | 06   | N    |         | 2    |
|      | 06   | N    | 07   | N    |         | 3    |
|      | 07   | N    | 05   | N    |         | 4    |

| IFG8 | 14   | N    | 14   | Y    | QDD\_P4  | 1    |
| ---- | ---- | ---- | ---- | ---- | -------- | ---- |
|      | 15   | N    | 13   | N    |          | 2    |
|      | 12   | N    | 15   | N    |          | 3    |
|      | 13   | N    | 12   | Y    |          | 4    |
|      | 08   | N    | 09   | Y    |          | 5    |
|      | 09   | N    | 10   | N    |          | 6    |
|      | 10   | Y    | 08   | N    |          | 7    |
|      | 11   | N    | 11   | Y    |          | 8    |
| IFG9 | 02   | Y    | 00   | N    | Q56\_P20 | 1    |
|      | 03   | N    | 03   | N    |          | 2    |
|      | 00   | N    | 01   | N    |          | 3    |
|      | 01   | Y    | 02   | Y    |          | 4    |
|      | 06   | N    | 06   | Y    | Q56\_P19 | 1    |
|      | 07   | N    | 05   | N    |          | 2    |
|      | 04   | N    | 04   | Y    |          | 3    |
|      | 05   | N    | 07   | N    |          | 4    |
|      | 08   | N    | 10   | Y    | QDD\_P3  | 1    |
|      | 09   | Y    | 09   | N    |          | 2    |
|      | 10   | N    | 11   | N    |          | 3    |

|       | 11   | N    | 08   | Y    |          | 4    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 12   | N    | 13   | Y    |          | 5    |
|       | 13   | N    | 14   | Y    |          | 6    |
|       | 14   | N    | 12   | N    |          | 7    |
|       | 15   | N    | 15   | Y    |          | 8    |
|       | 18   | N    | 16   | N    | Q56\_P22 | 1    |
|       | 19   | N    | 18   | N    |          | 2    |
|       | 16   | N    | 19   | N    |          | 3    |
|       | 17   | N    | 17   | N    |          | 4    |
|       | 22   | N    | 23   | N    | Q56\_P21 | 1    |
|       | 23   | Y    | 20   | Y    |          | 2    |
|       | 20   | N    | 22   | Y    |          | 3    |
|       | 21   | N    | 21   | N    |          | 4    |
| IFG10 | 03   | Y    | 00   | Y    | Q56\_P18 | 1    |
|       | 02   | N    | 02   | Y    |          | 2    |

| IFG10 | 01   | Y    | 01   | Y    |          | 3    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 00   | N    | 03   | N    |          | 4    |
|       | 04   | Y    | 04   | N    | Q56\_P17 | 1    |
|       | 05   | N    | 06   | Y    |          | 2    |

| IFG10 | 07   | Y    | 05   | Y    |          | 3    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 06   | N    | 07   | N    |          | 4    |
|       | 09   | Y    | 08   | N    | QDD\_P1  | 1    |
|       | 08   | N    | 09   | Y    |          | 2    |
|       | 11   | Y    | 11   | Y    |          | 3    |
|       | 10   | N    | 10   | Y    |          | 4    |
|       | 14   | N    | 14   | N    |          | 5    |
|       | 15   | N    | 13   | Y    |          | 6    |
|       | 12   | Y    | 12   | Y    |          | 7    |
|       | 13   | Y    | 15   | N    |          | 8    |
|       | 16   | Y    | 19   | Y    | QDD\_P2  | 1    |
|       | 17   | N    | 17   | N    |          | 2    |
|       | 18   | Y    | 18   | N    |          | 3    |
|       | 19   | N    | 16   | Y    |          | 4    |
|       | 21   | N    | 20   | Y    |          | 5    |
|       | 20   | N    | 22   | Y    |          | 6    |
|       | 22   | N    | 21   | N    |          | 7    |
|       | 23   | N    | 23   | Y    |          | 8    |
| IFG11 | 00   | N    | 00   | N    | QDD\_P5  | 1    |
|       | 01   | N    | 01   | N    |          | 2    |
|       | 02   | N    | 03   | N    |          | 3    |
|       | 03   | N    | 02   | Y    |          | 4    |
|       | 05   | N    | 07   | N    |          | 5    |
|       | 04   | Y    | 05   | N    |          | 6    |
|       | 06   | N    | 06   | Y    |          | 7    |
|       | 07   | N    | 04   | N    |          | 8    |
|       | 10   | N    | 10   | N    | Q56\_P26 | 1    |

| IFG11 | 11   | Y    | 09   | N    |          | 2    |
| ----- | ---- | ---- | ---- | ---- | -------- | ---- |
|       | 09   | Y    | 11   | N    |          | 3    |
|       | 08   | N    | 08   | Y    |          | 4    |
|       | 14   | N    | 15   | N    | Q56\_P25 | 1    |
|       | 15   | N    | 13   | Y    |          | 2    |
|       | 12   | Y    | 14   | N    |          | 3    |
|       | 13   | N    | 12   | N    |          | 4    |
|       | 20   | Y    | 22   | Y    | QDD\_P6  | 1    |
|       | 21   | Y    | 20   | N    |          | 2    |
|       | 22   | N    | 21   | Y    |          | 3    |
|       | 23   | Y    | 23   | N    |          | 4    |

| IFG11 | 16   | N    | 18   | Y    |      | 5    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
|       | 17   | N    | 16   | N    |      | 6    |
|       | 19   | Y    | 17   | Y    |      | 7    |
|       | 18   | N    | 19   | Y    |      | 8    |

### 5.4. Control Plane

Main control plane features are listed below:

- COM-Express BW-DE CPU module
- 8mm mating distance.
- Implemented on SCM
- BMC as management entity to control Switch ASIC and COM-E CPU module
- Enable/disable power of switch ASIC or COM-e
- OOB ethernet to front port
- Console port to front port
- SMB bus and I2C bus to SCM COM-E CPU module
- Front panel management and debug interface
- Meta 2nd generation debug connector
- PCIe Interface
- Switch ASIC: PCIe x2 gen3
- 2 pcs of DOM FPGAs: PCIe x 1/2 gen1/2
- NVMe: PCIe x4 gen3
- PCIe clock is from COM-E module
- LPC bus
- SCM COMe LPC bus control the following device
- BMC on SMB
- OOB Ethernet (BCM5389)
- 8-port OOB switch on SMB
- BMC GBE ethernet interface
- BMC RGMII interface
- SCM COM-E ethernet interface
- Switch ASIC management GBE port(SGMII)
- Front RJ45 OOB ethernet interface
- Two ports reserved for RackMon
- USB
- COM-E is root-complex port
- 3-port USB hub on SMB
- BMC USB slave port
- Meta OCP debug USB from the USB HUB

#### 5.4.1. Clock Tree

The following diagram shows the clock design in the system:

##### Figure 10: Clock Tree

| PCIE Clock                  |                  | 100MHz              |                     | RGMII reference clock |
| --------------------------- | ---------------- | ------------------- | ------------------- | --------------------- |
| 100MHz                      | Difference       | Dom FPGA 1#         | BCM54616S           | 25MHz                 |
| Difference                  | 100MHz           | 1#                  | BCM5389             |                       |
| SI53108                     | Difference       | Dom FPGA 2#         |                     |                       |
| COME                        | 8 output         | 100MHz              | BMC reference clock |                       |
| Difference                  | Gibraltar        | 24MHz               | OSC                 | SE                    |
| BCM5389                     | Difference       | NVMe M.2            |                     |                       |
| Serdes clock and Core clock | 156.25MHz        | Gibraltar           | 25MHz               |                       |
| x4                          | IFG REF CLK      | OSC                 | SE                  | TI                    |
| Difference                  | x 4              |                     | CDC304PW            | DOM FPGA 1#           |
| XTAL                        | 48MHz            | 156.25MHz           |                     | 4 output              |
| DOM FPGA 2#                 | 12 output        | 50MHz               | x1                  |                       |
| Difference                  |                  | Core clock          | Not Pop             |                       |
| OSC                         |                  | Not Pop             | TBD                 |                       |
| OSC                         | SE               | FCB CPLD            |                     |                       |
| OOB reference clock         | 25MHz            | USB reference clock |                     |                       |
| 25MHz                       | SE               | BCM5389             |                     |                       |
| SE                          | 25MHz            | XTAL                | 24MHz               | USB Hub               |
| 25MHz                       | SE               | BCM54616S           | 3#                  |                       |
| 1#                          | CDC304PW         | 25MHz               | SE                  | BCM54616S             |
|                             | 2#               | Component on SCM    |                     |                       |
|                             | Component on SMB |                     |                     |                       |
|                             | Component on FCB |                     |                     |                       |

#### 5.4.2. PCIe Assignments

The following diagram shows the PCIe port assignments from Broadwell-DE to GB, DOM FPGAs and NVMe SSD.

##### Figure 11: PCIe Diagram

PCIE And M.2 channel assignment

M.2

| PCIE\_TX/RX\[20:23] | PCIE\_TX/RX\[24:27] | PCIE\_TX/RX\[16:17] | PCIE\_TX/RX\[28:29] |
| ------------------- | ------------------- | ------------------- | ------------------- |
| 2                   | Gen3 x4             | Gen1 x2             | Gen1 x2             |
| GB                  | NVMe                | DOM FPGA 1#         | DOM FPGA 2#         |

### 5.5. Chassis management Plane

BMC on SMB works as the chassis management module, Chassis management bus is I2C, and the management bus can access the following modules/components:

#### 5.5.1. BSM (BMC Storage Module)

The BSM module was introduced to support FB security requirement. It contains NOR flashes (primary and secondary) and eMMC on a daughter card for easily removing and shredding by ERAD team when the unit goes through RMA. This daughter card is based on M.2 form factor and connector. Here is the diagram of BSM module:

##### Figure 12: BSM Diagram

| M.2 Type A key 2260 H-8.5mm |                     |
| --------------------------- | ------------------- |
| A-Key                       |                     |
| BMC\_EMMC\_RST\_N           | BMC\_EMMC\_CMD      |
| BMC\_EMMC\_Cu               | BMC\_FW\_SPI\_CO\_N |
| EMMC                        | BMC\_SpI \_ RSt     |
| PWR State s Led             |                     |
| MTFCBGACAALT-AMIT           | BMC\_SPL\_ \_"P\_N  |
| SPI FLASH                   | W25O256JVFIQ        |
| BMC\_EMMC\_DO               |                     |
| BMC\_EMMC\_DI               | Main                |
| BMC\_EMMC\_DZ               |                     |
| BMC\_EMMC\_D3               |                     |
| BMC\_FW\_SPI\_CLK           | BMC\_FW\_SPL\_Mosi  |
| BMC\_FW\_SPI\_Miso          |                     |
| XPJR3V\_BMC (2AJ            | SPI FLASH           |
| FRU                         | BMC\_FW\_SPL\_CI\_N |
| I2C EEPROM                  | BMC\_Spil ?\_Rst    |
| AT24C64D                    | EMC\_SPL\_?\_WP\_N  |

The components are all placed on top side to simplify the manufacturing process. Based on the placement, 2260 form factor is selected. The I2C interface is routed to the M.2 connector on SCM. An EEPROM is used for FRU info, located on M.2 card, accessible from BMC.

##### Figure 13: BSM PCB Design

Pinout definition (Based on A-key):

##### Table 2:M.2 Pin Definition

| 74 | BMC\_+3.3V        |
| -- | ----------------- |
| 75 | GND               |
| 73 | NC                |
| 72 | BMC\_+3.3V        |
| 71 | BMC\_EMMC\_D0     |
| 70 | NC                |
| 69 | GND               |
| 68 | NC                |
| 67 | BMC\_EMMC\_D1     |
| 66 | BMC\_EMMC\_RST\_N |
| 65 | BMC\_EMMC\_D2     |

| 64 | NC                                      |
| -- | --------------------------------------- |
| 63 | GND                                     |
| 62 | NC                                      |
| 61 | BMC\_EMMC\_D3                           |
| 60 | NC                                      |
| 59 | BMC\_EMMC\_CMD                          |
| 58 | BMC\_EMMC\_D4 (Reserved)                |
| 57 | GND                                     |
| 56 | BMC\_EMMC\_D5 (Reserved)                |
| 55 | BMC\_EMMC\_CLK                          |
| 54 | BMC\_EMMC\_D6 (Reserved)                |
| 53 | NC                                      |
| 52 | BMC\_EMMC\_D7 (Reserved)                |
| 51 | GND                                     |
| 50 | NC                                      |
| 49 | PERp0 (Reserved)                        |
| 48 | NC                                      |
| 47 | PERn0 (Reserved)                        |
| 46 | EEPROM\_WP                              |
| 45 | GND                                     |
| 44 | ALERT# (Reserved)                       |
| 43 | PETp0 (Reserved)                        |
| 42 | SMB\_DATA (3.3V)                        |
| 41 | PETn0 (Reserved)                        |
| 40 | SMB\_CLK (3.3V)                         |
| 39 | FRU\_EEPROM\_ADDR                       |
| 38 | (Floating on MB: 0xAC; GND on MB: 0xA8) |
| 37 | BMC\_FW\_SPI\_CS0\_N                    |
| 36 | GND                                     |
| 35 | BMC\_FW\_SPI\_CS1\_N                    |
| 34 | REFCLKp (Reserved)                      |
| 33 | GND                                     |
| 32 | REFCLKn (Reserved)                      |
| 31 | BMC\_FW\_SPI\_CLK                       |

| 30 | GND                  |
| -- | -------------------- |
| 29 | GND                  |
| 28 | BMC\_SPI\_0\_HOLD\_N |
| 27 | BMC\_FW\_SPI\_MOSI   |
| 26 | BMC\_SPI\_1\_HOLD\_N |
| 25 | BMC\_FW\_SPI\_MISO   |
| 24 | GND                  |
| 23 | GND                  |
| 22 | USB\_D+ (Reserved)   |
| 21 | BMC\_SPI\_1\_RST     |
| 20 | USB\_D- (Reserved)   |
| 19 | BMC\_SPI\_2\_RST     |
| 18 | GND                  |
| 17 | NC                   |
| 16 | EMMC\_PRESENT\_N     |
| 15 | A-Key                |
| 14 | A-Key                |
| 13 | A-Key                |
| 12 | A-Key                |
| 11 | A-Key                |
| 10 | A-Key                |
| 9  | A-Key                |
| 8  | A-Key                |
| 7  | GND                  |
| 6  | NC                   |
| 5  | BMC\_SPI\_1\_WP\_N   |
| 4  | BMC\_+3.3V           |
| 3  | BMC\_SPI\_2\_WP\_N   |
| 2  | BMC\_+3.3V           |
| 1  | GND                  |

As BMC is on SMB and it’s not easy to access if BMC flash and eMMC were located on SMB, so physically this daughter card (BSM, BMC Storage Module) is located on SCM as SCM is a FRU, and users can easily pull out the SCM card, and then take the BSM module out for ERAD/replacement. Here is the picture of W400 BSM module:

##### Figure 14:BSM proto picture

#### 5.5.2. UART Connection

The following diagram shows UART connections of front console port, uS and BMC’s UART ports.

##### Figure 15:UART Diagram

|     | 3     | COME board | 83   | UART                            | LPC         |
| --- | ----- | ---------- | ---- | ------------------------------- | ----------- |
| 8   | 3     | 83         | R8   | SCM\_UART5\_SEL/SCM\_UART2\_SEL | System CPLD |
| 82  | R LPC | UART2      | Mux  | Bz                              | UART5       |
| 8zs | BMC   | Uart       | 8242 | DS]+                            | Debug       |

USB3.0 Console Debug RJ45 card

#### 5.5.3. OOB Switch

The following diagram shows the OOB switch connections.

##### Figure 16:OOB Diagram

| 1OGbase-KR           | MCO               | TH3        |
| -------------------- | ----------------- | ---------- |
| Reserved for RackMon | Configure SPI     | Mux        |
| SGMII 6              | SGMII 7           | SGMII 3    |
| RGMII                | RGMII             | RGMII2     |
| BCM5389              | SGMII 4           | 1OOOBASE-X |
| BCM54616S            | RGMII             | RGMIII     |
| AST2520              |                   |            |
| W2C 10               | I2C 3             |            |
| SGMIO                | SGMII             | SGMI5      |
| RGMII                | 12C               |            |
| EZPROM               | PCA9548           |            |
| SGMII                | SGMII             |            |
| BCM54616S            | I2C               | EZPROM     |
| BCM54616S            | EZPROM            |            |
| 10/100/1OOOBASE-T    | 10/100/1OOOBASE-T | PCA9548    |

#### 5.5.4. RackMon Interface

The following diagram shows the RackMon interface in system.

##### Figure 17:Rackmon Diagram

### 5.6. System Powerup Sequence

Wedge400C has a PWR CPLD design to enable remotely power cycling the whole system. The powerup sequencer controls the major power rails coming up in the right sequence. The hot swap controller is designed for FRUs like SCM. Here is the diagram showing the detailed HW design:

#### Figure 18:Wedge400C power control/sequence diagram

| BMC       | COME    |   |   |
| --------- | ------- | - | - |
| USB\_2A   | USB Hub |   |   |
| USB Mux   | 2       |   |   |
| E         | F8      | 8 | 2 |
| Max3485   | x1      | 3 |   |
| Rack RJ45 | x4      |   |   |

### 5.7. Switch Main Boar (SMB)

Switch Main Board has two major function blocks:

- Data plane function with 12.8T Switch ASIC;
- Management plane function with BMC AST2520 system;
- BMC supports TPM 2.0 through I2C device SLB 9670VQ2.0.

SMB also provides DOM FPGA function for SCM CPU to access QSFP modules through PCIe.

Here is high level DOM FPGA diagram:

#### Figure 19: DOM FPGA Diagram

| LED Ctrl   | LED Stream | LED Ctrl   | LED Stream |     |
| ---------- | ---------- | ---------- | ---------- | --- |
| General    | Registers  | General    | Registers  |     |
| PCle       | Wishbone   | Module     | Mux        |     |
| DOM Engine | SFP 12C    | DOM Engine | SFP I2C    |     |
| 12C        | 12C        | Slave      | Slave      |     |
| #0         | @SFP       | @SFP       | X24        | X2A |

#### 5.7.1. Block Diagram of SMB

The following diagram shows the diagram of Switch Main Board (SMB).

SCM connector

##### Figure 20: Switch Main Board Diagram

| BMC     | USB Hub    | 1            | g                      |
| ------- | ---------- | ------------ | ---------------------- |
| USB     | SGMIIO     | USB 2.0 Down | 3#                     |
| SGMII   | SGMIIS     | OOB switch   | Uart                   |
| PG      | Reset      | #            | #                      |
| SGMII3  | BCM5389    | Mux          | monitor                |
| USB Mux | 1          | 8            | 1                      |
| SGMII4  | RGML       | System CPLD  | 1OOOBASE-T: ISO buffer |
| 8       | 8          | 3            | Phy\_                  |
| 3       | enable     | Decoder      | 8                      |
| 1       | Board type | 8            | Version                |
| E       | RGMII      | 2            | RGMII                  |
| 8       | 8          | ISMI         | 2                      |
| 34      | \&a        | BMG          | AST2520                |
| CPVR    | 8          | 2            | UART\_1                |
| 2       | PCA9555    | 28           | 8                      |
| g       | 1          | DOM FPGA A/B |                        |
| 2       | Gibraltar  | lw           |                        |
| Rack    | USB        | Pure         | RJ45                   |
| 205     | jb         | Mon          | 3.0                    |
| RJ45    | WIMag      | 16           | QSFP-DD                |
| 32      | QSFP-56    |              |                        |

#### 5.7.2. BMC I2C diagram

The following table shows the I2C topology of BMC.

##### Figure 21: SMB I2C Diagram

| Component on SCM | Component on FCB | 4GIqC   | DC lo       | RMPTRCPLD  | 12C Piojrerrn | 0,5n05  | 24C6-   | ZACEA | ZACE  | ZACr4  | ADMIZTF | OXAE | Lx4J | Zciz | cuhcTOFPIQ | |
| ---------------- | ---------------- | ------- | ----------- | ---------- | ------------- | ------- | ------- | ----- | ----- | ------ | ------- | ---- | ---- | ---- | ---------- |---|
| Component on SMB | Component on PDB | lo      |             |            |               |         |         |       |       |        |         |      |      |      |            | |
| DQuFPGA          | CCAu             | Dcu     | #CuAou      | Tmmna Bojm | Clack         | CcHux   |         |       |       |        |         |      |      |      |            | |
| 12C\_13          | 1C\_10           | LZC B   | COM-E Board | BMC        | 8             | J       |         |       |       |        |         |      |      |      |            | |
| POR1224          | SCH CPLD         | ILN75B  | USB J       | 6          | EZPRO         | 2       |         |       |       |        |         |      |      |      |            | |
| Wc               | ISLLJIJ          | u2kJule | PCna53-|    | Buoud      | PCA9SU        | FPGA 1# | FPGA 2# | 1354  | ECCoe | RC Cue |         |      |      |      |            |
| I2cHux           | IZCMux           | Hdswo   | 087258      | OSFP-DD    | 0sppes        | \`16    | OS-P-DD |       |       |        |         |      |      |      |            | |

#### 5.7.3. BMC I2C mapping

##### Table 3: BMC I2C address table

| HW Bus                               | SW Bus         | Address | Component                                       | Board   |
| ------------------------------------ | -------------- | ------- | ----------------------------------------------- | ------- |
| I2c\_1                               |                | 0x20    | Com-e EC                                        | SCM     |
| I2c\_2                               |                | 0x2F    | IR35215MTRPBF(XP3R3V\_RIGHT/XP0R75V\_PCIE)I2C   | SMB     |
|                                      |                | 0x47    | IR35215MTRPBF(XP3R3V\_RIGHT/XP0R75V\_PCIE)PMbus |         |
|                                      |                | 0x35    | IR35215MTRPBF(XP3R3V\_LEFT/XP0R94V\_VDDA)PMbus  |         |
|                                      |                | 0x4D    | IR35215MTRPBF(XP3R3V\_LEFT/XP0R94V\_VDDA)PMbus  |         |
|                                      |                | 0x0E    | PXE1211(XP1R2V\_HBM/XP1R15V\_VDDCK)I2C          |         |
|                                      |                | 0x28    | XDPE132G5C-G000 (GB Core Voltage)I2C            |         |
|                                      |                | 0x40    | XDPE132G5C-G000 (GB Core Voltage)PMbus          |         |
|                                      |                | 0x3A    | POWR1220                                        |         |
| I2c\_3                               |                | 0x3e    | SCM CPLD                                        | SCM     |
|                                      |                | 0x70    | PCA9548                                         | SCM     |
| I2c_3 <br/>0x70 <br/>I2C <br/>Switch | Channel1, 0x01 | 0x10    | ADM1278                                         | SCM     |
|                                      | Channel2, 0x02 | 0x4C    | TMP75#1                                         |         |
|                                      |                | 0x4D    | TMP75#2                                         |         |
|                                      | Channel4, 0x08 | 0x52    | 24C64 (SCM\_Inv)                                |         |
|                                      | Channel5, 0x10 | 0x50    | NU                                              |         |
|                                      | Channel6,0x20  |         | NVME                                            |         |
|                                      | Channel7, 0x40 | 0x56    | BSM EEPROM                                      |         |
|                                      |                | 0x2E    | BSM TPM 2.0                                     |         |
|                                      | Channel8, 0x80 | 0x6c    | SI53108(Clock buffer)                           |         |
| I2c\_4                               |                | 0x48    | TMP75#1                                         | SMB     |
|                                      |                | 0x49    | TMP75#2                                         |         |
|                                      |                | 0x4A    | TMP75#3                                         |         |
|                                      |                | 0x4B    | TMP75#4                                         |         |
|                                      |                | 0x4C    | TMP421 for intake air                           |         |
|                                      |                | 0x4E    | TMP421 for intake air                           |         |
|                                      |                | 0x2A    | GB I2C                                          |         |
| I2c\_5                               |                | 0x54    | OCP debug card                                  | SMB     |
|                                      |                | 0X27    | TCA9555                                         | SMB     |
| I2C\_6                               |                | 0x60    | DOM\_FPGA\_2                                    | SMB     |
| I2c\_7                               |                | 0x21    | PCA9534 (8-bit Borad ID)                        | SMB     |
|                                      |                | 0x20    | PCA9535 (LEDs)                                  | RackMon |
|                                      |                | 0x51    | 24C64 (SMB\_Inv)                                | SMB     |
| I2c\_8                               |                | 0x20    | SLB9645 (TPM)                                   | SMB     |

| I2c\_9                               |                | 0x70 | PCA9548                                 | SMB  |
| ------------------------------------ | -------------- | ---- | --------------------------------------- | ---- |
| I2c_9 <br/>0x70 <br/>I2C <br/>Switch | Channel1, 0x01 | 0x58 | AC PSU1 MCU/DC PSU 1 Hot swap           | SMB  |
|                                      |                | 0x50 | EEPROM                                  |      |
|                                      |                | 0x18 | PEM 1 Thermal sensor                    |      |
|                                      | Channel2, 0x02 | 0x58 | AC PSU2 MCU/DC PSU 2 Hot swap           |      |
|                                      |                | 0x50 | EEPROM                                  |      |
|                                      |                | 0x18 | PEM 1 Thermal sensor                    |      |
|                                      | Channel3, 0x4  | 0x50 | 24c02 (BMC RGMII PHY BCM54616S EEPROM ) |      |
|                                      | Channel4, 0x8  | 0x50 | 24c02 (BMC MDI PHY BCM54616S EEPROM )   |      |
|                                      | Channel5, 0x10 | 0x54 | NU                                      |      |
|                                      | Channel6, 0x20 |      | Reserved PWR\_CPLD\_I2C\_Programming    |      |
|                                      | Channel8, 0x80 | 0x3e | PWR\_CPLD                               |      |

| I2c\_10                               |                | 0x74 | SI5391 (GB 156.25MHz Clock) |           |
| ------------------------------------- | -------------- | ---- | --------------------------- | --------- |
| I2c\_11                               |                |      | PTP (Reserved)              | PTP       |
| I2c\_12                               |                | 0x70 | PCA9548                     | FCM       |
| I2c_12 <br/>0x70 <br/>I2C <br/>Switch | Channel1, 0x01 | 0x3e | FAN CPLD                    | FCM       |
|                                       | Channel2, 0x02 | 0x51 | 24c02 (FCB Inv)             |           |
|                                       | Channel3, 0x04 | 0x48 | TMP75                       |           |
|                                       |                | 0x49 | TMP75                       |           |
|                                       | Channel4, 0x10 | 0x10 | ADM1278                     |           |
|                                       | Channel5, 0x10 | 0x52 | 24c64 (Fan#1)               | FAN-Trays |
|                                       | Channel6, 0x20 | 0x52 | 24c64 (Fan#2)               |           |
|                                       | Channel7, 0x40 | 0x52 | 24c64 (Fan#3)               |           |
|                                       | Channel8, 0x80 | 0x52 | 24c64 (Fan#4)               |           |

| I2c\_13 |      | 0x3E | SMB SYS CPLD | SMB  |
| ------- | ---- | ---- | ------------ | ---- |
| I2c\_14 |      | 0x60 | DOM\_FPGA\_1 | SMB  |

#### 5.7.4. BMC SPI diagram

BMC’s SPI#0 is used to upgrade FWs/images. Here are the SPI devices connected to BMC’s SPI#0 and the chip select functionality implemented in SMB sys_CPLD.

SPI devices on SMB:

- 2 pcs of FPGA flash W25Q128
- Switching ASIC flash W25Q257
- BCM5396’s SPI EEPROM 93C46
- BMC’s SPI EEPROM 93C46
- SPI device on SCM:
- Backup BIOS flash W25Q128

The following diagram shows SPI connections in W400:

##### Figure 22:SPI Diagram

BMC56980  Mux  FW

5  #  #

8  8  2

SPL  Dom

FPGA 1#

SPL  Dom

BMC  SPII  MOSIMSQICLKICS  Mux  FPGA2#

inside

Control signals  SPL  FPGA

Or I2C command  System CPLD  flash 1#

SPL  FPGA

flash 2#

SPI EZPROM  CPLD_SPI_6#  COME  Mux  BIOS

93C46  CPLD_SPL 4#:  flash

WP 6#  Sel 4#  WP 4#

Sel_5#  #

dPLD_SPI_5#  2

BMC5389 SPI Mux  FW

flash

#### 5.7.5. PWR_CPLD Registers

PWR_CPLD is a dedicated CPLD to implement the functionality of power cycling the whole system. BMC configures the registers of PWR_CPLD and the system will be powered off for a certain period and then powered on automatically. Here is an example of CPLD diagram:

##### Figure 23:SPI Diagram

PDB

| SM B \_PSU \_L\_IN PU T        | 1                            |          |                       |      |                             |   |                             |
| ------------------------------ | ---------------------------- | -------- | --------------------- | ---- | --------------------------- | - | --------------------------- |
| Timer                          | 0                            | 0        | 0                     | 0    | C PLD \_PD B\_L1\_PSU \_O N |   |                             |
| 10ms\~10s                      | C PLD \_PD B \_L1\_PSU \_O N |          | H :PSU PO W E R O N   |      |                             |   |                             |
| T IM E R \_B A SE \_SE TT IN G | Reg 0x10                     |          | L : PSU PO W E R O FF |      |                             |   |                             |
| Reg 0x20                       |                              |          | 1                     | 0    | 0                           | 0 | C PLD \_PD B\_L2\_PSU \_O N |
| C PLD \_PD B \_L2\_PSU \_O N   | H :PSU PO W E R O N          | Reg 0x10 | L : PSU PO W E R O FF |      |                             |   |                             |
| H ITLESS\_L                    | I2C CFG                      | 0x40     | I2C Slave             | 0x60 |                             |   |                             |

##### table CPLD Registers

| Offset | Name                    | Description                    |
| ------ | ----------------------- | ------------------------------ |
| 0x01   | CPLD\_VERSION           | CPLD Version Register          |
| 0x02   | CPLD\_SUB\_VERSION      | CPLD Sub Version Register      |
| 0x10   | SYSTEM\_MISC\_1         | System Misc 1 Register         |
| 0x11   | SYSTEM\_MISC\_2         | System Misc 2 Register         |
| 0x20   | TIMER\_BASE\_SETTING    | Timer Base Setting Register    |
| 0x21   | TIMER\_COUNTER\_SETTING | Timer Counter setting Register |
| 0x22   | TIMER\_COUNTER\_STATE   | Timer Counter State Register   |
| 0x23   | TIMER\_MISC             | Timer Misc Register            |
| 0x25   | GB Frequency            | GB Core Frequency              |

##### Register 0x01: CPLD_VERSION – CPLD Version Register Table 4 – CPLD Version Register

| Bit #  | Name         | R/W  | Reset Value | Description                                                 |
| ------ | ------------ | ---- | ----------- | ----------------------------------------------------------- |
| \[7]   | Reserved     | R    |             |                                                             |
| \[6]   | RELEASE\_STA | R    |             | Released Bit 0= not released, 1= Released version after PVT |
| \[5:0] | CPLD\_VER    | R    |             | CPLD Revision\[5:0]                                         |

##### Register 0x02: CPLD_SUB_VERSION – CPLD Sub Version Register Table 5 – CPLD Sub Version Register

| Bit #  | Name            | R/W | Reset Value | Description                              |
| ------ | --------------- | --- | ----------- | ---------------------------------------- |
| \[7:0] | CPLD\_SUB\_VERS | R   |             | CPLD sub-version, used for HW debug only |

##### Register 0x10: SYSTEM_MISC_1 – System Misc 1 Register Table 6 – System Misc 1 Register

| Bit #  | Name           | R/W | Default Value | Description                                     |
| ------ | -------------- | --- | ------------- | ----------------------------------------------- |
| \[7:2] | Reserved       |     |               |                                                 |
| \[1]   | CPLD\_PSU2\_ON | R/W | 1             | 0: L2/R2 PSU2 POWER OFF, 1: L2/R2 PSU2 POWER ON |
| \[0]   | CPLD\_PSU1\_ON | R/W | 1             | 0: L1/R1 PSU1 POWER OFF, 1: L1/R1 PSU1 POWER ON |

##### Register 0x11: SYSTEM_MISC_2 – System Misc 2 Register Table 7 – System Misc 2 Register

| Bit #  | Name           | R/W  | Default Value | Description          |
| ------ | -------------- | ---- | ------------- | -------------------- |
| \[7:4] | Reserved       |      |               |                      |
| \[3]   | CPLD\_PSU2\_PG | R    | 1             | 1: Normal 0:Fail     |
| [2]    | CPLD_PSU1_PG   | R    | 1             | 1: Normal<br/>0:Fail |
| [1:0]  | Reserved       | R    | 0x3           |                      |

##### Register 0x20 TIMER_BASE_SETTING – Timer Base Setting Register Table 8 – Timer Base Setting Register

| Bit #  | Name               | R/W | Default Value | Description                                                   |
| ------ | ------------------ | --- | ------------- | ------------------------------------------------------------- |
| \[7:4] | Reserved           |     |               |                                                               |
| \[3]   | TIMER\_BASE\_10s   | R/W | 0             | Timer base 10s, (Note: This value needs 0x23\[1] to update)   |
| \[2]   | TIMER\_BASE\_1s    | R/W | 0             | Timer base 1s, (Note: This value needs 0x23\[1] to update)    |
| \[1]   | TIMER\_BASE\_100ms | R/W | 1             | Timer base 100ms, (Note: This value needs 0x23\[1] to update) |
| \[0]   | TIMER\_BASE\_10ms  | R/W | 0             | Timer base 10ms, (Note: This value needs 0x23\[1] to update)  |

##### Register 0x21: TIMER_COUNTER_SETTING – Timer Counter setting Register Table 9 – Timer Counter Setting Register

| Bit #  | Name                    | R/W | Default Value | Description                                                                                                                                      |
| ------ | ----------------------- | --- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| \[7:0] | TIMER\_COUNTER\_SETTING | R/W | 0xFF          | This timer is used for power up automatically, When counter down to zero, the power will repower up. (Note: This value needs 0x23\[1] to update) |

##### Register 0x22 TIMER_COUNTER_STATE – Timer Counter State Register Table 10 – Timer Counter State Register

| Bit #  | Name                  | R/W | Default Value | Description       |
| ------ | --------------------- | --- | ------------- | ----------------- |
| \[7:0] | TIMER\_COUNTER\_STATE | R   |               | The counter state |

##### Register 0x23: TIMER_MISC – Timer Misc Register Table 11 – Timer Misc Register

| Bit #  | Name                            | R/W | Reset Value | Description                                                                            |
| ------ | ------------------------------- | --- | ----------- | -------------------------------------------------------------------------------------- |
| \[7:2] | Reserved                        |     |             |                                                                                        |
| \[1]   | TIMER\_COUNTER\_SETTING\_UPDATE | R/W | 0           | 0: No Update, 1: Update the 0x21 and 0x20 TIMER\_BASE\_SETTING TIMER\_COUNTER\_SETTING |
| \[0]   | POWER\_CYCLE                    | R/W | 0           | 0: No power cycle, 1: Start the power cycle                                            |

##### Register 0x25: GB_FREQ_SET - PUC_DIFF_REG. Table 12 – GB Frequency Register

| Bit #  | Name           | R/W | Reset Value | Description                    |
| ------ | -------------- | --- | ----------- | ------------------------------ |
| \[7:0] | PUC\_DIFF\_REG | RW  | 0x35        | Set GB switching running freq. |

#### 5.7.6. SMB sys_CPLD Registers

Here are the main functionalities of system CPLD on SMB:

- All the major components power/reset sequence and controlling through reset registers;
- SCM/PSU/FCM present status access through registers;
- Control I/O signals on SMB board through register reads/writes, like Write protection pins, enable/disable pins, Programming pins, UART selection pins, SPI chip selection pins, etc;
- Control FPGA init and CPU reset sequence;
- Interrupt status/masks controlling through registers;
- SFP/SFP+ of OOB status controlling;
- UART selections;
- Support hitless programming; (This is general requirement for all the CPLDs.)
- Other clue logics.

Two identical FPGA share the same image to shorten programming time, so this CPLD needs to take care of this unique requirement. CPLD needs to allow the FPGA to be initialized one by one, from the same SPI flash, then reset release CPU, so both FPGA can get their PCI enumerated properly.

##### table CPLD Registers

| Offset | Name                              | Description |
| ------ | --------------------------------- | ----------- |
| 0x00   | SYSPLD\_REG\_BOARD\_INFO          |             |
| 0x01   | SYSPLD\_REG\_PLD\_VERSION         |             |
| 0x02   | SYSPLD\_REG\_PLD\_SUB\_VERSION    |             |
| 0x03   | SYSPLD\_REG\_PSU\_STATUS          |             |
| 0x05   | SYSPLD\_REG\_SYSTEM\_RST\_1       |             |
| 0x06   | SYSPLD\_REG\_SYSTEM\_RST\_2       |             |
| 0x07   | SYSPLD\_REG\_SYSTEM\_RST\_3       |             |
| 0x10   | SYSPLD\_REG\_SYSTEM\_INT\_1       |             |
| 0x11   | SYSPLD\_REG\_SYSTEM\_INT\_2       |             |
| 0x12   | SYSPLD\_REG\_SYSTEM\_INT\_3       |             |
| 0x20   | SYSPLD\_REG\_SYSTEM\_INT\_MASK\_1 |             |
| 0x21   | SYSPLD\_REG\_SYSTEM\_INT\_MASK\_2 |             |

| 0x22 | SYSPLD_REG_SYSTEM_INT_MASK_3 |      |
| ---- | ---------------------------- | ---- |
| 0x30 | SYSPLD_REG_SYSTEM_INT_STA_1  |      |
| 0x31 | SYSPLD_REG_SYSTEM_INT_STA_2  |      |
| 0x32 | SYSPLD_REG_SYSTEM_INT_STA_3  |      |
| 0x39 | SYSPLD_REG_PORT_LED_TEST     |      |
| 0x3A | SYSPLD_REG_UART_MUX          |      |
| 0x40 | SYSPLD_REG_MISC_BMC          |      |
| 0x41 | SYSPLD_REG_MISC_1            |      |
| 0x42 | SYSPLD_REG_MISC_2            |      |
| 0x43 | SYSPLD_REG_MISC_PWR_1        |      |
| 0x44 | SYSPLD_REG_MISC_PWR_2        |      |
| 0x45 | SYSPLD_REG_MISC_PWR_3        |      |
| 0x46 | SYSPLD_REG_MAC_ROV           |      |
| 0x47 | SYSPLD_REG_FPGA_INITIAL      |      |
| 0x48 | SYSPLD_REG_SPI_MUX_1         |      |
| 0x4A | REG_BMC_RESERVE_1            |      |
| 0x4B | REG_BMC_RESERVE_2            |      |
| 0x4C | REG_BMC_RESERVE_3            |      |
| 0x4D | Rack_Mon IO control_1        |      |
| 0x4E | Rack_Mon IO control_2        |      |
| 0x4F | Rack_Mon IO control_3        |      |
| 0x50 | CPLD_FPGA IO control_1       |      |
| 0x51 | CPLD_FPGA IO control_2       |      |
| 0x52 | CPLD_FPGA IO control_3       |      |
| 0x70 | Scratchpad Register          |      |

##### Register 0x00: Board_VERSION – Board Version Register Table 12 – CPLD Board Version Register

| Bit #  | Name           | R/W | Reset Value | Description                          |
| ------ | -------------- | --- | ----------- | ------------------------------------ |
| \[7-6] | Reserved       | R   | 2’b00       | Board TYPE                           |
| \[5:4] | Board\_TYPE    | R   |             | 2’b00 : Wedge‑400 2’b01 : Wedge‑400C |
| \[3:2] | Reserved       | R   | 2’b00       |                                      |
| \[1:0] | Board\_Version | R   |             | Board Version\[1:0]                  |

##### Register 0x01: CPLD_VERSION – CPLD Version Register Table 13 – CPLD Version Register

| Bit #  | Name         | R/W  | Reset Value | Description                                                 |
| ------ | ------------ | ---- | ----------- | ----------------------------------------------------------- |
| \[7]   | Reserved     | R    |             |                                                             |
| \[6]   | RELEASE\_STA | R    |             | Released Bit 0= not released, 1= Released version after PVT |
| \[5:0] | CPLD\_VER    | R    |             | CPLD Revision\[5:0]                                         |

##### Register 0x02: CPLD_SUB_VERSION – CPLD Sub Version Register Table 14 – CPLD Sub Version Register

| Bit #  | Name               | R/W | Reset Value | Description                              |
| ------ | ------------------ | --- | ----------- | ---------------------------------------- |
| \[7:0] | CPLD\_SUB\_VERSION | R   |             | CPLD sub-version, used for HW debug only |

##### Register 0x03: SYSPLD_REG_PSU_STATUS Table 15 – SYSPLD_REG_PSU_STATUS Register

| Bit #  | Name        | R/W | Default Value | Description                                                                                   |
| ------ | ----------- | --- | ------------- | --------------------------------------------------------------------------------------------- |
| \[7:4] | Reserved    | R   |               |                                                                                               |
| \[3]   | PSU2\_ACOK  | R   |               | 1: PSU input OK. When AC PSU, means AC input, when PEM, means 12V input. 0: PSU input Not OK. |
| \[2]   | PSU1\_ACOK  | R   |               | 1: PSU input OK. When AC PSU, means AC input, when PEM, means 12V input. 0: PSU input Not OK. |
| \[1]   | PSU2\_PWROK | R   |               | 1: PSU DC output OK. 0: PSU DC output Not OK.                                                 |
| \[0]   | PSU1\_PWROK | R   |               | 1: PSU DC output OK. 0: PSU DC output Not OK.                                                 |

##### Register 0x5: SYSPLD_REG_SYSTEM_RST_1 Table 16 – SYSPLD_REG_SYSTEM_RST_1 Register

| Bit # | Name                | R/W | Default Value | Description                            |
| ----- | ------------------- | --- | ------------- | -------------------------------------- |
| \[7]  | SI5391B\_RST\_N     | R/W | 1             | CLK buffer reset. Low active.          |
| \[6]  | USBHUB\_RST\_N      | R/W | 1             | USB bridge reset. Low active.          |
| \[5]  | BMC\_LPCRST\_N      | R/W | 1             | BMC\_LPC reset. Low active.            |
| \[4]  | BMC\_PHY\_2\_RST\_N | R/W | 1             | OOB front panel Phy reset. Low active. |
| \[3]  | BMC\_PHY\_1\_RST\_N | R/W | 1             | OOB RGMII Phy reset. Low active.       |
| \[2]  | BCM5389\_RESETB\_N  | R/W | 1             | OOB switch reset. Low active.          |
| \[1]  | Reserved            | R   | 1             | .                                      |
| \[0]  | MAC\_RESET\_N       | R/W | 1             | GB reset. Low active.                  |

##### Register 0x6: SYSPLD_REG_SYSTEM_RST_2 Table 17 – SYSPLD_REG_SYSTEM_RST_2 Register

| Bit # | Name            | R/W | Default Value | Description                   |
| ----- | --------------- | --- | ------------- | ----------------------------- |
| \[7]  | FT232\_RESET\_N | R/W | 1             | FT232\_RESET. Low active.     |
| \[6]  | TPM\_RST\_N     | R/W | 1             | TPM module reset. Low active. |

| [5]  | SCM_CPLD_RESET     | R/W  | 1    | SCM CPLD reset. Low active.                       |
| ---- | ------------------ | ---- | ---- | ------------------------------------------------- |
| [4]  | FCM_CPLD_RST       | R/W  | 1    | FCB board reset. Low active.                      |
| [3]  | FCM_PCA9548_RST    | R/W  | 1    | FCB board 9548 reset. BMC I2C bus 9. Low active.  |
| [2]  | PCA9534_RST_N      | R/W  | 1    | SMB board 9548 reset. BMC I2C bus 14. Low active. |
| [1]  | PCA9535_RST_N      | R/W  | 1    | SMB board 9548 reset. BMC I2C bus 10. Low active. |
| [0]  | PCA9548A_2_RESET_N | R/W  | 1    | SMB board 9548 reset. BMC I2C bus 9. Low active.  |

##### Register 0x7 SYSPLD_REG_SYSTEM_RST_3 Table 18 – SYSPLD_REG_SYSTEM_RST_3 Register

| Bit #  | Name                | R/W | Default Value | Description                  |
| ------ | ------------------- | --- | ------------- | ---------------------------- |
| \[7:2] | Reserved            |     |               |                              |
| \[1]   | DOM\_FPGA2\_RST\_IN | R/W | 1             | DOM\_FPGA2\_RST. Low active. |
| \[0]   | DOM\_FPGA1\_RST\_IN | R/W | 1             | DOM\_FPGA1\_RST. Low active. |

##### Register 0x10 SYSPLD_REG_SYSTEM_INT_1 Table 19 – SYSPLD_REG_SYSTEM_INT_1 Register

| Bit # | Name                    | R/W Default Value | Description                                                  |
| ----- | ----------------------- | ----------------- | ------------------------------------------------------------ |
| [7]   | PSU_ALERT_2_L           | RC 1              | SCM CPLD Interrupt<br>0: Status changed from last read<br>1: Status not changed |
| [6]   | PSU_ALERT_1_L           | RC 1              | FCB CPLD Interrupt<br>0: Status changed from last read<br>1: Status not changed |
| [5]   | SCM CPLD_Int            | RC 1              | SCM CPLD Interrupt<br>0: Status changed from last read<br>1: Status not changed |
| [4]   | FCB CPLD_Int            | RC 1              | FCB CPLD Interrupt<br>0: Status changed from last read<br>1: Status not changed |
| [3]   | TEMP_SENSOR CPLD_ALERT4 | RC 1              | Thermal sensor int_4<br>0: Status changed from last read<br>1: Status not changed |
| [2]   | TEMP_SENSOR CPLD_ALERT3 | RC 1              | Thermal sensor int_3<br>0: Status changed from last read<br>1: Status not changed |
| [1]   | TEMP_SENSOR CPLD_ALERT2 | RC 1              | Thermal sensor int_2<br>0: Status changed from last read<br>1: Status not changed |
| [0]   | TEMP_SENSOR CPLD_ALERT1 | RC 1              | Thermal sensor int_1<br>0: Status changed from last read<br>1: Status not changed |

##### Register 0x11 SYSPLD_REG_SYSTEM_INT_2 Table 20 – SYSPLD_REG_SYSTEM_INT_2

| Bit # | Name             | R/W | Default Value | Description               |
| ----- | ---------------- | --- | ------------- | ------------------------- |
| \[7]  | PSU\_PRNST\_2\_N | RC  | 1             | PSU 2 present interrupts. |

| [6]  | PSU_PRNST_1_N   | RC   | 1    | PSU 1 present interrupts.      |
| ---- | --------------- | ---- | ---- | ------------------------------ |
| [5]  | SCM_PRESET      | RC   | 1    | SCM present interrupts.        |
| [4]  | DEBUG_PRESENT_N | RC   | 1    | DEBUG card present interrupts. |
| [3]  | Reserved        | RC   | 1    |                                |
| [2]  | SMB_TPM_INT_N   | RC   | 1    | TPM I2C INTR                   |
| [1]  | Reserved        | RC   | 1    |                                |
| [0]  | TPM_PP          | RC   | 1    | TPM PP interrupt               |

##### Register 0x12 SYSPLD_REG_SYSTEM_INT_3 Table 21 – SYSPLD_REG_SYSTEM_INT_3 Register

| Bit # | Name                  | R/W | Default Value | Description                              |
| ----- | --------------------- | --- | ------------- | ---------------------------------------- |
| \[7]  | FAULT\_R\_XP5R0V\_USB | RC  | 1             | USB XP5R0V fault interrupts              |
| \[6]  | XP5R0V\_PG            | RC  | 1             | XP5R0V power good interrupts.            |
| \[5]  | BMC\_POWER\_OK        | RC  | 1             | BMC all power rails power ok interrupts. |
| \[4]  | Reserved              | RC  | 1             |                                          |
| \[3]  | PSU\_ACOK\_2          | RC  | 1             | PSU2 AC Input power ok interrupts.       |
| \[2]  | PSU\_ACOK\_1          | RC  | 1             | PSU1 AC Input power ok interrupts.       |
| \[1]  | PSU\_PWROK\_2         | RC  | 1             | PSU2 DC output power ok interrupts.      |
| \[0]  | PSU\_PWROK\_1         | RC  | 1             | PSU1 DC output power ok interrupts.      |

##### Register 0x20 SYSPLD_REG_SYSTEM_INT_Mask_1 Table 22 – SYSPLD_REG_SYSTEM_INT_Mask_1 Register

| Bit # | Name                               | R/W  | Default Value | Description                                     |
| ----- | ---------------------------------- | ---- | ------------- | ----------------------------------------------- |
| \[7]  | PSU\_ALERT\_2\_L mask              | R/W  | 1             | SCM_CPLD Interrupt mask 1: mask 0: Don’t mask   |
| \[6]  | PSU\_ALERT\_1\_L mask              | R/W  | 1             | FCB_CPLD Interrupt mask 1: mask 0: Don’t mask   |
| \[5]  | SCM\_CPLD\_Int mask                | R/W  | 1             | SCM_CPLD Interrupt mask 1: mask 0: Don’t mask   |
| \[4]  | FCB\_CPLD\_Int mask                | R/W  | 1             | FCB_CPLD Interrupt mask 1: mask 0: Don’t mask   |
| \[3]  | TEMP\_SENSOR\_CPLD\_ALERT\_T4 mask | R/W  | 1             | Thermal sensor int_4 mask 1: mask 0: Don’t mask |
| \[2]  | TEMP\_SENSOR\_CPLD\_ALERT\_T3 mask | R/W  | 1             | Thermal sensor int_3 mask 1: mask 0: Don’t mask |
| \[1]  | TEMP\_SENSOR\_CPL\_ALERT2 mask     | R/W  | 1             | Thermal sensor int_2 mask 1: mask 0: Don’t mask |
| \[0]  | TEMP\_SENSOR\_CPLD\_ALERT\_T1 mask | R/W  | 1             | Thermal sensor int_1 mask 1: mask 0: Don’t mask |

##### Register 0x21 SYSPLD_REG_SYSTEM_INT_Mask_2 Table 23 – SYSPLD_REG_SYSTEM_INT_Mask_2 Register 

| Bit # | Name                   | R/W | Default Value | Description                        |
| ----- | ---------------------- | --- | ------------- | ---------------------------------- |
| \[7]  | PSU\_PRNST\_2\_N mask  | R/W | 1             | PSU 2 present interrupts mask      |
| \[6]  | PSU\_PRNST\_1\_N mask  | R/W | 1             | PSU 1 present interrupts mask      |
| \[5]  | SCM\_PRESET mask       | R/W | 1             | SCM present interrupts mask        |
| \[4]  | DEBUG\_PRESENT\_N mask | R/W | 1             | DEBUG card present interrupts mask |
| \[3]  | Reserved               | R/W | 1             |                                    |
| \[2]  | SMB\_TPM\_INT\_N mask  | R/W | 1             | TPM I2C INTR mask                  |
| \[1]  | Reserved               | R/W | 1             |                                    |
| \[0]  | TPM\_PP mask           | R/W | 1             | TPM PP interrupt mask              |

##### Register 0x22 SYSPLD_REG_SYSTEM_INT_Mask_3 Table 24 – SYSPLD_REG_SYSTEM_INT_Mask_3 Register

| Bit # | Name                        | R/W | Default Value | Description                                  |
| ----- | --------------------------- | --- | ------------- | -------------------------------------------- |
| \[7]  | FAULT\_R\_XP5R0V\_US B mask | R/W | 1             | USB XP5R0V fault interrupts mask             |
| \[6]  | XP5R0V\_PG mask             | R/W | 1             | XP5R0V power good interrupts mask            |
| \[5]  | BMC\_POWER\_OK mask         | R/W | 1             | BMC all power rails power ok interrupts mask |
| \[4]  | Reserved                    | R/W | 1             |                                              |
| \[3]  | PSU\_ACOK\_2 mask           | R/W | 1             | PSU2 AC Input power ok interrupts mask       |
| \[2]  | PSU\_ACOK\_1 mask           | R/W | 1             | PSU1 AC Input power ok interrupts mask       |
| \[1]  | PSU\_PWROK\_2 mask          | R/W | 1             | PSU2 DC output power ok interrupts mask      |
| \[0]  | PSU\_PWROK\_1 mask          | R/W | 1             | PSU1 DC output power ok interrupts mask      |

##### Register 0x30 SYSPLD_REG_SYSTEM_INT_Status_1 Table 25 – SYSPLD_REG_SYSTEM_INT_Status_1 Register

| Bit # | Name                              | R/W  | Default Value | Description                                |
| ----- | --------------------------------- | ---- | ------------- | ------------------------------------------ |
| \[7]  | PSU\_ALERT\_2\_L Status           | R    | 1             | SCM\_CPLD Interrupt Status                 |
|       |                                   |      |               | 0: PSU has interrupts 1: Not interrupts    |
| \[6]  | PSU\_ALERT\_1\_L Status           | R    | 1             | FCB\_CPLD Interrupt Status                 |
|       |                                   |      |               | 0: PSU has interrupts 1: Not interrupts    |
| \[5]  | SCM\_CPLD\_Int Status             | R    | 1             | SCM\_CPLD Interrupt Status                 |
|       |                                   |      |               | 0: SCM has interrupts 1: Not interrupts    |
| \[4]  | FCB\_CPLD\_Int Status             | R    | 1             | FCB\_CPLD Interrupt Status                 |
|       |                                   |      |               | 0: FCB has interrupts 1: Not interrupts    |
| \[3]  | TEMP\_SENSOR\_CPLD\_ALERT4 Status | R    | 1             | Thermal sensor int\_4 Status               |
|       |                                   |      |               | 0: Sensor has interrupts 1: Not interrupts |

| [2]  | TEMP_SENSOR_CPLD_ALERT3 Status | R    | 1    | Thermal sensor int_3 Status<br>0: Sensor has interrupts<br>1: Not interrupts |
| ---- | ------------------------------ | ---- | ---- | ------------------------------------------------------------ |
| [1]  | TEMP_SENSOR_CPLD_ALERT2 Status | R    | 1    | Thermal sensor int_2 Status<br>0: Sensor has interrupts<br>1: Not interrupts |
| [0]  | TEMP_SENSOR_CPLD_ALERT1 Status | R    | 1    | Thermal sensor int_1 Status<br>0: Sensor has interrupts<br>1: Not interrupts |

##### Register 0x31 SYSPLD_REG_SYSTEM_INT_ Status _2 Table 26 – SYSPLD_REG_SYSTEM_INT_ Status _2 Register

| Bit # | Name                     | R/W | Default Value | Description                                           |
| ----- | ------------------------ | --- | ------------- | ----------------------------------------------------- |
| \[7]  | PSU\_PRNST\_2\_N Status  | R   | 1             | PSU 2 present interrupts Status                       |
|       |                          |     |               | 0: PSU present 1: PSU not present                     |
| \[6]  | PSU\_PRNST\_1\_N Status  | R   | 1             | PSU 1 present interrupts Status                       |
|       |                          |     |               | 0: PSU present 1: PSU not present                     |
| \[5]  | SCM\_PRESET Status       | R   | 1             | SCM present interrupts Status                         |
|       |                          |     |               | 0: SCM present 1: SCM not present                     |
| \[4]  | DEBUG\_PRESENT\_N Status | R   | 1             | DEBUG card present interrupts Status                  |
|       |                          |     |               | 0: Debug card present 1: Debug card not present       |
| \[3]  | Reserved                 | R   | 1             | PCIE Wake interrupt Status                            |
|       |                          |     |               | 0: PCIE Wake status 1: PCIE Not Wake status           |
| \[2]  | SMB\_TPM\_INT\_N Status  | R   | 1             | TPM I2C INTR Status                                   |
|       |                          |     |               | 0: TPM I2C has interrupt 1: TPM I2C has not interrupt |
| \[1]  | Reserved                 | R   | 1             |                                                       |
|       |                          |     |               | TPM PP interrupt Status                               |
| \[0]  | TPM\_PP Status           | R   | 1             | 0: TPM PP has interrupt 1: TPM PP has not interrupt   |

##### Register 0x32 SYSPLD_REG_SYSTEM_INT_ Status_3 Table 27 – SYSPLD_REG_SYSTEM_INT_ Status_3 Register

| Bit # | Name                         | R/W | Default Value | Description                                    |
| ----- | ---------------------------- | --- | ------------- | ---------------------------------------------- |
| \[7]  | FAULT\_R\_XP5R0V\_USB Status | R   | 1             | USB XP5R0V fault interrupts Status             |
| \[6]  | XP5R0V\_PG Status            | R   | 1             | XP5R0V power good interrupts Status            |
| \[5]  | BMC\_POWER\_OK Status        | R   | 1             | BMC all power rails power ok interrupts Status |
| \[4]  | Reserved                     | R   | 1             |                                                |
| \[3]  | PSU\_ACOK\_2 Status          | R   | 1             | PSU2 AC Input power ok interrupts Status       |
| \[2]  | PSU\_ACOK\_1 Status          | R   | 1             | PSU1 AC Input power ok interrupts Status       |
| \[1]  | PSU\_PWROK\_2 Status         | R   | 1             | PSU2 DC output power ok interrupts Status      |
| \[0]  | PSU\_PWROK\_1 Status         | R   | 1             | PSU1 DC output power ok interrupts Status      |

##### Register 0x39 SYSPLD_REG_PORT_LED_TEST Table 28 – SYSPLD_REG_PORT_LED_TEST Register

| Bit #  | Name            | R/W | Default Value | Description                                                          |
| ------ | --------------- | --- | ------------- | -------------------------------------------------------------------- |
| \[7:4] | Reserved        |     |               |                                                                      |
| \[3]   | LED Test enable | R/W | 0             | 1: Test mode, LED manual control. 0: LED control by FPGA LED stream. |
| \[2]   | LED\_Green      | R/W | 0             | 1: All Led Green on. 0: All Led Green off.                           |
| \[1]   | LED\_Blue       | R/W | 0             | 1: All Led Blue on. 0: All Led Blue off.                             |
| \[0]   | LED\_Red        | R/W | 0             | 1: All Led Red on. 0: All Led Red off.                               |

##### Register 0x3A SYSPLD_UART selection Table 29 – SYSPLD_UART selection Register

| Bit #  | Name                 | R/W  | Default Value | Description                                                  |
| ------ | -------------------- | ---- | ------------- | ------------------------------------------------------------ |
| \[7:6] | Debug UART Selection | R/W  | 0             | REAR\_DBG\_UART selection 00: Reserved 01: Q200L UART 10: Reserved 11: reserved |
| \[5:2] | Reserved             | R/W  | 0             | 1: All Led Blue on. 0: All Led Blue off.                     |
| \[1:0] | UART Selection       | R/W  | 10            | 00: UART\_SELECT\_BMC (BMC\_UART\_SEL5 signal controls UART selection) 01: UART\_SELECT\_DBG (USB\_UART\_SEL from FB USB Debug controls UART selection) 10: force to select 0 11: force to select 1 UART\_SEL 1: UART port of COMe connect to BMC UART-5, and FB USB Debug UART connect to BMC UART-2 0: UART port of COMe connect to FB USB Debug UART, |

##### Register 0x40 SYSPLD_REG_MISC_BMC Table 30 – SYSPLD_REG_MISC_BMC Register

| Bit # | Name                     | R/W | Default Value | Description          |
| ----- | ------------------------ | --- | ------------- | -------------------- |
| \[7]  | CPLD\_GB\_QSPI\_WP\_N    | R/W | 1             | GB PCIE FW E2PROM WP |
| \[6]  | CPLD\_BMC\_SPI\_1\_WP\_N | R/W | 1             | BMC SPI 1 Flash WP   |
| \[5]  | CPLD\_BMC\_PHY1\_WP      | R/W | 1             | PHY1 E2 WP           |
| \[4]  | CPLD\_BMC\_SPI\_2\_WP\_N | R/W | 1             | BMC SPI 2 Flash WP   |
| \[3]  | CPLD\_BMC\_PHY2\_WP      | R/W | 1             | PHY1 E2 WP           |
| \[2]  | SCM\_SPI\_WP\_N          | R/W | 1             | COME BIOS WP         |
| \[1]  | FPGA1\_SPI\_WP\_N        | R/W | 1             | FPGA SPI E2PROM WP   |
| \[0]  | FPGA2\_SPI\_WP\_N        | R/W | 1             | FPGA SPI E2PROM WP   |

##### Register 0x41 SYSPLD_REG_MISC_1 Table 31 – SYSPLD_REG_MISC_1 Register

| Bit #  | Name                 | R/W | Default Value | Description |
| ------ | -------------------- | --- | ------------- | ----------- |
| \[7:5] | Reserved             | R/W | 0             |             |
| \[4]   | CPLD\_USB\_MUX\_SEL1 | R/W | 0             |             |
| \[3]   | CPLD\_USB\_MUX\_SEL0 | R/W | 0             |             |
| \[2]   | USB\_EN3             | R/W | 1             |             |
| \[1]   | USB\_EN2             | R/W | 1             |             |
| \[0]   | USB\_EN1             | R/W | 1             |             |

##### Register 0x42 SYSPLD_REG_MISC_2 Table 32 – SYSPLD_REG_MISC_2 Register

| Bit #  | Name               | R/W | Default Value | Description |
| ------ | ------------------ | --- | ------------- | ----------- |
| \[7:4] | Reserved           |     | 1             |             |
| \[3]   | XP5R0V\_USB\_EN    | R/W | 1             |             |
| \[2]   | SCM\_POWER\_ENABLE | R/W | 1             |             |
| \[1]   | FCM\_3R3V\_EN      | R/W | 1             |             |
| \[0]   | GB\_TURN\_ON       | R/W | 0             |             |

##### Register 0x43 SYSPLD_REG_MISC_PWR_1 Table 33 – SYSPLD_REG_MISC_PWR_1 Register

| Bit #  | Name             | R/W | Default Value | Description                                  |
| ------ | ---------------- | --- | ------------- | -------------------------------------------- |
| \[7:6] | Reserved         | R   |               |                                              |
| \[5]   | XP1R15V\_BMC\_PG | R   |               | 1: Power good. 2. Power off or power failure |
| \[4]   | XP3R3V\_BMC\_PG  | R   |               | 1: Power good. 2. Power off or power failure |
| \[3]   | XP2R5V\_BMC\_PG  | R   |               | 1: Power good. 2. Power off or power failure |
| \[2]   | XP1R2V\_BMC\_PG  | R   |               | 1: Power good. 2. Power off or power failure |
| \[1]   | XP5R0V\_PG       | R   |               | 1: Power good. 2. Power off or power failure |
| \[0]   | XP3R3V\_1220\_PG | R   |               | 1: Power good. 2. Power off or power failure |

##### Register 0x44 SYSPLD_REG_MISC_PWR_2 Table 34 – SYSPLD_REG_MISC_PWR_2 Register

| Bit #  | Name                       | R/W  | Default Value | Description                                           |
| ------ | -------------------------- | ---- | ------------- | ----------------------------------------------------- |
| \[7:6] | Reserved                   | R    |               |                                                       |
| \[5]   | XP3R3V\_Optical\_Right\_PG | R    |               | 1: Power good. 2. Power off or power failure          |
| \[4]   | XP3R3V\_Optical\_Left\_PG  | R    |               | 1: Power good. 2. Power off or power failure          |
| \[3]   | USB\_OC\_PG                | R    |               | 1: Power good. 2. Power off or power failure          |
| [2]    | XP1R0V_FPGA_PG             | R    |               | 1: Power good.<br/><br/>2. Power off or power failure |
| [1]    | XP1R8V_FPGA_PG             | R    |               | 1: Power good.<br/><br/>2. Power off or power failure |
| [0]    | XP3R3V_FPGA_PG             | R    |               | 1: Power good.<br/><br/>2. Power off or power failure |

##### Register 0x45 SYSPLD_REG_MISC_PWR_3 Table 35 – SYSPLD_REG_MISC_PWR_3 Register

| Bit # | Name                  | R/W | Default Value | Description                                  |
| ----- | --------------------- | --- | ------------- | -------------------------------------------- |
| \[7]  | Reserved              | R   |               |                                              |
| \[6]  | Reserved              | R   |               |                                              |
| \[5]  | IR35215\_PVDD0P8\_VRR | R   |               | 1: Power good. 2. Power off or power failure |
| \[4]  | XP0R94V\_VDDA\_PG     | R   |               | 1: Power good. 2. Power off or power failure |
| \[3]  | NP\_POWER\_STABLE\_C  | R   |               | 1: Power good. 2. Power off or power failure |
| \[2]  | VDD\_CORE\_PG         | R   |               | 1: Power good. 2. Power off or power failure |
| \[1]  | XP0R75V\_PCIE\_PG     | R   |               | 1: Power good. 2. Power off or power failure |
| \[0]  | XP1R15V\_VDDCK\_PG    | R   |               | 1: Power good. 2. Power off or power failure |

##### Register 0x46 SYSPLD_REG_MAC_ROV Table 36 – SYSPLD_REG_MAC_ROV Register

| Bit # | Name     | R/W | Default Value | Description                  |
| ----- | -------- | --- | ------------- | ---------------------------- |
| \[7]  | ROV\_7   | R   |               | RST\_FSM\_STATE\_OBS\_0\_3V3 |
| \[6]  | ROV\_6   | R   |               | RST\_FSM\_STATE\_OBS\_1\_3V3 |
| \[5]  | ROV\_5   | R   |               | NP\_CATTRIP\_3V3             |
| \[4]  | ROV\_4   | R   |               | XP1R8V\_ALG\_PG              |
| \[3]  | Reserved | R   |               |                              |
| \[2]  | ROV\_2   | R   |               | RST\_FSM\_STATE\_OBS\_2\_3V3 |
| \[1]  | ROV\_1   | R   |               | NP\_SVS\_3V3<1>              |
| \[0]  | ROV\_0   | R   |               | NP\_SVS\_3V3<0>              |

##### Register 0x47 SYSPLD_REG_FPGA_Initial Table 37 – SYSPLD_REG_FPGA_Initial Register

| Bit # | Name                | R/W  | Default Value | Description                                                  |
| ----- | ------------------- | ---- | ------------- | ------------------------------------------------------------ |
| \[7]  | Reserved            |      |               |                                                              |
| \[6]  | Reserved            |      |               |                                                              |
| \[5]  | DOM\_FPGA2\_PROGRAM | R/W  | 1             | TBD                                                          |
| \[4]  | DOM\_FPGA1\_PROGRAM | R/W  | 1             | TBD                                                          |
| \[3]  | DOM\_FPGA2\_Initial | R/W  | 1             | TBD                                                          |
| [2]   | DOM_FPGA1_Initial   | R/W  | 1             | TBD                                                          |
| [1]   | DOM_FPGA2_Done      | R    |               | 1: DOM_FPGA2 load image finished.<br/><br/>0: DOM_FPGA load image not finished. |
| [0]   | DOM_FPGA1_Done      | R    |               | 1: DOM_FPGA2 load image finished.<br/><br/>0: DOM_FPGA load image not finished. |

##### Register 0x48 SYSPLD_REG_SPI_MUX_1 Table 38 – SYSPLD_REG_SPI_MUX_1 Register

| Bit #  | Name      | R/W | Default Value | Description                                                                                                        |
| ------ | --------- | --- | ------------- | ------------------------------------------------------------------------------------------------------------------ |
| \[7:3] | Reserved  | R   | 0             |                                                                                                                    |
|        |           | R/W | 0             | 00h: BMC Select the System\_E2. 01h: BMC Select the BIOS. 02h: BMC Select the BCM5389 E2.                          |
| \[2:0] | BIOS\_Sel |     |               | 03h: BMC Select the GB PCIE E2. 04h: BMC Select the FPGA1 flash. 05h: BMC Select the FPGA2 flash. Others: Reserved |

##### Register 0x4A REG_BMC_RESERVE_1 Table 39 – REG_BMC_RESERVE_1 Register

| Bit #  | Name               | R/W | Default Value | Description                 |
| ------ | ------------------ | --- | ------------- | --------------------------- |
| \[7:0] | RacK\_Mon\_R\[8:1] | R   |               | Rack\_Mon value input value |

##### Register 0x4B REG_BMC_RESERVE_2 Table 40 – REG_BMC_RESERVE_2 Register

| Bit #  | Name               | R/W | Default Value | Description                  |
| ------ | ------------------ | --- | ------------- | ---------------------------- |
| \[7:0] | RacK\_Mon\_W\[8:1] | R/W |               | Rack\_Mon value Output value |

##### Register 0x4C REG_BMC_RESERVE_3 Table 41 – REG_BMC_RESERVE_3 Register

| Bit #  | Name                | R/W  | Default Value | Description                                                  |
| ------ | ------------------- | ---- | ------------- | ------------------------------------------------------------ |
| \[7:0] | RacK\_Mon\_EN\[8:1] | R/W  | 0             | Rack\_Mon value Output enables. 0: Output disables. 1: Output enables. |

##### Register 0x4D Rack_Mon IO control_1 Table 42 – Rack_Mon IO control_1 Register

| Bit # | Name               | R/W  | Default Value | Description       |
| ----- | ------------------ | ---- | ------------- | ----------------- |
| \[7]  | Reserved           |      |               |                   |
| \[6]  | Reserved           |      |               |                   |
| \[5]  | RMON\_RF\_3\_input | R    |               | RF/PF input value |
| \[4]  | RMON\_PF\_3\_input | R    |               | RF/PF input value |
| \[3]  | RMON\_RF\_2\_input | R    |               | RF/PF input value |
| \[2]  | RMON\_PF\_2\_input | R    |               | RF/PF input value |
| \[1]  | RMON\_RF\_1\_input | R    |               | RF/PF input value |
| [0]   | RMON_PF_1_input    | R    |               | RF/PF input value |

##### Register 0x4E Rack_Mon IO control_2 Table 43 – Rack_Mon IO control_2 Register

| Bit # | Name                | R/W | Default Value | Description        |
| ----- | ------------------- | --- | ------------- | ------------------ |
| \[7]  | Reserved            |     |               |                    |
| \[6]  | Reserved            |     |               |                    |
| \[5]  | RMON\_RF\_3\_output | R/W | 0             | RF/PF output value |
| \[4]  | RMON\_PF\_3\_output | R/W | 0             | RF/PF output value |
| \[3]  | RMON\_RF\_2\_output | R/W | 0             | RF/PF output value |
| \[2]  | RMON\_PF\_2\_output | R/W | 0             | RF/PF output value |
| \[1]  | RMON\_RF\_1\_output | R/W | 0             | RF/PF output value |
| \[0]  | RMON\_PF\_1\_output | R/W | 0             | RF/PF output value |

##### Register 0x4F Rack_Mon IO control_3 Table 44 – Rack_Mon IO control_3 Register

| Bit # | Name                    | R/W  | Default Value | Description                                                  |
| ----- | ----------------------- | ---- | ------------- | ------------------------------------------------------------ |
| \[7]  | Reserved                |      |               |                                                              |
| \[6]  | Reserved                |      |               |                                                              |
| \[5]  | RMON\_RF\_3\_output\_en | R/W  | 0             | RF/PF output enable<br/>0: Output disables.<br/>1: Output enables. |
| \[4]  | RMON\_PF\_3\_output\_en | R/W  | 0             |                                                              |
| \[3]  | RMON\_RF\_2\_output\_en | R/W  | 0             |                                                              |
| \[2]  | RMON\_PF\_2\_output\_en | R/W  | 0             |                                                              |
| \[1]  | RMON\_RF\_1\_output\_en | R/W  | 0             |                                                              |
| \[0]  | RMON\_PF\_1\_output     | R/W  | 0             |                                                              |

##### Register 0x50 CPLD_FPGA IO control_1 Table 45 – CPLD_FPGA IO control_1Register

| Bit # | Name                    | R/W | Default Value | Description            |
| ----- | ----------------------- | --- | ------------- | ---------------------- |
| \[7]  | FPGA2\_CPLD\_RESERED\_4 | R   |               | FPGA\_CPLD input value |
| \[6]  | FPGA2\_CPLD\_RESERED\_3 | R   |               | FPGA\_CPLD input value |
| \[5]  | FPGA2\_CPLD\_RESERED\_2 | R   |               | FPGA\_CPLD input value |
| \[4]  | FPGA2\_CPLD\_RESERED\_1 | R   |               | FPGA\_CPLD input value |
| \[3]  | FPGA1\_CPLD\_RESERED\_4 | R   |               | FPGA\_CPLD input value |
| \[2]  | FPGA1\_CPLD\_RESERED\_3 | R   |               | FPGA\_CPLD input value |
| \[1]  | FPGA1\_CPLD\_RESERED\_2 | R   |               | FPGA\_CPLD input value |
| \[0]  | FPGA1\_CPLD\_RESERED\_1 | R   |               | FPGA\_CPLD input value |

##### Register 0x51 CPLD_FPGA IO control_2 Table 46 – CPLD_FPGA IO control_2Register

| Bit # | Name                            | R/W | Default Value | Description             |
| ----- | ------------------------------- | --- | ------------- | ----------------------- |
| \[7]  | FPGA2\_CPLD\_RESERED\_4\_output | R/W | 0             | FPGA\_CPLD output value |
| \[6]  | FPGA2\_CPLD\_RESERED\_3\_output | R/W | 0             | FPGA\_CPLD output value |

| Bit # | Name                            | R/W | Default Value | Description             |
| ----- | ------------------------------- | --- | ------------- | ----------------------- |
| \[5]  | FPGA2\_CPLD\_RESERED\_2\_output | R/W | 0             | FPGA\_CPLD output value |
| \[4]  | FPGA2\_CPLD\_RESERED\_1\_output | R/W | 0             | FPGA\_CPLD output value |
| \[3]  | FPGA1\_CPLD\_RESERED\_4\_output | R/W | 0             | FPGA\_CPLD output value |
| \[2]  | FPGA1\_CPLD\_RESERED\_3\_output | R/W | 0             | FPGA\_CPLD output value |
| \[1]  | FPGA1\_CPLD\_RESERED\_2\_output | R/W | 0             | FPGA\_CPLD output value |
| \[0]  | FPGA1\_CPLD\_RESERED\_1\_output | R/W | 0             | FPGA\_CPLD output value |

##### Register 0x52 CPLD_FPGA IO control_3 Table 47 – CPLD_FPGA IO control_3 Register

| Bit # | Name                        | R/W  | Default Value | Description                                                  |
| ----- | --------------------------- | ---- | ------------- | ------------------------------------------------------------ |
| \[7]  | FPGA2\_CPLD\_RESERED\_4\_en | R/W  | 0             | FPGA_CPLD output enable<br/>0: Output disables.<br/>1: Output enables. |
| \[6]  | FPGA2\_CPLD\_RESERED\_3\_en | R/W  | 0             |                                                              |
| \[5]  | FPGA2\_CPLD\_RESERED\_2\_en | R/W  | 0             |                                                              |
| \[4]  | FPGA2\_CPLD\_RESERED\_1\_en | R/W  | 0             |                                                              |
| \[3]  | FPGA1\_CPLD\_RESERED\_4\_en | R/W  | 0             |                                                              |
| \[2]  | FPGA1\_CPLD\_RESERED\_3\_en | R/W  | 0             |                                                              |
| \[1]  | FPGA1\_CPLD\_RESERED\_2\_en | R/W  | 0             |                                                              |
| \[0]  | FPGA1\_CPLD\_RESERED\_1\_en | R/W  | 0             |                                                              |

##### Register 0x70 Scratchpad Register Table 48– Scratchpad Register

| Bit #  | Name                | R/W | Reset Value | Description                 |
| ------ | ------------------- | --- | ----------- | --------------------------- |
| \[7:0] | Scratchpad register | R/W | 0           | Used for I2C interface test |

### 5.8. System Control Module (SCM)

The System Control Module (SCM) has the host COM-E CPU for Switching ASIC. The SCM support one Broadwell-DE COM-E CPU module.

#### 5.8.1. System Control Module Block Diagram

The SCM has the following components:

- BW-DE COM-E CPU modules (a.k.a Minilake)
- one M.2 256GB NVMe SSD
- CPLD is used to provide control and management function for SCM
- One dedicated I2C management bus for SMB BMC to access SCM
- I2C bus to SMB

##### Figure 24:System Controller Module (SCM) block diagram

#### 5.8.2. 10G KR interface

SCM reserves one pair of 10G KR signals to SMB. BW-DE COM-e CPU module supports extra 10G KR ethernet interface.

#### 5.8.3. SCM LPC bus

The LPC bus of SCM COM-e CPU is extended across the high speed connector to access the LPC slave devices on SMB. The LPC is connected to BMC on SMB.

#### 5.8.4. COM-Express CPU Module

COM-E CPU module is Meta MiniLake Type-7 COM-e CPU module. It has the following features:

- Processor
- Intel® Broadwell-DW processor D1527, 14nm process node
- Four-core, 2.2Ghz Base, 2.5Ghz Turbo, TDP 35W
- Cache: L1(32K data,32K instruction/core), L2 256K/core, L3 1.5MB/core
- 24x PCIe3, 6x SATA3, 4x USB3.0, 4x USB2.0
- Support Intel® TXT technology
- Up to DDR4-2133; SODIMM, UDIMM, RDIMM with ECC and non-ECC.
- BIOS
- AMI BIOS
- Memory
- Supports two SODIMM slots, each slot installs 16GB DDR4 SODIMM, up to 2133MT/s

Storage Devices

- One NVMe PCIe gen3 x4, M.2 SSD

Watchdog Timer

- Programmable by embedded controller

Expansion Interface

- Supports up to 8 PCI Express gen2 lanes, and up to 16 PCIe Gen3 lanes.
- 1 SPI interface for BIOS on carrier board
- 1 SM bus interface
- 1 I2C interface
- 1 LPC interface

I/O Interface

- 1 Ethernet - Onboard Intel I210IT
- At least 1 serial port supported by onboard EC (Embedded Controller)

USB

- One USB2.0

Mechanic and Environment

- Dimension - 95mm(L) x 125mm(W) x 2.0mm(H)

Power Supply

- DC 12V only

Wedge400C uses the following configuration:

- Boot SPI Flash: 8Mbyte, secondary on SCM main board
- M.2 PCIe NVMe SSD: 256Gbyte, physically located at SCM main board
- Memory: 2*16Gbyte DDR4 ECC 1600 with thermal sensor, 240-pin SODIMM
- BIOS: AMI UEFI
- Ethernet: 1000GbaseT, BCM PHY on SCM main board to provide SGMII interface
- PCIe: PCIe Gen3, x4 lanes are used for Switch ASIC PCIe access
- PCIe: 2 ports PCIe Gen1/2 x2 lanes are used from SCM to SMB, will be used for the two DOM FPGAs access
- PCIe: PCIe Gen3, x4 lanes are used for M.2 NVMe SSD access
- USB port: USB 2.0 port is used for SMB USB interface
- WDT: programmable via SW from 1s to 255min
- LPC: LPC bus at 33.33Mhz

The following is the block diagram of COM-E module:

##### Figure 25:Meta MiniLake CPU Module Block Diagram

DDR4 SODIMM wl ECC 2133MT/s

16GB Dual-Rank

CH0

| PCle Gen-2 x4                       | PCle Gen-3 | CH 1               | DDR4 SODIMM w/ ECC | 2133MT/s      |
| ----------------------------------- | ---------- | ------------------ | ------------------ | ------------- |
| 100Base-T Intel MDI i210            | PCle xl    | Intel Broadwell-DE | 16GB Dual-Rank     |               |
| \~lx SATA 6Gb/s                     | 4x USB 2.0 | 4 Core @ 2.2GHz    | 6MB LLC            | 35W TDP       |
| AB                                  | lx UART    | 2x 10GBASE-KR      | TPM 2.0            |               |
| LPC                                 | SMBuS      | SPI                | 12C                | Embedded BIOS |
| Power, Reset, Thermal Status & Ctrl | Controller | 16MB               |                    |               |

#### 5.8.5. SCM Sys_CPLD Registers

Registers in SCM CPLD are accessed by BMC through I2C interface. Here are the definitions of the registers which should be in SCM Sys_CPLD.

| CPLD Registers |                         |                                  |
| -------------- | ----------------------- | -------------------------------- |
| Offset         | Name                    | Description                      |
| 0x00           | BOARD\_INFO             | Board Info Register              |
| 0x01           | CPLD\_VERSION           | CPLD Version Register            |
| 0x02           | CPLD\_SUB\_VERSION      | CPLD Sub Version Register        |
| 0x0C           | Watch Dog               | Watch Dog Register               |
| 0x10           | SCM\_RST\_CTRL          | SCM Reset Control Register       |
| 0x11           | COME\_STA               | COMe Status Register             |
| 0x12           | COME\_BIOS\_DIS\_CTRL   | COMe Bios DIS Control Register   |
| 0x14           | COME\_PWR\_CTRL\_REG    | COMe Power Control Register      |
| 0x21           | SYSTEM\_INTERRUPT       | System Interrupt Register        |
| 0x28           | SYSTEM\_INTERRUPT\_MASK | System Interrupt Mask Register   |
| 0x29           | SYSTEM\_INTERRUPT\_STA  | System Interrupt Status Register |
| 0x30           | SYSTEM\_POWER\_STUTS    | System Power Status Register     |

| 0x31 | SYSTEM_POWER_ENABLE | System Power Enable Register |
| ---- | ------------------- | ---------------------------- |
| 0x32 | SYSTEM_ISO          | System ISO Register          |
| 0x34 | THERMAL             | Thermal Register             |
| 0x35 | SYSTEM_MISC_1       | System Misc_1 Register       |
| 0x36 | SYSTEM_MISC_2       | System Misc_2 Register       |
| 0x37 | SYSTEM_MISC_3       | System Misc_3 Register       |
| 0x38 | SYSTEM_MISC_4       | System Misc_4 Register       |
| 0x39 | SYSTEM_MISC_5       | System Misc_5 Register       |
| 0x3A | SYSTEM_MISC_6       | System Misc_6 Register       |

#### Register 0x00: BOARD_INFO – Board Info Register Table 48 – Board Version Register

| Bit #  | Name         | R/W  | Reset Value | Description                                                  |
| ------ | ------------ | ---- | ----------- | ------------------------------------------------------------ |
| \[7:3] | Reserved     | NA   |             |                                                              |
| \[2:0] | PCB\_Version | RO   | 100         | 000: R0A 001: R0B 010: R0C 011: R01 R02 101: R03 110: PVT1 111: PVT2 Others: Reserved |

#### Register 0x01: CPLD_VERSION – CPLD Version Register Table 49 – CPLD Version Register

| Bit #  | Name         | R/W  | Reset Value | Description                                                 |
| ------ | ------------ | ---- | ----------- | ----------------------------------------------------------- |
| \[7]   | Reserved     | RO   | 0           |                                                             |
| \[6]   | RELEASE\_STA | RO   | 0           | Released Bit 0= not released, 1= Released version after PVT |
| \[5:0] | CPLD\_VER    | RO   | 0           | CPLD Revision\[5:0]                                         |

#### Register 0x02: CPLD_SUB_VERSION – CPLD Sub Version Register Table 50 – CPLD Sub Version Register

| Bit #  | Name             | R/W | Reset Value | Description            |
| ------ | ---------------- | --- | ----------- | ---------------------- |
| \[7:0] | CPLD sub-version | RO  | 0           | used for HW debug only |

#### Register 0x0C: Watch Dog – Watch Dog Register Table 51 – Watch Dog Register

| Bit # | Name            | R/W  | Default Value | Description |
| ----- | --------------- | ---- | ------------- | ----------- |
| [7:1] | Reserved        | NA   | DA            | Reserved    |
| [0]   | ISO_COM_BRG_WDT | RO   |               |             |

#### Register 0x10: SCM_RST_CTRL – SCM Reset Control Register Table 52 –SCM Reset Control Register

| Bit #  | Name                   | R/W | Default Value | Description                                       |
| ------ | ---------------------- | --- | ------------- | ------------------------------------------------- |
| \[7:5] | Reserved               | NA  | NA            | Reserved                                          |
| \[4]   | ISO\_SMB\_CB\_RESET\_N | R/W | 1             | 0: write 0 to trigger System PCIE reset 1: normal |
| \[3]   | NVME\_SSD\_PERST       | R/W | 1             | 0: write 0 to trigger M.2 reset 1: normal         |
| \[2]   | PCA9548\_RST\_N        | R/W | 1             | 0: write 0 to trigger PCA9548 reset 1: normal     |
| \[1]   | CPLD\_COM\_PHY\_RST\_N | R/W | 1             | 0: write 0 to trigger BCM54616S reset 1: normal   |
| \[0]   | SYS\_RESET\_N          | R/W | 1             | 0: write 0 to trigger COMe reset 1: normal        |

#### Register 0x11: COME_STA – COMe Status Register Table 53 – COMe Status Register

| Bit #  | Name                     | R/W | Reset Value | Description                     |
| ------ | ------------------------ | --- | ----------- | ------------------------------- |
| \[7:4] | Reserved                 | NA  |             | Reserved                        |
| \[3]   | ISO\_COM\_SUS\_STA\_T\_N | RO  |             | COMe Module SUS\_STAT\_N Status |
| \[2]   | ISO\_COM\_SUS\_S5\_N     | RO  |             | COMe Module SUS\_S5\_N Status   |
| \[1]   | ISO\_COM\_SUS\_S4\_N     | RO  |             | COMe Module SUS\_S4\_N Status   |
| \[0]   | ISO\_COM\_SUS\_S3\_N     | RO  |             | COMe Module SUS\_S3\_N Status   |

#### Register 0x12: COME_BIOS_DIS_CTRL – COMe Bios DIS Control Register Table 54 – COMe Bios DIS Control Register

| Bit #  | Name                 | R/W  | Default Value | Description            |
| ------ | -------------------- | ---- | ------------- | ---------------------- |
| \[7:2] | Reserved             | R/W  |               | Reserved               |
| \[1]   | COM\_BIOS\_DIS1_N    | R/W  | 0             | Control COMe BIOS DIS1 |
| [0]    | COM_BIOS_DIS0_<br/>N | R/W  | 0             | Control COMe BIOS DIS0 |

#### Register 0x14: COME_PWR_CTRL_REG – COMe Power Control Register Table 55 – COMe Power Control Register

| Bit #  | Name                     | R/W  | Default Value | Description                                                  |
| ------ | ------------------------ | ---- | ------------- | ------------------------------------------------------------ |
| \[7:3] | Reserved                 |      | 0             | Reserved                                                     |
| \[2]   | come\_pwr\_ctrl\_reg\[2] | R/W  | 1             | PWR\_CYC\_N Write 0 to this bit will trigger CPLD power cycling the COMe Module, This bit will auto set to 1 after Power Cycle finish. |
| \[1]   | come\_pwr\_ctrl\_reg\[1] | R/W  | 1             | PWR\_Force\_off 0: COMe power is OFF 1: COMe power is ON     |
| \[0]   | Come\_pwr\_ctrl\_reg\[0] | R/W  | 1             | PWR\_COME\_EN 0: COMe power is OFF 1: COMe power is ON       |

#### Register 0x21: SYSTEM_INTERRUPT – System Interrupt Register Table 56 – System Interrupt Register

| Bit #  | Name              | R/W  | Reset Value | Description                  |
| ------ | ----------------- | ---- | ----------- | ---------------------------- |
| \[7:4] | Reserved          |      |             |                              |
| \[5]   | BCM54616S\_INT\_N | RC   |             | 1: No interrupt 0: Interrupt |
| \[4]   | LM75B\_INT\_N     | RC   |             | 1: No interrupt 0: Interrupt |
| \[3]   | HOTSWAP\_PG       | RC   |             | 1: No interrupt 0: Interrupt |
| \[2]   | HS\_ALERT2        | RC   |             | 1: No interrupt 0: Interrupt |
| \[1]   | HS\_ALERT1        | RC   |             | 1: No interrupt 0: Interrupt |
| \[0]   | HS\_FAULT\_N      | RC   |             | 1: No interrupt 0: Interrupt |

#### Register 0x28: SYSTEM_INTERRUPT_MASK – System Interrupt Mask Register Table 57 – System Interrupt Mask Register

| Bit #  | Name                    | R/W | Reset Value | Description                                                               |
| ------ | ----------------------- | --- | ----------- | ------------------------------------------------------------------------- |
| \[7:6] | Reserved                |     |             | Reserved                                                                  |
| \[5]   | BCM54616S\_INT\_N\_MASK | R/W | 1           | 1: CPLD blocks incoming the interrupt 0: CPLD passes the interrupt to CPU |

| [4]  | LM75B_INT_N_MASK | R/W  | 1    | 1: CPLD blocks incoming the interrupt<br>0: CPLD passes the interrupt to CPU |
| ---- | ---------------- | ---- | ---- | ------------------------------------------------------------ |
| [3]  | HOTSWAP_PG_MASK  | R/W  | 1    | 1: CPLD blocks incoming the interrupt<br>0: CPLD passes the interrupt to CPU |
| [2]  | HS_ALERT2_MASK   | R/W  | 1    | 1: CPLD blocks incoming the interrupt<br>0: CPLD passes the interrupt to CPU |
| [1]  | HS_ALERT1_MASK   | R/W  | 1    | 1: CPLD blocks incoming the interrupt<br>0: CPLD passes the interrupt to CPU |
| [0]  | HS_FAULT_N_MASK  | R/W  | 1    | 1: CPLD blocks incoming the interrupt<br>0: CPLD passes the interrupt to CPU |

#### Register 0x29: SYSTEM_INTERRUPT_Status – System Interrupt Status Register Table 58 – System Interrupt Status Register

| Bit #  | Name                 | R/W  | Reset Value | Description |
| ------ | -------------------- | ---- | ----------- | ----------- |
| \[7:6] | Reserved             |      |             | Reserved    |
| \[5]   | BCM54616S\_INT\_N    | R    |             |             |
| \[4]   | LM75B\_INT\_N        | R    |             |             |
| \[3]   | HOTSWAP\_PG\_status  | R    |             |             |
| \[2]   | HS\_ALERT2\_status   | R    |             |             |
| \[1]   | HS\_ALERT1\_status   | R    |             |             |
| \[0]   | HS\_FAULT\_N\_status | R    |             |             |

#### Register 0x30: SYSTEM_POWER_STATUS – System Power Status Register Table 59 – System Power Status Register

| Bit # | Name                | R/W  | Reset Value | Description       |
| ----- | ------------------- | ---- | ----------- | ----------------- |
| \[7]  | Reserved            |      |             | Reserved          |
| \[6]  | Reserved            |      |             | Reserved          |
| \[5]  | COM\_PWROK          | RO   |             | 1: Normal 0: Fail |
| \[4]  | PWRGD\_PCH\_PWR\_OK | RO   |             | 1: Normal 0: Fail |
| \[3]  | XP12R0V\_COME\_PG   | RO   |             | 1: Normal 0: Fail |
| \[2]  | XP5R0V\_COME\_PG    | RO   |             | 1: Normal 0: Fail |
| \[1]  | XP1R8V\_PG          | RO   |             | 1: Normal 0: Fail |
| \[0]  | XP3R3V\_SSD\_PG     | RO   |             | 1: Normal 0: Fail |

#### Register 0x31: SYSTEM_POWER_ENABLE – System Power Enable Register Table 60 – System Power Enable Register

| Bit #  | Name              | R/W | Reset Value | Description          |
| ------ | ----------------- | --- | ----------- | -------------------- |
| \[7:4] | Reserved          |     |             | Reserved             |
| \[3]   | XP12R0V\_COME\_EN | R/W | 1           | 1: Enable 0: disable |
| \[2]   | XP5R0V\_COME\_EN  | R/W | 1           | 1: Enable 0: disable |
| \[1]   | XP1R8V\_EN        | R/W | 1           | 1: Enable 0: disable |
| \[0]   | XP3R3V\_SSD\_EN   | R/W | 1           | 1: Enable 0: disable |

#### Register 0x32: SYSTEM_ISO_1 – System ISO 1 Register Table 61 – System ISO 1 Register

| Bit #  | Name                          | R/W | Reset Value | Description          |
| ------ | ----------------------------- | --- | ----------- | -------------------- |
| \[7:4] | Reserved                      |     |             | Reserved             |
| \[3]   | I2C1\_BUF\_EN                 | R/W | 0           | 0: Enable 1: Disable |
| \[2]   | COME\_USB\_BUF\_OE\_N         | R/W | 0           | 0: Enable 1: Disable |
| \[1]   | IO\_BUF\_3V3\_SCM\_SMB\_OE\_N | R/W | 0           | 0: Enable 1: Disable |
| \[0]   | IO\_BUF\_COME\_3V3\_OE\_N     | R/W | 0           | 0: Enable 1: Disable |

#### Register 0x34: THERMAL – Thermal Register Table 62 – Thermal Register 

| Bit #  | Name            | R/W | Reset Value | Description                                           |
| ------ | --------------- | --- | ----------- | ----------------------------------------------------- |
| \[7:1] | Reserved        |     |             |                                                       |
| \[0]   | CB\_THRMTRIP\_N | RO  |             | Indicating that the CPU has entered thermal shutdown. |

#### Register 0x35: SYSTEM_MISC_1 – System Misc 1 Register Table 63 – System Misc 1 Register

| Bit #  | Name       | R/W | Reset Value | Description                  |
| ------ | ---------- | --- | ----------- | ---------------------------- |
| \[7:2] | Reserved   |     |             |                              |
| \[1]   | COME\_GPI0 | RW  | 1           | TBD                          |
| \[0]   | RTC\_CLEAR | R/W | 1           | 0: Clear CMOS 1: Normal work |

#### Register 0x36: SYSTEM_MISC_2 – System Misc 2 Register Table 64 – System Misc 2 Register

| Bit #  | Name                 | R/W | Reset Value | Description                            |
| ------ | -------------------- | --- | ----------- | -------------------------------------- |
| \[7:5] | Reserved             |     |             |                                        |
| \[4]   | ISO\_HITLESS\_EN     | RO  | 1           | Hitless on going. 0: Normal operation. |
| \[3]   | NVME\_SSD\_CLKREQ\_N | RO  |             | 1: Normal operation. 0: NVME SSD Req.  |
| \[2]   | Reserved             | RO  |             |                                        |
| \[1]   | Reserved             | RO  |             |                                        |
| \[0]   | BATLOW\_N            | RO  |             | 1: Battery is normal 0: Battery is low |

#### Register 0x37: SYSTEM_MISC_3 – System Misc 3 Register Table 65 – System Misc 3 Register

| Bit # | Name               | R/W | Reset Value | Description                                  |
| ----- | ------------------ | --- | ----------- | -------------------------------------------- |
| \[7]  | PWR\_BTN\_N        | RO  |             | OCP debug card used                          |
| \[6]  | DEBUG\_RST\_BTN\_N | RO  |             | When negative edge detect, The bit will flag |
| \[5]  | UART\_SWITCH\_N    | RO  |             | When negative edge detect, The bit will flag |
| \[4]  | COME\_TYPE2        | RO  |             | Module Type Descriptions                     |
| \[3]  | COME\_TYPE1        | RO  |             | Module Type Descriptions                     |
| \[2]  | COME\_TYPE0        | RO  |             | Module Type Descriptions                     |
| \[1]  | Reserved           |     |             |                                              |
| \[0]  | COME\_GPO\_0       | RO  |             |                                              |

#### Register 0x38: SYSTEM_MISC_4 – System Misc 4 Register Table 66 – System Misc 4 Register

| Bit #  | Name                      | R/W | Reset Value | Description                      |
| ------ | ------------------------- | --- | ----------- | -------------------------------- |
| \[7:3] | Reserved                  |     |             |                                  |
| \[1]   | SCM\_EEPROM\_WP           | RW  | 1           | 1: Write protect 0: Write enable |
| \[0]   | BCM54616\_PHY\_EEPROM\_WP | RW  | 1           | 1: Write protect 0: Write enable |

#### Register 0x39: SYSTEM_MISC_5 – System Misc 5 Register Table 67 – System Misc 5 Register

| Bit #  | Name                           | R/W | Reset Value | Description                        |
| ------ | ------------------------------ | --- | ----------- | ---------------------------------- |
| \[7:5] | Reserved                       |     |             |                                    |
| \[4]   | SUS\_S3\_N\_CLK\_BUF           | RW  | 1           | 1: Power on 0: Power down          |
| \[3]   | PCIE\_CLK\_BUFFER\_DIF3\_OE\_N | RW  | 1           | 1: Buffer disable 0: Buffer enable |
| \[2]   | PCIE\_CLK\_BUFFER\_DIF2\_OE\_N | RW  | 1           | 1: Buffer disable 0: Buffer enable |
| \[1]   | PCIE\_CLK\_BUFFER\_DIF1\_OE\_N | RW  | 1           | 1: Buffer disable 0: Buffer enable |
| \[0]   | PCIE\_CLK\_BUFFER\_DIF0\_OE\_N | RW  | 1           | 1: Buffer disable 0: Buffer enable |

#### Register 0x3A: SYSTEM_MISC_6 – System Misc 6 Register Table 68 – System Misc 6 Register

| Bit #  | Name                  | R/W | Reset Value | Description         |
| ------ | --------------------- | --- | ----------- | ------------------- |
| \[7:3] | Reserved              |     |             |                     |
| \[2]   | CB\_GBE0\_ACT\_N      | RO  |             | Link Active.        |
| \[1]   | CB\_GBE0\_LINK1000\_N | RO  |             | Link speed on 1G.   |
| \[0]   | CB\_GBE0\_LINK100\_N  | RO  |             | Link speed on 100M. |

### 5.9. Fan Control Module(FCM) and Fan-tray

Wedge400C uses four 80mm x 80mm x 80mm CR fans to provide forced air cooling to the chassis. There is one Fan Control Module (FCM) inside Wedge400C chassis. The FCM has one CPLD used for fan controlling and fan status monitoring. The BMC on SMB can access the fan control CPLD via a system management I2C bus.

FAN CPLD’s JTAG goes directly from BMC’s GPIOs to make the CPLD re-programming fast. The following diagram shows the functional blocks of fan control module:

#### Figure 26:FAN Control Module (FCM)

#### 5.9.1. Fan_CPLD Registers

There is a FAN_CPLD located on FCM board. Here are the functionalities of the CPLD:

- CPU can access FAN CPLD via I2C interface to get fan status.
- Register to control Fan PWM signal for fan speed control and detect fan direction, and the counter for fan speed reporting.
- Fan power control to enable/disable Fan power rail.
- Detect fan speed to check fan status if there is any issue.
- Inform CPU by fan interrupt signal if any fan failure occurs, or temp sensor alerts or watchdog times out.
- The fan LED will report the fan status via Blue/Amber LEDs.

##### Figure 27: FAN Control Circuits

VCC12

PWM

FAN_DIR

Sensor

Sensor

FAN LED normal

CPU I2C SCL GGD6620 FAN_LED_ abnormal

SDA

PWM

FAN DIR

Sensor

Sensor

FAN LED normal

FAN_LED_ abnormal

##### Figure 28: FAN CPLD Diagram

Here is the Fan_CPLD diagram:

R :faul

G :norm al

ControlFan LED on/off LED R /

LED regi G

0xX ser

X

D i Pow er_enable

sabl

R eportFan faul e/enable Fan pow er

IN T t C urrentl

i

m i

t

er

R eportfan speed C ounter Tach

C ontrolFrontportFan LED on/

Front_port off

_LED _G C ontrolFan speed PW M Fan m odule

PW M

R egi

C PU access Fan stat ser

I2C _1 us R eportFan direct

i

Slave on Photocoupl

A ddr= er

R eportFan board i

nform ati

B oard versi

on /ID

“0” Fan_m os_ct

W atchdog CPLD_UPD_DISABLE JTA G rl

SW

#### 5.9.2. Fan Control Mechanism

Front fan max speed is 13400RPM, and rear fan max speed is 13700RPM. Period time is 200ms, CPLD counts negative waveform and records it at 0x20~0x23.

200ms / T ms = m (times / sec)

200ms / (1/2 * TS) = m (times / sec)

200ms/m (times / sec) = 1/2 * TS

TS = 60/N

N = 60/TS = 60/0.4*m=150*m (times / sec)

SW must multiple 150 and show it as RPM (Revolutions per minute).

##### Figure 29:FAN PWM Calculation

Vrc

0.5V

MAX.

RUNNING  LOCKED            RUNNING

BLADE   LOCKED

OR

12TS             Tl=T2-T3-T4=1/4 TS

N=RPM

TS-60 /N(SEC)

#VOLTAGE   LEVEL   AFTER   BLADE  LOCKED

*4 POLES

##### Fan PWM setting duty cycle table shown in below table Table 69 – FAN PWM Setting

| FAN\_PWM\[4:0] |                            |
| -------------- | -------------------------- |
| 00\_0000       | 0/63 or 0% duty cycle      |
| 00\_0001       | 1/63 or 1.549% duty cycle  |
| 00\_0010       | 2/63 or 3.116% duty cycle  |
| 00\_0011       | 3/63 or 4.671% duty cycle  |
| 00\_0100       | 4/63 or 6.235% duty cycle  |
| 00\_0101       | 5/63 or 7.804% duty cycle  |
| 00\_0110       | 6/63 or 9.358% duty cycle  |
| 00\_0111       | 7/63 or 10.923% duty cycle |
| 00\_1000       | 8/63 or 12.485% duty cycle |
| 00\_1001       | 9/63 or 14.047% duty cycle |

| 00_1010 | 10/63 or 15.611% duty cycle |
| ------- | --------------------------- |
| 00_1011 | 11/63 or 17.174% duty cycle |
| 00_1100 | 12/63 or 18.732% duty cycle |
| 00_1101 | 13/63 or 20.295% duty cycle |
| 00_1110 | 14/63 or 21.864% duty cycle |
| 00_1111 | 15/63 or 23.414% duty cycle |
| 01_0000 | 16/63 or 24.987% duty cycle |
| 01_0001 | 17/63 or 26.553% duty cycle |
| 01_0010 | 18/63 or 28.121% duty cycle |
| 01_0011 | 19/63 or 29.678% duty cycle |
| 01_0100 | 20/63 or 31.234% duty cycle |
| 01_0101 | 21/63 or 32.795% duty cycle |
| 01_0110 | 22/63 or 34.375% duty cycle |
| 01_0111 | 23/63 or 35.923% duty cycle |
| 01_1000 | 24/63 or 37.482% duty cycle |
| 01_1001 | 25/63 or 39.048% duty cycle |
| 01_1010 | 26/63 or 40.617% duty cycle |
| 01_1011 | 27/63 or 42.177% duty cycle |
| 01_1100 | 28/63 or 43.732% duty cycle |
| 01_1101 | 29/63 or 45.303% duty cycle |
| 01_1110 | 30/63 or 46.863% duty cycle |
| 01_1111 | 31/63 or 49.900% duty cycle |
| 10_0000 | 32/63 or 51.546% duty cycle |
| 10_0001 | 33/63 or 53.109% duty cycle |
| 10_0010 | 34/63 or 54.669% duty cycle |
| 10_0011 | 35/63 or 56.234% duty cycle |
| 10_0100 | 36/63 or 57.789% duty cycle |
| 10_0101 | 37/63 or 59.369% duty cycle |
| 10_0110 | 38/63 or 60.932% duty cycle |
| 10_0111 | 39/63 or 62.495% duty cycle |
| 10_1000 | 40/63 or 64.041% duty cycle |
| 10_1001 | 41/63 or 65.613% duty cycle |
| 10_1010 | 42/63 or 67.177% duty cycle |
| 10_1011 | 43/63 or 68.745% duty cycle |
| 10_1100 | 44/63 or 70.295% duty cycle |
| 10_1101 | 45/63 or 71.863% duty cycle |
| 10_1110 | 46/63 or 73.419% duty cycle |
| 10_1111 | 47/63 or 74.975% duty cycle |
| 11_0000 | 48/63 or 76.553% duty cycle |
| 11_0001 | 49/63 or 78.106% duty cycle |
| 11_0010 | 50/63 or 79.671% duty cycle |

| 11\_0011 | 51/63 or 81.234% duty cycle     |
| -------- | ------------------------------- |
| 11\_0100 | 52/63 or 82.796% duty cycle     |
| 11\_0101 | 53/63 or 84.349% duty cycle     |
| 11\_0110 | 54/63 or 85.925% duty cycle     |
| 11\_0111 | 55/63 or 87.482% duty cycle     |
| 11\_1000 | 56/63 or 89.039% duty cycle     |
| 11\_1001 | 57/63 or 90.606% duty cycle MAX |
| 11\_1010 | 58/63 or 92.169% duty cycle     |
| 11\_1011 | 59/63 or 93.736% duty cycle     |
| 11\_1100 | 60/63 or 95.297% duty cycle     |
| 11\_1101 | 61/63 or 96.861% duty cycle     |
| 11\_1110 | 62/63 or 98.424% duty cycle     |
| 11\_1111 | 63/63 or 100.00% duty cycle     |

In order to reduce the inrush current after Fan present, CPLD will auto control the Fan PWM value after Fan presented. By default, the Fan PWM target value will set to 50% (This might be changed based on thermal testing results). CPLD will take 8S to increase the PWM duty cycle from 0% to 50%. Every 500mS increase a duty cycle level.

Below figure shows out the Fan present status and the PWM Duty Cycle output status.

##### Figure 30:FAN Turn-on Slowly

Fan Present

Software Set

509

Software Set

PWM Duty Cycle

85 Auto Control

Software Control

##### Fan CPLD Register Mapping

| Address | Register          | R/W          | Default value | Description               |
| ------- | ----------------- | ------------ | ------------- | ------------------------- |
| 0x00    | BOARD\_VERSION    | Read Only    | 0x00          | Board Version Register    |
| 0x01    | CPLD\_VERSION     | Read Only    |               | CPLD Version Register     |
| 0x02    | CPLD\_SUB\_VERSI  | Read Only    | 0x01          | CPLD Sub Version Register |
| 0x04    | INT\_RPT          | Read clear   | 0xFF          | Interrupt Report Register |
| 0x07    | LM75 Alert Status | Read Only    |               |                           |
| 0x08    | LM75 Alert Mask   | Read & Write | 0x3           |                           |
| 0x0F    | FCB\_EEPROM\_WP   | Read & Write | 0x00          | Fan Control Board EEPROM  |

|           |                     |              |      | Write Protect Register                           |
| --------- | ------------------- | ------------ | ---- | ------------------------------------------------ |
| 0x10      | FAN\_ENABLE-REG     | Read & Write | 0x0F | Fan Enable Register                              |
| 0x11      | FCB\_ADM1278\_RE    | Read Only    |      | ADM1278 Alert Register                           |
| 0x12      | FCB\_ADM1278\_MA    | Read & Write | 0x00 | ADM1278 Alert Mask Register                      |
| 0x13      | FCB\_Efuse\_REG     | Read Only    |      | FCB\_Efuse Alert Register                        |
| 0x14      | FCB\_Efuse\_Mask\_R | Read & Write |      | FCB\_Efuse Alert Mask Register                   |
| 0x20      | FAN1\_TACH\_F\_N    | Read Only    | 0x00 | Fan1 Front Fan Speed Register                    |
| 0x21      | FAN1\_TACH\_B\_N    | Read Only    | 0x00 | Fan1 Back Fan Speed Register                     |
| 0x22      | FAN1\_PWM           | Read & Write | 0x10 | Fan1 PWM Control Register                        |
| 0x24      | FAN1\_LED           | Read & Write | 0x00 | Fan1 LED Control Register                        |
| 0x25      | FAN1\_EEPROM\_W     | Read & Write | 0x00 | Fan1 EEPOM Write Protect Register                |
| 0x28      | FAN1\_PRESENT       | Read Only    | 0x00 | Fan1 Status Register                             |
| 0x29      | FAN1\_INT\_MASK     | Read & Write | 0xFF | Fan1 Interrupt Mask Register                     |
| 0x30-0x3A | FAN2 control        |              |      | The same as Fan1 control register from 0x20-0x2A |
| 0x40-0x4A | FAN3 control        |              |      | The same as Fan1 control register from 0x20-0x2A |
| 0x50-0x5A | FAN4 control        |              |      | The same as Fan1 control register from 0x20-0x2A |

##### Register 0x00: BOARD_VERSION – Board Version Register Table 70 – Board Version Register

| Bit #  | Name              | R/W | Reset Value | Description                               |
| ------ | ----------------- | --- | ----------- | ----------------------------------------- |
| 7      | Reserved          |     |             | Reserved                                  |
| \[6:4] | Version\_ID\[3:0] | R   |             | 000: R0A Others: Reserved                 |
| \[3:2] | Reserved          |     |             | Reserved                                  |
| \[1:0] | Board\_ID\[1:0]   | R   |             | 00: Wedge 400 FCB board. Others: Reserved |

##### Register 0x01: CPLD_VERSION – CPLD Version Register Table 71 – CPLD Version Register

| Bit #  | Name            | R/W | Reset Value | Description                                 |
| ------ | --------------- | --- | ----------- | ------------------------------------------- |
| \[7]   | Reserved        | R   |             | Reserved                                    |
| \[6]   | Released Bit    | R   |             | 0=not released 1=Released version after PVT |
| \[5:0] | CPLD\_ver\[5:0] | R   |             | CPLD version                                |

##### Register 0x02: CPLD_SUB_VERSION – CPLD Sub Version Register Table 72 – CPLD Sub Version Register

| Bit #  | Name            | R/W | Reset Value | Description                              |
| ------ | --------------- | --- | ----------- | ---------------------------------------- |
| \[7:0] | CPLD\_SUB\_VERS | R   |             | CPLD sub-version, used for HW debug only |

##### Register 0x04: INT_RPT – Fan Interrupt Report Register Table 73 – Fan Interrupt Report Register

| Bit # | Name         | R/W  | Reset Value | Description                                 |
| ----- | ------------ | ---- | ----------- | ------------------------------------------- |
| \[7]  | HS\_INT      | RC   | 1           | Hot swap interrupt status.                  |
| \[6]  | Efuse\_INT   | RC   | 1           | Efuse interrupt status.                     |
| \[1]  | LM75\_INT\_1 | RC   | 1           | LM75 interrupt status.                      |
| \[0]  | LM75\_INT\_1 | RC   | 1           | FanTray-4 Interrupt                         |
| \[3]  | FAN4\_INT    | RC   | 1           | 0: No interrupt 1: Fan4 interrupt is active |
| \[2]  | FAN3\_INT    | RC   | 1           | 0: No interrupt 1: Fan3 interrupt is active |
| \[1]  | FAN2\_INT    | RC   | 1           | 0: No interrupt 1: Fan2 interrupt is active |
| \[0]  | FAN1\_INT    | RC   | 1           | 0: No interrupt 1: Fan1 interrupt is active |

##### Register 0x7: LM75 Alert Register Table 74 – LM75 Alert Register

| Bit #  | Name     | R/W | Reset Value | Description           |
| ------ | -------- | --- | ----------- | --------------------- |
| \[7:2] | Reserved |     |             |                       |
| \[1]   | LM75\_2  | R   |             | LM75 interrupt status |
| \[0]   | LM75\_1  | R   |             | LM75 interrupt status |

##### Register 0x8: LM75 Alert Mask Register Table 75 – LM75 Alert Mask Register

| Bit #  | Name         | R/W | Reset Value | Description         |
| ------ | ------------ | --- | ----------- | ------------------- |
| \[7:1] | Reserved     |     |             |                     |
| \[1]   | LM75\_2 MASK | R/W | 1           | 0: not mask 1: mask |
| \[0]   | LM75\_1 MASK | R/W | 1           | 0: not mask 1: mask |

##### Register 0x0F: FCB_EEPROM_WP – Fan Control Board EEPROM Write Protect Register Table 76 – Fan Control Board EEPROM Write Protect Register

| Bit #  | Name            | R/W | Reset Value | Description               |
| ------ | --------------- | --- | ----------- | ------------------------- |
| \[7:1] | Reserved        |     |             |                           |
| \[0]   | FCM\_EEPROM\_WP | R/W | 1           | 1: Not protect 0: Protect |

##### Register 0x10 FAN_ENALBE_REG – Fan Enable Register Table 77 – Fan Enable Register

| Bit #  | Name              | R/W | Reset Value | Description                                      |
| ------ | ----------------- | --- | ----------- | ------------------------------------------------ |
| \[7:4] | Reserved          |     |             |                                                  |
| \[3]   | FAN4\_ENALBE\_REG | R/W | 1           | 1: Enable the fan Power 2: Disable the fan Power |
| \[2]   | FAN3\_ENALBE\_REG | R/W | 1           | 1: Enable the fan Power 2: Disable the fan Power |
| \[1]   | FAN2\_ENALBE\_REG | R/W | 1           | 1: Enable the fan Power 2: Disable the fan Power |
| \[0]   | FAN1\_ENALBE\_REG | R/W | 1           | 1: Enable the fan Power 2: Disable the fan Power |

##### Register 0x11: ADM1278 Alert Register Table 78 – ADM1278 Alert Register

| Bit #  | Name        | R/W | Reset Value | Description        |
| ------ | ----------- | --- | ----------- | ------------------ |
| \[7:4] | Reserved    |     |             |                    |
| \[3]   | HS\_FAULT   | R   | 1           | HS\_FAULT status   |
| \[2]   | HS\_ALERT2  | R   | 1           | HS\_FAULT2 status  |
| \[1]   | HS\_ALERT1  | R   | 1           | HS\_FAULT1 status  |
| \[0]   | HOTSWAP\_PG | R   | 1           | HOTSWAP\_PG status |

##### Register 0x12: ADM1278 Alert Mask Register Table 79 – ADM1278 Alert Mask Register

| Bit #  | Name            | R/W  | Reset Value | Description         |
| ------ | --------------- | ---- | ----------- | ------------------- |
| \[7:4] | Reserved        |      |             |                     |
| \[3]   | HS\_FAULT\_MASK | R/W  | 1           | 0: not mask 1: mask |

| \[2] | HS\_ALERT2\_MASK  | R/W  | 1    |      | 0: not mask 1: mask |
| ---- | ----------------- | ---- | ---- | ---- | ------------------- |
| \[1] | HS\_ALERT1\_MASK  | R/W  | 1    |      | 0: not mask 1: mask |
| \[0] | HOTSWAP\_PG\_MASK | R/W  | 1    |      | 0: not mask 1: mask |

##### Register 0x13: FCB_Efuse Alert Register Table 80 – FCB_Efuse Alert RegisterS

| Bit # | Name       | R/W | Reset Value | Description          |
| ----- | ---------- | --- | ----------- | -------------------- |
| \[7]  | PG\_FAN4   | R   | 0           | Fan4 Efuse PG status |
| \[6]  | PG\_FAN3   | R   | 0           | Fan3 Efuse PG status |
| \[5]  | PG\_FAN2   | R   | 0           | Fan2 Efuse PG status |
| \[4]  | PG\_FAN1   | R   | 0           | Fan1 Efuse PG status |
| \[3]  | FLTB\_FAN4 | R   | 0           | Fan4 FLTB status     |
| \[2]  | FLTB\_FAN3 | R   | 0           | Fan4 FLTB status     |
| \[1]  | FLTB\_FAN2 | R   | 0           | Fan4 FLTB status     |
| \[0]  | FLTB\_FAN1 | R   | 0           | Fan4 FLTB status     |

##### Register 0x13: FCB_Efuse Alert Mask Register Table 81 – FCB_Efuse Alert Mask Register

| Bit # | Name             | R/W | Reset Value | Description |         |
| ----- | ---------------- | --- | ----------- | ----------- | ------- |
| \[7]  | PG\_FAN4\_MASK   | R/W | 1           | 0: not mask | 1: mask |
| \[6]  | PG\_FAN3\_MASK   | R/W | 1           | 0: not mask | 1: mask |
| \[5]  | PG\_FAN2\_MASK   | R/W | 1           | 0: not mask | 1: mask |
| \[4]  | PG\_FAN1\_MASK   | R/W | 1           | 0: not mask | 1: mask |
| \[3]  | FLTB\_FAN4\_MASK | R/W | 1           | 0: not mask | 1: mask |
| \[2]  | FLTB\_FAN3\_MASK | R/W | 1           | 0: not mask | 1: mask |
| \[1]  | FLTB\_FAN2\_MASK | R/W | 1           | 0: not mask | 1: mask |
| \[0]  | FLTB\_FAN1\_MASK | R/W | 1           | 0: not mask | 1: mask |

Below register definition is the same for all Fans. Fan1 control register range is 0x20-0x2F. Fan2 register range is 0x30-0x3F. Fan3 register range is 0x40-0x4F. Fan4 register range is 0x50-0x5F.

##### Register 0x10*(i-1) +20: FANi_TACH_F_N – Fan1 Front Fan Speed Register, (i=1,2,3,4) Table 82 – Fani Front Fan Speed Register

| Bit #  | Name             | R/W | Reset Value | Description          |
| ------ | ---------------- | --- | ----------- | -------------------- |
| \[7:0] | FANi\_TACH\_F\_N | RO  |             | Fani Front Fan Speed |

##### Register 0x10*(i-1) +21: FANi_RFAN_B_N – Fan1 Back Fan Speed Register, (i=1,2,3,4) Table 83 – Fani Back Fan Speed Register

| Bit #  | Name             | R/W | Reset Value | Description         |
| ------ | ---------------- | --- | ----------- | ------------------- |
| \[7:0] | FANi\_TACH\_B\_N | RO  |             | Fani Back Fan Speed |

##### Register 0x10*(i-1) +22: FANi_PWM – Fan1 PWM Control Register Table 84 – Fani PWM Control Register

| Bit #  | Name      | R/W | Reset Value | Description                                                                            |
| ------ | --------- | --- | ----------- | -------------------------------------------------------------------------------------- |
| \[7]   | Reserved  | RO  |             |                                                                                        |
| \[6:0] | FANi\_PWM | R/W |             | FanTray i PWM control signal Please refer to Table3 for the mapping to fan duty cycle. |

##### Register 0x10*(i-1) +24: FANi_LED – Fani LED Control Register Table 85– Fani LED Control Register

| Bit #  | Name            | R/W  | Reset Value | Description                                                  |
| ------ | --------------- | ---- | ----------- | ------------------------------------------------------------ |
| \[7:2] | Reserved        | R/W  |             |                                                              |
| \[1:0] | FANi\_LED\_CTRL | R/W  |             |                                                              |
| \[1:0] | FANi\_LED       | R/W  | 00          | 00: Under HW control 01: Red OFF, Blue ON 10: Red ON, Blue OFF 11: OFF If LED is under HW control Present\_n=0, fan\_alive\_n=0, then Red OFF, Blue ON Present\_n=1, fan\_alive\_n=x, then Red OFF, Blue OFF Present\_n=0, fan\_alive\_n=1, then Red ON, Blue OFF |

##### Register 0x10*(i-1) +25: FANi_EEPROM_WP – Fan1 EEPOM Write Protect Register Table 86– Fani EEPROM Write Protect Register

| Bit # | Name           | RMW  | Reset Value | Description                                               |
| ----- | -------------- | ---- | ----------- | --------------------------------------------------------- |
| [7:1] | Reserved       | RMW  |             |                                                           |
| [0]   | FANi_EEPROM_WP | RMW  |             | FANi EERPOM Write Protect<br>1: Protect<br>0: Not protect |

##### Register 0x10*(i-1) +28: FAN1_PRESENT – Fan1 Status Register Table 87– Fani Status Register

| Bit #  | Name          | R/W  | Reset Value | Description                             |
| ------ | ------------- | ---- | ----------- | --------------------------------------- |
| \[7:4] | Reserved      | RO   |             |                                         |
| \[3]   | FFANi\_ALIVE  | RO   |             | Front Fani Alive Status 0: alive 1: bad |
| \[2]   | RFANi\_ALIVE  | RO   |             | Rear Fani Alive Status 0: alive 1: bad  |
| \[1]   | FANi\_ALIVE   | RO   |             | Fani Alive Status 0: alive 1: bad       |
| \[0]   | FANi\_PRESENT | RO   |             | FanTray i Present 0: alive 1: bad       |

##### Register 0x10*(i-1) +29: FANi_INT_MASK – Fan1 Interrupt Mask Register Table 88– Fani Interrupt Mask Register

| Bit #  | Name               | R/W  | Reset Value | Description                                                  |
| ------ | ------------------ | ---- | ----------- | ------------------------------------------------------------ |
| \[7:4] | Reserved           |      |             |                                                              |
| \[3]   | FFANi\_ALIVE\_MASK | R/W  | 1           | Front Fani Alive Status Interrupt Mask 0: not mask 1: mask   |
| \[2]   | RFANi\_ALIVE\_MASK | R/W  | 1           | Rear Fani Alive Status Interrupt<br/>Mask<br/>0: not mask<br/>1: mask |
| \[1]   | FANi\_ALIVE\_MASK  | R/W  | 1           | Fani Alive Status Interrupt Mask<br/>0: not mask<br/>1: mask |
| \[0]   | FANi\_PRE\_MASK    | R/W  | 1           | FanTray i Present Interrupt Mask<br/>0: not mask<br/>1: mask |

### 5.10. LED

Wedge400C chassis and module cards have status LED to display the information of the system.

#### 5.10.1. LED Controlling

The following diagram shows the LED controlling in system.

##### Figure 31:LED Diagram

| BMC               | COME           |
| ----------------- | -------------- |
| 12C\_9            |                |
| PCIE              | PCIE           |
| PCA9548           | PCA9548        |
| DOM FPGA 1#       | DOM FPGA 2#    |
| SerialLedstream   |                |
| PCA9535           | FCB CPLD       |
| 0x20              | System CPLD    |
| System LEDs       | FanTrayLED     |
| System Status LED | Fan Status LED |
| PSU Status LED    | QSFP56 Port    |
| SCM status LED    | QSFP-DD Port   |
|                   | QSFP56 Port    |
|                   | Leds           |
|                   | Leds           |

#### 5.10.2. System Information LED (SIM)

There are four tri-color LED on the top left corner of Wedge400C front panel to display information of the system:

- STS: System Status LED
- FAN: Fan Status LED
- PSU: PSU Status LED
- SCM: System Control Module Status LED

BMC controls the SIM LED through an I2C IO expander on SMB. SIM PCA9535 Bit Mapping:

| Bit   | Name        | R/W  | Reset Value | Description                                                  |
| ----- | ----------- | ---- | ----------- | ------------------------------------------------------------ |
| 15:14 | Reserve     |      | 1           | NA                                                           |
| 13    | SCM\_BLU\_L | R/W  | 1           | SMB LED Blue 0: SMB LED Blue is ON 1: SMB LED Blue is OFF    |
| 12    | SCM\_GRN\_L | R/W  | 1           | SMB LED Green 0: SMB LED Green is ON 1: SMB LED Green is OFF |
| 11    | SCM\_RED\_L | R/W  | 1           | SMB LED Red 0: SMB LED Red is ON 1: SMB LED Red is OFF       |
| 10    | PSU\_BLU\_L | R/W  | 1           | PSU LED Blue 0: PSU LED Blue is ON 1: PSU LED Blue is OFF    |
| 9     | PSU\_GRN\_L | R/W  | 1           | PSU LED Green 0: PSU LED Green is ON 1: PSU LED Green is OFF |
| 8     | PSU\_RED\_L | R/W  | 1           | PSU LED Red 0: PSU LED Red is ON 1: PSU LED Red is OFF       |
| 7:6   | Reserve     |      | 1           | NA                                                           |
| 5     | FAN\_BLU\_L | R/W  | 1           | FAN LED Blue 0: FAN LED Blue is ON 1: FAN LED Blue is OFF    |
| 4     | FAN\_GRN\_L | R/W  | 1           | FAN LED Green 0: FAN LED Green is ON 1: FAN LED Green is OFF |
| 3     | FAN\_RED\_L | R/W  | 1           | FAN LED Red 0: FAN LED Red is ON 1: FAN LED Red is OFF       |
| 2     | SYS\_BLU\_L | R/W  | 1           | SYS LED Blue 0: SYS LED Blue is ON 1: SYS LED Blue is OFF    |

| 1    | SYS\_GRN\_L | R/W  | 1    | SYS LED Green<br/>0: SYS LED Green is ON<br/>1: SYS LED Green is OFF |
| ---- | ----------- | ---- | ---- | ------------------------------------------------------------ |
| 0    | SYS\_RED\_L | R/W  | 1    | SYS LED Red<br/>0: SYS LED Red is ON<br/>1: SYS LED Red is OFF |

OpenBMC software controls the system information LED per OCP Panel Indication Specification, and the following is the specific behavior in W400C. Please note that Amber is generated by turning on both Red and Green.

| LED     | Default Power-On State | Color                                                        | Condition                                                    |
| ------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SYS LED | Off                    | Blue                                                         | All FRUs are present, and no FRU-level alarms                |
|         |                        | Amber                                                        | One or more FRUs are not present; One or more FRUs have alarms |
|         |                        | Blue / Amber flashing(0.5s Blue and 0.5s <br/>Amber alternating) | Firmware upgrade in process (BIOS, EEPROM, CPLD, FPGA, etc.) |
|         |                        | Amber flashing                                               | Attention from service technician required                   |
| Fan LED | Off                    | Blue                                                         | All fans are present, and are within the normal RPM range    |
|         |                        | Amber                                                        | One or more fans are not present; One or more fans have out-of-range RPM |
| PSU LED | Off                    | Blue                                                         | All PSUs are present, and both INPUT OK and PWR OK are asserted for every PSU (accessible through SMB Sys CPLD by BMC) |
|         |                        | Amber                                                        | One or more PSUs are not present; One or more PSUs have INPUT OK or PWR OK de-asserted |
| SCM LED | Off                    | Blue                                                         | No out-of-range voltage and temperature sensors              |
|         |                        | Amber                                                        | One or more sensors out-of-range                             |

#### 5.10.3. Management OOB port LEDs

The OOB RJ45 port on SMB front panel also have typical Active LED and Link status LED to indicate the status of OOB Ethernet:

- Link Speed LED, Left of OOB RJ45 port, Green/Amber
- Solid Green: 1Gbps
- Solid Amber: 100Mbps
- OFF: No link/10Mbps
- Activity LED, right of OOB RJ45 port
- Blinking Green: TX or RX activity
- OFF: no activity

#### 5.10.4. QSFP Port LEDs

There is one LED per QSFP56 port, and two LEDs per QSFP-DD port. The microserver / CPU accesses the port LED control registers in DOM FPGA through PCIe, and DOM FPGA lights up the port LEDs on front panel.

Following is the port LED control design diagram. This design uses time-division-multiplex concept to drive external logic with a serial interface: The external logic could be discrete shifters, or external CPLD, or simply FPGA user logic.

##### Figure 32:Port LED Control Path

| Color    | Color        | 3       | RGB    |
| -------- | ------------ | ------- | ------ |
| profile  | profile      | 3.1 P2S | PO-P47 |
| Port #0  | profile\_sel |         |        |
| Port #1  | profile\_sel | 3       |        |
| Port #47 | profile\_sel |         |        |

Here is the expected port LED behavior under micro-server/DOM FPGA’s control.

##### Table 90: Port LED Behavior

| LED          | Default <br/>Power-On <br/>State | Color          | Condition                                  |
| ------------ | -------------------------------- | -------------- | ------------------------------------------ |
| Port<br/>LED | Rotating <br/>colors             | Rotating Blue  | Link up                                    |
|              |                                  | Amber          | Optic transceiver present but link down    |
|              |                                  | Amber flashing | Attention from service technician required |
|              |                                  | Off            | Optic transceiver not present              |

##### 5.10.4.1. Background of Adding LED button

W400 is designed with 2 LEDs per QSFP-DD port, and 1 LED per QSFP port on the front panel.

###### Figure 33: Front Port View

##### 5.10.4.2. LED button

There is an LED Select button and LED indicating the LED modes.

###### Figure 34: Silkscreen on LED SEL and LED button

RS485 RS485

RS485 GPIO

CONSOLE IolOIL

USB

SCMG RST

LED SEL MGMT

## 6. Modules Interfaces

Wedge400C has the following components:

- Switch Main Board (SMB)
- System Controller Module (SCM)
- Fan Control Module (FCM)
- Power Distribution Board (PDB)
- Power Distribution Board Top (PDB-T)
- Power Distribution Board Bottom (PDB-B)
- Power Supply Unit (PSU)
- AC/DC: AC PSU
- DC/DC: DC PEM
- Fan Tray Unit (FAN)
- 80mm x 80mm x 80mm Fan tray FRU

Here are the descriptions of the interfaces between modules.

### 6.1. Interfaces between SCM and SMB

Signal definitions/mappings:

|           | MPN            | Vendor |
| --------- | -------------- | ------ |
| SCM       | 10124308-101LF | FCI    |
| SMB       | 10128415-101LF | FCI    |
| Guide pin | TBD            | FCI    |

|      | 8                   | 7                           | 6                             | 5                    | 4                     | 3                     | 2                     | 1                     |
| ---- | ------------------- | --------------------------- | ----------------------------- | -------------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| K    | CPLD_RESET          | Gnd                         | {ISO_M2_ALERT}–BMC_SPI_2_WP_N | Gnd                  | ISO_PWR_BTN_N         | Gnd                   | BMC_FW_SPI_CS1_N      | Gnd                   |
| J    | Gnd                 | SCM_PCIE_FPGA1_RX_1_P       | Gnd                           | DOM_FPGA1_PCIE_CLK_N | Gnd                   | SCM_SGMII_TX_P        | Gnd                   | SCM_PCIE_FPGA1_TX_1_P |
| I    | SCM_10G_RX_P        | SCM_PCIE_FPGA1_RX_1_N       | SCM_PCIE_FPGA1_RX_0_P         | DOM_FPGA1_PCIE_CLK_P | SCM_PCIE_FPGA2_TX_0_N | SCM_SGMII_TX_N        | SCM_PCIE_FPGA1_TX_0_P | SCM_PCIE_FPGA1_TX_1_N |
| H    | SCM_10G_RX_N        | Gnd                         | SCM_PCIE_FPGA1_RX_0_N         | Gnd                  | SCM_PCIE_FPGA2_TX_0_P | Gnd                   | SCM_PCIE_FPGA1_TX_0_N | Gnd                   |
| G    | Gnd                 | SCM_PCIE_FPGA2_RX_1_P       | Gnd                           | DOM_FPGA2_PCIE_CLK_N | Gnd                   | SCM_PCIE_TH3_TX_1_N   | Gnd                   | SCM_PCIE_TH3_TX_2_N   |
| F    | SCM_SGMII_RX_P      | SCM_PCIE_FPGA2_RX_1_N       | SCM_PCIE_FPGA2_RX_0_P         | DOM_FPGA2_PCIE_CLK_P | SCM_USB_DN            | SCM_PCIE_TH3_TX_1_P   | SCM_10G_TX_P          | SCM_PCIE_TH3_TX_2_P   |
| E    | SCM_SGMII_RX_N      | Gnd                         | SCM_PCIE_FPGA2_RX_0_N         | Gnd                  | SCM_USB_DP            | Gnd                   | SCM_10G_TX_P          | Gnd                   |
| D    | Gnd                 | SCM_PCIE_TH3_RX_2_N         | Gnd                           | SCM_PCIE_TH3_RX_0_N  | Gnd                   | SCM_PCIE_FPGA2_TX_1_N | Gnd                   | SCM_PCIE_TH3_TX_0_N   |
| C    | SCM_PCIE_TH3_RX_3_P | SCM_PCIE_TH3_RX_2_P         | SCM_PCIE_TH3_RX_1_N           | SCM_PCIE_TH3_RX_0_P  | SW_TH3_PCIE_CLK_N     | SCM_PCIE_FPGA2_TX_1_P | SCM_PCIE_TH3_TX_3_N   | SCM_PCIE_TH3_TX_0_P   |
| B    | SCM_PCIE_TH3_RX_3_N | Gnd                         | SCM_PCIE_TH3_RX_1_P           | Gnd                  | SW_TH3_PCIE_CLK_P     | Gnd                   | SCM_PCIE_TH3_TX_3_P   | Gnd                   |
| A    | Gnd                 | {SCM_Preset} BMC_SPI_1_WP_N | Gnd                           | ISO_DEBUG_RST_BTN_N  | Gnd                   | ISO_COM_SUS_S3_N      | Gnd                   | BMC_FW_SPI_CLK        |

|      | 8                | 7                | 6                | 5               | 4            | 3            | 2                      | 1    |
| ---- | ---------------- | ---------------- | ---------------- | --------------- | ------------ | ------------ | ---------------------- | ---- |
| K    | COM_PWROK        | Gnd              | SCM_LPC_SERIRQ_N | Gnd             | BMC_EMMC_CLK | Gnd          | SCM_SPI_WP_N           | 12V  |
| J    | Gnd              | SCM_LPC_AD_0     | Gnd              | SCM_SPI_MISI    | Gnd          | BMC_EMMC_D0  | Gnd                    | 12V  |
| I    | BMC_FW_SPI_MISO  | SCM_LPC_AD_1     | SCM_SPI_Set_N    | SCM_SPI_MISO    | SCM_I2C_SCL  | BMC_EMMC_D1  | DMO_FPGA_SCM_CPLD_SCL  | 12V  |
| H    | BMC_FW_SPI_CS0_N | Gnd              | SCM_LPC_CLK      | Gnd             | SCM_I2C_SDA  | Gnd          | DMO_FPGA_SCM_CPLD_SDAS | 12V  |
| G    | Gnd              | BMC_SPI_1_RST    | Gnd              | SCM_SPI_CLK     | Gnd          | SCM_COM_MDC  | Gnd                    | 12V  |
| F    | BMC_FW_SPI_MISO  | BMC_SPI_2_RST    | SCM_LPC_AD_2     | SCM_SPI_CS      | BMC_EMMC_D2  | SCM_COM_MDIO | SCM_Preset             | 12V  |
| E    | ISO_CB_RESET_N   | Gnd              | SCM_LPC_AD_3     | Gnd             | BMC_EMMC_D3  | Gnd          | SCM_Power_enable       | 12V  |
| D    | Gnd              | SCM_COM_UART5_TX | Gnd              | SMB_TCK         | Gnd          | XP3R3V_BMC   | Gnd                    | 12V  |
| C    | SCM_SMBUS_SCL    | SCM_COM_UART5_RX | SCM_LPC_FRAME_N  | SMB_TMS         | SMB_TDI      | XP3R3V_BMC   | HITLESS_EN             | 12V  |
| B    | SCM_SMBUS_SDA    | Gnd              | BMC_EMMC_RST_N   | Gnd             | SMB_TDO      | Gnd          | OSO_M2_ALERT           | 12V  |
| A    | Gnd              | PWRGD_PCH_PWROK  | Gnd              | BMC_SCM_CPLD_EN | Gnd          | BMC_EMMC_CMD | Gnd                    | 12V  |

### 6.2. Interfaces between FMC and SMB

Signal definitions:

| MPN         | Vendor |            |
| ----------- | ------ | ---------- |
| 501190-2017 | Molex  | FCB signal |
| 449141201   | Molex  | FCB power  |

Signal

| Pin Number | Signal Name  | Pin Number | Signal Name     |
| ---------- | ------------ | ---------- | --------------- |
| 1          | Gnd          | 2          | Gnd             |
| 3          | FCM_SCL      | 4          | FCM_SDA         |
| 5          | FAN_ALARM    | 6          | FCM_PCA9548_RST |
| 7          | CARD_PRESENT | 8          | FCM_CPLD_RST    |
| 9          | Gnd          | 10         | Gnd             |
| 11         | FCM_SEL      | 12         | FCM_TMS         |
| 13         | FCM_TCK      | 14         | FCM_TDI         |
| 15         | FCM_TDO      | 16         | Gnd             |
| 17         | 3R3V_EN      | 18         | FCM_Hitless     |
| 19         | NC           | 20         | NC              |

Power

| Pin number  | 1    | 2    | 3    | 4    | 5    | 6    |
| ----------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Signal name | 12V  | 12V  | 12V  | GND  | GND  | GND  |
| Signal name | 12V  | 12V  | 12V  | GND  | GND  | GND  |
| Pin number  | 7    | 8    | 9    | 10   | 11   | 12   |

### 6.3. Interfaces between PDB and SMB

Signal definitions:

|                     | MPN            | Vendor   |
| ------------------- | -------------- | -------- |
| PDB_T signal        | 501190-2017    | Molex    |
| PDB_T power         | C10-761044-000 | AMPHENOL |
| SMB signal to PDB_T | 501190-2017    | Molex    |
| SMB signal to PDB_B | 501190-3017    | Molex    |
| SMB power           | C10-760262-000 | AMPHENOL |
| PDB_B signal        | 501190-3017    | Molex    |
| PDB_B power         | C10-760246-000 | AMPHENOL |

| Pin  | Signal Name | Pin  | Signal Name |
| ---- | ----------- | ---- | ----------- |
| 1    | PSU_I2C_SCL | 2    | PSU_I2C_SDA |
| 3    | PSU_ALERT_L | 4    | PSU_PWROK   |
| 5    | PSU_ACOK    | 6    | PSU_PRNST_N |
| 7    | PSU_L1_ON   | 8    | Gnd         |
| 9    | V_SENSE     | 10   | V_SENSE_R   |
| 11   | ISHARE      | 12   | Gnd         |
| 13   | Gnd         | 14   | Gnd         |
| 15   | Gnd         | 16   | Gnd         |
| 17   | 3.3V_SBY    | 18   | 3.3V_SBY    |
| 19   | 3.3V_SBY    | 20   | 3.3V_SBY    |
| 21   | NC          | 22   | NC          |
| 23   | NC          | 24   | NC          |
| 25   | NC          | 26   | NC          |
| 27   | NC          | 28   | NC          |
| 29   | NC          | 30   | NC          |

### 6.4. Interfaces between Rackmon board and SMB

Signal definitions:

| Rack Mon connector | NA                       | NA       |
| ------------------ | ------------------------ | -------- |
| SMB connector      | HSEC8-125-01-L-DV-A-K-TR | Samtec   |
| RackMon RJ45 2 * 2 | RMR4JZ-Z6B3-3ED-0R       | Luxshare |
| USB 3.0            | 484040004                | Molex    |
| Led(4)             |                          |          |

| Pin  | Signal Name     | Pin  | Signal Name     |
| ---- | --------------- | ---- | --------------- |
| 1    | RMON_PF_1       | 2    | RMON_RF_1       |
| 3    | RMON_PF_2       | 4    | RMON_RF_2       |
| 5    | RMON_PF_3       | 6    | RMON_RF_3       |
| 7    | PCA9535_LED_SCL | 8    | PCA9535_LED_SDA |
| 9    | RACK_GPIO_1     | 10   | RACK_GPIO_2     |
| 11   | RACK_GPIO_3     | 12   | RACK_GPIO_4     |
| 13   | RACK_GPIO_5     | 14   | RACK_GPIO_6     |
| 15   | RACK_GPIO_7     | 16   | RACK_GPIO_8     |
| 17   | FT232_Reset_N   | 18   | Debug_Present_N |
| 19   | **XP3R3V**      | 20   | **XP3R3V**      |

| Pin number      | 21   | 23                | 25                | 27   | 29             | 31             | 33   | 35                | 37                | 39   |
| --------------- | ---- | ----------------- | ----------------- | ---- | -------------- | -------------- | ---- | ----------------- | ----------------- | ---- |
| **Signal name** | Gnd  | OOB_SW_SMIIA_TX_P | OOB_SW_SMIIA_TX_N | Gnd  | USB_FT232_P    | USB_FT232_N    | Gnd  | OOB_SW_SMIIA_RX_P | OOB_SW_SMIIA_RX_N | Gnd  |
| **Signal name** | Gnd  | OOB_SW_SMIIB_TX_P | OOB_SW_SMIIB_TX_N | Gnd  | MGMT_BRD_USB_P | MGMT_BRD_USB_N | Gnd  | OOB_SW_SMIIB_RX_P | OOB_SW_SMIIB_RX_N | Gnd  |
| Pin number      | 22   | 24                | 26                | 28   | 30             | 32             | 34   | 36                | 38                | 40   |

| 41   | **XP5R0V**        | 42   | **XP5R0V**       |
| ---- | ----------------- | ---- | ---------------- |
| 43   | Debug_SCL         | 44   | Debug_SDA        |
| 45   | Gnd               | 46   | PCA9535_reset_N  |
| 47   | Debug_UART_TX     | 48   | Debug_UART_RX    |
| 49   | Rack_Mon_Ge_MDC   | 50   | Gnd              |
| 51   | Gnd               | 52   | Rack_Mon_Ge_MDIO |
| 53   | Rack_Button_LED_G | 54   | Gnd              |
| 55   | Rack_Button_LED_B | 56   | Rack_LED_BUTTON  |
| 57   | **XP12R0V**       | 58   | **XP12R0V**      |
| 59   | Rack_RESET_BUTTON | 60   | Gnd              |

### 6.5. Interfaces between Timing board and SMB

Signal definitions:

|              | MPN            | Vendor |
| ------------ | -------------- | ------ |
| SMB          | 61082-042422LF | FCI    |
| Timing board | TBD            | FCI    |

| 1    | **XP12R0V**       | 2    | **XP12R0V**       |
| ---- | ----------------- | ---- | ----------------- |
| 3    | GND               | 4    | GND               |
| 5    | **XP3R3V**        | 6    | **XP3R3V**        |
| 7    | **XP3R3V**        | 8    | **XP3R3V**        |
| 9    | GND               | 10   | GND               |
| 11   | PTP_BMC_SCL       | 12   | PTP_SPI_CS1       |
| 13   | PTP_BMC_SDA       | 14   | PTP_SPI_CS2       |
| 15   | GND               | 16   | GND               |
| 17   | PTP_RESET         | 18   | PTP_SPI_MISO      |
| 19   | PTP_PRESENT       | 20   | PTP_SPI_MOSI      |
| 21   | GND               | 22   | PTP_SPI_SCK       |
| 23   | DPLL_REF_CLK_P    | 24   | GND               |
| 25   | DPLL_REF_CLK_N    | 26   | PTP_FPGA_CLK_4K   |
| 27   | GND               | 28   | PTP_FPGA_CLK_1PPS |
| 29   | NC                | 30   | GND               |
| 31   | NC                | 32   | GND               |
| 33   | GND               | 34   | PTP_FPGA_CLK_25M  |
| 35   | L1_RCVRD_CLK      | 36   | NC                |
| 37   | GND               | 38   | GND               |
| 39   | L1_RCVRD_CLK_BKUP | 40   | NC                |

## 7. Transceivers and cables

100G optic

- QSFP28 CWDM4 100G transceiver (MSA)
- QSFP28 LR4/LR4-lite 100G transceiver (IEEE)
- QSFP28 SR4 100G transceiver (IEEE)
- 100G DAC Cable
- QSFP28 100GE to QSFP28 100GE cable, 1M, 2M, 3M, 3.5M
- QSFP28 100GE to 2 QSFP28 50GE split cable, aka Y-cable, 1M, 2M, 3M, 3.5M
- QSFP28 100GE to 4 SFP28 25GE fanout cable, 1M, 2M, 3M, 3.5M

200G optic

- QSFP56 FR4 200G transceiver
- QSFP56 200G to QSFP56 200G cable, 1M, 1.5M, 2M

400G optic

- QSFP-DD FR4 400G transceiver

## 8. Wedge400C Power and Mechanical

Wedge400C has AC version and DC version. The DC version is based on 12V ORv2 power supply.

### 8.1. DC/DC Power Extension Module (PEM)

Wedge400C has 12V DC PEM to support ORv2 rack installation. It supports:

- current capacity up to 70A;
- one PEM module without load sharing on 12V;
- Hot-swap controlling;
- 3.3V@0.5A standby always on, and ORing / LDO inside module;
- PSU_ON signal to enable/disable 12V output.

### 8.2. AC/DC PSU

Wedge400C uses Delta DDM1500BH12A3F AC power supply unit (PSU) to provide power to the chassis. There are 2 PSU in the chassis. Each PSU is rated at 1500W with 12V output. The power system of Wedge400C is load sharing of two PSU, usually it is used as 1+1 PSU redundancy, one PSU connect to one AC feed and the other PSU connect to redundant feed, providing feed redundancy. The following Figure shows the AC PSU from Delta.

#### Figure 35: DDM1500BH12A3F 1.5KW PSU

Power Supply Connector: Tyco Electronics P/N 2-1926736-3 (NOTE: Column 5 is recessed (short pins))

Mating Connector: Tyco Electronics P/N 2-1926739-5 or FCI 10108888-R10253SLF

#### Figure 36:PSU power output connector

HOUSING-

FIRST C]RCU]T-

TE PART NUMBER 1NDCA TOR AND DATE CODE

S]GNAL contAcTS

POWER ContACTS

|       | 1    | 2        | 3         | 4      | 5         | PGND      | V1         |
| ----- | ---- | -------- | --------- | ------ | --------- | --------- | ---------- |
| **A** | VSB  | SGND     | APS       | SCL    | PSKILL_H  | 1,2,3,4,5 | 6,7,8,9,10 |
| **B** | VSB  | SGND     | N/C       | PSON_L | ISHARE    |           |            |
| **C** | VSB  | HOTSTAN  | SMB_ALERT | T_L    | PWOK_H    |           |            |
| **D** | VSB  | VSB_SENS | V1_SENSE  | N/C    | VSB_SEL   |           |            |
| **E** | VSB  | VSB_SENS | V1_SENSE  | ACOK_H | PRESENT_L |           |            |

| Signal Name | Type                 | Vlow\_ max | Vhigh\_ min | Function                     | Comments                                                     |
| ----------- | -------------------- | ---------- | ----------- | ---------------------------- | ------------------------------------------------------------ |
| PWOK\_H     | Output / Active high | 0.4V       | 2.4V        | Power OK                     | Logic “High” –<br/>Output is OK<br/>Logic “Low” –<br/>Output is not OK<br/>Pull up resistor is <br/>10kohm |
| ACOK\_H     | Output / Active high | 0.4V       | 2.4V        | Power OK                     | Logic “High” –<br/>Output is OK<br/>Logic “Low” –<br/>Output is not OK<br/>Pull up resistor is <br/>10kohm |
| PSON\_L     | Input / Active low   | 0.8V       | 2.0V        | Enable / Disable Main Output | Logic “Low” – turn ON Logic “High” – turn Off Pull up resistor is <br/>10kohm |

| PRESENT\_L      | Output / Active low | 0.4V | -    | PSU                                                          | Connected to SGND inside PSU                                 |
| --------------- | ------------------- | ---- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SCL             | Input               | 0.4V | 2.1V | I2C clock                                                    | Pull down resistor is 47.5ohm                                |
| SDA             | Bi-directional      | 0.4V | 2.1V | I2C data                                                     | Pull down resistor is 47.5ohm                                |
| SMB\_ALERT\_L   | Output / Active low | 0.4  | 2.4  | SM Alert                                                     | Logic “Low” – Fault <br/>or Warning<br/>Logic “High” – OK    |
| PSKILL\_H       | Input / Active low  | 0.8V | 2.0V | Control the <br/>PSU                                         | Logic “Low” – PSU <br/>OK Logic “High” –<br/>PSU shut down<br/>Pull up resistor is <br/>47.5kohm |
| HOTSTANDBYEN\_H | Input / Active low  | 0.8V | 2.0V | Control the <br/>Smart <br/>standby <br/>mode                | Logic “Low” –<br/>normal redundancy <br/>mode Logic “High” <br/>– Smart standby <br/>mode Pull up <br/>resistor is 10kohm |
| APS             | Input               | -    | -    | The I2C address                                              | Pull up resistor is 12.1kohm Select the address Pull up resistor is <br/>12.1kohm |
| VSB\_SEL        | Input               | -    | -    | Select the standby output                                    | NA                                                           |
| ISHARE          | Analog              | -    | -    | Main output <br/>current <br/>share bus                      |                                                              |
| V1\_SENSE\_R    | Analog              | -    | -    | Main output remote negative sense line                       |                                                              |
| V1\_SENSE       | Analog              | -    | -    | Main output remote positive sense line                       |                                                              |
| VSB\_SENSE      | Analog              | -    | -    | Standby output<br/><br/>remote<br/><br/>positive<br/><br/>sense line |                                                              |

| VSB_SENSE<br/>_R | Analog | -    | -    | Standby <br/>output <br/>remote <br/>positive <br/>sense line |
| ---------------- | ------ | ---- | ---- | ------------------------------------------------------------ |
| SGND             | Analog | -    | -    | Signal ground                                                |
| VSB              | Power  | -    | -    | output power pin                                             |

### 8.3. Power Circuits Design Target

Here is the power estimation which is for DC/DC design to support worst case. It’s target for board DC/DC design, not for thermal design.

|         | Component     | QTY  | 12V  | 5V   | 3.3V | 1.2V  |
| ------- | ------------- | ---- | ---- | ---- | ---- | ----- |
| **SCM** | COMe Module   | 1    | 5    | 2    |      |       |
|         | CPLD          | 1    |      |      | 0.15 |       |
|         | M.2           | 2    |      |      | 2.5  |       |
|         | BCM54616S     | 1    |      |      | 0.35 | 0.24  |
|         | Other         | 1    |      |      | 0.5  |       |
|         | **Total (W)** | 93.4 | 60   | 10   | 23.1 | 0.288 |

### 8.4. Power Tree

Here is the power tree estimated from 12V main input to low voltage power rails:

#### Figure 37:Power Tree Diagram

### 8.5. Voltage Detection Sensors

There are 9 Low Voltage Monitor Inputs which can accept voltage range between 0.075V and 5.734V and 1 High Voltage Monitor Inputs which can accept voltage range between 0.3V and 13.2V.

There are 8 power rails on board and 2 power rails from PSU. The detail channel mapping is shown below.

#### Table 91 ispPAC_POWR1220AT8 IO Assignment

| Sequence  | Power rails    | board | Monitor | Power on condition      | Enable      | Default | PG connect to | Device 1      | Device 2     | Device 3  |
| --------- | -------------- | ----- | ------- | ----------------------- | ----------- | ------- | ------------- | ------------- | ------------ | --------- |
| SMB board |                |       |         |                         |             |         |               |               |              |           |
| 1         | XP3R3V\_VSB    | SMB   | NA      | Auto power on           | NA          | On      | NA            | PWR CPLD      |              |           |
| 2         | XP12R0V        | SMB   | PWR1220 | Auto power on           | PWR CPLD    | On      | NA            | Power devices |              |           |
| 3         | XP3R3V\_1220   | SMB   | NA      | XP12R0V OK              | NA          | On      | System CPLD   | PWR 1220      |              |           |
| 3         | XP5R0V         | SMB   | PWR1220 | XP12R0V OK              | NA          | On      | System CPLD   | Power devices |              |           |
| 4         | XP3R3V\_BMC    | SMB   | PWR1220 | XP5R0V OK               | PWR1220     | Off     | System CPLD   | BMC           | System CPLD  | BCM54616S |
| 4         | XP1R0V\_FPGA   | SMB   | BMC     | XP5R0V OK               | PWR1220     | Off     | System CPLD   | DOM FPGA      |              |           |
| 5         | XP5R0V\_USB    | SMB   | NA      | XP3R3V\_BMC & XP5R0V OK | System CPLD | On      | System CPLD   | USB           |              |           |
| 5         | XP2R5V\_BMC    | SMB   | BMC     | XP3R3V\_BMC & XP5R0V OK | NA          | On      | System CPLD   | BMC           | OOB switch   | BCM54616S |
| 5         | XP1R2V\_BMC    | SMB   | PWR1220 | XP3R3V\_BMC OK          | PWR1220     | Off     | System CPLD   | BMC           |              |           |
| 6         | XP1R15V\_BMC   | SMB   | BMC     | XP2R5V\_BMC OK          | NA          | On      | System CPLD   |               |              |           |
| 7         | XP1R8V\_FPGA   | SMB   | PWR1220 | XP1R2V\_BMC OK          | PWR1220     | Off     | System CPLD   | DOM FPGA      |              |           |
| 8         | XP3R3V\_FPGA   | SMB   | PWR1220 | XP1R8V\_FPGA OK         | PWR1220     | Off     | System CPLD   | DOM FPGA      |              |           |
| 9         | XP3R3V\_Left   | SMB   | BMC     | XP3R3V\_FPGA OK         | PWR1220     | Off     | System CPLD   | QSFP-DD       | QSFP-56      | SI5391    |
| 9         | XP3R3V\_right  | SMB   | BMC     | XP3R3V\_FPGA OK         | PWR1220     | Off     | System CPLD   | QSFP-DD       | QSFP-56      |           |
| 9         | XP1R8V\_IO     | SMB   | PWR1220 | XP3R3V\_FPGA OK         | PWR1220     | Off     | System CPLD   | GB switch     |              |           |
| 10        | VDD\_CORE      | SMB   | PWR1220 | XP1R8V\_IO OK           | PWR1220     | Off     | System CPLD   | GB switch     |              |           |
| 11        | XP0R75V\_PCIE  | SMB   | PWR1220 | VDD\_CORE OK            | PWR1220     | Off     | System CPLD   | GB switch     |              |           |
| 11        | XP0R75V\_VDDA  | SMB   | NA      | VDD\_CORE OK            | PWR1220     | Off     | System CPLD   | GB switch     |              |           |
| 11        | XP0R94V\_VDDA  | SMB   | PWR1220 | VDD\_CORE OK            | PWR1220     | Off     | System CPLD   | GB switch     |              |           |
| 11        | XP1R2V\_VDDH   | SMB   | BMC     | VDD\_CORE OK            | PWR1220     | Off     | CPLD/PWR1220  | GB switch     |              |           |
| 11        | XP1R8V\_ALG    | SMB   | BMC     | VDD\_CORE OK            | PWR1220     | Off     | CPLD/PWR1220  | GB switch     |              |           |
| 11        | XP2R5V\_HBM    | SMB   | PWR1220 | VDD\_CORE OK            | PWR1220     | Off     | System CPLD   | GB switch     |              |           |
| 12        | XP1R2V\_HBM    | SMB   | BMC     | XP2R5V\_HBM OK          | PWR1220     | Off     | CPLD/PWR1220  | GB switch     |              |           |
| 13        | XP1R15V\_VDDCK | SMB   | PWR1220 | XP0R94V\_VDDA OK        | PWR1220     | Off     | System CPLD   | GB switch     |              |           |
| SCM board |                |       |         |                         |             |         |               |               |              |           |
| 1         | SCM\_Hot swap  | SCM   | NA      | Auto power on           | System CPLD | ON      | SCM CPLD      |               |              |           |
| 2         | XP3R3V\_SCM    | SCM   | NA      | Auto power on           | SCM CPLD    | Off     | SCM CPLD      | CPLD          | Phy          |           |
| 3         | 12V\_COME      | SCM   | NA      | BMC SW enable           | SCM CPLD    | Off     | SCM CPLD      | COME          |              |           |
| 3         | 5V\_COME       | SCM   | NA      | BMC SW enable           | SCM CPLD    | Off     | SCM CPLD      | COME          |              |           |
| 3         | XP3R3V\_M2     | SCM   | NA      | BMC SW enable           | SCM CPLD    | Off     | SCM CPLD      | M.2 module    |              |           |
| FCB board |                |       |         |                         |             |         |               |               |              |           |
| 1         | FCB\_Hot swap  | FCB   | NA      | Auto power on           | System CPLD | ON      | FCB CPLD      |               |              |           |
| 2         | XP3R3V_CPLD    | FCB   | NA      | Auto power on           | FCB CPLD    | off     | FCB CPLD      | CPLD          | logic device |           |
| 3         | E-fuse         | FCB   | NA      | Auto power on           | FCB CPLD    | off     | FCB CPLD      | Fan tray      |              |           |

### 8.6. Current Detection Sensors

The current detection on Wedge400C will be categorized as follows.

- Current of 12V primary power can be read from PSU through I2C
- Currents of switch core/analogy power rails (high current) can be read from PWM controllers through I2C
- Current of QSFP-DD 3.3V can be read from PWM controller through I2C
- Current of other power rails (small current) will NOT be monitored

#### Figure 38:Power Monitor Diagram

| PSU1/PEM1                    | 3.3V SBY            | 12V             | PSU2/PEM2     | 3.3V SBY | 12V               |
| ---------------------------- | ------------------- | --------------- | ------------- | -------- | ----------------- |
| Dummy Load                   | to GND              |                 | Dummy Load    | to GND   |                   |
| 115A                         |                     |                 |               |          |                   |
|                              | PWR1220 VMON1       | 0.05A           | TPS54320      | 0.15A    | 0.15A             |
|                              | XP3R3V\_1220\@0.15A |                 | PWR 1220      |          |                   |
| 0.5A                         | TPS54320            | 1A              | PWR1220 VMON2 | TPS2553  | 1A                |
| 1A                           |                     | XP5R0V\_USB\@1A |               |          |                   |
| 1.6A                         | TPS548A20           | 4.7A            | PWR1220 VMON3 | 0.1A     | XP3R3V\_BMC\@0.1A |
| SPI\*2                       |                     |                 |               |          |                   |
| 0.1A                         |                     |                 |               |          | XP3R3V\_BMC\@0.1A |
| 0.2A                         |                     |                 |               |          | XP3R3V\_BMC\@0.2A |
| 0.5A                         |                     |                 |               |          | XP3R3V\_BMC\@0.5A |
| 0.7A                         |                     |                 |               |          | XP3R3V\_BMC\@0.7A |
| PHY(BCM54616S)\*2            |                     |                 |               |          |                   |
| XP1R2V\_BMC\@0.48A(Internal) |                     |                 |               |          |                   |

Power Distribution

| 0.5A            | XP3R3V\_BMC\@0.5A       |                          |                        |                | LDO:TPS74801            | 0.8A             | XP1R15V\_BMC\@0.8A            | PWR1220 ADC2        |          |                    |             |
| --------------- | ----------------------- | ------------------------ | ---------------------- | -------------- | ----------------------- | ---------------- | ----------------------------- | ------------------- | -------- | ------------------ | ----------- |
| 0.3A            | TPS54320                | 2.1A                     |                        |                | 2.5V/1.15V/0.8A         | 0.2A             | XP2R5V\_BMC\@0.2A             | Aspeed 2520         |          |                    |             |
|                 |                         | 12V/1.2V/2.1A            |                        |                |                         | 0.7A             | XP1R2V\_BMC\@0.7A             |                     |          |                    |             |
|                 |                         |                          |                        |                |                         | 0.02A            | XP2R5V\_BMC\@0.02A            |                     | 0.31A    | XP1R2V\_BMC\@0.31A |             |
| LDO:            | 1.06A                   |                          |                        | NCP59744       | PWR1220 ADC1            |                  | XP2R5V\_BMC\@0.04A            | OOB Switch(BCM5389) |          |                    |             |
| 3.3V/2.5V/1.06A |                         |                          |                        |                | PWR1220 VMON5           | 0.812A           | XP1R2V\_BMC\@0.812A           |                     |          |                    |             |
|                 |                         |                          |                        | NCP45560       | 0.74A                   | PWR1220 VMON4    | 0.74A                         | XP3R3V\_FPGA\@0.74A |          |                    |             |
|                 |                         |                          |                        | LDO:TPS74801   | 0.4A                    | PWR1220 VMON6    | 0.4A                          | XP1R8V\_FPGA\@0.4A  | FPGA\*2  |                    |             |
|                 |                         |                          |                        |                |                         | 0.2A             | XP1R2V\_BMC\@0.2A             | 0.3A                | TPS54620 | 3A                 | 12V/1.0V/3A |
| LDO: NCP59744   |                         |                          |                        | 3.3V/1.2V/0.2A | PWR1220 ADC6            |                  | XP1R2V\_VDDH\@0.2A            |                     |          |                    |             |
|                 |                         |                          |                        | LDO: NCP59744  | PWR1220 VMON7           | 0.5A             | XP1R8V\_IO\@0.5A              | LDO                 | 0.15A    |                    |             |
| NCP45560        | SWITCH                  |                          |                        | LDO: NCP59744  | PWR1220 VMON8           | 0.25A            | XP2R5V\_HBM\@0.25A            |                     |          |                    |             |
|                 |                         |                          |                        | LDO: ISL80101  |                         | 0.2A             | XP0R75V\_VDDA\@0.2A           | GB                  |          |                    |             |
| 5A              | 1.2V/27A: TDA21472\*1   | 27A                      | 3.3V/0.75V/0.2A        | PWR1220 ADC7   | 27A                     | XP1R2V\_HBM\@27A | Switch                        |                     |          |                    |             |
|                 | TPS54820                | 1.15V/8A: TDA21472\*1    | 8A                     |                | 8A                      |                  | FLT\_IFG\_VDDCK\_1P15V\_0\@8A |                     |          |                    |             |
|                 | TPS54820                | 12V/1.15V/8A             | 8A                     |                | PWR1220 VMON12          | 8A               | FLT\_IFG\_VDDCK\_1P15V\_1\@8A |                     |          |                    |             |
|                 |                         |                          |                        |                | PWR1220 VMON10          | 54A              | VDD\_CORE 0.83V\@370A         |                     |          |                    |             |
|                 | 20A                     | IR35215                  | 0.96V/54A: TDA21472\*2 | 54A            | 3.3V/58.2A: TDA21472\*2 | 58.2A            |                               |                     |          |                    |             |
|                 |                         |                          |                        |                | PWR1220 ADC4            | 58.2A            | XP3R3V\_LEFT58.2A(max)        | QSFP\_Left          |          |                    |             |
| 25A             |                         | 0.75V/52.2A: TDA21472\*2 | 52.2A                  | IR35215        | 0.94V/68A: IR3556\*3    | 58.2A            |                               |                     |          |                    |             |
|                 | 3.3V/58.2A: TDA21472\*2 |                          |                        |                | PWR1220 ADC3            |                  | XP3R3V\_RIGHT 58.2A(max)      | QSFP\_Right         |          |                    |             |

Power Monitor Diagram

| 12V from SMB          | ADM1278/8A         | NCP45560    | 12v\_COMEIA     |                             |              |            |      |
| --------------------- | ------------------ | ----------- | --------------- | --------------------------- | ------------ | ---------- | ---- |
|                       | (Voltage & Current | Load switch |                 | COME Card                   |              |            |      |
|                       |                    | TPS54320    | Sv\_COMEIZA     | 12VISVIZA                   |              |            |      |
|                       |                    |             | XF3R3VI0.154    | +-593                       | CPLD         |            |      |
| SCM board             | TPS548420          | NCP45560    | XP3R3V\_BBISA   | +-593                       | SSD\*2       |            |      |
| Hotswap               | 12v/3.3V/6A        | Load switch |                 |                             |              |            |      |
|                       |                    |             | 358             | XF3R3VI0.354                | +-593        | PHY 54616S |      |
| 'IRZVIO.24A(internal) |                    |             | XPZR3VIC.54     | +-598                       | Others       |            |      |
| 12V from SMB          | 24A                | ADM1278/24A | 2364 MP5022C\*4 | 12vi23.8A(6A FANE1O.8A\_pk} | Fan tray     |            |      |
| FCB Board             | OCP 50A            | E-fuse      |                 |                             |              |            |      |
| (Voltage & Current    | Monitor)           | TPS54320    | 0.45            | 0                           | XP3R3VIC.154 | +-556      | CPLD |
|                       |                    |             |                 |                             | EZprom/1zc   |            |      |

## 9. Thermal design</h9>
The thermal design of Wedge400C is optimized for better thermal performance to support 55C CWDM4 100G optics, 65C FR4 200G optics and 65C FR4 400G optics, which are specified by Meta.

Totally there are 4 fan-tray in Wedge400C chassis, each fan-tray has one 80mm x 80mm x 80mm CR fan. The FCM (Fan Control Module) supports 4 fan-tray.

### 9.1. Fan tray</h9>
Wedge400C chassis supports four fan-tray with 3+1 redundancy.

#### Figure 39: Wedge400C Fan-tray

The following Sanyo Denki CR fan is recommended.

- Sanyo Denki: 9CRA0812P8G001 (80mm x 80mm x 80mm)
- 63.6W Max
- Rated speed: 12000 inlet, 11300 outlet
- Max Airflow: 4.5 M3/min, or 158.9CFM
- Max Static Pressure: 4.62 inchH2O

#### Figure 40: Wedge 400C fan

80mm CR fan 9CRA0812P8G001 from Sanyo Denki has the following technical parameters

#### Table 3: Sanyo Denki fan 9CRA0812P8G001

| 9CRA0812P8G001              |                                    |
| --------------------------- | ---------------------------------- |
| Item                        | Description                        |
| Rated voltage               | 12 VDC                             |
| Operating voltage           | 7.0 \~ 13.2 VDC                    |
| Input current               | 5.30A                              |
| Input power                 | 63.6W                              |
| Safety Current on label     | 1.82A                              |
| Speed                       | Front 12000, Rear 11300 RPM +/-10% |
| Max Air flow at zero static | 4.50m3/min, or 158.9CFM            |
| Max Air Pressure            | 4.62 in-H2O                        |
| Acoustic                    | 76 dB-A                            |
| Lead Wire                   |                                    |

#### Figure 41:PQ Curve of CR Fan 9CRA0812P8G001

| Lead Wire   | Description    |
| ----------- | -------------- |
| Black Wire  | Negative (-)   |
| Red Wire    | Positive (+)   |
| Yellow wire | DC 12V         |
| Blue wire   | PWM Duty Cycle |

| (inch HzO) | (Pa) | Frequency (-FOO) | Speed control (-PWM) |
| ---------- | ---- | ---------------- | -------------------- |
| 1400       | 5.0  |                  |                      |
| 1200       | 4.0  |                  |                      |
| 1000       | 3.0  |                  |                      |
| 800        | 2.0  |                  |                      |
| 600        | 1.0  |                  |                      |
| 400        |      |                  |                      |
| 200        |      |                  |                      |

### 9.2. Temperature Sensors

Each module card can have multiple temperature sensors to monitor temperature. Temperature information needs to be reported to the BMC via system management I2C bus. Additionally, over-temperature thresholds are configurable, and an alert mechanism is provided to enable thermal shutdown and / or an increase in airflow. The sensors are accurate to +/-2C. The ambient temperature sensor can be a TMP75 from Texas Instruments or an equivalent part from other vendors. Its I2C address can be set to 0x98 to 0x9F. 8 TMP75 temperature sensors can share one i2c bus.

#### Figure 42:Temperature I2C Access

| BMC <br/>Channel | I2C <br/>switch <br/>address | switch channel | Device type and address | Description                        |
| ---------------- | ---------------------------- | -------------- | ----------------------- | ---------------------------------- |
| I2C\_3           | 0x70                         | 2              | LM75,0x4C               | Sensor on SCM.No need for FSC      |
| I2C\_3           | 0x70                         | 2              | LM75,0x4D               | Sensor on SCM.No need for FSC      |
| I2C\_4           | NA                           | NA             | LM75,0x48               | system inlet sensor(left)          |
| I2C\_4           | NA                           | NA             | LM75,0x49               | GB outlet sensor                   |
| I2C\_4           | NA                           | NA             | LM75,0x4A               | SMB outlet sensor                  |
| I2C\_4           | NA                           | NA             | LM75,0x4B               | system inlet sensor(right)         |
| I2C\_4           | NA                           | NA             | TPM421,0x4C             | system left side. No need for FSC. |
| I2C\_4           | NA                           | NA             | TPM421,0x4D             | system left side. No need for FSC. |
| I2C\_4           | NA                           | NA             | GB,0x2A                 | GB internal sensor.                |
| I2C\_12          | 0x76                         | 3              | LM75,0x48               | system outlet sensor(left)         |
| I2C\_12          | 0x76                         | 3              | LM75,0x49               | system outlet sensor(right)        |

## 10. Regulatory Compliance Requirements

Every ODM engaged with Meta to develop a L10 product to be used in our Data Center’s infrastructure must meet the following regulatory compliance requirements. Reports must be from labs accredited to a current version of IEC 17025. The reports and certificates must name the ODM as the applicant.

### 10.1. CE Declaration to the following Regulatory Directives by ODMs

- EMC Directive 2014/30/EU
- Low Voltage (LVD) Directive 2014/35/EU

### 10.2. Safety Certification

- CB certificate/report to IEC 62368-1 including all national deviations
- CB certificate/report to IEC/EN 60950-1 including all national deviations
- UL/CSA/IEC/EN 60950-1 with all latest amendments
- UL/IEC 62368-1 with all latest amendments
- CNS14336 Taiwan BSMI safety regulation
- EN 60825-1 Safety of Laser products – part 1
- UL 94-V0 Flammability rating

### 10.3. EMC Certification

Every ODM engaged with Meta to develop a L10 product to be used in our Data Center’s infrastructure must meet the following regulatory compliance requirements. Reports must be from labs accredited to a current version of IEC 17025. The reports and certificates must name the ODM as the applicant. EMC certification and report:

- FCC Part 15 (Class A)
- ICES-003 (Canada) Class A
- EN55032 (Europe) Class A
- CISPR32 (International) Class A
- AS/NZS CISPR32 (Australia and New Zealand) Class A
- VCCI CISPR 32 (Japan) Class A
- CNS 13438 (Taiwan) Class A
- EN61000-3-2
- EN61000-3-3
- EN55024
- EN 61000-4-2 ESD
- EN 61000-4-3 Radiated Immunity
- EN 61000-4-4 EFT
- EN 61000-4-5 Surge
- EN 61000-4-6 Low Frequency Conducted Immunity
- EN 61000-4-11 Voltage Variations and Dips

### 10.4. Immunity Levels

The ODM must strive to design to the FB Goal at the start and during the project. The design team will decide if levels below the goal are acceptable. Off the shelf power supplies must meet the required level at a minimum.

| Network Equipment |                               |                              |                    |                           |                        |                                                            |
| ----------------- | ----------------------------- | ---------------------------- | ------------------ | ------------------------- | ---------------------- | ---------------------------------------------------------- |
| Immunity Standard | Description                   | Standard Criteria (Required) | FB Criteria (Goal) | Standard Level (Required) | FB Level (Goal)        | Remarks                                                    |
| IEC 61000-4-2     | Electrostatic Discharge (ESD) | B                            | A                  | 4 kV Cont. / 8 kV Air     | 8 kV Cont. / 15 kV Air | Criteria A (FB Goal) is highly desirable for any level     |
| IEC 61000-4-3     | Radiated Immunity             | A                            | A                  | 3 V/m                     | 10 V/m                 | For communication cables >3 meters                         |
| IEC 61000-4-4     | EFT                           | B                            | B                  | 0.5 kV                    | -                      | Ports: Signal & Telecom (>3 meters), DC power input        |
|                   |                               | B                            | B                  | 1 kV                      | -                      | Ports: AC power input & AC/DC Converter                    |
| IEC 61000-4-5     | Surges                        | C                            | A                  | 1 kV                      | -                      | Ports: Signal and Telecom connected to outdoor cables      |
|                   |                               | B                            | A                  | 0.5 kV                    | -                      | Ports: DC power input                                      |
|                   |                               |                              |                    | 1 kV L-L / 2 kV L-GND     | -                      | Ports: AC power input & AC/DC Converter                    |
| IEC 61000-4-6     | Conducted Immunity            | A                            | A                  | 3 V                       | 10 V                   | Ports: Signal & Telecom (>3 meters), AC and DC power input |
| IEC 61000-4-8     | Magnetic Field                | A                            | A                  | 1 A/m                     | -                      | Only EUT containing devices susceptible to magnetic fields |
| IEC 61000-4-11    | Voltage Dips                  | B                            | B                  | >95% Reduction            | -                      | Ports: AC power input & AC/DC Converter (0.5 Period)       |
|                   |                               | C                            | C                  | 30% Reduction             | -                      | Ports: AC power input & AC/DC Converter (25 Periods)       |
|                   | Voltage Interruptions         | C                            | C                  | >95% Reduction            | -                      | Ports: AC power input & AC/DC Converter (250 Periods)      |

### 10.5. Sound

The ODM must strive to design to the FB Goal at the start and during the project. The design team will decide if levels above the goal are acceptable. The sound power level limits apply to the normal operating conditions where the system is configured and equipped in its deployed state with the worst case configuration to produce the loudest noise. Maintenance conditions, open covers, are not considered normal conditions and do not need to be measured. Sound from alarms does not need to be measured. Maximum fan speed expected under normal operation should be measured.

| OHSA (Required) | Directive 2003/10/EC (Goal) | FB Design Goal | Remarks                                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | --------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 85              | 80                          | 78             | Under normal operation at 25 %C, the system must not produce a A-weighted sound power level above the required limit: The FB design goal should be targeted during development of the product. The Directive goal represents the limit that requires hearing protection to be provided to our Data Center Staff in Europe. The ODM must provide the result of the formal testing: |

### 10.6. Environmental Compliance

Every ODM engaged with Meta to develop a L10 product to be used in our Data Center’s infrastructure must meet the following environmental compliance requirements. Reports must be from labs accredited to a current version of IEC 17025. Environmental Compliance reports:

- RoHS 2
- REACH (SVHC &#x26; Annex 17)
- WEEE
- POP Regulation
- Prop 65
- Batteries Directive
- Halogen-free IEC/EN 61249-2-21 (900 ppm Br or Cl, 1500 ppm combined)
- Phthalate (DEHP, DBP, DiBP, BBP)-free (1000 ppm)
- Arsenic-free (1000 ppm)
- The Packaging and Packaging Waste Directive 94/62/EC

CE Declaration to the following environmental Directives by ODM:

- RoHS Directive 2011/65/EU

## 11. Labels and Markings

### 11.1. PCBA Labels and Markings

Wedge400C PCBAs shall include the following labels on the component side of the boards. The labels shall not be placed in such a way that may cause them to disrupt the functionality or the airflow path of the system.

#### Table 92 PCBA Label Requirements

| Description                                                                                                                                                                                                                                                                                                                                         | Type           | Barcode Required? |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------- |
| Safety markings                                                                                                                                                                                                                                                                                                                                     | Silkscreen     | No                |
| Vendor P/N, S/N, REV (revision would increment for any approved changes)                                                                                                                                                                                                                                                                            | Adhesive label | Yes               |
| Vendor logo, name & country of origin                                                                                                                                                                                                                                                                                                               | Silkscreen     | No                |
| PCB vendor logo, name                                                                                                                                                                                                                                                                                                                               | Silkscreen     | No                |
| Meta P/N                                                                                                                                                                                                                                                                                                                                            | Adhesive label | Yes               |
| Date code (industry standard: WEEK/YEAR)                                                                                                                                                                                                                                                                                                            | Adhesive label | Yes               |
| DC input ratings                                                                                                                                                                                                                                                                                                                                    | Silkscreen     | No                |
| RoHS compliance                                                                                                                                                                                                                                                                                                                                     | Silkscreen     | No                |
| WEEE symbol: The motherboard will have the crossed out wheeled bin symbol to indicate that it will be taken back by the manufacturer for recycling at the end of its useful life. This is defined in the European Union Directive 2002/96/EC of January 27, 2003 on Waste Electrical and Electronic Equipment (WEEE) and any subsequent amendments. |                |                   |

### 11.2. Chassis Labels and Markings

TBD

## 12. References (OPTIONAL)

1. “Title”, publication year, publication journal/conference/standard, volume, pages, link to publication if available
2. OCP Profiles - https://github.com/opencomputeproject/OCP-Profiles
3. Redfish Interop Validator - https://github.com/DMTF/Redfish-Interop-Validator
4. Redfish Service Validator - https://github.com/DMTF/Redfish-Service-Validator
5. Redfish Service Conformance Check - https://github.com/DMTF/Redfish-Service-Conformance-CheckS

## Appendix A - Requirements for IC Approval

[Note to author: appendix A must be completed by the Contributor of Baseline Specification]

| Requirements                                                 | Details                                                      | Link to which Section in Spec |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------- |
| Contribution License Agreement                               | Which one?                                                   | Link to Sec 1                 |
| If OWF CLA, please provide link to OWFa 1.0 Final Spec Agreement. |                                                              |                               |
| If OCP CLA, please provide link to OCP Hardware Licence of choice. |                                                              |                               |
| Tenets                                                       | Which <br/>ones?<br/>Openness<br/>Efficiency<br/>Impact<br/>Scale | Link to Sec 2                 |
| Supplier Requirements:                                       |                                                              |                               |
| Supplier must be an OCP Member.                              |                                                              |                               |
| Supplier must become an OCP Solution Provider.               |                                                              |                               |
| Supplier must provide product based on this spec within 120 days |                                                              |                               |
| Supplier must make product available to the PUBLIC           |                                                              |                               |
| Name of Supplier(s)                                          |                                                              |                               |

## Appendix B - OCP Supplier Information (to be provided by the Supplier of Product within 120 days)

Your product must apply for OCP Product Recognition within 120 days.

| Company:      |   |
| ------------- | - |
| Contact Info: |   |
| Product Name: |   |
| Product SKU#: |   |
| Description:  |   |
