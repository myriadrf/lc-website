.. figure:: /images/CIRF4x16_Front_Panel_1280w.jpg

CIRF4x16
========

4x to 16x RF splitter/combiner, plus digitally controlled attenuation. 

Up to four modem banks may be connected on one side, with up to four base
stations on the other side. The signal routed to and from each base station may
be individually attenuated, so as to test operating under varying conditions and
to trigger handover.

Views
-----

.. figure:: /images/CIRF4x16_Rear_Panel_1280w.jpg
   
   CIRF4x16 Rear Panel.

.. figure:: /images/CIRF4x16_Internal_1280w.jpg
   
   CIRF4x16 Internal.

Theory of operation
-------------------

.. figure:: /images/CIRF4x16_Block_Diagram.svg

Up to four base stations may be connected via a 4-channel digitally controlled RF attenuator, which is in turn cabled to a 1:4 RF splitter/combiner, with a single connection from this to a front panel mounted SMA connector.

Up to sixteen cellular modems may be connected, via four groups of four, with each group connected to a 1:4 RF splitter/combiner + attenuation. The resulting four RF paths are then connected to another 1:4 RF splitter/combiner, following which a single connection from this to a second front panel mounted SMA connector.

In typical operation a link is connected across the two front panel SMA connectors, bridging the two networks. However, this link may be removed in order to allow other equipment to be inserted into the RF path, such as a fading simulator, for example.

A single CIRF4x16 may support up to four base stations plus sixteen cellular modems in SISO operation, and two units may be used for 2x2 MIMO etc.

Bill of materials
-----------------

.. list-table:: CIRF4x16 BOM
   :header-rows: 1

   * - Component
     - Description
     - Manufacturer
     - Man. Part
     - Distributor
     - Dist. Part
   * - Enclosure
     - 1U Rack-mount enclosure
     - nVent SCHROFF
     - 20860122
     - Farnell
     - `1455925`_
   * - D1
     - Panel mount LED indicator, green
     - RS Pro
     - 205-331
     - RS Components
     - `205-331`_
   * - R1
     - 330 ohm 0.25W 5% axial resistor
     - RS Pro
     - 707-7622
     - RS Components
     - `707-7622`_
   * - J1
     - Male panel mount XLR connector
     - Neutrik
     - NC3MD-LX-M3
     - Mouser
     - `568-NC3MD-LX-M3`_
   * - J2
     - 2.5x5.5mm barrel plug
     - RS Pro
     - 487-854
     - RS Components
     - `487-854`_
   * - J3-J4
     - 3-contact female box header
     - Harwin
     - M20-1060300
     - RS Components
     - `681-2821`_
   * - CBL1-16
     - U.FL to SMA female bulkhead
     - RF Solutions
     - CBA-UFLSMA20
     - RF Solutions
     - `CBA-UFLSMA20`_
   * - CBL17-20
     - SMA female bulkhead to SMA male 75mm
     - Taoglas
     - CAB.0114
     - Mouser
     - `960-CAB.0114`_
   * - CBL21-24
     - SMA female to right-angle MCX male
     - RF Solutions
     - CBA-SMAF-MCXMR
     - RF Solutions
     - CBA-SMAF-MCXMR
   * - CBL25-26
     - Right-angle SMA male to SMA female bulkhead
     - Wurth Elektronik
     - 65503603215303
     - Mouser
     - `710-65503603215303`_
   * - CBL27-30
     - Right-angle SMA male to right-angle SMA male
     - Crystek Corporation
     - CCSMA2-MM-RG174-12
     - Mouser
     - `549-SMA2-MM-RG174-12`_
   * - CBL31
     - Semi-rigid 2" SMA male to male jumper
     - Mini-Circuits
     - 086-2SMR+
     - Mouser
     - `139-086-2SMR`_
   * - M1
     - Four-channel digitally controlled step attenuator
     - Sysmocom
     - sysmoRFDSATT-4-62
     - Sysmocom
     - `sysmoRFDSATT-4-62`_
   * - M2-3
     - 1:4 splitter/combiner
     - e-meca
     - 804-S-1.900-MO1
     - 
     - 
   * - M4-7
     - 1:4 splitter/combiner + attenutation
     - Sysmocom
     - rfcomb4r-att
     - Sysmocom
     - `rfcomb4r-att`_
   * - M8
     - Console IO board
     - LibreCellular
     - CONIO-B
     - 
     - 
   * - Misc.
     - SMA male to SMA male right-angle adapter
     - RF Solutions
     - ADP-SMAM-SMAM90
     - RF Solutions
     - `ADP-SMAM-SMAM90`_
   * - Misc.
     - Female crimp terminals for Harwin M20 series
     - Harwin
     - M20-1180042
     - RS Components
     - `681-2878`_
   * - Misc.
     - 22awg hook-up wire to build signal harnesses
     - 
     - 
     - 
     - 

Resources
---------

* `Mechanical design and graphics`_.

.. _1455925: https://uk.farnell.com/schroff/20860-122/case-19-rack-1u-340mm/dp/1455925
.. _205-331: https://uk.rs-online.com/web/p/panel-mount-indicators/0205331
.. _707-7622: https://uk.rs-online.com/web/p/through-hole-resistors/7077622
.. _568-NC3MD-LX-M3: https://mou.sr/3SJLxYK
.. _487-854: https://uk.rs-online.com/web/p/dc-power-connectors/0487854
.. _CBA-UFLSMA20: https://www.rfsolutions.co.uk/cable-assemblies-adaptors-c4/cable-assembly-ufl-to-sma-200mm-p7
.. _960-CAB.0114: https://www.mouser.co.uk/ProductDetail/960-CAB0114
.. _CBA-SMAF-MCXMR: https://www.rfsolutions.co.uk/cable-assemblies-adaptors-c4/sma-female-rg174-mcx-m-r-angle-200mm-long-p22
.. _710-65503603215303: https://www.mouser.co.uk/ProductDetail/710-65503603215303
.. _549-SMA2-MM-RG174-12: https://www.mouser.co.uk/ProductDetail/549-SMA2-MM-RG174-12
.. _ADP-SMAM-SMAM90: https://www.rfsolutions.co.uk/cable-assemblies-adaptors-c4/rf-adaptors-c154/rf-adaptor-sma-male-to-sma-male-right-angle-p508
.. _681-2821: https://uk.rs-online.com/web/p/wire-housings-plugs/6812821
.. _681-2878: https://uk.rs-online.com/web/p/crimp-contacts/6812878
.. _sysmoRFDSATT-4-62: https://www.sysmocom.de/products/lab/rfdsatt/index.html
.. _rfcomb4r-att: https://shop.sysmocom.de/52.5dB-IL-resistive-1-4-RF-splitter-combiner-attenuator-PCBA-U.FL-in-SMA-out/rfcomb4r-att40
.. _139-086-2SMR: https://www.mouser.co.uk/ProductDetail/139-086-2SMR
.. _Mechanical design and graphics: https://github.com/myriadrf/lc-ci-mechanical/tree/main/CIRF4x16
