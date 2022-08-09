.. figure:: /images/CICON_Front_Panel_1280w.jpg

CICON
=====

The test controller unit:

* Provides remote console and power/reset control for base stations.
* Drives LTE modem banks.

Views
-----

.. figure:: /images/CICON_Rear_Panel_1280w.jpg
   
   CICON Rear Panel.

.. figure:: /images/CICON_Internal_1280w.jpg
   
   CICON Internal.

Theory of operation
-------------------

.. figure:: /images/CICON_Block_Diagram.svg

A PC Engines APU2E4 SBC is used together with a LibreCellular CONIO-A board, to provide remote access to base station serial consoles, along with power and reset toggling, via connection to CONIO-B boards at the remote end.

The SBC also provides USB ports, which together with those provided by the :doc:`cihost`, may be used to drive cellular modems and control RF attenuators.

Bill of materials
-----------------

.. list-table:: CICON BOM
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
   * - M1
     - PC Engines single board computer
     - PC Engines
     - APU2E4
     - 
     - 
   * - M2
     - Console IO board
     - LibreCellular
     - CONIO-A
     -
     -
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
     - Panel mount dual USB 2.0 connector
     - RS Pro
     - 862-1567
     - RS Components
     - `862-1567`_
   * - J4
     - Panel mount dual USB 3.0 connector
     - RS Pro
     - 862-1576
     - RS Components
     - `862-1576`_
   * - J5
     - 2.5x5.5mm barrel plug
     - RS Pro
     - 487-854
     - RS Components
     - `487-854`_
   * - J6-7
     - 2x10 box header
     - Harwin
     - M20-1071000
     - RS Components
     - `681-2871`_
   * - J7-8
     - 4-contact female connector
     - Molex
     - 22013047
     - RS Components
     - `679-5388`_
   * - J9-10
     - 5-contact female connector
     - Molex
     - 22013057
     - RS Components
     - `679-5385`_
   * - J11-12
     - DE-9 socket
     - RS Pro
     - 544-3749
     - RS Components
     - `544-3749`_
   * - CBL1-2
     - Internal USB 2.0 patch cable
     - Startech
     - USBINT5PIN12
     - RS Components
     - `240-6253`_
   * - Misc.
     - Female crimp terminals for Harwin M20 series
     - Harwin
     - M20-1180042
     - RS Components
     - `681-2878`_
   * - Misc.
     - Female crimp terminals for Molex KK 254 series
     - Molex
     - 08500113
     - RS Components
     - `670-2263`_
   * - Misc.
     - DE-9 connector shells
     - MH Connectors
     - MHCCOV-09SC-LG
     - RS Components
     - `821-2810`_
   * - Misc.
     - 0.5mm\ :sup:`2` tri-rated wire in red and black
     - 
     - 
     - 
     -
   * - Misc.
     - 1.5mm\ :sup:`2` tri-rated wire in red and black
     - 
     - 
     - 
     -
   * - Misc.
     - 22awg hook-up wire to build signal harnesses
     - 
     - 
     - 
     - 

.. _1455925: https://uk.farnell.com/schroff/20860-122/case-19-rack-1u-340mm/dp/1455925
.. _205-331: https://uk.rs-online.com/web/p/panel-mount-indicators/0205331
.. _707-7666: https://uk.rs-online.com/web/p/through-hole-resistors/7077666
.. _568-NC3MD-LX-M3: https://mou.sr/3SJLxYK
.. _907-5656: https://uk.rs-online.com/web/p/ethernet-couplers/9075656
.. _862-1567: https://uk.rs-online.com/web/p/usb-connectors/8621567
.. _862-1576: https://uk.rs-online.com/web/p/usb-connectors/8621576
.. _487-854: https://uk.rs-online.com/web/p/dc-power-connectors/0487854
.. _681-2871: https://uk.rs-online.com/web/p/wire-housings-plugs/6812871
.. _240-6253: https://uk.rs-online.com/web/p/wire-to-board-cables/2406253
.. _679-5388: https://uk.rs-online.com/web/p/wire-housings-plugs/6795388
.. _679-5385: https://uk.rs-online.com/web/p/wire-housings-plugs/6795385
.. _544-3749: https://uk.rs-online.com/web/p/d-sub-connectors/5443749
.. _681-2878: https://uk.rs-online.com/web/p/crimp-contacts/6812878
.. _670-2263: https://uk.rs-online.com/web/p/crimp-contacts/6702263
.. _821-2810: https://uk.rs-online.com/web/p/d-sub-backshells/8212810