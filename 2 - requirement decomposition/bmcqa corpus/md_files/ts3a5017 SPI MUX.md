# TS3A5017 双 SP4T 模拟开关/多路复用器/多路信号分离器

## 1 特性

1. 在断电模式中提供了隔离，V+ = 0

2. 低导通状态电阻

3. 低电荷注入

4. 出色的通态电阻匹配

5. 低总谐波失真 (THD)

6. 2.3V 至 3.6V 单电源运行

7. 锁断性能超过 100mA（符合 JESD 78，II 类规范的要求）

8. 静电放电 (ESD) 性能测试符合 JESD 22 标准

   – 1500V 人体放电模型

   （A114-B，II 类）

   – 1000V 充电器件模型 (C101)

## 2 应用

- 采样和保持电路
- 电池供电类设备
- 音频和视频信号路由
- 通信电路

## **3** 说明

TS3A5017 器件是一款双通道单刀四掷 (4:1) 模拟开关，其设计工作电压为 2.3V 至 3.6V。此器件可以处理数字和模拟信号，并且高达 V+ 的信号可在任一方向上传输。

### 器件信息(1)

| 器件型号     | 封装       | 封装尺寸（标称值） |
| :----------- | :--------- | :----------------- |
| **TS3A5017** | SOIC (16)  | 9.90 mm × 3.90 mm  |
|              | SSOP (16)  | 4.90 mm × 3.90 mm  |
|              | TSSOP (16) | 5.00 mm × 4.40 mm  |
|              | TVSOP (16) | 4.40 mm × 3.60 mm  |
|              | UQFN (16)  | 2.50 mm × 1.80 mm  |
|              | VQFN (16)  | 4.00 mm × 3.50 mm  |

## 目 录

1. 特 性...... 1
2. 应 用...... 1
3. 说 明...... 1
4. 修 订 历 史 记 录 .......................... 2
5. Pin Configuration and Functions ......................... 3
6. Specifications........................ 4
7. - 6.1 Absolute Maximum Ratings ..... 4
- 6.2 ESD Ratings ........................... 4
- 6.3 Recommended Operating Conditions....................... 4
- 6.4 Thermal Information ................. 4
- 6.5 Electrical Characteristics for 3.3-V Supply................ 5
- 6.6 Electrical Characteristics for 2.5-V Supply................ 6
- 6.7 Switching Characteristics for 3.3-V supply................ 7
- 6.8 Switching Characteristics for 2.5-V supply................ 7
- 6.9 Typical Characteristics ............. 8

Parameter Measurement Information ................ 10
8. Detailed Description ........... 14
9. - 8.1 Overview ................................ 14

Application and Implementation ........................ 16
10. - 9.1 Application Information........... 16
- 9.2 Typical Application ................ 16

Power Supply Recommendations ..................... 17
11. - 11.1 Layout Guidelines ................ 17
- 11.2 Layout Example ................... 18

器 件 和 文 档 支 持 .................... 19
12. - 12.1 器件支持............................... 19
- 12.2 文档支持............................... 19
- 12.3 商标 ... 20
- 12.4 静电放电警告........................ 20
- 12.5 术语表 . 20

机 械、封 装 和 可 订 购 信 息...... 21

## 4 修订历史记录

Changes from Revision F (October 2018) to Revision G

- 将特性 从“2000V 人体放电模型”更改为“1500V 人体放电模型”........................... 1
- Changed the HBM value From: ±2000 V To: ±1500 V in the ESD Ratings....... 4

Changes from Revision E (April 2015) to Revision F

- Changed the XTALK MAX value From:–49 dB To – 69 dB in the Electrical Characteristics for 3.3-V Supply......................... 6

Changes from Revision D (December 2008) to Revision E

- 添加了应用、器件信息 表、引脚功能 表、ESD 额定值 表、热性能信息 表、典型特性、特性 说明 部分、器件功能模
式、应用和实施 部分、电源建议 部分、布局 部分、器件和文档支持 部分以及机械、封装和可订购信息 部分。 ................. 1
- 已删除 订购信息 表。 ..................... 1

## 5 Pin Configuration and Functions

|     | D, DBQ, DGV, and PW Package        |               | RGY Package   |     |   |
| --- | ---------------------------------- | ------------- | ------------- | --- | - |
|     | 16-Pin SOIC, SSOP, TVSOP and TSSOP |               | 16-Pin VQFN   |     |   |
|     | (Top View)                         | (Top View)    |               |     |   |
| 1EN | 1                                  | Logic Control | Logic Control |     |   |
| IN2 | 2                                  |               | 15            | 2EN |   |
| 1S4 | 3                                  |               | 14            | IN1 |   |
| 1S3 | 4                                  |               | 13            | 2S4 |   |
| 1S2 | 5                                  |               | 12            | 2S3 |   |
| 1S1 | 6                                  |               | 11            | 2S2 |   |
| 1D  | 7                                  |               | 10            | 2S1 |   |
| GND | 8                                  |               | 9             | 2D  |   |

If exposed center pad is used, it must be connected as a secondary ground or left electrically open.

|    |     |   |            |   |    |     | RSV Package |     |     |    |   |
| -- | --- | - | ---------- | - | -- | --- | ----------- | --- | --- | -- | - |
|    |     |   |            |   |    |     | 16-Pin UQFN |     |     |    |   |
|    |     |   | (Top View) |   |    |     |             |     |     |    |   |
|    |     |   |            |   |    | IN2 | 1EN+        | 2EN |     |    |   |
| V  |     |   |            |   |    |     | 16          | 15  | 14  | 13 |   |
|    |     |   |            |   |    | 1S4 | 1           | 12  | IN1 |    |   |
|    |     |   |            |   |    | 1S3 | 2           | 11  | 2S4 |    |   |
|    |     |   |            |   |    | 1S2 | 3           | 10  | 2S3 |    |   |
|    |     |   |            |   |    | 1S1 | 4           | 9   | 2S2 |    |   |
| 1D |     |   |            |   |    |     | 5           | 6   | 7   | 8  |   |
|    | GND |   |            |   | 2D |     |             |     | 1   |    |   |

### Pin Functions

| PIN NAME | SOIC, SSOP, TVSOP, TSSOP, VQFN NO. | UQFN NO. | TYPE | DESCRIPTION                    |
| -------- | ---------------------------------- | -------- | ---- | ------------------------------ |
| 1D       | 7                                  | 5        | I/O  | Common path for switch 1       |
| 1EN      | 1                                  | 15       | I    | Active-low enable for switch 1 |
| 1S1      | 6                                  | 4        | I/O  | Switch 1 channel 1             |
| 1S2      | 5                                  | 3        | I/O  | Switch 1 channel 2             |
| 1S3      | 4                                  | 2        | I/O  | Switch 1 channel 3             |
| 1S4      | 3                                  | 1        | I/O  | Switch 1 channel 4             |
| 2D       | 9                                  | 7        | I/O  | Common path for switch 2       |
| 2EN      | 15                                 | 13       | I    | Active-low enable for switch 2 |
| 2S1      | 10                                 | 8        | I/O  | Switch 2 channel 1             |
| 2S2      | 11                                 | 9        | I/O  | Switch 2 channel 2             |
| 2S3      | 12                                 | 10       | I/O  | Switch 2 channel 3             |
| 2S4      | 13                                 | 11       | I/O  | Switch 2 channel 4             |
| GND      | 8                                  | 6        | -    | Ground                         |
| IN1      | 14                                 | 12       | I    | Switch 1 input select          |
| IN2      | 2                                  | 16       | I    | Switch 2 input select          |
| V+       | 16                                 | 14       | -    | Supply voltage                 |

## 6 Specifications

### 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted)(1) (2)

