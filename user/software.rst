Software Installation
=====================

The software stack is currently comprised of:

* **srsEPC**. Lightweight LTE Evolved Packet Core.
* **srsENB**. LTE eNodeB basestation implemented entirely in software.
* **Lime Suite**. Software-defined radio (SDR) driver.
* **Ubuntu Linux**. Operating system.

This will be updated over time. For example, the EPC will be replaced with Open5GS, which can be used to provide both a 5G network core + LTE (4G) EPC.

Ubuntu Server 20.04
-------------------

`Ubuntu Server`_ version 20.04 LTS should be downloaded and installed. Default installation options should suffice, although for convenience the SSH server should probably be selected for installation.

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

This is required so as to ensure that the SDR transceiver application, the eNodeB component of srsRAN, does not suffer scheduling delays, which could result in reduced performance and/or instability.

Lime Suite and srsRAN
---------------------

srsRAN version
^^^^^^^^^^^^^^

At the present time a fork of the srsRAN software is being maintainted, which adds native support for LMS API, the API provided by Lime Suite and used by LimeSDR hardware. In testing this has been found to provide much better performance than use via SoapySDR. In addition to which, direct integration enables greater control of the SDR hardware, such as providing the ability to configure an external reference clock.

Moving forward this position will be reevaluated, as we investigate why use with SoapySDR incurs a performance overhead — it probably shouldn't do and there may be optimisation needed in the SoapySDR<>LMS API glue — and if it subsequently becomes possible to also configure key features, such as an external clock reference, via the SoapySDR API.

.. warning::
   Issues in connection with this fork should be logged under the `srsRAN repo in the MyriadRF organisation`_ and not the upstream srsRAN repo, since this is an experimental fork which is not supported by the srsRAN developers.

PPA packages
^^^^^^^^^^^^

With the PPAs configured, install Lime Suite and the srsRAN fork:

.. code-block:: bash

   sudo apt install limesuite srsran

.. note::
   Due to an issue with the latest Lime Suite packages a temporary workaround is required, whereby Lime Suite is also installed from source and this takes precedence over the packaged install. An issue has been logged and this step will be removed in due course.

   To implement the workaround, build Lime Suite from source, as described below. Note that it is not neccessary to build srsRAN from source also.

Source build
^^^^^^^^^^^^

Install Lime Suite build dependencies:

.. code-block:: bash

   sudo apt install build-essential git g++ cmake libsqlite3-dev libi2c-dev libusb-1.0-0-dev libwxgtk3.0-gtk3-dev freeglut3-dev

Clone, build and install Lime Suite:

.. code-block:: bash

   git clone https://github.com/myriadrf/LimeSuite.git
   cd LimeSuite
   git checkout v22.09.1
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

   git clone https://github.com/myriadrf/srsRAN.git
   cd srsRAN
   git checkout lc/main
   mkdir build
   cd build
   cmake -DUSE_LTE_RATES=true ../
   make -j 4
   sudo make install

This will install the latest development build. 

To install a LibreCellular release, instead of checking out :code:`lc/main`, check out a release tag, e.g. :code:`release_22_04_LC01`. The latest LibreCellular release will be the one with the highest upstream version and highest LC release suffix. Note that if a release if checked out which does not have an LCnn suffix, this will not have LMS API support and hence the eNodeB cannot be configured with the *device_name* parameter set to *lime*.

.. _Ubuntu Server: https://ubuntu.com/download/server
.. _srsRAN repo in the MyriadRF organisation: https://github.com/myriadrf/srsRAN