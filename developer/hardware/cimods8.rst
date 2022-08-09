.. figure:: /images/CIMODS8_Front_Panel_1280w.jpg

CIMODS8
=======

8x LTE modem bank utilising two sysmoQMOD modem carrier boards.

Views
-----

.. figure:: /images/CIMODS8_Rear_Panel_1280w.jpg
   
   CIMODS8 Rear Panel.

.. figure:: /images/CIMODS8_Internal_1280w.jpg
   
   CIMODS8 Internal.

Theory of operation
-------------------

.. figure:: /images/CIMODS8_Block_Diagram.svg

Two Sysmocom sysmoQMOD boards provide 8x LTE modems connected via two front-panel USB B ports. Each sysmoQMOD provides an on-board USB hub to connect all four modems with the ability to reset each device.

Bill of materials
-----------------

.. list-table:: CIMODS8 BOM
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
     - 20860120
     - RS Components
     - `454-9666`_
   * - M1-2
     - sysmoQMOD modem carrier board
     - Sysmocom
     - sysmoQMOD
     - Sysmocom
     - `sysmoQMOD`_
   * - M3-M11
     - LTE modem
     - Sierra Wireless
     - MC7304
     - 
     - 
   * - CBL1-16
     - U.FL to SMA female bulkhead
     - RF Solutions
     - CBA-UFLSMA20
     - RF Solutions
     - `CBA-UFLSMA20`_
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
   * - J1-2
     - 2.5x5.5mm barrel plug
     - RS Pro
     - 487-854
     - RS Components
     - `487-854`_
   * - FAN1-2
     - 30x30mm 12Vdc fan
     - Nidec Copal
     - F310R-12LLC
     - Mouser
     - `229-F310R-12LLC`_
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
   * - Misc.
     - 30mm fan guard
     - Qualtek
     - 08346
     - Mouser
     - `562-08346`_
   * - Misc.
     - 0.5mm\ :sup:`2` ferrules
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

.. _454-9666: https://uk.rs-online.com/web/p/server-cabinet-accessories/4549666
.. _sysmoQMOD: https://www.sysmocom.de/news/sysmoqmod/index.html
.. _CBA-UFLSMA20: https://www.rfsolutions.co.uk/cable-assemblies-adaptors-c4/cable-assembly-ufl-to-sma-200mm-p7
.. _205-331: https://uk.rs-online.com/web/p/panel-mount-indicators/0205331
.. _707-7666: https://uk.rs-online.com/web/p/through-hole-resistors/7077666
.. _487-854: https://uk.rs-online.com/web/p/dc-power-connectors/0487854
.. _229-F310R-12LLC: https://mou.sr/3SydiTV
.. _562-08346: https://mou.sr/3QqYqEX
.. _207-2850: https://uk.rs-online.com/web/p/distribution-blocks/2072850
.. _207-2847: https://uk.rs-online.com/web/p/distribution-blocks/2072847