|                            |                                              |                   | MIN  | MAX  | UNIT |
| :------------------------- | :------------------------------------------- | ----------------- | :--- | :--- | :--- |
| **$ V_{+} $**              | Supply voltage<sup>(3)</sup>                 |                   | -0.5 | 4.6  | V    |
| **$ V_{S} $, $ V_{D} $**   | Analog voltage<sup>(3)(4)</sup>              |                   | -0.5 | 4.6  | V    |
| **$ I_{SK} $, $ I_{DK} $** | Analog port clamp current                    | VS, VD < 0        | -50  |      | mA   |
| **$ I_{S} $, $ I_{D} $**   | ON-state switch current                      | VS, VD = 0 to 7 V | -128 | 128  | mA   |
| **$ V_{I} $**              | Digital input voltage                        |                   | -0.5 | 4.6  | V    |
| **$ I_{IK} $**             | Digital input clamp current<sup>(3)(4)</sup> | VI < 0            | -50  |      | mA   |
| **$ I_{L} $**              | Continuous current through $ V_{+} $         |                   | -    | 100  | mA   |
| **$ I_{GND} $**            | Continuous current through GND               |                   | -100 | -    | mA   |
| **$ T_{stg} $**            | Storage temperature                          |                   | -65  | 150  | °C   |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

(2) The algebraic convention, whereby the most negative value is a minimum and the most positive value is a maximum.

(3) All voltages are with respect to ground, unless otherwise specified.

(4) The input and output voltage ratings may be exceeded if the input and output clamp-current ratings are observed.

### 6.2 ESD Ratings

|                                |                                                              | VALUE | UNIT |
| ------------------------------ | ------------------------------------------------------------ | ----- | ---- |
| V(ESD) Electrostatic discharge | Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)        | ±1500 |      |
|                                | Charged-device model (CDM), per JEDEC specification JESD22-<br/>C101(2) | ±1000 | V    |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.

