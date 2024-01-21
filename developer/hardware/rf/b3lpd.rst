.. figure:: /images/B3LPD_0p1_PCB_1.jpg
   :align: center

LTE Band 3 Low Power Duplexer
=============================

The Band 3 Low Power Duplexer (B3LPD) is an LTE Band 3 (1800 MHz) duplexer rated at 30 dBm (1W) downlink. It was initially designed for use in :doc:`/developer/hardware/ci/ciran2/index`, in place of the much larger and over-specified cavity duplexer used in :doc:`/developer/hardware/ci/ciran1`. However, it could also be used in base stations with <30 dBm transmit power.

B3LPD also provides a -24 dB coupled output which may be used for monitoring downlink.

Version 0.1
-----------

The B3LPD board is based around a Qorvo QPQ1297 high-performance Bulk Acoustic Wave (BAW) Duplexer, plus a TDK HHM22139A2 directional coupler.

Design
^^^^^^

.. figure:: /images/B3LPD_0p1_Schematic.svg
   :align: center

   B3LPD v0.1 schematic diagram.

.. figure:: /images/B3LPD_0p1_Board_Plot.png
   :align: center

   B3LPD v0.1 PCB layout.

Track widths have been calculated for fabrication using the `JLCPCB 4L impedance controlled service`_ (JLC04161H-7628 stackup).

.. warning::
   Other appropriate substrates could be used, however, RF signal path traces would need to be recalculated and modified accordingly.

The PCB design was entered using KiCAD. The project files have been published to the `lc-filters repository`_.

Bill of Materials
^^^^^^^^^^^^^^^^^

.. list-table:: B3LPD BOM
    :header-rows: 1

    * - Component
      - Description
      - Manufacturer
      - Man. Part
      - Distributor
      - Dist. Part
    * - J1
      - Edge launch SMA plug
      - Wurth
      - 60314202124525
      - 
      - 
    * - J2, J3, J4
      - U.FL connector
      - Hirose
      - U.FL-R-SMT(01)
      - 
      - 
    * - R1
      - 50R resistor
      - 
      - 
      - 
      - 
    * - U1
      - Duplexer
      - Qorvo
      - QPQ1297
      - 
      - 
    * - U2
      - Directional coupler
      - TDK
      - HHM22139A2
      - 
      -

.. _JLCPCB 4L impedance controlled service: https://jlcpcb.com/impedance
.. _lc-filters repository: https://github.com/myriadrf/lc-filters