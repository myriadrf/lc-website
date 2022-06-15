.. figure:: /images/LC_CI_Hardware_Header_1280w.jpg

CI Hardware Platform
====================

The continous integration hardware platform provides a combination of base stations and modem banks, with cabled RF and splitter/combiner network which features digitally controlled attenuation. The platform also includes support infrastructure such as clock distribution, interfacing and control.

The platform is modular in nature and housed in a 20U 19" equipment rack.

Subsystems
----------

The CI platform is comprised of numerous subsystems and for details of these see the pages linked below andfrom the site menu. External links are provided for further details of COTS/third party components used, while details of original components developed as part of the project are hosted on this website.

.. list-table:: Rack Layout
   :widths: 5 8 6 50
   :header-rows: 1

   * - Position
     - Subsystem
     - Status
     - Description
   * - *TOP*
     - :doc:`rftst`
     - 
     - RF test and measurement (GenComm GC747A)
   * - 20
     - FAN
     - 
     - Fan tray 
   * - 19
     - SWITCH
     - 
     - Managed Gigabit Ethernet switch
   * - 18
     - :doc:`cihost`
     - 
     - CI server
   * - 17
     - :doc:`cicon`
     - *Build*
     - CI controller
   * - 15-16
     - :doc:`ciran1`
     - *Build*
     - Base station #1 (LimeSDR-USB + Intel NUC)
   * - 13-14
     - :doc:`ciran2`
     - 
     - Base station #2 (LimeSDR Mini + UP2)
   * - 11-12
     - :doc:`cirf44`
     - 
     - RF distribution network
   * - 10
     - :doc:`ciclkd`
     -  
     - Reference clock distribution
   * - 9
     - :doc:`cimods8`
     - *Build*
     - 8x LTE modem bank
   * - 7-8
     - :doc:`cimodq4`
     -   
     - 4x LTE (VoLTE) modem bank
   * - 3-4
     - :doc:`cipsu`
     - *Build*
     - 12V + 5V DC power supply
   * - 1-2
     - UPS
     -
     - Uninterruptible power supply

.. note::
   Future possible expansion options include:

   * a second RF network to enable MIMO testing
   * audio test capabilities for VoLTE voice quality measurement

.. toctree::
   :hidden:

   rftst

   cihost
   cicon
   ciran1
   ciran2
   cirf44
   ciclkd
   cimods8
   cimodq4
   cipsu

Components
----------

At this point the only custom components are the :doc:`/developer/hardware/conio` board set, which is used to provide a remote console, plus remote power and reset control, for SDR base stations.

.. toctree::
   :hidden:

   conio