(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

### 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|      |                                   | MIN  | MAX  | UNIT |
| ---- | --------------------------------- | ---- | ---- | ---- |
| VI/O | Switch input/output voltage range | 0    | 3.6  | V    |
| V+   | Supply voltage range              | 2.3  | 3.6  | V    |
| VI   | Control input voltage range       | 0    | 3.6  | V    |
| TA   | Operating Temperature Rang        | –40  | 85   | °C   |

### 6.4 Thermal Information TS3A5018

| THERMAL METRIC(1)                           | D (SOIC) | DBQ     | DGV     | PW      | RGY     | RSV (UQFN) | UNIT |
| ------------------------------------------- | -------- | ------- | ------- | ------- | ------- | ---------- | ---- |
|                                             | 16 PINS  | 16 PINS | 16 PINS | 16 PINS | 16 PINS | 16 PINS    |      |
| RθJA Junction-to-ambient thermal resistance | 73       | 82      | 120     | 108     | 91.6    | 184        | °C/W |

(1) For more information about traditional and new thermal metrics, see the IC Package Thermal Metrics application report, SPRA953.

### 6.5 Electrical Characteristics for 3.3-V Supply

V₊ = 2.7 V to 3.6 V, TA = –40°C to 85°C (unless otherwise noted)(1)

| PARAMETER                                               |                                            | TEST CONDITIONS                           |                              | TA   | V+    | MIN  | TYP  | MAX  | UNIT |
| ------------------------------------------------------- | ------------------------------------------ | ----------------------------------------- | ---------------------------- | ---- | ----- | ---- | ---- | ---- | ---- |
| **ANalog Switch**                                       |                                            |                                           |                              |      |       |      |      |      |      |
| VD, Vs                                                  | ANalog signal range                        |                                           |                              |      |       | 0    |      | V+   | V    |
| ron                                                     | ON-state resistance                        | 0 ≤ Vs ≤ V+, Ib = -32 mA                  | Switch ON,<br/>see Figure 12 | 25°C | 3 V   |      | 11   | 12   | Ω    |
|                                                         |                                            |                                           |                              | Full |       |      |      | 14   |      |
| Δron                                                    | ON-state resistance match between channels | Vs = 2.1 V, Ib = -32 mA                   | Switch ON, see Figure 12     | 25°C | 3 V   |      | 1    | 2    | Ω    |
|                                                         |                                            |                                           |                              | Full |       |      |      | 3    |      |
| ron(flat)                                               | ON-state resistance flatness               | 0 ≤ Vs ≤ V_z, Ib = -32 mA                 | Switch ON, see Figure 12     | 25°C | 3 V   |      | 7    | 9    | Ω    |
|                                                         |                                            |                                           |                              | Full |       |      |      | 10   |      |
| Is(SOFF)                                                | S OFF leakage current                      | Vs = 1 V, VD = 3 V, Vs = 3 V, VD = 1 V    | Switch OFF, see Figure 13    | 25°C | 3.6 V | -0.1 | 0.05 | 0.1  | μA   |
|                                                         |                                            |                                           |                              | Full |       | -0.2 |      | 0.2  |      |
| IsSPWR(FF)                                              |                                            | Vs = 0 to 3.6 V, VD = 3.6 V to 0          |                              | 25°C | 0 V   | -1   | 0.5  | 1    |      |
|                                                         |                                            |                                           |                              | Full |       | -5   |      | 5    |      |
| id(off)                                                 | D OFF leakage current                      | Vs = 1 V, VD = 3 V, or Vs = 3 V, VD = 1 V | Switch OFF, see Figure 13    | 25°C | 3.6 V | -0.1 | 0.05 | 0.1  | μA   |
|                                                         |                                            |                                           |                              | Full |       | -0.2 |      | 0.2  |      |
| I dPWR(OFF)                                             |                                            | VD = 0 to 3.6 V, Vs = 3.6 V to 0          |                              | 25°C | 0 V   | -1   | 0.5  | 1    |      |
|                                                         |                                            |                                           |                              | Full |       | -5   |      | 5    |      |
| Is(ON)                                                  | S ON leakage current                       | Vs = 1 V, VD = Open, Vs = 3 V, VD = Open  | Switch ON, see Figure 14     | 25°C | 3.6 V | -0.1 | 0.05 | 0.1  | μA   |
|                                                         |                                            |                                           |                              | Full |       | -0.2 |      | 0.2  |      |
| Id(ON)                                                  | D ON leakage current                       | VD = 1 V, Vs = Open, VD = 3 V, Vs = Open  | Switch ON, see Figure 14     | 25°C | 3.6 V | -0.1 | 0.05 | 0.1  | μA   |
|                                                         |                                            |                                           |                              | Full |       | -0.2 |      | 0.2  |      |
| **Digital Control Inputs (IN1, IN2, EN)<sup>(2)</sup>** |                                            |                                           |                              |      |       |      |      |      |      |
| VlH                                                     | Input logic high                           |                                           |                              | Full |       | 2    |      | V+   | V    |
| VlL                                                     | Input logic low                            |                                           |                              | Full |       | 0    |      | 0.8  | V    |
| IlH, IlL                                                | Input leakage current                      | V1 = V_z, or 0                            |                              | 25°C | 3.6 V | -1   | 0.05 | 1    | μA   |
|                                                         |                                            |                                           |                              | Full |       | -1   |      | 1    |      |
| Qc                                                      | Charge injection                           | VGEN = 0, RGEN = 0, CL = 0.1 nF           | See Figure 21                | 25°C | 3.3 V |      |      | 5    | pC   |
| CS(off)                                                 | S OFF capacitance                          | Vs = V_z or GND, Switch OFF               | See Figure 15                | 25°C | 3.3 V |      |      | 4.5  | pF   |
| CD(off)                                                 | D OFF capacitance                          | VD = V_z or GND, Switch OFF               | See Figure 15                | 25°C | 3.3 V |      |      | 19   | pF   |
| CS(ON)                                                  | S ON capacitance                           | Vs = V_z or GND, Switch ON                | See Figure 15                | 25°C | 3.3 V |      |      | 25   | pF   |
| CD(ON)                                                  | D ON capacitance                           | VD = V_z or GND, Switch ON                | See Figure 15                | 25°C | 3.3 V |      |      | 25   | pF   |
| Cl                                                      | Digital input capacitance                  | V1 = V_z, or GND                          | See Figure 15                | 25°C | 3.3 V |      |      | 2    | pF   |
| BW                                                      | Bandwidth                                  | R_L = 50 Ω, Switch ON                     | See Figure 17                | 25°C | 3.3 V |      |      | 165  | MHz  |
| OISO                                                    | OFF isolation                              | R_L = 50 Ω, f = 1 MHz                     | See Figure 18                | 25°C | 3.3 V |      |      | -69  | dB   |

(1) The algebraic convention, whereby the most negative value is a minimum and the most positive value is a maximum

(2) All unused digital inputs of the device must be held at V+ or GND to ensure proper device operation. Refer to the TI application report, Implications of Slow or Floating CMOS Inputs, literature number SCBA004.

### Electrical Characteristics for 3.3-V Supply (continued)

V₊ = 2.7 V to 3.6 V, TA = –40°C to 85°C (unless otherwise noted)(1)

| PARAMETER  |                           | TEST CONDITIONS                                | TA   | V+    | MIN   | TYP  | MAX  | UNIT |      |      |
| ---------- | ------------------------- | ---------------------------------------------- | ---- | ----- | ----- | ---- | ---- | ---- | ---- | ---- |
| XTALK      | Crosstalk                 | RL = 50 Ω, See Figure 19                       | 25°C | 3.3 V | –69   |      |      | dB   |      |      |
| XTALK(ADJ) | Crosstalk adjacent        | RL = 50 Ω, See Figure 20                       | 25°C | 3.3 V | –74   |      |      | dB   |      |      |
| THD        | Total harmonic distortion | RL = 600 Ω, f = 20 Hz to 20 kHz, see Figure 22 | 25°C | 3.3 V | 0.21% |      |      |      |      |      |
| I+         | Positive supply current   | VI = V+ or GND, Switch ON or OFF               | 25°C | 3.6 V |       | 2.5  | 7    | μA   |      |      |
|            |                           |                                                | full |       |       |      | 10   |      |      |      |

### 6.6 Electrical Characteristics for 2.5-V Supply

V₊ = 2.3 V to 2.7 V, TA = –40°C to 85°C (unless otherwise noted)(1)

| PARAMETER                                    |                                            | TEST CONDITIONS                                            |                           | TA   | V+    | MIN  | TYP  | MAX  | UNIT |
| -------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------- | ------------------------- | ---- | ----- | ---- | ---- | ---- | ---- |
| **ANalog Switch**                            |                                            |                                                            |                           |      |       |      |      |      |      |
| VD, Vs                                       | ANalog signal range                        |                                                            |                           |      |       | 0    |      | V+   | V    |
| ron                                          | ON-state resistance                        | 0 ≤ Vs ≤ V+, Ib = -24 mA                                   | Switch ON, see Figure 12  | 25°C | 2.3 V |      | 20.5 | 32   | Ω    |
|                                              |                                            |                                                            |                           | Full |       |      |      | 24   |      |
| Δron                                         | ON-state resistance match between channels | Vs = 1.6 V, Ib = -24 mA                                    | Switch ON, see Figure 12  | 25°C | 2.3 V |      | 1    | 2    | Ω    |
|                                              |                                            |                                                            |                           | Full |       |      |      | 3    |      |
| ron(flat)                                    | ON-state resistance flatness               | 0 ≤ Vs ≤ V_+, Ib = -24 mA                                  | Switch ON, see Figure 12  | 25°C | 2.3 V |      | 16   | 18   | Ω    |
|                                              |                                            |                                                            |                           | Full |       |      |      | 20   |      |
| Is(OFF)                                      | S OFF leakage current                      | VS = 0.5 V, VD = 2.2 V,<br/>or<br/>VS = 2.2 V, VD = 0.5 V, | Switch OFF, see Figure 13 | 25°C | 2.7 V | -0.1 | 0.05 | 0.1  | μA   |
|                                              |                                            |                                                            |                           | Full |       | -0.2 |      | 0.2  |      |
| IsSPWR(OFF)                                  |                                            | VS = 0 to 2.7 V,<br/>VD = 2.7 V to 0,                      |                           | 25°C | 0 V   | -1   | 0.5  | 1    |      |
|                                              |                                            |                                                            |                           | Full |       | -5   |      | 5    |      |
| id(off)                                      | D OFF leakage current                      | VS = 0.5 V, VD = 2.2 V,<br/>or<br/>VS = 2.2 V, VD = 0.5V,  | Switch OFF, see Figure 13 | 25°C | 2.7 V | -0.1 | 0.05 | 0.1  | μA   |
|                                              |                                            |                                                            |                           | Full |       | -0.2 |      | 0.2  |      |
| I dPWR(FF)                                   |                                            | VD = 0 to 2.7 V,<br/>VS = 2.7 V to 0,                      |                           | 25°C | 0 V   | -1   | 0.5  | 1    |      |
|                                              |                                            |                                                            |                           | Full |       | -5   |      | 5    |      |
| Is(ON)                                       | S ON leakage current                       | VS = 0.5 V, VD = Open,<br/>or<br/>VS = 2.2 V, VD = Open,   | Switch ON, see Figure 14  | 25°C | 2.7 V | -0.1 | 0.05 | 0.1  | μA   |
|                                              |                                            |                                                            |                           | Full |       | -0.2 |      | 0.2  |      |
| Id(ON)                                       | D ON leakage current                       | VD = 0.5 V, VS = Open,<br/>or<br/>VD = 2.2 V, VS = Open    | Switch ON, see Figure 14  | 25°C | 2.7 V | -0.1 | 0.05 | 0.1  | μA   |
|                                              |                                            |                                                            |                           | Full |       | -0.2 |      | 0.2  |      |
| **Digital Control Inputs (IN1, IN2, EN)(2)** |                                            |                                                            |                           |      |       |      |      |      |      |
| VIH                                          | Input logic high                           |                                                            |                           | Full |       | 1.7  |      | V+   | V    |
| VIL                                          | Input logic low                            |                                                            |                           | Full |       | 0    |      | 0.7  | V    |
| IIH, IIL                                     | Input leakage current                      | V1 = V_z, or 0                                             |                           | 25°C | 2.7 V | -1   | 0.05 | 1    | μA   |
|                                              |                                            |                                                            |                           | Full |       | -1   |      | 1    |      |
| Qc                                           | Charge injection                           | VGEN = 0, RGEN = 0,<br/>CL = 0.1 nF,                       | See Figure 21             | 25°C | 2.5V  |      |      |      | pC   |
| CS(off)                                      | S OFF capacitance                          | VS = V+ or GND,<br/>Switch OFF,                            | See Figure 15             | 25°C | 2.5 V |      |      | 4.5  | pF   |

### Digital Control Inputs (IN1, IN2, EN)(2)

| PARAMETER | VALUE                                                           |
| --------- | --------------------------------------------------------------- |
| VIH       | Input logic high                                                |
| VIL       | Input logic low                                                 |
| IIH, IIL  | Input leakage current VI = V+ or 0                              |
| QC        | Charge injection VGEN = 0, RGEN = 0, CL = 0.1 nF, See Figure 21 |
| CS(OFF)   | S OFF capacitance VS = V+ or GND, Switch OFF, See Figure 15     |

(1) The algebraic convention, whereby the most negative value is a minimum and the most positive value is a maximum

(2) All unused digital inputs of the device must be held at V+ or GND to ensure proper device operation. Refer to the TI application report, Implications of Slow or Floating CMOS Inputs, literature number SCBA004.

### Electrical Characteristics for 2.5-V Supply (continued)

V₊ = 2.3 V to 2.7 V, TA = –40°C to 85°C (unless otherwise noted)(1)

| PARAMETER                          | TEST CONDITIONS                                | TA   | V+    | MIN  | TYP   | MAX  | UNIT |
| ---------------------------------- | ---------------------------------------------- | ---- | ----- | ---- | ----- | ---- | ---- |
| CD(OFF) D<br/>OFF capacitance      | VD = V+ or GND, See Figure 15                  | 25°C | 2.5 V |      | 18.5  |      | pF   |
| CS(ON)  S<br/>ON capacitance       | VS = V+ or GND, See Figure 15                  | 25°C | 2.5 V |      | 24    |      | pF   |
| CD(ON) D<br/>ON capacitance        | VD = V+ or GND, See Figure 15                  | 25°C | 2.5 V |      | 24    |      | pF   |
| CI  Digital input<br/>capacitance  | VI = V+ or GND, See Figure 15                  | 25°C | 2.5 V |      | 2     |      | pF   |
| BW  Bandwidth                      | RL = 50 Ω, See Figure 17                       | 25°C | 2.5 V |      | 165   |      | MHz  |
| OISO  OFF isolation                | RL = 50 Ω, See Figure 18                       | 25°C | 2.5 V |      | –69   |      | dB   |
| XTALK  Crosstalk                   | RL = 50 Ω, See Figure 19                       | 25°C | 2.5 V |      | –69   |      | dB   |
| XTALK(ADJ)  Crosstalk adjacent     | RL = 50 Ω, See Figure 20                       | 25°C | 2.5 V |      | –74   |      | dB   |
| THD  Total harmonic<br/>distortion | RL = 600 Ω, f = 20 Hz to 20 kHz, see Figure 22 | 25°C | 2.5 V |      | 0.29% |      |      |
| I+   Positive supply<br/>curren    | VI = V+ or GND, Switch ON or OFF               | 25°C | 2.7 V |      | 2.5   | 7    | μA   |
|                                    |                                                | FULL |       |      |       | 10   |      |

### 6.7 Switching Characteristics for 3.3-V supply

over operating free-air temperature range (unless otherwise noted)

| PARAMETER | TEST CONDITIONS                   | TA   | V+           | MIN | TYP | MAX  | UNIT |
| --------- | --------------------------------- | ---- | ------------ | --- | --- | ---- | ---- |
| tON       | Turnon time VD = 2 V, CL = 35 pF  | 25°C | 3.3 V        | 1   | 5   | 9.5  | ns   |
|           | RL = 300 Ω, see Figure 16         | Full | 3 V to 3.6 V | 1   |     | 10.5 |      |
| tOFF      | Turnoff time VD = 2 V, CL = 35 pF | 25°C | 3.3 V        | 0.5 | 1.5 | 3.5  | ns   |
|           | RL = 300 Ω, see Figure 16         | Full | 3 V to 3.6 V | 0.5 |     | 4.5  |      |

### 6.8 Switching Characteristics for 2.5-V supply

over operating free-air temperature range (unless otherwise noted)

| PARAMETER          | TEST CONDITIONS           | TA   | V+             | MIN  | TYP  | MAX  | UNIT |
| ------------------ | ------------------------- | ---- | -------------- | ---- | ---- | ---- | ---- |
| tON Turnon time    | VCOM = 2 V, CL = 35 pF    | 25°C | 2.5 V          | 1.5  | 5    | 8    | ns   |
|                    | RL = 300 Ω, see Figure 16 | Full | 2.3 V to 2.7 V | 1    |      | 10   |      |
| tOFF  Turnoff time | VCOM = 2 V, CL = 35 pF    | 25°C | 2.5 V          | 0.3  | 2    | 4.5  | ns   |
|                    | RL = 300 Ω, see Figure 16 | Full | 2.3 V to 2.7 V | 0.3  |      | 6    |      |

### 6.9 Typical Characteristics

| Ω) | (ON | r   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18   |
| -- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| 0  | 0.0 | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 | 5.5 | 6.0 | 6.5 | 7.0 | 7.5 | 8.0 | 8.5 | 9.0 | 9.5 | 10.0 |

| Leakage Current (nA) |   |     | –40 | 25  | 85  |     |     |     |
| -------------------- | - | --- | --- | --- | --- | --- | --- | --- |
| 0                    |   | 0.0 | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 |

### Typical Characteristics (continued)

| 2.0                                         | 1.8 | Logic-Level Threshold (nA) | 1.6 | 1.4 | VIH | 1.2 | VIL | 1.0 | 0.8 | 0.6 | 0.4 | 0.2 | 0.0 |
| ------------------------------------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.0 2.2 2.4 2.6 2.8 3.0 3.2 3.4 3.6 3.8 4.0 |     |                            |     |     |     |     |     |     |     |     |     |     |     |

#### Figure 7. Logic-Level Threshold vs V+

#### Figure 8. Bandwidth (Gain vs Frequency) (V+ = 3.3 V)

|                        | 0.35    |                |   |   |   |   |   |   |
| ---------------------- | ------- | -------------- | - | - | - | - | - | - |
|                        | 0.30    |                |   |   |   |   |   |   |
|                        | 0.25    |                |   |   |   |   |   |   |
|                        | THD (%) |                |   |   |   |   |   |   |
|                        | 0.20    |                |   |   |   |   |   |   |
|                        | 0.15    |                |   |   |   |   |   |   |
|                        | 0.10    |                |   |   |   |   |   |   |
| 10 100 1000 10 K 100 K |         |                |   |   |   |   |   |   |
|                        |         | Frequency (Hz) |   |   |   |   |   |   |

#### Figure 9. OFF Isolation and Crosstalk vs Frequency (V+ = 3.3 V)

#### Figure 10. Total Harmonic Distortion vs Frequency

#### Figure 11. Power-Supply Current vs Temperature (V+ = 3.6 V)

## 7 Parameter Measurement Information

Channel ON

ron = VD – VS2-S4 or Vs1 Ω

ID

VI = VIH or VIL

OFF-State Leakage Current

Channel OFF

V = VIH or VIL

VS1 or VS2-S4 = 0 to V+

and

VD = V+ to 0

ON-State Leakage Current

Channel ON

V = VIH or VIL

### Parameter Measurement Information (continued)

VBIAS = V+ to GND

V = VIH or VIL

Capacitance is measured at S1, S2-S4, D, and IN inputs during ON and OFF conditions.

#### Figure 15. Capacitance (CI, CD(OFF), CD(ON), CS(OFF), CS(ON))

| (A)   | (B)   | (C)   |
| ----- | ----- | ----- |
| 300 Ω | 35 pF | 300 Ω |
|       | 35 pF |       |

All input pulses are supplied by generators having the following characteristics:

- PRR ≤ 10 MHz
- ZO = 50 Ω
- tr &#x3C; 5 ns
- tf &#x3C; 5 ns

CL includes probe and jig capacitance.

See Electrical Characteristics for VD.

#### Figure 16. Turnon (tON) and Turnoff Time (tOFF)

50 Ω Channel ON: S1 to D

V = VI or GND

Network Analyzer Setup

Source Power = 0 dBm

(632-mV P-P at 50-Ω load)

DC Bias = 350 mV

#### Figure 17. Bandwidth (BW)

### Parameter Measurement Information (continued)

Channel OFF: S to D

| 50 Ω | V = V or GND | I + |
| ---- | ------------ | --- |

Network Analyzer Setup

| Source Power = 0 dBm | (632-mV P-P at 50-Ω load) | DC Bias = 350 mV |
| -------------------- | ------------------------- | ---------------- |

#### Figure 18. OFF Isolation (OISO)

Channel ON: S1 to D

Channel OFF: S -S to D

| 50 Ω | V = V or GND | I + |
| ---- | ------------ | --- |

Network Analyzer Setup

| Source Power = 0 dBm | (632-mV P-P at 50-Ω load) | DC Bias = 350 mV |
| -------------------- | ------------------------- | ---------------- |

#### Figure 19. Crosstalk (XTALK)

Channel ON: S1 to D

| 50 Ω | V1S | 1S1 | Channel ON: S1 to D |
| ---- | --- | --- | ------------------- |
| V2S  | 2S1 | 2D  | 50 Ω                |

Network Analyzer Setup

| Source Power = 0 dBm | (632-mV P-P at 50-Ω load) | DC Bias = 350 mV |
| -------------------- | ------------------------- | ---------------- |

#### Figure 20. Adjacent Crosstalk (XTALK)

### Parameter Measurement Information (continued)

VIH

VIL

ΔVD

VGEN = 0 to V+

RGEN = 0

CL = 0.1 nF

QC = CL X ΔVD

V = VIH or VIL

A.

All input pulses are supplied by generators having the following characteristics: PRR ≤ 10 MHz, ZO = 50 Ω, tr &#x3C; 5 ns, tf &#x3C; 5 ns.

B.

CL includes probe and jig capacitance.

#### Figure 21. Charge Injection (QC)

10 µF

10 µF

| 600 Ω | 600 Ω | (A) |
| ----- | ----- | --- |
| 600 Ω |       |     |

A.

CL includes probe and jig capacitance.

## Figure 22. Total Harmonic Distortion (THD)

## 8 Detailed Description

### 8.1 Overview

The TS3A5017 is a dual Single-Pole-4-Throw (SP4T) solid-state analog switch. The TS3A5017, like all analog switches, is bidirectional. Each D pin connects to its four respective S pins, with the switch connection dependent on the status of EN, IN2, and IN1. See Table 1 for the switch configuration truth table.

### 8.2 Functional Block Diagram

EN

IN1

IN2

D

S1

S2

S3

S4

### 8.3 Feature Description

Isolation in powered-down mode allows signals to be present at the inputs while the switch is powered off without causing damage to the device. The low ON-state resistance and low charge injection give the TS3A5017 better performance at higher speeds.

### 8.4 Device Functional Modes

| EN | IN2 | IN1 | D TO S, S TO D |
| -- | --- | --- | -------------- |
| L  | L   | L   | D = S1         |
| L  | L   | H   | D = S2         |
| L  | H   | L   | D = S3         |
| L  | H   | H   | D = S4         |
| H  | X   | X   | OFF            |

## 9 Application and Implementation
NOTE

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

### 9.1 Application Information
The TS3A5018 can be used in a variety of customer systems. The TS3A5018 can be used anywhere multiple analog or digital signals must be selected to pass across a single line.

### 9.2 Typical Application

#### Figure 24. System Schematic for TS3A5017

3.3 V

EN V+ S1

IN1 S2

To/From

C or System

IN2 S3 System

D S4

GND

#### 9.2.1 Design Requirements</h9>
In this particular application, V+ was 3.3 V, although V+ is allowed to be any voltage specified in Recommended Operating Conditions. A decoupling capacitor is recommended on the V+ pin. See Power Supply Recommendations for more details.

#### 9.2.2 Detailed Design Procedure</h9>
In this application, EN, IN1, and IN2 are, by default, pulled low to GND. Choose these resistor sizes based on the current driving strength of the GPIO, the desired power consumption, and the switching frequency (if applicable). If the GPIO is open-drain, use pullup resistors instead.

### Typical Application (continued)

#### 9.2.3 Application Curve

##### Figure 25. tON and tOFF vs Temperature (V+ = 3.3 V)

|   |   | 5.0  | 4.5 | 4.0      | ~~t~~ON | 3.5 |
| - | - | ---- | --- | -------- | ------- | --- |
|   |   | (ns  | OFF | 2.5      | t       | 2.0 |
|   |   | / ON | 1.5 | ~~t~~OFF | t       | 1.0 |
|   |   | 0.5  | 0.0 |          |         |     |
|   |   | –40  | 25  | 85       | TA (°C) |     |

## 10 Power Supply Recommendations

The power supply can be any voltage between the minimum and maximum supply voltage rating located in the Recommended Operating Conditions.

Each VCC terminal should have a good bypass capacitor to prevent power disturbance. For devices with a single supply, a 0.1-μF bypass capacitor is recommended. If there are multiple pins labeled VCC, then a 0.01-μF or 0.022-μF capacitor is recommended for each VCC because the VCC pins will be tied together internally. For devices with dual-supply pins operating at different voltages, for example VCC and VDD, a 0.1-μF bypass capacitor is recommended for each supply pin. It is acceptable to parallel multiple bypass capacitors to reject different frequencies of noise. 0.1-μF and 1-μF capacitors are commonly used in parallel. The bypass capacitor should be installed as close to the power terminal as possible for best results.

## 11 Layout

### 11.1 Layout Guidelines

Reflections and matching are closely related to loop antenna theory, but different enough to warrant their own discussion. When a PCB trace turns a corner at a 90° angle, a reflection can occur. This is primarily due to the change of width of the trace. At the apex of the turn, the trace width is increased to 1.414 times its width. This upsets the transmission line characteristics, especially the distributed capacitance and self–inductance of the trace — resulting in the reflection. It is a given that not all PCB traces can be straight, and so they will have to turn corners. Below figure shows progressively better techniques of rounding corners. Only the last example maintains constant trace width and minimizes reflections.

Unused switch I/Os, such as NO, NC, and COM, can be left floating or tied to GND. However, the IN1, IN2, and EN pins must be driven high or low. Due to partial transistor turnon when control inputs are at threshold levels, floating control inputs can cause increased ICC or unknown switch selection states. See Implications of Slow or Floating CMOS Inputs, SCBA004 for more details.

## 11.2 Layout Example

### Figure 26. Trace Example

|   | WORST | BETTER | BEST    |   |
| - | ----- | ------ | ------- | - |
|   |       | 2W     | 1W min. | W |
|   |       |        |         |   |

## 12 器件和文档支持

### 12.1 器件支持

#### 12.1.1 器件命名规则

##### 表 **2.** 参数 说明

| 符号        | 说明                                                                                                                                |
| --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| VCOM      | COM 处的电压                                                                                                                          |
| VNC       | NC 处的电压                                                                                                                           |
| VNO       | NO 处的电压                                                                                                                           |
| ron       | 通道打开时 COM 和 NC 或 NO 端口之间的电阻                                                                                                       |
| Δron      | 特定器件中通道间 ron 的差值                                                                                                                  |
| ron(flat) | 额定条件范围下，同一通道内 ron 最大值与最小值之间的差值                                                                                                    |
| INC(OFF)  | 相应通道（NC 到 COM）处于关断状态时，在 NC 端口测得的泄漏电流                                                                                              |
| INC(ON)   | 相应通道（NC 到 COM）处于导通状态且输出 (COM) 处于开路状态时，在 NC 端口测得的泄漏电流                                                                              |
| INO(OFF)  | 相应通道（NO 到 COM）处于关断状态时，在 NO 端口测得的泄漏电流                                                                                              |
| INO(ON)   | 相应通道（NO 到 COM）处于导通状态且输出 (COM) 处于开路状态时，在 NO 端口测得的泄漏电流                                                                              |
| ICOM(OFF) | 相应通道（COM 到 NC 或 NO）处于关断状态时，在 COM 端口测得的泄漏电流                                                                                        |
| ICOM(ON)  | 相应通道（COM 到 NC 或 NO）处于导通状态且输出 (NC 或 NO) 处于开路状态时，在 COM 端口测得的泄漏电流                                                                    |
| VIH       | 控制输入 (IN, EN) 逻辑高电平的最小输入电压                                                                                                        |
| VIL       | 控制输入 (IN, EN) 逻辑低电平的最大输入电压                                                                                                        |
| VI        | 控制输入 (IN, EN) 处的电压                                                                                                                |
| IIH、IIL   | 控制输入 (IN, EN) 处测量的泄漏电流                                                                                                            |
| tON       | 开关开通时间。此参数是在特定条件范围下，开关开通时，通过数字控制 (IN) 信号和模拟输出 NC 或 NO）信号之间的传播延迟测量得出。                                                              |
| tOFF      | 开关关断时间。此参数是在特定条件范围下，开关开通时，通过数字控制 (OFF) 信号和模拟输出（NC 或 NO）信号之间的传播延迟测量得出。                                                             |
| QC        | 电荷注入是测量从控制 (IN) 输入到模拟（NC 或 NO）输入产生的不需要的信号耦合的方法。电荷注入以库仑为单位，可通过测量开关控制输入产生的总感应电荷得出该值。电荷注入，QC = CL × ΔVCOM，CL 是负载电容，ΔVCOM 是模拟输出电压的变化。 |
| CNC(OFF)  | 相应通道（NC 到 COM）关闭时 NC 端口的电容                                                                                                        |
| CNC(ON)   | 相应通道（NC 到 COM）开启时 NC 端口的电容                                                                                                        |
| CNO(OFF)  | 相应通道（NO 到 COM）关闭时 NC 端口的电容                                                                                                        |
| CNO(ON)   | 相应通道（NO 到 COM）开启时 NC 端口的电容                                                                                                        |
| CCOM(OFF) | 相应通道（COM 到 NC）关闭时 COM 端口的电容                                                                                                       |
| CCOM(ON)  | 相应通道（COM 到 NC）开启时 COM 端口的电容                                                                                                       |
| CI        | 控制输入 (IN, EN) 电容                                                                                                                  |
| OISO      | 开关关断隔离用于衡量关断状态开关阻抗的大小。关断隔离以 dB 为单位，当相应通道（NC 到 COM）处于关断状态时，在额定频率下测量得出。                                                             |
| XTALK     | 串扰是测量从开启状态的通道到关断状态的通道（NC1 到 NO1）产生的不必要信号耦合的方法。相邻串扰是测量从一条开启状态的通道到相邻开启状态的通道（NC1 到 NC2）产生的不必要信号耦合的方法。相邻串扰在额定频率下测量得出且以 dB 为单位。        |
| BW        | 开关带宽。这是导通通道增益低于直流增益 -3dB 时的频率。                                                                                                    |
| THD       | 总谐波失真用于描述由模拟开关导致的信号失真。其定义为二次、三次和更高次谐波与基波绝对幅度之比的均方根 (RMS) 值。                                                                       |
| I+        | 静态电源电流，以及 V+ 或 GND 的控制 (IN) 引脚                                                                                                    |

### 12.2 文档支持

#### 12.2.1 相关文档

- 《慢速或浮点 CMOS 输入的影响》，SCBA004

### 12.3 商标

All trademarks are the property of their respective owners.

### 12.4 静电放电电警告

这些装置包含有限的内置 ESD 保护。 存储或装卸时，应将导线一起截短或将装置放置于导电泡棉中，以防止 MOS 门极遭受静电损伤。

### 12.5 术语表

SLYZ022 — TI 术语表。 这份术语表列出并解释术语、缩写和定义。

## 13 机械、封装和可订购信息

以下页面包含机械、封装和可订购信息。这些信息是指定器件的最新可用数据。数据如有变更，恕不另行通知，且不会对此文档进行修订。如需获取此数据表的浏览器版本，请查阅左侧的导航栏。

## PACKAGING INFORMATION

| Orderable part number | Status   | Material type | Package     | Pins | Package qty | Carrier   | RoHS | Lead finish/ Ball material | MSL rating/ Peak reflow | Op temp (°C) | Part marking |
| :-------------------- | :------- | :------------ | :---------- | :--- | :---------- | :-------- | :--- | :------------------------- | :---------------------- | :----------- | :----------- |
| TS3A5017D             | Obsdete* | Production    | SOIC(D)     | 16   | -           | -         | -    | Call Ti                    | Call Ti                 | -40 to 85    | TS3A5017     |
| TS3A5017DBQR          | Active   | Production    | SSOP (DBQ)  | 16   | 2500        | LARGE T&R | Yes  | NIPDAU                     | Level-2-260C-1 YEAR     | -40 to 85    | YA017        |
| TS3A5017DBQR.B        | Active   | Production    | SSOP (DBQ)  | 16   | 2500        | LARGE T&R | Yes  | NIPDAU                     | Level-2-260C-1 YEAR     | -40 to 85    | YA017        |
| TS3A5017DBQRG4.B      | Active   | Production    | SSOP (DBQ)  | 16   | 2500        | LARGE T&R | Yes  | NIPDAU                     | Level-2-260C-1 YEAR     | -40 to 85    | YA017        |
| TS3A5017DGVR          | Active   | Production    | TVSOP (DVV) | 16   | 2000        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | YA017        |
| TS3A5017DGVR.B        | Active   | Production    | TVSOP (DVV) | 16   | 2000        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | YA017        |
| TS3A5017DR            | Active   | Production    | SOIC(D)     | 16   | 2500        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | TS3A5017     |
| TS3A5017DR.B          | Active   | Production    | SOIC(D)     | 16   | 2500        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | TS3A5017     |
| TS3A5017PW            | Obsdete* | Production    | TSSOP (PW)  | 16   | -           | -         | -    | Call Ti                    | Call Ti                 | -40 to 85    | YA017        |
| TS3A5017PWR           | Active   | Production    | TSSOP (PW)  | 16   | 2000        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | YA017        |
| TS3A5017PWR.B         | Active   | Production    | TSSOP (PW)  | 16   | 2000        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | YA017        |
| TS3A5017RGYR          | Active   | Production    | VQFN (RGY)  | 16   | 3000        | LARGE T&R | Yes  | NIPDAU                     | Level-2-260C-1 YEAR     | -40 to 85    | YA017        |
| TS3A5017RGYR.B        | Active   | Production    | VQFN (RGY)  | 16   | 3000        | LARGE T&R | Yes  | NIPDAU                     | Level-2-260C-1 YEAR     | -40 to 85    | YA017        |
| TS3A5017RSVR          | Active   | Production    | UQFN (RSV)  | 16   | 3000        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | ZVL          |
| TS3A5017RSVRG4.B      | Active   | Production    | UQFN (RSV)  | 16   | 3000        | LARGE T&R | Yes  | NIPDAU                     | Level-1-260C-UNLIM      | -40 to 85    | ZVL          |

Footnotes

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer: The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

OTHER QUALIFIED VERSIONS OF TS3A5017 :

- Automotive : TS3A5017-Q1

NOTE: Qualified Version Definitions:

- Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects

### TAPE AND REEL INFORMATION

| REEL DIMENSIONS                                                                                                                                                                                                                                                          | TAPE DIMENSIONS |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| * A0 Dimension designed to accommodate the component width
* B0 Dimension designed to accommodate the component length
* K0 Dimension designed to accommodate the component thickness
* W Overall width of the carrier tape
* P1 Pitch between successive cavity centers | - K0
- P1       |

Reel Dimensions

Reel Width (W1)

QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

Sprocket Holes

Q1 Q2 Q1 Q2

Q3 Q4 Q3 Q4 User Direction of Feed

Pocket Quadrants

| Device       | Package Type | Package Drawing | Pins | SPQ  | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| ------------ | ------------ | --------------- | ---- | ---- | ------------------ | ------------------ | ------- | ------- | ------- | ------- | ------ | ------------- |
| TS3A5017DBQR | SSOP         | DBQ             | 16   | 2500 | 330.0              | 12.5               | 6.4     | 5.2     | 2.1     | 8.0     | 12.0   | Q1            |
| TS3A5017DGVR | TVSOP        | DGV             | 16   | 2000 | 330.0              | 12.4               | 6.8     | 4.0     | 1.6     | 8.0     | 12.0   | Q1            |
| TS3A5017DR   | SOIC         | D               | 16   | 2500 | 330.0              | 16.4               | 6.5     | 10.3    | 2.1     | 8.0     | 16.0   | Q1            |
| TS3A5017PWR  | TSSOP        | PW              | 16   | 2000 | 330.0              | 12.4               | 6.9     | 5.6     | 1.6     | 8.0     | 12.0   | Q1            |
| TS3A5017RGYR | VQFN         | RGY             | 16   | 3000 | 330.0              | 12.4               | 3.8     | 4.3     | 1.5     | 8.0     | 12.0   | Q1            |
| TS3A5017RSVR | UQFN         | RSV             | 16   | 3000 | 180.0              | 12.4               | 2.1     | 2.9     | 0.75    | 4.0     | 12.0   | Q1            |

*All dimensions are nominal

### TAPE AND REEL BOX DIMENSIONS

| Device       | Package Type | Package Drawing | Pins | SPQ  | Length (mm) | Width (mm) | Height (mm) |
| ------------ | ------------ | --------------- | ---- | ---- | ----------- | ---------- | ----------- |
| TS3A5017DBQR | SSOP         | DBQ             | 16   | 2500 | 353.0       | 353.0      | 32.0        |
| TS3A5017DGVR | TVSOP        | DGV             | 16   | 2000 | 356.0       | 356.0      | 35.0        |
| TS3A5017DR   | SOIC         | D               | 16   | 2500 | 353.0       | 353.0      | 32.0        |
| TS3A5017PWR  | TSSOP        | PW              | 16   | 2000 | 356.0       | 356.0      | 35.0        |
| TS3A5017RGYR | VQFN         | RGY             | 16   | 3000 | 356.0       | 356.0      | 35.0        |
| TS3A5017RSVR | UQFN         | RSV             | 16   | 3000 | 200.0       | 183.0      | 25.0        |

### DGV (R-PDSO-G**) PLASTIC SMALL-OUTLINE

24 PINS SHOWN

|   | 0,40       | 0,23 | 0,07     | M    |      | 0,13 |      | 24 | 13 |
| - | ---------- | ---- | -------- | ---- | ---- | ---- | ---- | -- | -- |
|   | 0,16 NOM   |      | 4,50     | 6,60 |      | 4,30 | 6,20 |    |    |
|   | Gage Plane | 0,25 | 0°– 8°   |      | 1    | 12   | 0,75 |    |    |
|   | 0,50       |      | 1,20 MAX | 0,15 | 0,08 | 0,05 |      |    |    |

| DIM   | PINS \*\* | 14   | 16   | 20   | 24   | 38   | 48   | 56    |
| ----- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ----- |
| A MAX |           | 3,70 | 3,70 | 5,10 | 5,10 | 7,90 | 9,80 | 11,40 |
| A MIN |           | 3,50 | 3,50 | 4,90 | 4,90 | 7,70 | 9,60 | 11,20 |

NOTES:

- A. All linear dimensions are in millimeters.
- B. This drawing is subject to change without notice.
- C. Body dimensions do not include mold flash or protrusion, not to exceed 0,15 per side.
- D. Falls within JEDEC: 24/48 Pins – MO-153
- 14/16/20/56 Pins – MO-194

### PLASTIC SMALL OUTLINE

| 0.394 | (10.00) |
| ----- | ------- |
| 0.386 | (9.80)  |
| 0.244 | (6.20)  |
| 0.228 | (5.807) |
| 0.157 | (4.00)  |
| 0.150 | (3.80)  |

Pin .020 (0.51)

Index Area 0.050 0.012 (0.31) 0.010 (0.25)

0.004 (0.10)

0.069 (1.75) Max

C10 (0, 005 (0.13)

Gauge Plane

0.010 (0.25)

Seating Plane

0'-8'

.050 (1.27)

0.016 (0.40)

4040047-6 /M 06/11

NOTES:

All linear dimensions are in inches (millimeters):

This drawing is subject to change without notice:

Body length does not include mold flash, protrusions; gate burrs. Mold flash, protrusions; gate burrs shall not exceed 0.006 (0.15) each side. Interlead flash shall not exceed 0.017 (0.43) each side:

Body width does not include interlead flash.

Reference JEDEC MS-012 variation AC.

### PACKAGE OUTLINE

PW0016A
TSSOP - 1.2 mm max height
~~SCALE 2.500~~
SMALL OUTLINE PACKAGE

SEATING PLANE

| 6.6 TYP |    |     |   |            |              |          |            | C     | 6.2  | PIN 1 INDEX AREA | 14X 0.65 | 0.1 C |
| ------- | -- | --- | - | ---------- | ------------ | -------- | ---------- | ----- | ---- | ---------------- | -------- | ----- |
| 1       | 16 |     |   |            |              |          |            |       |      |                  |          |       |
| 5.1     |    |     |   |            | 4.55         | 4.9      | NOTE 3     |       |      |                  |          |       |
| 8       |    | 4.5 |   |            | 9            | 16X 0.30 | 1.2 MAX    |       |      |                  |          |       |
|         | B  | 4.3 |   |            | 0.19         | NOTE 4   | 0.1        | C A B |      |                  |          |       |
|         |    |     |   | (0.15) TYP | SEE DETAIL A | 0.25     | GAGE PLANE | 0.15  | 0.05 |                  |          |       |
| 0.75    |    |     |   |            | 0 -8         | 0.50     | DETAIL A   | 20    | A    |                  |          |       |

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-153.

### EXAMPLE BOARD LAYOUT

PW0016A

TSSOP - 1.2 mm max height

SMALL OUTLINE PACKAGE

|            | 16X (1.5) | SYMM |            |             |
| ---------- | --------- | ---- | ---------- | ----------- |
|            | 1         |      |            | (R0.05) TYP |
| 16X (0.45) | 16        |      |            |             |
|            |           | SYMM | 14X (0.65) |             |
|            | 8         |      | 9          | (5.8)       |

LAND PATTERN EXAMPLE

EXPOSED METAL SHOWN

SCALE: 10X

| SOLDER MASK OPENING                 | METAL                       | METAL UNDER SOLDER MASK | SOLDER MASK OPENING |
| ----------------------------------- | --------------------------- | ----------------------- | ------------------- |
| EXPOSED METAL                       | 0.05 MAX                    | 0.05 MIN                | ALL AROUND          |
| NON-SOLDER MASK DEFINED (PREFERRED) | SOLDER MASK DETAILS DEFINED | 15.000                  |                     |

4220204/A 02/2017

NOTES:

(continued)

1. Publication IPC-7351 may have alternate designs.
2. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

### EXAMPLE STENCIL DESIGN

PW0016A

TSSOP - 1.2 mm max height

SMALL OUTLINE PACKAGE

| 16X (1.5) |             | SYMM       |
| --------- | ----------- | ---------- |
| 1         | (R0.05) TYP | 16X (0.45) |
| SYMM      |             | 14X (0.65) |
| 8         | 9           | (5.8)      |

SOLDER PASTE EXAMPLE

BASED ON 0.125 mm THICK STENCIL

SCALE: 10X

4220204/A  02/2017

NOTES: (continued)

1. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
2. Board assembly site may have different recommendations for stencil design.

### MECHANICAL DATA

RGY R-PVQFN-N16

PLASTIC QUAD FLATPACK NO-LEAD

| Pin Index Area | Top and Bottom |
| -------------- | -------------- |
| 0,20 Nominal   | Lead Frame     |
| 0,80           | Seating Plane  |
| 2,50           | Seating Height |
| 16X 50         |                |

THERMAL PAD SIZE AND SHAPE

Shown on separate sheet

Bottom View

4203539-3/1 06 /2011

NOTES:

- All linear dimensions are in millimeters.
- Dimensioning and tolerancing per ASME Y14.5M-1994.
- This drawing is subject to change without notice.
- QFN (Quad Flatpack No-Lead) package configuration.
- The package thermal pad must be soldered to the board for thermal and mechanical performance.
- See the additional figure in the Product Data Sheet for details regarding the exposed thermal pad features and dimensions.
- Pin identifiers are located both top and bottom of the package and within the zone indicated.
- The Pin identifiers are either molded, marked, or metal feature.
- Package complies to JEDEC MO-241 variation BA.

TEXAS INSTRUMENTS

### THERMAL PAD MECHANICAL DATA

RGY (R-PVQFN-N16)

PLASTIC QUAD FLATPACK NO-LEAD

THERMAL INFORMATION

This package incorporates an exposed thermal pad that is designed to be attached directly to an external heatsink. The thermal pad must be soldered directly to the printed circuit board (PCB). After soldering, the PCB can be used as a heatsink. In addition, through the use of thermal paste, the thermal pad can be attached directly to the appropriate copper plane shown in the electrical schematic for the device; alternatively, it can be attached to a special heatsink structure designed into the PCB. This design optimizes the heat transfer from the integrated circuit (IC).

For information on the Quad Flatpack No-Lead (QFN) package and its advantages, refer to Application Report; QFN/SON PCB Attachment; Texas Instruments Literature No: SLUA271. This document is available at www.ti.com.

Exposed Thermal Pad Dimensions

| Exposed Thermal Pad |             |
| ------------------- | ----------- |
| 2.05                | 10.10       |
| 16                  |             |
| 15                  |             |
| 12.55 +0.10 -       | Bottom View |

NOTE: All linear dimensions are in millimeters

TEXAS INSTRUMENTS

### LAND PATTERN DATA

RGY (R-PVQFN-N16)

PLASTIC QUAD FLATPACK NO-LEAD

Example Stencil Design

Example Board Layout

0.125mm Stencil Thickness (Note E)

| 280          | 0.82          |
| ------------ | ------------- |
| 205          | 2 PL          |
| 0.85 % 16 PL | Q80 \* 16 PL  |
| -104050      | 0.28 X 10 Fe  |
| 10.0,50      | 0.23 \* 10 FL |

677 solder coverage by printed area center thermal pad

Non Solder Mask Defined Pad

Example Via Layout Design

may vary depending on constraints (Note D, F)

Solder Mask Opening

(Note F)

| 0.08-  | 0.85       |
| ------ | ---------- |
| RO,14- | 0.28       |
| 0.07   | All Around |

Pad Geometry

(Note C)

4208122-J/P 03/14

NOTES:

- All linear dimensions are in millimeters
- This drawing is subject to change without notice
- Publication IPC-7351 is recommended for alternate designs:
- This package is designed to be soldered to thermal pad on the board. Refer to Application Note; Quad Flat-Pack QFN/SON PCB Attachment, Texas Instruments Literature No. SLUA271, and also the Product Data Sheets for specific thermal information, via requirements, and recommended board layout:
- These documents are available at www.ti.com
- Laser cutting apertures with trapezoidal walls and also rounding corners will offer better paste release. Customers should contact their board assembly site for stencil design recommendations: Refer to IPC 7525 for stencil design considerations.
- Customers should contact their board fabrication site for minimum solder mask web tolerances between signal pads.

TEXAS INSTRUMENTS

### GENERIC PACKAGE VIEW

RSV 16

UQFN - 0.55 mm max height

1.8 x 2.6, 0.4 mm pitch

ULTRA THIN QUAD FLATPACK - NO LEAD

This image is a representation of the package family, actual package may vary.

Refer to the product data sheet for package details.

TEXAS INSTRUMENTS

### PACKAGE OUTLINE

RSV0016A

UQFN - 0.55 mm max height

ULTRA THIN QUAD FLATPACK - NO LEAD

| B        | 1.85             | A             |
| -------- | ---------------- | ------------- |
|          | 1.75             |               |
|          | PIN 1 INDEX AREA |               |
|          | 2.65             |               |
|          | 2.55             |               |
| 0.55     | C                |               |
| 0.45     |                  | SEATING PLANE |
| 0.05     | 0.05             | C             |
| 0.00     |                  |               |
| 2X 1.2   | SYMM             | (0.13) TYP    |
| 5        | ℄                | 8             |
|          | 15X 0.45         |               |
| 0.35     | 4                | 9             |
| SYMM     | 2X 1.2           | ℄             |
| 12X 0.4  | 1                | 12            |
| 16X 0.25 |                  | 0.15          |
| 0.07     | C                | A             |
| 0.55     | 16               | PIN 13        |
| 0.45     | (45 1 ID         | ° X 0.1)      |

4220314/C 02/2020

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.

### EXAMPLE BOARD LAYOUT

RSV0016A

UQFN - 0.55 mm max height

ULTRA THIN QUAD FLATPACK - NO LEAD

| (0.7)               | ℄                    | 16         | 13    | SEE SOLDER MASK DETAIL |   |   |   |   |
| ------------------- | -------------------- | ---------- | ----- | ---------------------- | - | - | - | - |
| 16X (0.2)           | 1                    | 12         |       |                        |   |   |   |   |
| 12X (0.4)           |                      | SYMM       |       | (2.4)                  |   |   |   |   |
| (R0.05) TYP         | 4                    | 9          |       |                        |   |   |   |   |
| 15X (0.6)           |                      | 5          | 8     |                        |   |   |   |   |
| (1.6)               | LAND PATTERN EXAMPLE |            |       |                        |   |   |   |   |
| EXPOSED METAL SHOWN |                      |            |       |                        |   |   |   |   |
| SCALE: 25X          |                      |            |       |                        |   |   |   |   |
| 0.05 MAX            | ALL 0.05 MIN         |            |       | AROUND                 |   |   |   |   |
|                     |                      | METAL EDGE |       | METAL UNDER            |   |   |   |   |
| EXPOSED METAL       | SOLDER MASK          | EXPOSED    | METAL | SOLDER MASK            |   |   |   |   |
| NON SOLDER MASK     | SOLDER MASK DEFINED  |            |       | (PREFERRED)            |   |   |   |   |

SOLDER MASK DETAILS

NOTES: (continued)

3. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).

### EXAMPLE STENCIL DESIGN

RSV0016A

UQFN - 0.55 mm max height

ULTRA THIN QUAD FLATPACK - NO LEAD

|             |    |    |           |   |       |      |   |       |
| ----------- | -- | -- | --------- | - | ----- | ---- | - | ----- |
| (0.7)       | 16 |    |           |   |       |      |   |       |
| 16X (0.2)   | 1  | 12 | SYMM      | ℄ | (2.4) |      |   |       |
| (R0.05) TYP | 4  | 9  | 15X (0.6) | 5 | 8     | SYMM | ℄ | (1.6) |

SOLDER PASTE EXAMPLE

BASED ON 0.125 MM THICK STENCIL

SCALE: 25X

4220314/C 02/2020

NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

## PACKAGE OUTLINE

DBQ0016A

SSOP - 1.75 mm max height

SCALE 2.800

SHRINK SMALL-OUTLINE PACKAGE

C

SEATING PLANE

| .228-.244  | TYP           | \[5.80-6.19]  | .004 \[0.1]       |
| ---------- | ------------- | ------------- | ----------------- |
| A          | PIN 1 ID AREA | 14X .0250     |                   |
| 1          | 16            | \[0.635]      |                   |
| .189-.197  |               | 2X            | .175              |
| NOTE 3     |               | \[4.45]       |                   |
| 8          |               | 9             |                   |
| B          | .150-.157     | 16X .008-.012 | .069 MAX          |
|            | \[3.81-3.98]  | \[0.21-0.30]  | \[1.75]           |
| NOTE 4     |               | .007 \[0.17]  | C A B             |
|            | .005-.010     | TYP           | \[0.13-0.25]      |
|            | .010          | \[0.25]       |                   |
| GAGE PLANE |               |               |                   |
| 0 - 8      |               | .004-.010     | \[0.11-0.25]      |
|            | .016-.035     | \[0.41-0.88]  | (.041)            |
|            | DETAIL A      |               |                   |
|            | \[1.04]       | TYPICAL       | 4214846/A 03/2014 |

NOTES:

1. Linear dimensions are in inches [millimeters]. Dimensions in parenthesis are for reference only. Controlling dimensions are in inches. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed .006 inch, per side.
4. This dimension does not include interlead flash.
5. Reference JEDEC registration MO-137, variation AB.

### EXAMPLE BOARD LAYOUT

DBQ0016A

SSOP - 1.75 mm max height

SHRINK SMALL-OUTLINE PACKAGE

| 16X (.063)  | \[1.6]              | SYMM                    | SEE DETAILS         |
| ----------- | ------------------- | ----------------------- | ------------------- |
| 1           | 16                  | 16X (.016)              | \[0.41]             |
| 14X (.0250) | \[0.635]            | 8                       | 9                   |
| (.213)      | \[5.4]              | LAND PATTERN EXAMPLE    |                     |
| SCALE: 8X   |                     |                         |                     |
| METAL       | SOLDER MASK OPENING | SOLDER MASK OPENING     | METAL               |
| .002 MAX    | \[0.05]             | .002 MIN                | \[0.05]             |
| ALL AROUND  | ALL AROUND          | NON SOLDER MASK DEFINED | SOLDER MASK DEFINED |

SOLDER MASK DETAILS

4214846/A 03/2014

NOTES:

1. Publication IPC-7351 may have alternate designs.
2. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

### EXAMPLE STENCIL DESIGN

DBQ0016A

SSOP - 1.75 mm max height

SHRINK SMALL-OUTLINE PACKAGE

|             | 16X (.063) | \[1.6] | SYMM   | 1 | 16 |
| ----------- | ---------- | ------ | ------ | - | -- |
| 16X (.016)  | \[0.41]    | SYMM   |        |   |    |
| 14X (.0250) | \[0.635]   | 8      | 9      |   |    |
|             |            | (.213) | \[5.4] |   |    |

SOLDER PASTE EXAMPLE

BASED ON .005 INCH [0.127 MM] THICK STENCIL

SCALE: 8X

4214846/A 03/2014

NOTES: (continued)

1. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
2. Board assembly site may have different recommendations for stencil design.

