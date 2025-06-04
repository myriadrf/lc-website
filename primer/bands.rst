Bands, Bandwidths and Duplexing
===============================

.. toctree::
   :maxdepth: 2
   :hidden:

LTE frequency bands are identified by a number. For example, LTE Band 3 corresponds to the 1800 MHz band. Why not just state the frequency? LTE Band 3 denotes more than simply the frequency range and 3GPP specifications state that this is to be used with frequency division duplex (FDD) operation, with downlink to the UE on 1805-1880 MHz and uplink from it on 1710-1785 MHz. The specs furthermore state that valid channel bandwidths for LTE Band 3 are 1.4, 3, 5, 10, 15 and 20 MHz. 

Duplex operation is required because we need to be able to send and receive data, and to speak and listen at the same time (insofar as we’re able to perceive anyway). With mobile networks this is achieved via one of two methods: the aforementioned FDD operation, where we transmit on one frequency and receive on another, or via time division duplex (TDD) operation, where we very quickly switch between transmitting and receiving on the same frequency. 

The channel bandwidth will determine the maximum network throughput and this is shared by all users accessing the network via the same eNodeB. With LTE networks this is frequently expressed in terms of the number of resource blocks, where 15 resource blocks corresponds to 3 MHz bandwidth, 25 is 5 MHz and 100 is 20 MHz, for example. A resource block is the smallest amount of resource that can be allocated to a user and is part of the LTE physical layer structure. The details of which are not something which you generally need to be too concerned with, beyond being aware of the mapping between resource blocks and RF channel bandwidth. 

5G bands have a prefix of “n” and it just so happens that there is a band n3, which is also designated for FDD use and with the same uplink and downlink frequency ranges as LTE Band 3. However, the 3GPP specs state that valid bandwidths for n3 are 5, 10, 15, 20, 25, 30, 35, 40, 45 and 50 MHz. Mixed 4G and 5G operation within the same band is possible provided that use is coordinated. 


