MIMO
====

.. toctree::
   :maxdepth: 2
   :hidden:

Wireless multiple-input and multiple-output (MIMO) is a somewhat more advanced topic, but worth mentioning here in brief as it can have implications when it comes to spectrum licensing. In short, MIMO is a technique which can be used to exploit multipath propagation (signals travelling to the receiver via different paths) in order to reduce interference and increase throughput.

Simpler systems with single transmit and receive antennas are referred to as single-input single-output (SISO). Whereas a 2x2 MIMO system would have two transmit and two receive antennas. Though in reality this could be just one physical antenna for SISO and two with 2x2 MIMO, if for example TDD operation were used and with each antenna switching between transmit and receive. 

The important thing to understand is that with SISO we have one transmit stream and one receive stream, whereas with 2x2 MIMO we would have two of each, with 4x4 MIMO we’d have four transmit and four receive streams, and so on. Furthermore, each transmit port is operating on the same frequency, as are all the receive ports. With some clever maths making sense of it all.

The reason we need to consider this with licensing is that with a MIMO system the total RF power output from the base station would be the sum of the power output from all the transmit ports. Cost is also another consideration, since MIMO systems require more advanced SDRs and additional RF components — such as amplifiers and filters — for the extra channels.

