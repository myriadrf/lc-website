Minimal Software Installation
=============================

The minimal software stack is comprised of:

* **srsEPC**. Lightweight LTE Evolved Packet Core.
* **srsENB**. LTE eNodeB basestation implemented entirely in software.
* **Lime Suite**. Software-defined radio (SDR) driver.
* **Ubuntu Linux**. Operating system.

This is the quickest way to get up and running and provides only a data service, with a simple EPC where subscribers are provisioned via a CSV file.

The minimal configuration may also prove useful where there is an existing EPC and only the eNodeB is required.

Ubuntu Server 22.04
-------------------

`Ubuntu Server`_ version 22.04 LTS should be downloaded and installed. Default installation options should suffice, although for convenience the SSH server should probably be selected for installation.

Desktop Ubuntu could be used instead, but includes all sorts of redundant software which is not required. Other Ubuntu versions or Linux distros could also likely be used, but have not been tested.

Once rebooted install any updates, then configure the PPAs for Lime Suite and the LibreCellular fork of srsRAN:

.. code-block:: bash

   sudo apt update && sudo apt dist-upgrade
   sudo add-apt-repository ppa:myriadrf/drivers
   sudo add-apt-repository ppa:myriadrf/librecellular
   sudo apt update

If the command to add a PPA hangs, this may be due to IPv6 issues and to resolve edit the file :code:`/etc/gai.conf` and uncomment the line :code:`precedence ::ffff:0:0/96 100`, following which save and retry the command.

Next configure the CPU governor to use performance mode:

.. code-block:: bash

   sudo apt install cpufrequtils
   echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils
   sudo systemctl disable ondemand
   sudo reboot

This is to ensure that the SDR transceiver application does not suffer scheduling delays, which could result in reduced performance and/or instability.

Lime Suite and srsRAN
---------------------

srsRAN version
^^^^^^^^^^^^^^

A fork of the srsRAN 4G software is being maintainted which adds native support for LMS API, the API provided by Lime Suite and used by LimeSDR hardware. In testing this has been found to provide much better performance than use via SoapySDR. In addition to which, direct integration enables greater control of the SDR hardware, such as providing the ability to configure an external reference clock.

.. warning::
   Issues in connection with this fork should be logged under the `srsRAN 4G repo in the MyriadRF organisation`_ and not the upstream srsRAN repo, since this is an experimental fork which is not supported by the srsRAN developers.

PPA packages
^^^^^^^^^^^^

With the PPAs configured, install Lime Suite and the srsRAN fork:

.. code-block:: bash

   sudo apt install limesuite srsran

Source build
^^^^^^^^^^^^

Install Lime Suite build dependencies:

.. code-block:: bash

   sudo apt install build-essential git g++ cmake libsqlite3-dev libi2c-dev libusb-1.0-0-dev libwxgtk3.0-gtk3-dev freeglut3-dev

Clone, build and install Lime Suite:

.. code-block:: bash

   git clone https://github.com/myriadrf/LimeSuite.git
   cd LimeSuite
   git checkout v23.11.0
   mkdir builddir
   cd builddir
   cmake ../
   make -j 4
   sudo make install
   sudo ldconfig

Install srsRAN build dependencies:

.. code-block:: bash

   sudo apt install build-essential cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev

Some of these will already be installed if Lime Suite was previously built from source, but are included here for completeness.

Note that if Lime Suite has not been installed from source, it will be neccessary to add :code:`liblimesuite-dev` to the above dependencies installation.

.. code-block:: bash

   git clone https://github.com/myriadrf/srsRAN_4G.git
   cd srsRAN_4G
   git checkout lc/main
   mkdir build
   cd build
   cmake -DUSE_LTE_RATES=true ../
   make -j 4
   sudo make install

This will install the latest development build. 

To install a LibreCellular release, instead of checking out :code:`lc/main`, check out a release tag, e.g. :code:`release_23_11_LC01`. The latest LibreCellular release will be the one with the highest upstream version and highest LC release suffix. Note that if a release if checked out which does not have an LCnn suffix, this will not have LMS API support and hence the eNodeB cannot be configured with the *device_name* parameter set to *lime*.

Configuration
-------------

eNodeB 
^^^^^^

The eNodeB can be configured by editing the file :code:`/etc/srsran/enb.conf`.

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
++++++++++++++++++

An `example is provided`_ for a 3 MHz channel in LTE Band 3, with SISO configuration. This corresponds to the Ofcom Shared Access 1800 MHz allocation.

Note that it will be neccessary to update the srsENB config if you need to use another channel.

EPC
^^^

The EPC is configured via :code:`/etc/srsran/epc.conf` and the main parameters of interest are:

* **[mme]** section:

  * **mcc**.  As described above.
  * **mnc**.  As described above.
  * **full_net_name** & **short_net_name**. Set both to the same, as described above.
  * **apn**. As described above.
  * **dns_addr**. Set to configure the DNS server for user equipment.

Note that subscribers must also be provisioned in the UE database and for details, see :doc:`/user/subscribers`.

.. _Ubuntu Server: https://ubuntu.com/download/server
.. _srsRAN 4G repo in the MyriadRF organisation: https://github.com/myriadrf/srsRAN_4G
.. _srsRAN documentation: https://docs.srsran.com/en/latest/
.. _example is provided: https://github.com/myriadrf/lc-configs/tree/master/srsran/b3-3mhz-siso