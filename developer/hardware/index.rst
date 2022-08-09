.. figure:: /images/LC_CI_Hardware_Header_1280w.jpg

CI Hardware Platform
====================

The continous integration hardware platform provides a combination of base stations and modem banks, with cabled RF and splitter/combiner network which features digitally controlled attenuation. The platform also includes support infrastructure such as clock distribution, interfacing and control.

The platform is modular in nature and housed in a 20U 19" equipment rack.

Subsystems
----------

The CI platform is comprised of numerous subsystems and for details of these see the pages linked below and from the site menu. External links are provided for further details of COTS/third party components used, while details of original components developed as part of the project are hosted on this website.

.. list-table:: Rack Layout
   :widths: 5 8 10 50
   :header-rows: 1

   * - Position
     - Subsystem
     - Status
     - Description
   * - *TOP*
     - :doc:`rftst`
     - Procured
     - RF test and measurement (GenComm GC747A)
   * - 24
     - Blank
     - 
     - 1U blanking panel  
   * - 23
     - SWITCH
     - Procured
     - Managed Gigabit Ethernet switch  
   * - 22
     - *Empty*
     - *N/A*
     - Leave empty to allow network cables to be routed out
   * - 21
     - :doc:`cihost`
     - Procured
     - CI server
   * - 20
     - :doc:`cicon`
     - Assembled
     - CI controller
   * - 18-19
     - :doc:`ciran1`
     - Assembled
     - Base station #1 (LimeSDR-USB + Intel NUC)
   * - 16-17
     - :doc:`ciran2`
     - Assembled
     - Base station #2 (LimeSDR Mini + UP2)
   * - 13-15
     - CIRANn
     - *Future*
     - Base stations #3 + #4 (TBC)  
   * - 12
     - :doc:`cirf4x16`
     - Assembled
     - RF distribution network A
   * - 11
     - :doc:`cirf4x16`
     - *Future*
     - RF distribution network B (MIMO)
   * - 10
     - :doc:`cimods8`
     - Assembled
     - 8x LTE modem bank
   * - 8-9
     - :doc:`cimodq4`
     - *Future*
     - 4x LTE (VoLTE) modem bank
   * - 7
     - AUDTST
     - *Future*
     - Audio test and mesurement (for VoLTE)    
   * - 6
     - :doc:`ciclkd`
     - Assembled
     - Reference clock distribution
   * - 5
     - Shelf
     - 
     - 1U shelf for general use, e.g. a local GPSDO     
   * - 3-4
     - :doc:`cipsu`
     - Assembled
     - 12V + 5V DC power supply  
   * - 1-2
     - UPS
     - *Future*
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
   cirf4x16
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
