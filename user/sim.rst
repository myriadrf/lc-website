SIM Card Programming
====================

.. figure:: /images/SIM_Programming_1.jpg
   :align: center

In order to provision subscribers we will need to program SIM cards.

Hardware
--------

One or more programmable SIM cards and a suitable card reader (ideally compliant with the USB CCID specification) are requried. We use:

* `sysmoISIM-SJA2`_ SIM cards
* `Omnikey CardMan 3121`_ reader
* `Professional SIM card adapter`_

The adapter takes a regular, micro or nano SIM — snapped out of the full size card — and allows it to be inserted into the reader for re-programming.

SIM programming
---------------

The PySim software should be installed and for details, see the `Osmocom Wiki`_.

Before we can program a SIM card we need to know:

* Manufacturer supplied parameters:

  * **ICCID**. SIM card unique ID.
  * **ADM1**. Admin key.
* Network parameters:

  * **MCC**. Mobile country code.
  * **MNC**. Mobile network code.
  * **IMSI**. Subscriber ID.
  * **MSISDN**. Telephone number.
  * **Network name**.

.. attention::
   The provided example configuration for the :doc:`/user/software/standard` uses an MCC/MNC of 001/01, which is used in the example below. However, if configured for some other MCC/MNC this will need to be amended accordingly.

To program a SIM card we enter:

.. code-block:: bash

   ./pySim-prog.py -p 0 -n LibreCellular -c 44 -x 001 -y 01 -s <ICCID> -a <ADM1> -i <IMSI> --msisdn <MSISDN> --epdgid epdg.epc.mnc001.mcc001.pub.3gppnetwork.org --pcscf pcscf.ims.mnc001.mcc001.3gppnetwork.org --ims-hdomain ims.mnc001.mcc001.3gppnetwork.org --impi <IMSI>@ims.mnc001.mcc001.3gppnetwork.org --impu sip:<IMSI>@ims.mnc001.mcc001.3gppnetwork.org

This would program our SIM card with a network name of *LibreCellular*, using the SIM card ID and admin key supplied by sysmocom, setting the MCC/MNC to 001/01, and configuring the IMSI as specified by us. 

The :code:`-c` option sets the country code for the card issuer (us) and hence should be set appropriately if you are not located in the UK.

The :code:`--epdgid`, :code:`--pcscf`, :code:`--ims-hdomain`, :code:`--impi`` and :code:`--impu` options are used to configure the IMS network settings. These are not necessary for the EPC to function and basic data service, but are required if you will be running an IMS for VoLTE and SMS services.

How do we know what IMSI to use? sysmoISIM-SJA2 SIM cards are supplied pre-programmed with an IMSI already set. However, the first five digits of the IMSI should be set to the same as our network MCC+MNC. So with the above example, using 001/01, we would have an IMSI prefix of 00101. Since the cards were supplied with an IMSI prefix of 90170, one option when re-programming is to simply reuse the provided IMSI and change the first five digits, from 90170 to 00101. Of course, other schemes may be employed and the important thing is to ensure it is unique in your network and the IMSI prefix matches the MCC+MNC.

.. figure:: /images/SIM_Programming_Example.jpg
   :align: center

When successfully programmed we need to note down the security parameters that are returned:

* Ki
* OPC
  
If we would prefer to reuse an existing Ki and OPC, we can specify these with additional :code:`-k` and :code:`-o` parameters respectively. 

.. attention::
   Obviously the ADM1, Ki and OPC keys should be kept secure and not shared as we have done here!

.. _Osmocom Wiki: https://osmocom.org/projects/pysim/wiki 
.. _sysmoISIM-SJA2: https://shop.sysmocom.de/sysmoISIM-SJA2-SIM-USIM-ISIM-Card-10-pack-with-ADM-keys/sysmoISIM-SJA2-10p-adm
.. _Omnikey CardMan 3121: https://shop.sysmocom.de/Omnikey-CardMan-3121-USB-CCID-interface/cm3121
.. _Professional SIM card adapter: https://shop.sysmocom.de/Professional-SIM-card-adapter-plug-in-micro-nano-SIM-to-full-size/sim-adapter-pcb