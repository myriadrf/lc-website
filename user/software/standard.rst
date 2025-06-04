Standard Software Installation
==============================

The standard software stack is much more complex than the mimimal configuration and is installed using Ansible and Docker containers. This provides a flexible Home Subscriber Server (HSS), Evolved Packet Core (EPC), IP Multimedia Subsystem (IMS), and eNodeB (LTE radio base station). 

The software stack is comprised of main components:

* **PyHSS**. Home Subscriber Server.
* **Open5GS**. LTE Evolved Packet Core (EPC).
* **Kamailio**. IP Multimedia Subsystem (IMS).
* **srsENB**. LTE eNodeB implemented purely in software.
* **Lime Suite**. Software-defined radio (SDR) driver.

Plus their dependencies. E.g. PyHSS and Kamailio both require MySQL. Such service dependencies are also installed via Docker containers.

Where only a data service is required — i.e. no native voice (VoLTE) or SMS support — the IMS components can be omitted. 

Linux Docker Host
-----------------

At the time of writing testing has been completed using Ubuntu Server 22.04 for the Docker host. However, given that the software stack is containerised other versions and distros should work.

`Ubuntu Server`_ version 22.04 LTS — or another version/distro — should be downloaded and installed. Default installation options will typically suffice, although the SSH server should be selected for installation. Desktop Linux variants are best avoided as these include all manner of uneccessary software.

Once rebooted install updates. E.g.:

.. code-block:: bash

   sudo apt update && sudo apt dist-upgrade

See the Docker documentation for details of `how to install Docker Engine`_.

Next configure the CPU governor to use performance mode:

.. code-block:: bash

   sudo apt install cpufrequtils
   echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils
   sudo systemctl disable ondemand
   sudo reboot

This is to ensure that the SDR transceiver application does not suffer scheduling delays, which could result in reduced performance and/or instability.

Ansible
-------

Ansible will need to be installed on the system which will be used to deploy the software stack. This can be the target system itself, or a separate admin system which has SSH access to the target system.

.. code-block:: bash

   sudo apt install ansible

LibreCellular Ansible Collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An Ansible collection has been created with the roles required to deploy the standard software stack. This can be installed with:

.. code-block:: bash

   ansible-galaxy collection install myriadrf.librecellular

This is comprised of the following roles:

* **myriadrf.librecellular.base**. 

  * Base role which installs Ansible Python dependencies on the target system, and creates the base config directory and Docker private network.

* **myriadrf.librecellular.hss**. 

  * Installs and configures the PyHSS Home Subscriber Server, along with MySQL, Redis and BIND. 

* **myriadrf.librecellular.epc**. 

  * Installs and configures the Open5GS Evolved Packet Core, comprised of the MME, SGW-C, SGW-U, UPF and SMF.

* **myriadrf.librecellular.ims**. 

  * Installs and configures the Kamailio IP Multimedia Subsystem (IMS) core, comprised of I-CSCF, S-CSCF, P-CSCF and SMSC.

* **myriadrf.librecellular.enb**. 

  * Installs and configures the srsENB LTE eNodeB, along with Lime Suite.

The roles should be executed in the order listed above, since each role depends on the previous one. The base role should always be run first, followed by the HSS, EPC, IMS and finally the eNodeB.

In certain cases some roles may be omitted, e.g. IMS if this is not required.

Example Playbooks
^^^^^^^^^^^^^^^^^

Minimal 
+++++++

A minimal playbook to deploy the complete software stack is as follows:

.. code-block:: yaml

   - name: Deploy LibreCellular standard software stack
     hosts: all
     become: true
     vars:
       enb_earfcn: '1934'
       enb_nprb: '15'
       hss_mysql_root_password: 'rootpasswd'
       hss_mysql_db_password: 'pyhsspasswd'
       ims_mysql_password: 'imspasswd'
       hss_provisioning_key: 'changeThisKeyInProduction'
     roles:
       - myriadrf.librecellular.base
       - myriadrf.librecellular.hss
       - myriadrf.librecellular.epc
       - myriadrf.librecellular.ims
       - myriadrf.librecellular.enb

The Ansible roles have many default values and using the above minimal playbook will result in a working system with the following notable defaults:

* **MCC**: 001
* **MNC**: 01
* **Network name**: LibreCellular

However, no defaults are provided for the eNodeB EARFCN and number of PRBs, since this could easily result in transmitting on unlicensed spectrum. Therefore these must be specified in the playbook, as shown above.

Similarly, the MySQL root password, HSS MySQL password, IMS MySQL password and HSS provisioning key must also be specified. Since providing defaults for these would not be secure.

Typical 
+++++++

A more typical playbook would also include the MCC, MNC and network name. 

.. code-block:: yaml

   - name: Deploy LibreCellular standard software stack
     hosts: all
     become: true
     vars:
       lc_mcc: '999'
       lc_mnc: '99'
       lc_network_name_full: 'LibreCellular'
       lc_network_name_short: 'LibreCellular'
       enb_earfcn: '1934'
       enb_nprb: '15'
       hss_mysql_root_password: 'rootpasswd'
       hss_mysql_db_password: 'pyhsspasswd'
       ims_mysql_password: 'imspasswd'
       hss_provisioning_key: 'changeThisKeyInProduction'
     roles:
       - myriadrf.librecellular.base
       - myriadrf.librecellular.hss
       - myriadrf.librecellular.epc
       - myriadrf.librecellular.ims
       - myriadrf.librecellular.enb

For details of the variables which can be set in the playbook, see the `myriadrf.librecellular Ansible collection`_, and in particular the `roles/<role_name>/defaults/main.yml` files for each role. 

Where a variable is used by multiple roles it can be set with an `lc_` prefix, e.g. `lc_mcc` and `lc_mnc`, or alternatively the variable can be set at the level of the role, e.g. `hss_mcc` and `hss_mnc`.

Note that there are a large number of parameters which can be configured across the entire cellular network stack and many ways in which this can be customised. The above examples are intended to provide a starting point and demonstrate the minimum required configuration to get a working system. 

It is hoped to eventually provide a more comprehensive set of example base configurations, which demonstrate how to configure the network for different use cases. For example, with EPC and IMS core running on a central host and then with one or more distributed eNodeBs securely connected to these.

.. warning::
   Some parameters are configured in multiple places. For example, the MCC and MNC, which are configured in the HSS, EPC and IMS. Therefore care must be taken to ensure that these are consistent across the entire network stack.

.. _Ubuntu Server: https://ubuntu.com/download/server
.. _how to install Docker Engine: https://docs.docker.com/engine/install/usermanuals/source/srsenb/source/index.html
.. _myriadrf.librecellular Ansible collection: https://github.com/myriadrf/lc-ansible-collection
