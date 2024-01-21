.. figure:: /images/CSAD10_0p2_PCB_1.jpg
   :align: center

CSAD10
======

Clock shape and distribution with 10 outputs.

The CSAD10 board takes a sine or square wave reference clock input and provides ten buffered CMOS square wave outputs. It was designed with the CI platform in mind, where it might be used to distribute the reference clock within a subsystem such as :doc:`/developer/hardware/ci/ciran2/index`, or perhaps replace the TADD-1 board which is currently used in :doc:`/developer/hardware/ci/ciclkd`.

Version 0.3
-----------

CSAD10 is based around an LTC6957IMS-3 low phase noise buffer/driver, which is able to translate a sine wave signal to logic levels, plus an LMK00101 ultra-low jitter fanout buffer. The input and outputs are 50R impedance.

The LTC6957IMS-3 features input filtering which can be configured for bandwidths of 50MHz, 160MHz, 500MHz and 1,200MHz (full bandwidth).

Design
^^^^^^

.. figure:: /images/CSAD10_0p3_Schematic.svg
   :align: center

   CSAD10 v0.3 schematic diagram.

.. figure:: /images/CSAD10_0p3_Board_Plot.png
   :align: center

   CSAD10 v0.3 PCB layout.

Track widths have been calculated for fabrication using the `JLCPCB 4L impedance controlled service`_ (JLC04161H-7628 stackup).

.. warning::
   Other appropriate substrates could be used, however, RF signal path traces would need to be recalculated and modified accordingly.

The PCB design was entered using KiCAD. The project files have been published to the `lc-clock repository`_.

Bill of Materials
^^^^^^^^^^^^^^^^^

.. list-table:: CSAD10 BOM
    :header-rows: 1

    * - Component
      - Description
      - Manufacturer
      - Man. Part
      - Distributor
      - Dist. Part
    * - C1, C2, C30, C31, C32
      - 1uF MLCC capacitor
      - Yageo
      - CC0603KRX7R7BB105 
      - 
      - 
    * - C3
      - 4.7uF MLCC capacitor
      - muRata
      - GRM188R61E475KE11D
      - 
      - 
    * - C6, C7, C8, C9, C10, C16, C17, C18, C19, C20, C24, C25, C26, C27, C28, C29
      - 0.1uF MLCC capacitor
      - Yageo
      - CC0603KRX7R9BB104
      - 
      - 
    * - C11, C12, C13, C14, C15
      - 100pF MLCC capacitor
      - Yageo
      - CC0402JRNPO9BN101
      - 
      - 
    * - C21, C22, C23
      - 0.1uF MLCC capacitor
      - 
      - 
      - 
      - 
    * - D1
      - Green LED
      - Wurth Elektronik
      - 150080GS75000 
      - 
      - 
    * - D2
      - RF Schottky barrier diode
      - Broadcom
      - HSMS-281C-BLKG
      - 
      - 
    * - FB1
      - Ferrite bead
      - muRata
      - 150080GS75000 
      - 
      - 
    * - J1
      - 2-pin KK 100 header
      - Molex
      - 22-23-2021
      - 
      - 
    * - J2
      - USB-C connector
      - GCT
      - USB4110-GF-A
      - 
      - 
    * - J5, J6, J7, J8, J9, J10, J11, J12, J13, J14, J15
      - U.FL connector
      - Hirose
      - U.FL-R-SMT(01)
      - 
      - 
    * - R1
      - 680R resistor
      - Yageo
      - RC0603JR-07680RL
      - 
      - 
    * - R4, R5
      - 5K1 resistor
      - Bourns
      - CR0603-FX-5101ELF
      - 
      - 
    * - R10, R12
      - 100R resistor
      - TE Connectivity
      - CRGCQ0603F100R
      - 
      - 
    * - R11
      - 604R resistor
      - Yageo
      - RC0603FR-07604RL
      - 
      - 
    * - R15
      - 50R resistor
      - Yageo
      - RC0402JR-0750RL
      - 
      - 
    * - T1
      - 1:16 transformer
      - Coilcraft
      - RC0603FR-07604RL
      - 
      - 
    * - U1
      - 3.3v LDO
      - Diodes Inc.
      - AP7361C-33E
      - 
      - 
    * - U2
      - Clock buffer
      - Analog Devices
      - LTC6957IMS-3
      - 
      - 
    * - U3
      - Clock fanout
      - Texas Instruments
      - LMK00101SQ/NOPB
      - 
      - 

.. _JLCPCB 4L impedance controlled service: https://jlcpcb.com/impedance
.. _lc-clock repository: https://github.com/myriadrf/lc-clock