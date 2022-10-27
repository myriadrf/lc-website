Running the Network
===================

With the cellular stack configured and subscribers provisioned we can now start the network. 

First we need to enable masquerading if we'd like connected user equipment to have Internet access:

.. code-block:: bash

   sudo /usr/bin/srsepc_if_masq.sh <primary network interface>

Next the eNodeB can be started with:

.. code-block:: bash

   sudo srsenb /etc/srsran/enb.conf

Following which we should see output similar to that shown below and indicating that an external reference of 10 MHz has been configured.

.. figure:: /images/srsENB_startup_1.jpg
   :align: center

If we enter :code:`t` this will enable tracing. 

As this point, without the EPC started we would actually see an error that it cannot connect to this, but in the above screenshot it has already been started.

We should also see an LED on the LimeSDR-USB illuminate to indicate that we are locked to an external frequency reference.

.. figure:: /images/LimeSDR-USB_ExtRef_Locked.jpg
   :align: center

With the SDR fitted in this particular enclosure, the LED is top-left.

The EPC can be started with:

.. code-block:: bash

   sudo srsenb /etc/srsran/epc.conf

.. figure:: /images/srsEPC_Startup_Attach.jpg
   :align: center

Here we can see the EPC starting up, an incoming S1 request as the eNodeB connects, and then an IMSI attach request and bearer setup as a handset camps on to the network.

Finally, a speed test was run in a web browser on the handset.

.. figure:: /images/srsENB_SpeedTest_1.jpg
   :align: center

In the above eNodeB trace we can first see the download speed test, resulting in a downlink speed of 10Mbps. Following which the upload test results in uplink speeds of around 5Mbps. This is with a 3MHz RF channel (15 PRBs) and SISO configuration.

Automatic startup 
-----------------

Automatic start-up can be configured by enabling :code:`srsepc.service` and :code:`srsepc.service`.

Troubleshooting
---------------

The srsRAN documentation provides troubleshooting information for both `srsENB`_ and `srsEPC`_.

Questions concerning the srsENB fork with LMS API support should be directed to the `MyriadRF forum`_ and issues logged via the `MyriadRF srsRAN repo`_.

.. _srsENB: https://docs.srsran.com/en/latest/usermanuals/source/srsenb/source/3_enb_trouble.html
.. _srsEPC: https://docs.srsran.com/en/latest/usermanuals/source/srsepc/source/3_epc_trouble.html
.. _MyriadRF forum: https://discourse.myriadrf.org/c/projects/librecellular/39
.. _MyriadRF srsRAN repo: https://github.com/myriadrf/srsRAN/
