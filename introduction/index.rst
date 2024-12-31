.. figure:: images/LC_Board_Logo_Detail_A_1280w.jpg

Introduction
============

LibreCellular uses commodity compute hardware together with software-defined
radio to create a highly flexible LTE base station, where the cellular core
network may optionally run alongside this for a fully self-contained solution. A
reference hardware platform will be provided, together with validated software
versions and configuration to enable repeatable deployment. 

The main use is envisaged as low power small cells, configured for typical
bandwidths of 1.4MHz and 3MHz, operating in `Ofcom Shared Access`_ and `CBRS`_
spectrum. 

Software Stack
--------------

The key software components are summarised below.

Note that the IMS need not be deployed if only a data service is required, i.e. no VoLTE or SMS service. 

eNodeB
^^^^^^

The 4G base station component is provided by the `MyriadRF fork of srsRAN 4G`_. This has native support — direct API integration — for the LimeSDR family of boards, which are the main focus for SDR hardware. Although it is also possible to use LimeSDR hardware via the SoapySDR API, we have found that this has a significant performance overhead and is not recommended. 

Home Subscriber Server (HSS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`PyHSS`_ is used to provide a HSS where subscribers are provisioned, for both the EPC and an IMS if one is set up. It also provides a Policy and Charging Rules Function (PCRF) and an Equipment Identity Register (EIR).

Evolved Packet Core (EPC)
^^^^^^^^^^^^^^^^^^^^^^^^^

The Standard Software Installation makes use of `Open5GS`_ to provide all EPC functions apart from the HSS and PCRF, which are provided by PyHSS.

.. note::

   A Minimal Software Installation is also available, which uses the srsEPC component of srsRAN 4G. This provides a simple EPC which integrates a basic HSS and therefore PyHSS is not required. 

IP Multimedia Subsystem (IMS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Kamailio`_ is used to provide the P-CSCF, I-CSCF, S-CSCF and SMSC elements of an IMS, which are used to provide native voice (VoLTE) and SMS services.

Reference Hardware Platform
---------------------------

Given that ease of use is a key aim, having a validated reference hardware
platform is important and should save a lot of time getting new users up and
running. In addition to which, this will make it much easier to rule out
hardware problems when issues do arise.

The initial reference hardware is specified with a reasonable degree of headroom
in terms of performance and flexibility, which clearly has cost implications and
a future cost-optimised version is also anticipated.

For details, see: :doc:`/user/hardware/index`

.. _OsmoGSMTester: https://osmocom.org/projects/osmo-gsm-tester
.. _Ofcom Shared Access: https://www.ofcom.org.uk/manage-your-licence/radiocommunication-licences/shared-access
.. _CBRS: https://en.wikipedia.org/wiki/Citizens_Broadband_Radio_Service
.. _MyriadRF fork of srsRAN 4G: https://github.com/myriadrf/srsRAN_4G/
.. _PyHSS: https://github.com/nickvsnetworking/pyhss
.. _Open5Gs: https://open5gs.org/
.. _Kamailio: https://www.kamailio.org/
