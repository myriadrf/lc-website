Radio Access Network
====================

.. toctree::
   :maxdepth: 2
   :hidden:

In an LTE RAN we have one or more eNodeBs and these connect to the core network via the S1 interface, an IP-based protocol. Some basic configuration needs to match on both sides and the eNodeB is configured to connect to an IP address within the core network.

Note that an eNodeB is usually an appliance and may run embedded Linux, but with no end user access to this or ability to install software and run other workloads. However, in our case since the eNodeB is SDR-based and all the network functions are software, we have the advantage that we can run everything on a single system and therefore have a complete cellular “network-in-a-box”. 

A key benefit of using a software-defined radio to create an eNodeB is that this is extremely flexible. If we wanted to change frequency band it’s just configuration, that is assuming our RF front-end (RFE) comprised of amplifiers and filters is compatible with the new band. If the software is updated to support a new 3GPP release or add new features, this is just a software update. Indeed, if we wanted to switch from 4G to 5G operation, or perhaps to 2G/GSM, this is just a question of changing the SDR software — again assuming that the RFE is compatible with the frequency band.

The downside to using an SDR is that this is just part of the system and to go beyond a benchtop experiment, we really need RF filtering and very likely amplification also. Which is why we provide designs for an RF Front-End (RFE) and complete base station reference design.

The LibreCellular project makes use of the eNodeB provided as part the srsRAN 4G stack from Software Radio Systems. There are plans to eventually add support for srsRAN 5G also and possibly the Osmocom 2G stack, since GSM can have advantages in certain applications. E.g. where only voice/SMS is required and greater coverage range and/or UE battery life is desirable. 

