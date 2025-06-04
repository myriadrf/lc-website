Network Architecture
====================

.. toctree::
   :maxdepth: 2
   :hidden:

Mobile networks are split at a high level into:

* Radio access network (RAN)

  * Comprised of the base stations which UEs connect to

* Mobile core network

  * Provides functions such as subscriber management, mobility management, and data routing

* IP Multimedia System (IMS) core

  * Used to provide native voice and SMS support, along with other media services

With LTE (4G) networks the RAN is implemented by eNodeBs, while the core network is provided by an Evolved Packet Core (EPC). The IMS core is used to provide native voice and SMS support, known as Voice-over-LTE (VoLTE).

With 5G NR the RAN is implemented by gNodeBs, while the core network is provided by the 5G Core (5GC). The IMS core largely remains the same, although there are some differences in how this is implemented for Voice-over-NR (VoNR).

The current focus of the LibreCellular project is on LTE networks, but there are plans to add support for 5G NR in the future.

The most basic LTE network is comprised of a single eNodeB for the RAN, plus a core network which this connects to. An IMS core would also be required in order to support native voice and SMS, but this is optional and can be omitted if only a data service is required.

Next let’s take a look at the three subsystems in a little more detail.
