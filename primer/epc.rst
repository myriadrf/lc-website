Evolved Packet Core
===================

.. toctree::
   :maxdepth: 2
   :hidden:

The srsRAN 4G stack is provided complete with a minimal, easy to use, single binary EPC. This may be sufficient for simple requirements and for details see EPC Minimal Software Configuration.

A much more fully featured EPC is provided by Open5GS, which can also be configured to provide a 5G Core, or a combination of this and EPC. Whereas the srsRAN EPC is a monolithic solution, Open5GS is a series of software components which provide the various different functions of a core network. An approach which provides a lot more flexibility and means that, for example, configurations can be created where certain network functions are provided by other software.

Open5GS is used to provide the EPC Standard Software Configuration.

Home Subscriber Server (HSS)
----------------------------

The Home Subscriber Server (HSS) is the master database where users are provisioned. It is responsible for authentication and authorisation, and provides information about subscriber location and IP information, enabling UEs to be paged, and bearers and SIPs session setup. 

Although Open5GS provides a HSS, the PyHSS software is used for this function instead, since it provides the necessary functionality to also support use with an IMS core, whereas the Open5GS HSS does not. PyHSS is a reasonably lightweight application which makes use of MySQL and Redis, and it exposes a web API for managing subscriber records.

Mobility Management Entity (MME)
--------------------------------

The Mobility Management Entity (MME) is the main control node in an LTE network and amongst other things it is responsible for authenticating subscribers (in turn via connection to the HSS), allocating temporary IDs to UEs and paging them. It also takes care of handovers from one eNodeB to another, and to/from other RATs, and manages encryption and enforces roaming.

Serving Gateway (SGW)
---------------------

The LTE Serving Gateway (SGW) acts as a mobility anchor, routing and forwarding data between the eNodeB and Packet Data Network Gateway (PGW). It works together with the MME to coordinate handovers between different eNodeBs and to/from other RATs, and is also responsible for managing quality-of-service (QoS).

The SGW is split into control plane (SGW-C) and user plane (SGW-U) parts and each of these is a distinct function within Open5GS.

Packet Data Network Gateway (PGW)
---------------------------------

The Packet Data Network Gateway (PGW) is responsible for allocating IP address to UEs, enforcing policies such as packet filtering, and routes packets to and from external networks.

With Open5GS the PGW function is provided by a combination of the UPF and SMF components. These are technically the 5G Core Session Management Function (SMF) and User Plane Function (UPF), but with Open5GS they can be configured to provide the 4G EPC PGW function.

Summary
-------

So just to recap our core network is comprised of:

* **Home Subscriber Server (HSS)**. Subscriber information.

  * Provided by PyHSS plus MySQL and Redis.

* **Mobility Management Entity (MME)**. Attaching UEs, allocating temporary IDs, authentication, ciphering, and managing handovers etc.

  * Provided by Open5GS MME.

* **Serving Gateway (SGW)**. Mobility anchor which routes and forwards data, and works with the MME to coordinate handovers.

  * Provided by Open5GS SGW-C and SWG-U.

* **Packet Data Network Gateway (PGW)**. Allocate IPs to UEs, enforce policies and route to/from external networks.

  * Provided by Open5GS UPF and SMF.
