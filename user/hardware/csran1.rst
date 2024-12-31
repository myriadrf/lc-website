.. figure:: /images/CSRAN1_Front_Panel_1280w.jpg

CSRAN1
======

CSRAN1 is an LTE-FDD base station designed for use at a cell site, which is 2x2 MIMO and with a modulated RF power output of around 33dBm.

The design integrates an SDR and baseband processing, together with an RF front-end (RFE) comprised of the LibreCellular :doc:`/developer/hardware/rf/rfe` and two :doc:`/developer/hardware/rf/b3mpa` (PAs), plus cavity duplexers. It requires a 24VDC power supply and external frequency reference, e.g. GPSDO.

The reference design provided here is for LTE Band 3 (1800 MHz) operation. However, it could easily be modified for other bands by selecting different RF PA modules and duplexers, since the SDR and LibreCellular RFE together support operation from 500MHz-3.8GHz. Similarly, different power output PA modules might be selected, or perhaps omitted entirely for reduced coverage range. 

Views
-----

.. figure:: /images/CSRAN1_Rear_Panel_1280w.jpg
   
   CIRAN1 Rear Panel.

*Photographs to be added once build of the first system has been completed.*

Theory of operation
-------------------

.. figure:: /images/CSRAN1_Block_Diagram.svg

An Intel NUC running Linux and the cellular network stack is cabled via USB 3.0
to a LimeSDR-USB, with Tx and Rx for channels A + B cabled to the LibreCellular RFE transmit in ports. The RFE functions as a PA driver in the transmit path and is also used to inhibit transmit until the eNodeB has fully started and SDR calibration has completed. The RFE is controlled by the Intel NUC via USB 2.0.

RFE transmit A and B out are cabled to the input of a pair of Band 3 PAs, which provide final RF power amplification. The PA outputs are then cabled to the downlink ports of a pair of Band 3 cavity duplexers. The RFE switched DC outputs provide voltage regulation (5V rail) and power sequencing for the PAs.

The duplexer uplink outputs are cabled to the RFE receive in ports, with the RFE functioning as a dual LNA in the receive path, with optional RF attenuation which may be engaged to prevent ADC overload. Finally, RFE receive out is cabled to the LimeSDR-USB Rx channels A and B.

Bill of materials
-----------------

.. list-table:: CSRAN1 BOM
   :header-rows: 1

   * - Component
     - Description
     - Manufacturer
     - Man. Part
     - Distributor
     - Dist. Part
   * - Enclosure
     - 2U Rack-mount enclosure
     - nVent SCHROFF
     - 20860127
     - RS Components
     - `245-7831`_
   * - SW1
     - Illuminated Push Button Switch
     - APEM
     - IPR3SAD2L0G
     - RS Components
     - `224-899`_
   * - SW2 
     - Push Button Switch
     - APEM
     - ISR3SAD600
     - RS Components
     - `373-1678`_
   * - J1
     - Male panel mount XLR connector
     - Neutrik
     - NC3MD-LX-M3
     - Mouser
     - `568-NC3MD-LX-M3`_
   * - J2
     - Panel mount Ethernet connector
     - Neutrik
     - NE8FDX-P6-B
     - RS Components
     - `121-6998`_
   * - J3-5
     - SMA Socket to SMA Socket
     - Molex
     - 73251-0361
     - RS Components
     - `800-6986`_
   * - J6
     - 9-way D-sub Connector Plug
     - TE Connectivity
     - 5-747904-5
     - RS Components
     - `756-1108`_
   * - J7
     - XLR Mount Female HDMI Connector
     - Neutrik
     - NAHDMI-W-B
     - RS Components
     - `909-3717`_
   * - J8
     - XLR USB 3.0 Feedthrough Connector
     - Neutrik
     - NAUSB3-B
     - RS Components
     - `121-7003`_
   * - F1 
     - 10A Panel Mount Fuse Holder
     - Wurth Elektronik
     - 696211001102
     - RS Components
     - `893-0606`_
   * - TB1
     - Distribution block with 6 terminals, red
     - Phoenix Contact
     - 3002765
     - RS Components
     - `207-2850`_
   * - TB2
     - Distribution block with 6 terminals, blue
     - Phoenix Contact
     - 3002761
     - RS Components
     - `207-2847`_
   * - M1
     - Intel NUC single-board computer
     - Intel
     - NUC7i7DNBE
     - 
     - 
   * - M2
     - LimeSDR-USB software-defined radio
     - Lime Microsystems
     - LimeSDR-USB
     - 
     - 
   * - M3
     - Flexible 2x2 MIMO RF Front-End
     - LibreCellular
     - :doc:`/developer/hardware/rf/rfe`
     -
     -
   * - M4-M5
     - LTE Band 3 Medium Power Amplifier
     - LibreCellular
     - :doc:`/developer/hardware/rf/b3mpa`
     -
     -
   * - M6-7
     - 1800MHz band 3 duplexer
     - Sysmocom
     - dx1800-kt30
     - Sysmocom
     - `dx1800-kt30`_
   * - FAN1-2
     - 60x60mm 24Vdc fan
     - ebm-papst
     - 614F
     - RS Components
     - `299-1526`_

*Cables to be added once build of the first system has been completed.*
  
Resources
---------

* `Mechanical design and graphics`_.

=======

.. _245-7831: https://uk.rs-online.com/web/p/subracks/2457831
.. _224-899: https://uk.rs-online.com/web/p/push-button-switches/0224899
.. _373-1678: https://uk.rs-online.com/web/p/push-button-switches/3731678 
.. _568-NC3MD-LX-M3: https://mou.sr/3SJLxYK
.. _121-6998: https://uk.rs-online.com/web/p/av-connector-accessories/1216998
.. _800-6986: https://uk.rs-online.com/web/p/coaxial-adapters/8006986
.. _756-1108: https://uk.rs-online.com/web/p/d-sub-connectors/7561108
.. _909-3717: https://uk.rs-online.com/web/p/hdmi-connectors/9093717
.. _121-7003: https://uk.rs-online.com/web/p/av-connector-accessories/1217003
.. _893-0606: https://uk.rs-online.com/web/p/fuse-holders/8930606
.. _207-2850: https://uk.rs-online.com/web/p/distribution-blocks/2072850
.. _207-2847: https://uk.rs-online.com/web/p/distribution-blocks/2072847
.. _dx1800-kt30: https://shop.sysmocom.de/1800-MHz-DCS-UMTS-LTE-Band-3-duplexer-30W/dx1800-kt30
.. _299-1526: https://uk.rs-online.com/web/p/axial-fans/2991526
.. _Mechanical design and graphics: https://github.com/myriadrf/lc-site-mechanical/tree/main/CSRAN1