.. figure:: /images/CICLKD_Front_Panel_1280w.jpg

CICLKD
======

Clock distribution. This takes a GPS reference and distributes it to the SDR
base stations and RF test equipment. An optional TADD-3 PPS distribution board can be installed to distribute pulse-per-second signals.

Views
-----

.. figure:: /images/CICLKD_Rear_Panel_1280w.jpg
   
   CICLKD Rear Panel.

.. figure:: /images/CICLKD_Internal_1280w.jpg
   
   CICLKD Internal.

Theory of operation
-------------------

.. figure:: /images/CICLKD_Block_Diagram.svg

A clock distribution circuit on the TADD-1 board distributes 10MHz to six transformer isolated BNC output connectors. 

Bill of materials
-----------------

.. list-table:: CICLKD BOM
   :header-rows: 1

   * - Component
     - Description
     - Manufacturer
     - Man. Part
     - Distributor
     - Dist. Part
   * - M1
     - TADD-1 RF distribution amplifier
     - TAPR
     - TADD-1
     - TAPR
     - `TADD-1`_
   * - M2
     - TADD-3 PPS distribution amplifier (optional)
     - TAPR
     - TADD-3
     - TAPR
     - `TADD-3`_
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
   * - J2-3
     - Female panel mount BNC connector
     - Amphenol RF
     - 031-10-RFXG1
     - Mouser
     - `523-31-10-RFXG1`_
   * - Misc.
     - RG58 coaxial cable
     - 
     - 
     - 
     - 
   * - Misc (TODO: proper component category)
     - 0.5mm\ :sup:`2` tri-rated wire in red and black
     - 
     - 
     - 
     -

.. _TADD-1: https://tapr.org/product/tadd-1-rf-distribution-amplifier/
.. _TADD-3: https://tapr.org/product/tadd-3-pulse-per-second-distribution-amplifier/
.. _205-331: https://uk.rs-online.com/web/p/panel-mount-indicators/0205331
.. _707-7666: https://uk.rs-online.com/web/p/through-hole-resistors/7077666
.. _568-NC3MD-LX-M3: https://mou.sr/3SJLxYK
.. _523-31-10-RFXG1: https://mou.sr/3zEnQZ8