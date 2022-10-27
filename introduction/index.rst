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
spectrum. These networks will initially support a data service only, but support
for native voice dialling via VoLTE — aka "HD voice" — is planned, along with
potentially circuit-switched fallback (CSFB) also at some point in the future. 

Roadmap
-------

The project is split at a high level into four initial phases, with the first
being concerned with building out the CI hardware platform. This will be
followed by CI configuration and test, support for basic LTE data service, and
then support for native voice calling over LTE.

Continous Integration (CI) Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CI platform integrates one or more test base stations with LTE modem
banks via a cabled RF network, with reference clock distribution, control, and
RF measurement.

CI Platform Configuration and Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Automated testing will be made possible via use of the `OsmoGSMTester`_ software. Test coverage will be extended over time as the project develops.

This is the current development focus and see :doc:`/developer/software/ci/index` for details.

Basic Service
^^^^^^^^^^^^^

This stage has been completed and for details see the :doc:`/user/index`.

Voice over LTE (VoLTE) Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An IP Multimedia Subsystem (IMS) will be integrated to enable native voice calling using the network.

Software Stack
--------------

The key software components in the provisional stack are summarised below, but
this is by no means a comprehensive list and is subject to change.

eNodeB
^^^^^^

The 4G base station component will be provided by `srsRAN`_.

Evolved Packet Core (EPC)
^^^^^^^^^^^^^^^^^^^^^^^^^

It is planned to use `Open5Gs`_ to provide the core network, but initially the srsEPC component of srsRAN is being used.

IP Multimedia Subsystem
^^^^^^^^^^^^^^^^^^^^^^^

It is intended to use `Kamailio`_ for the IMS.

Reference Hardware Platform
---------------------------

Given that ease of use is a key aim, having a validated reference hardware
platform is important and should save a lot of time getting new users up and
running. In addition to which, this will make it much easier to rule out
hardware problems when issues do arise.

The initial reference hardware is specified with a reasonable degree of headroom
in terms of performance and flexibility, which clearly has cost implications and
a future cost-optimised version is also anticipated.

For details, see: :doc:`/user/hardware`

.. _OsmoGSMTester: https://osmocom.org/projects/osmo-gsm-tester
.. _Ofcom Shared Access: https://www.ofcom.org.uk/manage-your-licence/radiocommunication-licences/shared-access
.. _CBRS: https://en.wikipedia.org/wiki/Citizens_Broadband_Radio_Service
.. _srsRAN: https://www.srsran.com/
.. _Open5Gs: https://open5gs.org/
.. _Kamailio: https://www.kamailio.org/
