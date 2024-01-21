.. figure:: /images/CIRAN2_Front_Panel_1280w.jpg

CIRAN2
======

CIRAN2 is a more modular version of :doc:`../ciran1` and is designed to host up to two separate base stations on removable sleds.

Views
-----

.. figure:: /images/CIRAN2_Rear_Panel_1280w.jpg
   
   CIRAN2 Rear Panel.

.. figure:: /images/CIRAN2_Internal_1280w.jpg
   
   CIRAN2 Internal shown with a CR2S01 (LimeSDR Mini 2.0 + UP 4000 SBC) sled fitted.

Theory of operation
-------------------

.. figure:: /images/CIRAN2_Block_Diagram.svg

12VDC and 5VDC power is available on PTFIX distribution terminals and the enclosure is fitted with two fans for cooling. 

A :doc:`../csad10` board provides reference clock distribution within the chassis. 

See the sled designs for base station details.

Sleds
*****

.. list-table:: CIRAN2 Sleds
   :header-rows: 1

   * - Sled
     - Description
     - Status
   * - :doc:`cr2s01`
     - LimeSDR Mini 2.0, UP 4000 SBC and low power duplexer
     - Assembled

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
   * - Enclosure
     - 2U Rack-mount enclosure
     - nVent SCHROFF
     - 20860127
     - RS Components
     - `245-7831`_
   * - D1-D2
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
   * - R2
     - 270 ohm 0.25W 5% axial resistor
     - RS Pro
     - 707-7625
     - RS Components
     - `707-7625`_
   * - J1
     - Male panel mount XLR connector
     - Neutrik
     - NC3MD-LX-M3
     - Mouser
     - `568-NC3MD-LX-M3`_
   * - J2-J3
     - Panel mount ethernet connector
     - RS Pro
     - 907-5656
     - RS Components
     - `907-5656`_
   * - J4
     - BNC bulkhead connector
     - RS Pro
     - 546-4083
     - RS Components
     - `546-4083`_
   * - J5-J8
     - Panel mount SMA socket to SMA socket
     - Amphenol
     - SMA7471B1-3GT50G-50
     - RS Components
     - `700-9607`_
   * - J9
     - RF Adapter SMA Socket to BNC Plug
     - RF Solutions
     - ADP-SMAF-BNCM
     - RS Components
     - `125-1250`_
   * - M1-2
     - Console IO board
     - LibreCellular
     - CONIO-B
     - 
     - :doc:`../conio`
   * - M3
     - Reference clock distribution (10 outputs)
     - LibreCellular
     - CSAD10
     - 
     - :doc:`../csad10`
   * - CBL1 
     - 250mm Female U.FL to Male SMA Coaxial Cable
     - RF Solutions
     - CBA-UFL-SMAM25
     - RS Components
     - `125-8188`_
   * - TB1
     - PTFIX Distribution Block, 6 way, 2.5mm, red
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
   * - TB3
     - PTFIX 1.5-F Series Flange Cover
     - Phoenix Contact 
     - 1049503
     - RS Components
     - `207-2831`_
   * - FAN1-2
     - 60x60mm 12Vdc fan
     - Sunon
     - MF60151VX-1000U-A99
     - RS Components
     - `202-5421`_
   * - FG1-4
     - 60mm fan guard
     - RS Pro
     - 737-3973
     - RS Components
     - `737-3973`_
   * - Misc.
     - 1.5mm\ :sup:`2` tri-rated wire in red, white black
     - 
     - 
     - 
     - 
   * - Misc.
     - 1.5mm\ :sup:`2` ferrules
     - 
     - 
     - 
     -  

Resources
---------

* `Mechanical design and graphics`_.

.. _245-7831: https://uk.rs-online.com/web/p/subracks/2457831
.. _205-331: https://uk.rs-online.com/web/p/panel-mount-indicators/0205331
.. _707-7666: https://uk.rs-online.com/web/p/through-hole-resistors/7077666
.. _707-7625: https://uk.rs-online.com/web/p/through-hole-resistors/7077625
.. _568-NC3MD-LX-M3: https://mou.sr/3SJLxYK
.. _907-5656: https://uk.rs-online.com/web/p/ethernet-couplers/9075656
.. _546-4083: https://uk.rs-online.com/web/p/coaxial-adapters/5464083
.. _700-9607: https://uk.rs-online.com/web/p/coaxial-adapters/7009607
.. _125-8188: https://uk.rs-online.com/web/p/coaxial-cable/1258188
.. _125-1250: https://uk.rs-online.com/web/p/coaxial-adapters/1251250
.. _207-2850: https://uk.rs-online.com/web/p/distribution-blocks/2072850
.. _207-2847: https://uk.rs-online.com/web/p/distribution-blocks/2072847
.. _207-2831: https://uk.rs-online.com/web/p/din-rail-terminal-accessories/2072831
.. _202-5421: https://uk.rs-online.com/web/p/axial-fans/2025421
.. _737-3973: https://uk.rs-online.com/web/p/finger-guards/7373973
.. _Mechanical design and graphics: https://github.com/myriadrf/lc-ci-mechanical/tree/main/CIRAN2

.. toctree::
   :hidden:

   cr2s01