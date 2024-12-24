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

However, for simple networks at least we can mostly use defaults and just need to know what we want our network to be called, the MCC/MNC tuple to use (PLMN ID), the radio channel (which we have licensed), and the APN which user equipment (handsets and modems) should connect to.

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

eNodeB 
------

With the :doc:`software/minimal` the eNodeB can be configured by editing the file /etc/srsran/enb.conf.

With the :doc:`software/standard` the eNodeB can be configured by editing the file /etc/lc/srslte/enb.conf.

The main parameters of interest are:

* **[enb]** section:
  
  * **mcc**. As described above.
  * **mnc**. As described above.
  * **n_prb**. As described above.
* **[rf]** section:
  
  * **dl_earfcn**. As described above.
  * **tx_gain**. A value of *66* seems to work well.
  * **rx_gain**. A value of *47* seems to work well.
  * **device_name**. *lime*.
  * **device_args**. *index=0,rxant=LNAH,txant=BAND2,cal=all,refclk=10e6*.
  * **time_adv_nsamples**. *73*.

The tx_gain value probably shouldn't be increased, as overdriving may compromise performance. rx_gain may be reduced if overloading is suspected, e.g. due to very close operation or perhaps use of an external LNA.

If an external GPS reference clock is not available, the device_args line should be trimmed to remove *refclk=10e6*, so that the SDR on-board reference clock is used instead. If configuring for an uplink (receive) frequency <1.5 GHz, the *rxant* parameter should be changed to *LNAL*, while being sure to also connect the receive antenna or duplexer port to the associated RF port on the SDR. 

The value for the time_adv_nsamples parameter is specific to particular SDR hardware and corrects for the delay that this introduces. A value of *73* for the parameter appears to be optimal for LimeSDR-USB. Synchronisation is important in cellular networks and there is no harm in experimenting with this parameter in an attempt to futher improve performance.

For further details, please see the `srsRAN documentation`_.

LTE Band 3 Example
^^^^^^^^^^^^^^^^^^

An `example is provided`_ for a 3 MHz channel in LTE Band 3, with SISO configuration. This corresponds to the Ofcom Shared Access 1800 MHz allocation.

Note that it will be neccessary to update the srsENB config if you need to use another channel.

EPC
---

Minimal Software Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The EPC is configured via :code:`/etc/srsran/epc.conf` and the main parameters of interest are:

* **[mme]** section:

  * **mcc**.  As described above.
  * **mnc**.  As described above.
  * **full_net_name** & **short_net_name**. Set both to the same, as described above.
  * **apn**. As described above.
  * **dns_addr**. Set to configure the DNS server for user equipment.

Note that subscribers must also be provisioned in the UE database and for details, see :doc:`subscribers`.

Standard Software Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the :doc:`software/standard` things are somewhat more complex. Changing the network name is easily enough done by updating the values in /etc/lc/open5gs/mme.yaml. However, changing the MCC/MNC would require making changes in a lot of places.

A collection of Ansible roles are planned which will make it trivial to configure a custom MCC/MNC, along with other network parameters.

.. _ITU-T Recommendation E.212 Amendment 1 (07/2018): https://www.itu.int/rec/T-REC-E.212/en
.. _online tools: https://www.sqimway.com/lte_band.php
.. _example is provided: https://github.com/myriadrf/lc-configs/tree/master/srsran/b3-3mhz-siso
.. _srsRAN documentation: https://docs.srsran.com/en/latest/