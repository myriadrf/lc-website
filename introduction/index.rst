Introduction
============

LibreCellular will use commodity compute hardware together with software-defined
radio to create a highly flexible LTE base station, where the cellular core
network may optionally run alongside this for a fully self-contained solution. A
reference hardware platform will be provided, together with validated software
versions and configuration to enable repeatable deployment. 

The main use is envisaged as low power small cells, configured for typical
bandwidths of 1.4MHz and 3MHz, operating in `Ofcom Shared Access`_ and `CBRS`_
spectrum. These networks will initially support a data service only, but support
for native voice dialling via VoLTE — aka "HD voice" — is planned, along with
potentially circuit-switched fallback (CFSB) also at some point in the future. 

Roadmap
-------

The project will be split at a high level into four phases, with the first
being concerned with building out the CI hardware platform. This will be
followed by CI configuration and test, support for basic LTE data service, and
then support for native voice calling over LTE.

Continous Integration (CI) Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CI platform will integrate one or more test base stations with LTE modem
banks via a cabled RF network, with reference clock distribution, control, and
RF measurement.

This is the current development focus and see :ref:`ci_hardware` for details.

CI Platform Configuration and Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Automated testing will be made possible via use of the OsmoGSMTester software.
Test coverage will be extended over time as the project develops.

Basic Service
^^^^^^^^^^^^^

Upon completion of this phase it will be possible to provision subscribers,
connect user equipment (handsets or other terminals) to the network and use this
to transfer data.

Voice over LTE (VoLTE) Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An IP Multimedia Subsystem (IMS) will be integrated to enable native voice calling
using the network.

Architecture
------------

The key software components in the provisional architecture are summarised
below, but this is by no means a comprehensive list and is subject to change.

eNodeB
^^^^^^

The 4G base station componenent will be provided by `srsRAN`_.

Evolved Packet Core (EPC)
^^^^^^^^^^^^^^^^^^^^^^^^^

It is planned to use `Open5Gs`_ to provide the core network.

IP Multimedia Subsystem
^^^^^^^^^^^^^^^^^^^^^^^

It is intended to use `Kamailio`_ for the IMS.

.. _Ofcom Shared Access: https://www.ofcom.org.uk/manage-your-licence/radiocommunication-licences/shared-access
.. _CBRS: https://en.wikipedia.org/wiki/Citizens_Broadband_Radio_Service
.. _srsRAN: https://www.srsran.com/
.. _Open5Gs: https://open5gs.org/
.. _Kamailio: https://www.kamailio.org/
