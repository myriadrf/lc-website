Subscriber Provisioning
=======================

.. figure:: /images/SIM_Programming_1.jpg
   :align: center

In order to provision subscribers we will need to program SIM cards and add details to the EPC UE database.

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
  * **Network name**.

To program a SIM card we enter:

.. code-block:: bash

   ./pySim-prog.py -p 0 -n LibreCellular -t sysmoISIM-SJA2 -a <ADM1> -i <IMSI> -c 44 -x 001 -y 01 -s <ICCID>

This would program a sysmoISIM-SJA2 SIM card with a network name of *LibreCellular*, using the SIM card ID and admin key supplied by sysmocom, setting the MCC/MNC to 001/01, and configuring the IMSI as specified by us. 

The :code:`-c` option sets the country code for the card issuer (us) and hence should be set appropriately if not located in the UK.

How do we know what IMSI to use? sysmoISIM-SJA2 SIM cards are supplied pre-programmed with an IMSI already set. However, the first five digits of the IMSI should be set to the same as our network MCC+MNC. So with the above example, using 001/01, we would have an IMSI prefix of 00101. Since the cards were supplied with an IMSI prefix of 90170, one option when re-programming is to just reuse the provided IMSI and change the first five digits, from 90170 to 00101. Of course, other schemes may be used and the important thing is to ensure that the prefix matches the MCC+MNC.

.. figure:: /images/SIM_Programming_Example.jpg
   :align: center

When successfully programmed we need to note down the security parameters that are returned:

* Ki
* OPC
  
If we would prefer to reuse an existing Ki and OPC, we can specify these with additional :code:`-k` and :code:`-o` parameters respectively. 

.. attention::
   Obiously the ADM1, Ki and OPC keys should be kept secure and not shared as we have done here!

UE database configuration
-------------------------

Subscribers need to be provisioned via the CSV file :code:`/etc/srsran/user_db.cv`, with one line per subscriber. For the above example this might look like:

.. code-block:: bash

   andrew,mil,001010000045391,bbd6b6bf43cf9e9a436567410a9dfc09,opc,9a0d35d8bcec3f9eee0ca614637f1142,9001,000000000652,7,dynamic

The fields are as follows:

* **Name**. A useful label (not used by srsRAN)
* **Auth**. Authentication algorithm used by the UE.
* **IMSI**. UE's IMSI value.
* **Key**. UE's key (Ki).
* **OP Type**. Operator's code type, either OP or OPc.
* **AMF**. Authentication management field.
* **SQN**. UE's Sequence number for freshness of the authentication.
* **QCI**. QoS Class Identifier for the UE's default bearer.
* **IP alloc**. IP allocation strategy (dynamic or a valid IPv4 for static).




.. _Osmocom Wiki: https://osmocom.org/projects/pysim/wiki 
.. _sysmoISIM-SJA2: https://shop.sysmocom.de/sysmoISIM-SJA2-SIM-USIM-ISIM-Card-10-pack-with-ADM-keys/sysmoISIM-SJA2-10p-adm
.. _Omnikey CardMan 3121: https://shop.sysmocom.de/Omnikey-CardMan-3121-USB-CCID-interface/cm3121
.. _Professional SIM card adapter: https://shop.sysmocom.de/Professional-SIM-card-adapter-plug-in-micro-nano-SIM-to-full-size/sim-adapter-pcb