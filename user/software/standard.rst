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

Network Components
------------------

The various components are installed using Ansible playbooks. The git repo containing these and the software stack configuration should be cloned:

.. code-block:: bash

   git clone https://github.com/myriadrf/lc-configs.git
   cd lc-configs/standard

The site.yml file should be edited and at minimum the following config parameters updated:

* **network.host**. The hostname of the target system.
* **mysql.root_passwd**. The MySQL root password.

Although it would be prudent to also change the MySQL passwords for the network elements.

If the Ansible playbooks are being run from an admin system the hostname should resolve to a remote IP. Whereas if the playbooks are being run directly on the target system the value can be set to localhost. Note that the target system will also need to be in your /etc/ansible/hosts file.

The user account on the target system should be a member of the docker group and have sudo acccess. With network deployment it is assumed that the remote system has a user with the same name as the local user, but of course the target system username can be set to be something different, e.g. via the ansible_user option with the system's entry in /etc/ansible/hosts.

Base
^^^^

The base playbook creates a Docker private network and installs the software stack configuration under /etc/lc.

.. code-block:: bash

   ansible-playbook base.yml

At this stage if the MySQL passwords have been changed for any of the network elements — pyhss, pcscf and icscf etc. — you may wish to update their configuration files accordingly, before deploying the stack itself.

It also vitally important to update the eNodeB configuration, to ensure that the base station will be operating on an appropriately licensed RF channel and bandwidth for the site in question. This can be done by editing the file /etc/lc/srsenb/enb.conf. See the `srsRAN 4G documentation`_ for details.

.. danger::
   LTE networks operate in licensed spectrum and operating equipment without a licence from the regulatory authority in your country is likely to be a crime punishable under applicable law.

HSS
^^^

The HSS playbook deploys the following Docker containers:

* **BIND**. DNS server dependency for IMS.
* **MySQL**. Database server dependency for PyHSS and Kamailio.
* **Redis**. In-memory data store dependency for PyHSS.
* **PyHSS Base**. HSS base container.
* **PyHSS API**. HSS API (RESTful server) container.

A DNS server is required for the IMS components to function correctly and this will only be available via the Docker private network.

.. code-block:: bash

   ansible-playbook hss.yml

EPC
^^^

The EPC playbook deploys the following Open5GS Docker containers:

* **PGW-C / SMF**. Packet Gateway Control Plane (contained in Open5GS SMF).
* **PGW-U / UPF**. Packet Gateway User Plane (contained in Open5GS UPF).
* **SGW-C**. Serving Gateway Control Plane.
* **SGW-U**. Serving Gateway User Plane.
* **MME**. Mobility Management Entity.

.. code-block:: bash

   ansible-playbook epc.yml

IMS Databases
^^^^^^^^^^^^^

This playbook creates the MySQL databases which are required by Kamailio:

.. code-block:: bash

   ansible-playbook ims_dbs.yml

.. danger::
   This playbook should only be run once and if run a second time will create duplicate entries. In case of errors it may be easiest to drop the offending database(s) and re-run the playbook or part of it. This is a temporary limitation and will be addressed in future.

IMS
^^^

This playbook deploys the following Kamailio Docker containers:

* **P-CSCF**. Proxy Call Session Control Function.
* **I-CSCF**. Interrogating Call Session Control Function.
* **S-CSCF**. Serving Call Session Control Function.
* **SMSC**. Short Message Service Centre.

.. code-block:: bash

   ansible-playbook ims.yml

eNodeB
^^^^^^

This playbook deploys the srsENB Docker container:

.. code-block:: bash

   ansible-playbook enb.yml

Ensure that you have configured this component for the appropriate radio channel and bandwidth via /etc/lc/srsenb/enb.conf before deploying!

.. _Ubuntu Server: https://ubuntu.com/download/server
.. _how to install Docker Engine: https://docs.docker.com/engine/install/
.. _srsRAN 4G documentation: https://docs.srsran.com/projects/4g/en/latest/usermanuals/source/srsenb/source/index.html

