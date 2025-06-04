Network Configuration
=====================

Introduction
------------

The following minimum parameters are required when configuring an LTE network:

* Network name
* Mobile Country Code (MCC)
* Mobile Network Code (MNC)
* RF channel number (EARFCN)
* Bandwidth (PRBs)

There are plenty of other configuration options, some of which are specific to the hardware configuration, while others define network behaviour. Examples of the former include the SDR type, receive and transmit gains, and whether to configure for SISO or MIMO operation. While examples of the latter include timers, resource scheduling and neighbouring cell information.

However, for simple networks at least we can mostly use defaults and just need to know what we want our network to be called, the MCC/MNC tuple to use (PLMN ID), RF channel and bandwidth, and the APN.

Network name and PLMN ID
^^^^^^^^^^^^^^^^^^^^^^^^

It's best if the network name is something short. 

It's generally not possible to obtain a unique MNC, as these are very much in short supply, so instead we must use parameters which we know will not be used by any public mobile network. One option and the most appropriate for testing at least is an MCC/MNC of 001/01, which is designated for *Test Networks*. `ITU-T Recommendation E.212 Amendment 1 (07/2018)`_ specifies MCC of 999 for internal use within a private network and suggests that any MNC — which can be two or three digit — may be allocated under this. 

.. danger::
   A mobile network code of 99 is not the same as 099! Therefore the same MNC length must be used across all configuration.

EARFCN
^^^^^^

The are various `online tools`_ which let you look up the EARFCN for a radio frequency allocation. What we need to know is the EARFCN number which corresponds to the centre frequency of our *downlink* allocation. With the Ofcom Shared Access 3.3 MHz allocation in LTE Band 3 (1800 MHz), this happens to 1878.4 MHz, which corresponds to EARFCN 1934.

PRBs
^^^^

The bandwidth must be configured such that we do not transmit outside of our allocation. In LTE this is typically expressed in terms of the number of *resource blocks* (PRBs), where:

* 1.4MHz = 6 PRBs
* 3MHz = 15 PRBs
* 5MHz = 25 PRBs
* 10MHz = 50 PRBs
* 15 MHz = 75 PRBs
* 20 MHz = 100 PRBs

Using the same Ofcom Shared Access example, we would need to configure our eNodeB to use 15 PRBs. Alternatively, we could configure it for just 6 PRBs and move the centre frequency (downlink EARFCN), so as to leave more free contigous spectrum. Then use the remaining spectrum to operate one or more GSM BTS and perhaps even configure the two networks to interoperate. Which would be possible under an Ofcom Shared Access low power license, which permits operation of as many base stations as required within a 50m radius. However, this would obviously be a much more complex configuration.

.. note::
   Not all LTE bands support all possible channel bandwidths.  

.. _ITU-T Recommendation E.212 Amendment 1 (07/2018): https://www.itu.int/rec/T-REC-E.212/en
.. _online tools: https://www.sqimway.com/lte_band.php

