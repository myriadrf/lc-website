Frequently Asked Questions
==========================

Is this a fork or duplication of <insert project name>?
-------------------------------------------------------

No, the intention is to build upon existing projects, rather than to duplicate
efforts.

Why not simply contribute to an existing project?
-------------------------------------------------

A particular combination of hardware and functionality is being targeted, with
the objective of creating a complete hardware + software solution that is
relatively easy to set up and that is reliable. As such, it's possible that over
time some of the software components used may change. However, the intention
will also be to contribute back to upstream projects where possible.

Is it legal to operate a mobile phone network?
----------------------------------------------

Of course, provided that you have a spectrum licence. Cellular spectrum may be
licensed in the UK via `Ofcom Shared Access`_ and `CBRS`_ is available in the
US, for example. There are also other licensing schemes available elsewhere.
Further details will be provided in due course.

What are the operational requirements going to be?
--------------------------------------------------

Availability of suitable spectrum, as noted above. Plus of course a power supply and, if you'd like to provide Internet access, some form of connection. Although it would also be possible to operate fully standalone networks which provide access to local applications only. Where greater coverage is required it may also be neccessary to install an outdoor antenna. 

What will a LibreCellular setup cost?
-------------------------------------

This will vary depending upon the performance, e.g. whether it is a SISO configuration or 2x2 MIMO, and the transmit output power. However, the aim is for a basic setup which would cover a small-medium size residential property to cost less than £1,000. This is obviously a lot more expensive than a femtocell, but cheaper than a typical commercial small cell eNodeB and with the benefit of being an open source solution, with integrated core network and the ability to run mobile edge compute (MEC) workloads also.

Can I already buy a kit?
------------------------

No, but we will be providing a reference design with a complete bill of materials (shopping list). However, in future we do also hope to be able to offer some sort of kit.

What can I do to support the project? Can I make donations?
-----------------------------------------------------------

We're not soliciting financial donations at this stage, but may be interested in donations of equipment, e.g. eNodeB equipment for interoperability testing and RF power amplifiers etc.

How can I keep up to date with the development of the project?
--------------------------------------------------------------

We'll be posting updates to the `MyriadRF blog`_ and are considering setting up a newsletter also.

.. _Ofcom Shared Access: https://www.ofcom.org.uk/manage-your-licence/radiocommunication-licences/shared-access
.. _CBRS: https://en.wikipedia.org/wiki/Citizens_Broadband_Radio_Service
.. _MyriadRF blog: https://myriadrf.org/news/
