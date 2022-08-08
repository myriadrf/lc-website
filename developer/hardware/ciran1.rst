.. figure:: /images/CIRAN1_Front_Panel_1280w.jpg

CIRAN1
======

LimeSDR base station #1.

This is comprised of the Reference Hardware Platform:

* `Intel NUC7i7DNBE`_ SBC.
* :ref:`developer/hardware/conio:conio-b` console IO board.
* `LimeSDR-USB`_.

With the notable exception of the LimeRFE board or any other sort of RF power
amplifier or LNA.

.. _Intel NUC7i7DNBE: https://ark.intel.com/content/www/us/en/ark/products/130394/intel-nuc-board-nuc7i7dnbe.html

.. _LimeSDR-USB: https://limemicro.com/products/boards/limesdr/

Views
-----

.. figure:: /images/CIRAN1_Rear_Panel_1280w.jpg
   
   CIRAN1 Rear Panel.

.. figure:: /images/CIRAN1_Internal_1280w.jpg
   
   CIRAN1 Internal.

Theory of operation
-------------------

.. figure:: /images/CIRAN1_Block_Diagram.svg

Fill in.

Bill of materials
-----------------

.. list-table:: CIRAN1 BOM
   :header-rows: 1

   * - Component
     - Description
     - Manufacturer
     - Man. Part
     - Distributor
     - Dist. Part
   * - D1
     - Panel mount LED indicator, green
     - RS Pro
     - 205-331
     - RS Components
     - `205-331`_
   * - R1
     - 1K ohm 0.25W 5% axial resistor
     - RS Pro
     - 707-7666
     - RS Components
     - `707-7666`_
   * - J1
     - Male panel mount XLR connector
     - Neutrik
     - NC3MD-LX-M3
     - Mouser
     - `568-NC3MD-LX-M3`_
   * - J2
     - Panel mount ethernet connector
     - RS Pro
     - 907-5656
     - RS Components
     - `907-5656`_
   * - J3
     - BNC bulkhead connector
     - RS Pro
     - 546-4083
     - RS Components
     - `546-4083`_
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
     - Removable hotswap HDD enclosure
     - Startech
     - S251BU31REM
     - Startech
     - `S251BU31REM`_
   * - M4
     - Console IO board
     - LibreCellular
     - CONIO-B
     - 
     - 
   * - M5-6
     - 1800MHz band 3 duplexer
     - Sysmocom
     - dx1800-kt30
     - Sysmocom
     - `dx1800-kt30`_
   * - FAN1-2
     - 60x60mm 12Vdc fan
     - ebm-papst
     - 612F
     - RS Components
     - `299-1510`_
   * - Misc.
     - SMA female to SMA male right-angle adapters
     - Siretta
     - ADAPT/SMAM/SMAF/RA
     - RS Components
     - `140-7605`_

.. _205-331: https://uk.rs-online.com/web/p/panel-mount-indicators/0205331
.. _707-7666: https://uk.rs-online.com/web/p/through-hole-resistors/7077666
.. _568-NC3MD-LX-M3: https://mou.sr/3SJLxYK
.. _907-5656: https://uk.rs-online.com/web/p/ethernet-couplers/9075656
.. _546-4083: https://uk.rs-online.com/web/p/coaxial-adapters/5464083
.. _207-2850: https://uk.rs-online.com/web/p/distribution-blocks/2072850
.. _207-2847: https://uk.rs-online.com/web/p/distribution-blocks/2072847
.. _S251BU31REM: https://www.startech.com/en-gb/hdd/s251bu31rem
.. _dx1800-kt30: https://shop.sysmocom.de/1800-MHz-DCS-UMTS-LTE-Band-3-duplexer-30W/dx1800-kt30
.. _299-1510: https://uk.rs-online.com/web/p/axial-fans/2991510
.. _140-7605: https://uk.rs-online.com/web/p/coaxial-adapters/1407605