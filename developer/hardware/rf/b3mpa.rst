.. figure:: /images/B3MPA_0p1_PCB_1.jpg
   :align: center

LTE Band 3 Medium Power Amplifier
=================================

Low power RF amplifiers for cellular bands can be obtained as off-the-shelf items without too great a cost. Whereas amplifiers which are capable of producing a few watts or more of RF power tend to become quite expensive. Meanwhile the advent of spectrum licensing schemes which permit operation of medium power systems — such as Ofcom Shared Access in rural designated areas — has meant that affordable medium power RF amplifier solutions are needed.

The objective is to create a low cost RF power amplifier for LTE Band 3 (1800 MHz), which can be used together with another amplifier as a driver stage, between the SDR and the final PA. A target minimum *modulated* power output of at 32dBm (1.6W) has been set, which into an 8dBi gain antenna would result in an EIRP of 40dBM (10W).

.. note::
   Modern wireless systems such as LTE use waveforms which have a high Peak-to-Average Power Ratio (PAPR), which means that a power amplifier *back-off* of at least 6-7dB is typically required in order to maintain linearity in the PA. This is essential for ensuring both good system performance and wireless regulatory compliance. 

Version 0.1
-----------

The initial design makes use of a BGY2016 three-stage UHF amplifier module, which is specified to have a gain of at least 28dB and a CW (not modulated) output power of 16W. The reason for selecting this particular device is that, while it is not a current part, it is available in large numbers via sites such as AliExpress and can cost as little as around £8 in single quantity.

Design
^^^^^^

.. figure:: /images/B3MPA_0p1_Schematic.jpg
   :align: center

The BGY2016 data sheet provides a reference layout for fabrication using a high performance PCB laminate which is commonly used in professional RF designs. However, since this is quite expensive, the design has been modified to use the `OSH Park 4-layer Prototype Service`_ (FR408-HR substrate), which is much lower cost and has previously been used with good results in a number of RF designs.

.. figure:: /images/B3MPA_0p1_Board_Plot.jpg
   :align: center

.. warning::
   The design should not be fabricated using a regular 2 layer PCB service, since this will not provide sufficient impedance control. Other appropriate substrates could be used, however, the microstrip traces would need to be recalculated and modified accordingly.

The PCB design was entered using KiCAD. The project files have been published to the `lc-b3-mpa repository`_. This repository also includes the mechanical design for a CNC machined aluminium palette, which is used to thermally couple the RF module to a heatsink. The palette design also assumes a board fabricated using the OSH Park 4-layer substrate and similarly may need to be modified if some other stack-up were used.

Bill of Materials
^^^^^^^^^^^^^^^^^

*BOM table here with same format as previously used*

P1dB Test Results
^^^^^^^^^^^^^^^^^

.. figure:: /images/B3MPA_0p1_P1dB_Test_Setup.jpg
   :align: center

*Add a few words here about the test setup*

*Add a table listing the equipment and include the serial numbers*

.. figure:: /images/B3MPA_0p1_P1dB_Test_Block_Diagram.jpg
   :align: center

*Add some words about the test process*

*Add table of results*

.. figure:: /images/B3MPA_0p1_P1dB_Test_Plot.jpg
   :align: center

.. _OSH Park 4-layer Prototype Service: https://docs.oshpark.com/services/four-layer/
.. _lc-b3-mpa repository: https://github.com/myriadrf/lc-b3-mpa