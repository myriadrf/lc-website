IP Multimedia Subsystem
=======================

.. toctree::
   :maxdepth: 2
   :hidden:

The IMS core is comprised of a number of SIP servers or proxies which perform different Call Session Control Function (CSCF) roles. The Kamailio software is used to provide the IMS core and is configured to connect to PyHSS for subscriber information.

Proxy Call Session Control Function (P-CSCF)
--------------------------------------------

The P-CSCF is the first point of contact for the IMS terminal (UE) and amongst other things it provides subscriber authentication, implements encryption using IPSec or TLS, inspects signalling and protects the IMS core.

Interrogating Call Session Control Function (S-CSCF)
----------------------------------------------------

The I-CSCF provides a forwarding point to the IMS domain and its IP address is published in DNS so that remote servers can find it. It is responsible for querying the HSS to ascertain the address of the S-CSCF and assign it to a user during SIP registration.

Serving Call Session Control Function (S-CSCF)
----------------------------------------------

The S-CSCF is the central node which handles SIP registrations, provides routing services and enforces network policy.  It connects to the HSS to retrieve user profiles and update associations. 

Short Message Centre (SMSC)
---------------------------

The SMSC is responsible for storing and forwarding SMS messages. It is also implemented using Kamailio.

The IMS also needs a HSS to operate and while we could have two HSS, one for the EPC and one for the IMS, this would be inconvenient and mean that we had to provision subscribers in two places. Each function (Kamailio instance) also has its own MySQL database. Finally, an internal DNS server is required and this is provided by the BIND software.