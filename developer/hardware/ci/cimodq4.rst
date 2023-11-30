CIMODQ4
=======

4x LTE modem bank with VoLTE support.

Theory of operation
-------------------

.. figure:: /images/

Four `Quectel Mini PCIe EVB`_ boards provide 4x `Quectel EC25`_ Mini PCIe modems connected via a USB hub to a front-panel USB port.

Bill of materials
-----------------

.. list-table:: CIMODQ4 BOM
   :header-rows: 1

   * - Component
     - Description
     - Manufacturer
     - Man. Part
     - Distributor
     - Dist. Part
   * - Enclosure
     - 1U 19" rackmount enclosure
     - nVent Schroff
     - 20860-122
     - Farnell
     - `1455925`_
   * - USBHUB
     - Four port USB hub
     - Infineon
     - CY4608
     - RS Components
     - `273-2018`_
   * - EVB1-4
     - Mini PCIe EVB Kit
     - Quectel
     - MINIPCIEEVB-KIT
     - RS Components
     - `908-4199`_
   * - MOD1-4
     - LTE EC25 Mini PCIe modem
     - Quectel
     - EC25AFA-MINIPCIE
     - DigiKey
     - `2958-EC25AFA-MINIPCIE-ND`_
   * - S1-16
     - M3x20 F-F threaded standoff
     - Wurth
     - 970200321
     - RS Components
     - `205-3043`_
   * - S17-24
     - M3x10 F-F threaded standoff
     - Wurth
     - 970100321
     - RS Components
     - `176-8403`_
   * - F1
     - 5Vdc 30x30mm fan
     - Sunon
     - MF30150V1-1000U-A99
     - RS Components
     - `202-5395`_
   * - D1
     - Panel mount LED indicator, green
     - RS Pro
     - 205-331
     - RS Components
     - `205-331`_
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
   * - J1
     - 2.5x5.5mm barrel plug
     - RS Pro
     - 487-854
     - RS Components
     - `487-854`_
   * - J2
     - 16-way socket
     - Binder
     - 09-0340-00-16
     - RS Components
     - `734-5969`_
   * - J3
     - Male panel mount XLR connector
     - Neutrik
     - NC3MD-LX-M3
     - Mouser
     - `568-NC3MD-LX-M3`_
   * - J4
     - Panel-mount USB feed through
     - RS Pro
     - 124-6393
     - RS Components
     - `124-6393`_
   * - J5-8
     - Internal audio connector for modem modules
     - Multicomp Pro
     - MP-435LN
     - Farnell
     - `MP-435LN`_
   * - CBL1-4
     - USB A to R/A Micro B 0.5m
     - RS Pro
     - 236-9078
     - RS Components
     - `236-9078`_
   * - CBL5
     - USB A to B 0.5m
     - RS Pro
     - 182-8547
     - RS Components
     - `182-8547`_
   * - CBL6-13
     - Female SMA to U.FL 300mm
     - RS Pro
     - 794-2831
     - RS Components
     - `794-2831`_
   * - M1-4
     - Full size SIM to FPC adapter
     - Sysmocom
     - fullsize-sim-fpc
     - Sysmocom
     - `fullsize-sim-fpc`_
   * - FPC1-4
     - microSIM (3FF) FPC Cable, opposite cut corner side 
     - Sysmocom
     -  simffc-3ff-st-o
     - Sysmocom
     - `simffc-3ff-st-o`_
   * - Fan guard
     - 30mm fan guard
     - Qualtek
     - 08346
     - Mouser
     - `562-08346`_
   * - Misc.
     - 0.5mm\ :sup:`2` tri-rated wire in white and black
     - 
     - 
     - 
     -
   * - Misc.
     - 0.5mm\ :sup:`2` ferrules
     - 
     - 
     - 
     -
.. _Quectel Mini PCIe EVB: https://www.quectel.com/product/mini-pcie-evb-kit/
.. _Quectel EC25: https://www.quectel.com/product/lte-ec25-e-minipcie/
.. _1455925: https://uk.farnell.com/schroff/20860-122/case-19-rack-1u-340mm/dp/1455925
.. _273-2018: https://uk.rs-online.com/web/p/communication-wireless-development-tools/2732018
.. _908-4199: https://uk.rs-online.com/web/p/communication-wireless-development-tools/9084199
.. _2958-EC25AFA-MINIPCIE-ND: https://www.digikey.co.uk/en/products/detail/quectel/EC25AFA-MINIPCIE/13278160
.. _205-3043: https://uk.rs-online.com/web/p/standoffs/2053043
.. _176-8403: https://uk.rs-online.com/web/p/standoffs/1768403
.. _202-5395: https://uk.rs-online.com/web/p/axial-fans/2025395
.. _205-331: https://uk.rs-online.com/web/p/panel-mount-indicators/0205331
.. _207-2850: https://uk.rs-online.com/web/p/distribution-blocks/2072850
.. _207-2847: https://uk.rs-online.com/web/p/distribution-blocks/2072847
.. _487-854: https://uk.rs-online.com/web/p/dc-power-connectors/0487854
.. _734-5969: https://uk.rs-online.com/web/p/industrial-circular-connectors/7345969
.. _236-9078: https://uk.rs-online.com/web/p/usb-cables/2369078
.. _182-8547: https://uk.rs-online.com/web/p/usb-cables/1828547
.. _794-2831: https://uk.rs-online.com/web/p/coaxial-cable/7942831
.. _568-NC3MD-LX-M3: https://mou.sr/3SJLxYK
.. _124-6393: https://uk.rs-online.com/web/p/usb-connectors/1246393
.. _562-08346: https://mou.sr/3QqYqEX
.. _fullsize-sim-fpc: https://shop.sysmocom.de/Full-size-SIM-card-to-FPC-adapter/fullsize-sim-fpc
.. _simffc-3ff-st-o: https://shop.sysmocom.de/SIMtrace-microSIM-3FF-FPC-Cable-FPC-opposite-cut-corner-side/simffc-3ff-st-o
.. _MP-435LN: https://uk.farnell.com/multicomp-pro/mp-435ln/3-5mm-audio-plug-r-a-4pos-cable/dp/4066358